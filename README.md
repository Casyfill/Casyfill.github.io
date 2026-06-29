# Casyfill.github.io — personal site

My personal site: project write-ups, talks, papers, and a few reflective pieces.
A static site built with [Pelican](https://getpelican.com/) and a customized,
Tufte-style theme (a narrow reading column with right-hand margin notes).

## Stack

- **Pelican** (Python) for static generation.
- **`theme_tufte/`** — a customized [FLEX](https://github.com/alexandrevicenzi/Flex) theme: Tokyo Night palette with a light/dark toggle, Inter + JetBrains Mono, and MathJax for LaTeX.
- **[uv](https://github.com/astral-sh/uv)** for dependency management (`pyproject.toml`, `uv.lock`). Requires Python 3.11+.
- **`ipynb2pelican`** for rendering notebooks (pulled as a submodule when present).

## Develop

Clone (use `--recurse-submodules` so the notebook helper comes along):

```bash
git clone --recurse-submodules https://github.com/Casyfill/Casyfill.github.io
cd Casyfill.github.io
```

Install dependencies, build, and preview:

```bash
uv sync        # create .venv and install
make html      # build the site into output/
make serve     # preview at http://localhost:8000  (make devserver to auto-rebuild)
```

## Deploy

Pushing to `master` triggers the GitHub Actions workflow
(`.github/workflows/main.yml`): it builds with `uv run pelican ... -s publishconf.py`
and deploys the result to GitHub Pages.

## Layout

- `content/` — pages and posts in `Work/`, `AI/`, `Personal/`, `Others/`. Folder sets the category, but URLs stay flat and slug-based (`/slug/`).
- `pelicanconf.py` — config and the curated `NAV_GROUPS` sidebar.
- `theme_tufte/` — the theme (`templates/`, `static/`).
- `docs/roadmap.md` — what's shipped and what's next. `IDEAS.md` — unscoped post ideas.
