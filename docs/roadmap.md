# Site roadmap

Working notes for the personal site (Pelican + customized Tufte theme). What's
shipped, and what's next in priority order. Unscoped content ideas live in
`IDEAS.md`; this file is for things that are actually queued to build.

---

## Shipped — v2 redesign

- [x] Custom `theme_tufte/` — Tokyo Night palette, light/dark toggle, Tufte reading layout, MathJax
- [x] Flat slug URLs; curated `NAV_GROUPS`; auto "Recent" block; `/all/` archive
- [x] Folder-as-category content model (`Work`, `AI`, `Personal`, `Others`)
- [x] uv dependency management; GitHub Actions redeploy to gh-pages
- [x] About rewrite, photo, favicon, design tokens as CSS vars
- [x] **PyCombo** — full long-form write-up (the bar for a mature Work piece)
- [x] **Data Journalism** — narrative piece (the tone reference)
- [x] **311 requests** — paper write-up + figures
- [x] Papers and talks split into flat pages; pre-2016 talks collapsed to one line

---

## Now — close the four visible gaps

What a first-time visitor notices. Ordered. Each can ship as a short first pass
before it's deepened.

### 1. AI section is empty

The `AI` nav group renders "— soon —" (`content/AI/` holds only `.gitkeep`).
For someone doing applied ML in 2026, this is the loudest "unfinished" signal on
the site.

- [ ] Pick the first AI piece. Strongest candidate: something grounded in real work (home-value estimate / matching / recommendation), or an LLM experiment you actually ran. A "how this site is built" meta-post (Pelican + Tufte + AI-assisted editing) is a cheap, honest first entry that fits the section and shows craft.
- [ ] Ship one short post to kill the empty-section smell, then expand.
- [ ] Add it to `NAV_GROUPS` and `all.md`.

### 2. DataFrame Schema — promote from stub to a real Work piece

Right now it reads like a pasted README: thin, dated 2022, with typos. It's a
flagship Work item sitting next to PyCombo, and the gap shows.

- [x] Quick typo pass — `derived`, `as it wishes`, `a few cornerstone`, `DataFrame` casing, stray comma + plurals fixed.
- [ ] Rewrite to PyCombo depth: the problem (validating DataFrames in day-to-day work), the design choice (DataFrame-agnostic core, Pydantic, one dependency), how it compares to `pandera` / `great_expectations` / `tableschema`, and a "what I took away" close.
- [ ] State current status honestly: pandas-only today, other flavors on the roadmap. Refresh or drop the bare 2022 date.

### 3. Background / education arc

Already named as planned in `CLAUDE.md`. The architect → Strelka → NYU CUSP
throughline that lets individual pieces stop re-explaining how you got here.

- [ ] Draft the arc as a standalone Personal piece (carries the cities/urbanism thread).
- [ ] First pass can be short. Once it exists, trim the arc recap from pycombo and data-journalism and cross-link to it instead.

### 4. About / homepage round-out

The homepage is three short paragraphs. A little more substance and a clearer
landing lifts the whole site.

- [ ] Add a sentence or two of real substance (what you actually build, what you're curious about now).
- [ ] Cross-link into Work (pycombo, dataframe-schema) so the landing routes somewhere.

---

## Polish — quick wins (cheap, high signal)

- [x] **README.md rewritten** to the real uv + Pelican + `make` flow — dropped the sidewalklabs musing and the conda / Python 3.7 / `requirements.txt` steps, fixed the clone URL.
- [x] **Removed `homepage-and-nav.patch`** from the repo root (already applied; was committed by mistake). Also cleared 13 stray `.DS_Store` files.
- [ ] **Resolve the lost talk link.** "Open data & urban analytics, F.M. Dostoyevsky Public Library, Moscow (2015)" carries a dangling `TODO` in `all.md` and `talks-and-presentations.md`. Recover the slides/PDF and link, or drop the line.
- [ ] **Fill the `data-science-for-planners.md` TODO** — the main examples/case studies and how the poster relates to the talk.
- [x] **Consolidated index pages** — dropped the orphaned `books-and-articles.md`; `papers.md` and `all.md` remain.

---

## Later — depth & breadth

- [ ] Deepen the thin talk pages where it's worth it: `cities-through-data`, `data-science-infrastructure`, `city-through-foursquare`.
- [ ] **"On faults"** — a piece on what didn't work and what it taught you (carried over from the old roadmap; pairs well with the honest tone of the PyCombo and Data Journalism closes).
- [ ] **MosPlus** — promote into the Work nav or fold into a project list. It's currently reachable only from `/all/`.
- [ ] **Teaching / "on education"** — your philosophy on learning to build with data (distinct from the background arc; you teach at university and school level).

---

## Backlog — see `IDEAS.md`

NYC ViewShed, Project Branchpoint, parametric architecture, and the salvaged
Afisha data-journalism pieces. Move an item up here once it's scoped enough to draft.
