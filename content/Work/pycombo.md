Title: Wrapping Combo, three times over
Date: 2026-06-15 20:08
Slug: pycombo

*Turning a research C++ algorithm into something anyone can `pip install` — and what a decade of maintaining it taught me about shipping software that lasts.*

---

A decade ago, in grad school, the analysis in my notebook had a hole in the middle of it. To run the community-detection algorithm I leaned on — Combo — I couldn't just call a function. I had to stop, write my graph out to a text file in exactly the right format, drop into a shell to run a compiled C++ binary, then read its output file back into the notebook to keep going. Every run broke the train of thought, and the notebook's tidy narrative with it. The algorithm worked fine. Living with it, in the middle of real work, did not.

That friction is why `pycombo` exists — at first only to get Combo out of the shell and behind a single function call, so I never had to leave the notebook. The bigger problem came into focus later: the compiled binary I'd been handed ran on my Mac and nowhere else. Closing _that_ gap — from _works on my machine_ to _`pip install pycombo` on a stranger's laptop_ — turned out to be the real project, and I've rebuilt it three times to get there, as much because Python's packaging tools kept shifting underneath me as because I kept getting better at this. Almost none of that work was about the algorithm. It was about the build — which is exactly the part that decides whether a good algorithm ever makes it into someone else's work.

## What Combo is, and why it's worth the trouble

Combo works on networks, and it detects *communities* — partitioning a graph into groups that are more densely connected within than between, the network analogue of clustering. The usual way to score a partition is **modularity** (Q): how much denser the within-group edges are than you'd expect in a random graph with the same degrees.

<div class="marginnote">
\[ Q = \sum_{c}\left[\frac{L_c}{m}-\left(\frac{k_c}{2m}\right)^2\right] \]
Modularity \(Q\): \(L_c\) = edges inside community \(c\), \(k_c\) = total degree of its nodes, \(m\) = total edges — the share of edges inside communities, minus what chance predicts.
</div>

Most methods, Combo included, then search the vast space of possible partitions for the one that maximizes Q. That space is enormous and riddled with local optima, so _how_ you search matters enormously.

