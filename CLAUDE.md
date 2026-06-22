# Casyfill.github.io — personal site

Personal static website. **Python + Pelican**, built on a customized **FLEX** theme vendored as `theme_tufte/` (Tufte-style: a narrow text column with right-hand margin notes). Environment managed with **uv** (`pyproject.toml`, `uv.lock`); build with `make html`, preview with `make serve`; deploys via GitHub Actions → gh-pages. Notebooks come in through the `ipynb2pelican` submodule.

It's a personal site — **warm, quirky, reflective** — and represents my interests and views.

## Voice & style (page content)

- First person, narrative, reflective; warm and a little wry. **Not self-deprecating** — convey real pride and excitement in the work, and frame limits/gaps honestly (what I lacked, what I learned) rather than apologizing for them.
- **Concise and direct.** If a word can go, cut it.
- Keep my voice and idioms. I'm a non-native English speaker: copyedit grammar/spelling and get proper names exactly right, but **don't over-formalize or rewrite wholesale.**
- Long pieces follow a **"spine + threaded asides"** shape: a prose narrative spine, projects/visuals as margin notes, at most one full-width figure as a centerpiece, and a short reflective "what I took away" close.
- **Dek**: one italic line under the title, then `---`, in the same tone as the piece.
- Em dashes for parenthetical breaks (house style — see `pycombo`).
- **Don't invent technical detail.** Propose the structure and leave clearly-marked HTML-comment placeholders for me to fill; flag anything uncertain.
- **Sensitive context** (I'm Russian; the news agency I worked at was state-aligned): state it plainly, once, with dignity. Don't foreground "state media," and don't be defensive or apologetic — pride-forward. Hedge contested claims ("by some accounts").
- Credits go compactly inside captions: `Code: … · Design: … · Editor/analyst: … · Director: …`.

## Markup conventions (theme_tufte)

- **Margin note** — the default aside for an image + caption/credits. Put the image and caption text *directly* inside the div; **do not** wrap it in `<figure>`/`<figcaption>`:
  ```html
  <div class="marginnote"><img src="/static/…/img.png" alt="…">
  <strong>Title.</strong> caption + credits</div>
  ```
- **Full-width figure** (centerpiece only): `<figure><img …><figcaption>…</figcaption></figure>`. Never nest a `.marginnote` inside a `<figure>` — it breaks the float layout and is invalid HTML.
- **Strikethrough**: use `<del>…</del>` (the `~~…~~` markdown extension isn't enabled).
- **Math**: `pymdownx.arithmatex` generic mode, `\[ … \]`, often placed inside a margin note.
- Images live in `content/static/<topic>/`.

## Structure & navigation

- Content lives in `content/{AI, Work, Others, Personal, pages, static}/`. Folder = category, but URLs are **flat and slug-based** (`/slug/`), so moving a file between folders does **not** change its URL.
- Nav is **curated, not auto-taxonomy**: edit `NAV_GROUPS` in `pelicanconf.py` (sections: AI, Work, Talks & Publications, Personal; an empty group renders "— soon —").
- `content/pages/all.md` is a hand-maintained master index.
- **To add or move a page**: drop the `.md` in the right `content/<Section>/` folder, add/move its `NAV_GROUPS` entry, and update `all.md`. Heads-up: a desktop editor can silently re-save to the old path and create a **duplicate slug → build error** — check for stray copies after a move.

## Page goals & content plan

- The site should round out my persona beyond "data scientist / engineer": curious, civically engaged, creative, self-aware, and shaped by history.
- **Work** = technical/professional projects (e.g. `pycombo`, `dataframe-schema`) — deeper, technically substantive write-ups.
- **Personal** = biographical, reflective pieces. `content/Personal/data_journalism.md` is the reference for tone and structure.
- A strong piece should: (1) showcase the work and its technical hurdles; (2) tell how I got there, what I learned, and how I moved on; (3) weave in a personal/historical thread; (4) optionally, an epistemic note (e.g. verifying the record).
- **Planned**: a separate background/education note (architect → urban data at Strelka → NYU CUSP) that carries the cities/urbanism throughline, so individual pieces don't have to over-explain that arc.
- Cross-link opportunity: the hand-rolled community detection in the data-journalism piece later became the `pycombo` package.