Combo ([Sobolevsky, Campari, Belyi & Ratti, _Phys. Rev. E_ **90**, 012811, 2014](https://arxiv.org/abs/1308.3508), out of MIT's Senseable City Lab) is a quality-first optimizer by design: maximizing modularity, it reliably finds **higher-scoring partitions** than the standard greedy and non-greedy alternatives, and on description length it's on par with Infomap.

<div class="marginnote"><img src="https://senseable.mit.edu/community_detection/img/portugal_img.png" alt="Communities detected across Portugal from network data">Community detection in the wild: regions of Portugal recovered from network structure. <a href="https://senseable.mit.edu/community_detection/">MIT Senseable City Lab</a>.</div>

What makes it different is a richer _move set_: where methods like *Louvain* reassign one node at a time — fast, but easily trapped in local optima — Combo also merges whole communities, splits them, and shifts blocks of nodes between them, more global moves that climb out of those traps at the cost of speed. It's built for the _best_ partition, not the _fastest_.

Where it sits today: **Leiden** (2019) is the fast Louvain successor that guarantees well-connected communities, and **stochastic block models** (e.g. `graph-tool`) are the principled generative alternative that sidesteps modularity's _resolution limit_. Combo's niche is quality-first maximization on networks up to ~10⁴ nodes — and it's objective-agnostic: hand it an arbitrary score matrix and it solves a general clique-partitioning problem.

## The algorithm was a file someone handed me

I was working in Stanislav Sobolevsky's lab on a string of urban-network papers, and Combo was our default tool for pulling structure out of these graphs — recovering, say, the latent districts of a city from a social-activity network (see _[Social Activity Networks Shaping St. Petersburg](https://scholarspace.manoa.hawaii.edu/items/9f2923ae-874a-4e24-971b-b88c72e08e8d)_, HICSS 2021). The way I "had" the algorithm, though, was literally a file: someone handed me the C++, and I ran it.

The reference implementation behaves like a classic research artifact. You clone [Alexander Belyi's repo](https://github.com/Alexander-Belyi/Combo), run `make`, and you get `comboCPP` — a command-line program that reads a graph from a Pajek `.net` file, writes the community labels to a `.txt`, and prints the achieved modularity to stdout.

That's perfectly fine for a one-off. It's quietly miserable as a daily dependency. Every experiment becomes shell orchestration: serialize your graph to disk in exactly the right format, invoke a binary that must already be compiled and on your `PATH`, then parse a text file back into memory before you can use the result. Nothing is importable, and the binary only runs where it was compiled. For a tool you want to live inside a notebook — and, eventually, hand to someone else — it's a bad foundation. What followed was three attempts at fixing that, spread across a decade, each shaped as much by where Python's tooling stood that year as by how much I'd learned since the last.

## Version one: wrapping the ergonomics, not the dependency

So the first `pycombo` was the naive thing, and I'll own it: a thin Python function that wrote the graph out to a temporary Pajek file, shelled out to `comboCPP` through `subprocess`, read the output file back, and parsed it into a `{node: community}` dictionary. An afternoon's work! It was the conda era; "just use a virtual environment" still felt like a new habit, and I built the thing inside one of mine without once wondering how it would run on anyone else's.

It did the job — my notebooks got a single function call instead of a shell ritual — but it didn't actually _solve_ anything. It just moved the mess behind a nicer-looking door. The compiled binary still had to exist on the machine. The temp files still got written and parsed. Anyone who wanted to use it first had to reproduce the C++ build I was quietly leaning on. I had wrapped the ergonomics, not the dependency.

## Version two: compile the C++ _into_ Python

The version that mattered came years later, and it showed up alongside better tools — this was around when Poetry appeared and `pyproject.toml` was beginning to push out `setup.py`. It stopped treating Combo as an external program and started treating it as a library.

I vendored the upstream C++ as a **git submodule** at `src/Combo`, so the package tracks Belyi's source exactly rather than carrying a drifting copy. Then I wrote a small [pybind11](https://github.com/pybind/pybind11) binder (`src/Binder.cpp`) and let the build compile `Graph.cpp`, `Combo.cpp`, and `Binder.cpp` together into a single extension module, `pycombo._combo`.

Concretely, the binder is a thin layer of glue. `Binder.cpp` includes pybind11 and the submodule's `Graph.h`/`Combo.h`, then defines a few small functions — `execute`, `execute_from_file`, `execute_from_matrix` — that each build a `Graph`, run the `ComboAlgorithm`, and hand the result back as a `std::tuple<std::vector<size_t>, double>` (community labels plus the achieved modularity). A single `PYBIND11_MODULE(_combo, m)` macro registers those functions as a Python module, and including `pybind11/stl.h` quietly handles the marshalling: C++ `std::vector`, `std::tuple`, and `std::optional` cross the boundary as Python lists, tuples, and `None` with no conversion code of my own.

The build itself is just a C++ extension build, orchestrated so the user never sees it. The compiler turns `Binder.cpp`, `Graph.cpp`, and `Combo.cpp` into object files and **links** them into one shared library — `pycombo/_combo.cpython-3XX-<platform>.so` (a `.pyd` on Windows) — which Python then imports like any other module. The pure-Python layer on top stays tiny: `pycombo.execute` turns a NetworkX graph into a node count and a weighted edge list, calls `_combo.execute(...)`, and zips the returned integer labels back onto the original node names. That's the whole seam — Python for ergonomics, compiled C++ for the work, pybind11 in between.

This was my **first real foray into writing C/C++**, and I want to be honest about that: pybind11 was the on-ramp that made it survivable, and I leaned heavily on the people who knew the code. I owe a genuine thank-you to **Alexander Belyi**, who wrote and maintains the C++, and to **Stanislav Sobolevsky** — both were remarkably patient with a stream of beginner questions about the algorithm and its internals.

The payoff is that the change collapses the entire awkward middle. There's no subprocess, no temp file, no text parsing. `execute()` hands a graph straight into C++ memory and gets back the partition and its modularity.

## The real work was packaging

Here's the lesson I didn't expect going in: **writing the binding was a weekend; making it installable was the project.**

Poetry and a small `build.py` drove the compilation, and GitHub Actions built **wheels for Linux, macOS, and Windows** across the supported Python versions. The payoff is the only thing the end user ever sees:

```sh
pip install pycombo
```

No compiler, no submodule, no `make`. That single line is the actual difference between _code that exists on GitHub_ and _code a peer can drop into their environment and reproduce_. Everything upstream of it — the binder, the build script, the CI matrix — exists purely so that line works on a stranger's laptop.

## Version three: rebuilding on standard ground (now)

That tidy story had a fragile foundation, and a decade is a long time in Python packaging. The Poetry-plus-`build.py` path was a product of its moment: `build.py` was an imperative script driving the compile through `distutils` — and `distutils` was deprecated and then removed from the standard library outright in Python 3.12. The Poetry lockfile had grown to thousands of lines. Wheel publishing broke more than once (Windows quirks, CI artifact changes, a hand-maintained build matrix). And the most visible gap was hardware: there were no native **Apple Silicon** wheels, so every M-series Mac silently fell back to compiling from source — exactly the friction the package exists to remove.

[The latest stab at this project](https://github.com/Casyfill/pyCombo/pull/124) (v0.1.10) rebuilds the foundation on what has, in the years since, become the standard toolchain for shipping a compiled Python package:

- **[uv](https://github.com/astral-sh/uv)** for dependency management and fast, reproducible locking — replacing Poetry.
- **[scikit-build-core](https://github.com/scikit-build/scikit-build-core) + CMake** for the compile, replacing `build.py`/`distutils`. pybind11 stays; it's now located by CMake's `find_package`.
- **[cibuildwheel](https://github.com/pypa/cibuildwheel)** in CI to produce the whole wheel matrix in one shot — Linux `x86_64` and `aarch64`, macOS `arm64` (Apple Silicon) and `x86_64`, and Windows `AMD64`, across CPython 3.9–3.13.

The interesting part is _how differently it works_. The old build was a script I babysat; the new one is configuration that delegates to tools built for the job. Instead of running my own `build.py`, `pyproject.toml` now simply **names a build backend** — scikit-build-core, under the [PEP 517 standard](https://peps.python.org/pep-0517/) — and the backend hands the actual compilation to **CMake**, a real build system that already knows how to find **pybind11**, choose the right compiler on each platform, and emit the extension. `uv` resolves and locks the environment in a fraction of Poetry's time. `cibuildwheel` spins up each target platform and builds every wheel without a matrix I maintain by hand. I stopped writing build logic and started declaring intent.

Is this a de-facto standard? Mostly — and that's the whole point. cibuildwheel is what most projects shipping compiled wheels now reach for. scikit-build-core is the standard PEP 517 backend for CMake-based extensions — it's the path pybind11's own docs point you to — with **meson-python** as the Meson-based equivalent for projects that prefer Meson. uv is the fast-rising default for locking and environments. None of it is clever; it's the boring, blessed path. Which is exactly what I want underneath a dependency: the less novel my build, the better the odds it still works, untouched, on a stranger's laptop three years from now. (I even wrote the decision down as an ADR in the repo, so the _next_ rebuild starts from the reasoning instead of archaeology.)

The user-visible payoff is small, and it's the entire reason for the work: `pip install pycombo` on an M-series Mac stops shelling out to a compiler and just drops in a prebuilt wheel. The honest trade-off is that building *from source* now needs a CMake toolchain, not just a compiler — but with a matching wheel for almost every platform, almost nobody builds from source at all.

One correctness fix the rebuild folded in, too: because the wheel compiles Combo's GPL-3.0 source directly into the binary, pyCombo is a derivative work — so I realigned its own license from MIT to GPL-3.0, to match what it actually ships.

## What using it looks like

The common case is one call — and because the result is just a NetworkX graph plus a label dict, plotting it is the ordinary NetworkX path:

```python
import pycombo
import networkx as nx
import matplotlib.pyplot as plt

G = nx.karate_club_graph()
# weight=None treats the graph as unweighted — the classic karate setup
partition, modularity = pycombo.execute(G, weight=None, random_seed=42)

print(f"modularity Q = {modularity:.4f}")               # -> 0.4198
print(f"communities  = {len(set(partition.values()))}")  # -> 4

# color each node by the community Combo assigned it
colors = [partition[n] for n in G.nodes()]
nx.draw_networkx(
    G, pos=nx.spring_layout(G, seed=7),
    node_color=colors, cmap="tab10",
    edge_color="#cccccc", font_color="white", node_size=500,
)
plt.axis("off")
plt.show()
```

Run on Zachary's karate club — the _Drosophila_ of community detection — that finds four communities at Q ≈ 0.4198, the textbook optimum for this graph.

<div class="marginnote"><img src="/static/pycombo/1_karate_combo.png" alt="Zachary's Karate Club, partitioned by Combo (Q = 0.4198, 4 communities)" style="display:block;margin-bottom:.35rem;">Zachary's karate club, partitioned by Combo — Q ≈ 0.4198, four communities.</div>

## What it can do beyond the one-liner

- **Flexible input** — NetworkX graphs, Pajek `.net` files, or an adjacency matrix as a NumPy array or list.
- **The knobs that change results** — `modularity_resolution`, a cap on the number of communities (`max_communities`), and a `random_seed` so a run is actually reproducible.
- **Custom objectives** — set `treat_as_modularity=True` and pass your own score matrix, and you're using Combo as a general **clique-partitioning** solver, not just a modularity maximizer. This is the underused superpower: the same engine optimizes whatever matrix you hand it.

## Does the quality claim actually show up?

It's worth checking the headline claim rather than taking it on faith. I ran Combo, Louvain, and Leiden on the same graphs and scored every resulting partition with the _same_ (NetworkX) modularity function — best over five runs each, on a MacBook Pro (Apple Silicon, CPython 3.10):

|Graph|Combo|Louvain|Leiden|
|---|---|---|---|
|Karate (n = 34)|**0.4198**|0.4198|0.4198|
|Les Misérables (n = 77)|**0.5667**|0.5667|0.5667|
|LFR benchmark (n = 300, μ = 0.45)|**0.4139**|0.3874|0.3962|
|LFR benchmark (n = 1,000, μ = 0.45)|**0.4581**|0.4238|0.4476|

On the small, well-separated classics all three land on the same optimum — there the real difference is _consistency_: Combo and Leiden reach it on every run, while Louvain's average drifts below its best. The gap opens up on harder networks with heavy inter-community mixing (the LFR benchmarks at μ = 0.45), where Combo posts the highest modularity at both sizes — on the 1,000-node graph, roughly +2% over Leiden and +8% over Louvain. That's exactly the regime Combo was built for: when you're willing to spend more compute to get a better partition.

And it isn't only my benchmark. An independent study by [Aref, Mostajabdaveh & Chheda (2023)](https://arxiv.org/abs/2302.14698) pitted eight popular heuristics against an exact integer-programming solver on 80 networks: Combo recovered the _exact_ maximum-modularity partition more often than any other heuristic — for 55% of the networks, versus ~36% for Leiden and 19% for Louvain — and its near-optimal partitions stayed the closest to a true optimum.

That quality isn't free: Combo is markedly slower and hungrier for memory than Louvain or Leiden, and practical only up to networks of ~10⁴ nodes, while they scale to millions. The full timing-and-scaling comparison lives in the [benchmark notebook](https://github.com/Casyfill/pyCombo/blob/master/example/benchmark.ipynb) — the short version is: reach for Combo when partition quality is the priority and the graph is small enough; reach for Leiden when it's large. pyCombo doesn't move that ceiling — it just makes the high-quality regime painless to get to.

## Where it's ended up

I started `pycombo` to scratch my own itch, but the part I'm proudest of is what came after. It's been installed more than 80,000 times, and it's quietly become the default way to run Combo from Python — the workhorse behind urban-structure analyses I worked on, like recovering the social fabric of [St. Petersburg](https://scholarspace.manoa.hawaii.edu/items/9f2923ae-874a-4e24-971b-b88c72e08e8d) from social-media activity, and a baseline that turns up in independent [community-detection benchmarks](https://arxiv.org/abs/2302.14698). None of that reach came from the algorithm itself — it came from the unglamorous work of making the algorithm usable, and keeping it usable for the better part of a decade.

## What I took away

A few things stuck with me, in roughly increasing order of how long it took to believe them:

**Distribution is the feature.** A great algorithm behind a manual build step is, for most people, not available at all. The wheel on PyPI did more for adoption than any cleverness in the wrapper.

**Speak the ecosystem's language.** NetworkX in, a plain dict out, one function named `execute`. The less the wrapper asks a user to learn, the more the underlying algorithm gets used.

**Vendor upstream, don't fork it.** A git submodule means the package tracks Belyi's real source and inherits his fixes, instead of slowly rotting as a copy that drifts from the original.

**Reproducibility is an artifact, not an intention.** A pinned, installable wheel beats a README full of build instructions every time. The goal was never "wrap Combo" — it was to make sure `pip install pycombo` keeps working a year from now, on my laptop and on a machine I'll never see.

**Boring tooling is a feature.** The third rewrite taught me what the first two didn't: a build is most valuable when it's the least original thing in the repo. Standard backend, standard wheel builder, standard lockfile — the more my packaging looks like everyone else's, the longer it keeps working without me.

Combo was always a good algorithm — that credit belongs to Belyi and Sobolevsky. What's mine is the layer that lets anyone actually use it: the binding, the build, the wheels, and the years of keeping all three working as the ecosystem shifted underneath them. That layer is unglamorous, and it's also the whole difference between an algorithm that exists and one people can reach for. Building it well — and rebuilding it as the tools change — turns out to be its own discipline, and it's the one I'd point to.

---

## References & resources

**The algorithm**

- Sobolevsky, S., Campari, R., Belyi, A., & Ratti, C. (2014). General optimization technique for high-quality community detection in complex networks. _Physical Review E_, 90(1), 012811. [arXiv:1308.3508](https://arxiv.org/abs/1308.3508)
- [MIT Senseable City Lab — Community Detection project](http://senseable.mit.edu/community_detection/)

**Code**

- pyCombo (this package): [repo](https://github.com/Casyfill/pyCombo), [PyPi page](https://pypi.org/project/pycombo/)
- [Benchmark notebook](https://github.com/Casyfill/pyCombo/blob/master/example/benchmark.ipynb) — the quality and timing comparisons behind this post.
- [Combo, C++ reference implementation](https://github.com/Alexander-Belyi/Combo)
- [pybind11](https://github.com/pybind/pybind11)

**Methods it's compared to / alternatives**

- Newman, M. E. J., & Girvan, M. (2004). Finding and evaluating community structure in networks. _Physical Review E_, 69(2), 026113. _(modularity)_
- Blondel, V. D., Guillaume, J.-L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. _J. Stat. Mech._, P10008. _(Louvain)_
- Rosvall, M., & Bergstrom, C. T. (2008). Maps of random walks on complex networks reveal community structure. _PNAS_, 105(4), 1118–1123. _(Infomap)_
- Traag, V. A., Waltman, L., & van Eck, N. J. (2019). From Louvain to Leiden: guaranteeing well-connected communities. _[Scientific Reports](https://www.nature.com/articles/s41598-019-41695-z)_, 9, 5233. _(Leiden)_

**Selected work citing or using Combo**

- Aref, S., Mostajabdaveh, M., & Chheda, H. (2023). Heuristic Modularity Maximization Algorithms for Community Detection Rarely Return an Optimal Partition or Anything Similar. _ICCS 2023_. [arXiv:2302.14698](https://arxiv.org/abs/2302.14698) — an independent benchmark in which Combo recovered the exact modularity optimum most often of eight popular heuristics.
- Sobolevsky, S., & Belyi, A. (2022). Graph neural network inspired algorithm for unsupervised network community detection. _Applied Network Science_, 7, 63. [arXiv:2103.02520](https://arxiv.org/abs/2103.02520) — benchmarks a new GNN method against Combo.
- Landsman, D., Kats, P., Nenko, A., Kudinov, S., & Sobolevsky, S. (2021). _[Social Activity Networks Shaping St. Petersburg](https://scholarspace.manoa.hawaii.edu/items/9f2923ae-874a-4e24-971b-b88c72e08e8d)_. HICSS 2021 — Combo applied to recover urban structure from a social-activity network.
