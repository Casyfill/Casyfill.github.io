# Changelog

## 2026-06-20 — Site redesign: flat structure + Tufte / Tokyo Night theme

### Added
- New custom Pelican theme `theme_tufte/`, ported from the approved prototype: Tokyo Night palette (light/dark with a toggle), Inter + JetBrains Mono, a Tufte-style reading layout with right-margin sidenotes/figures, and MathJax for LaTeX.
- Curated sidebar nav (`NAV_GROUPS`): AI, Work, Talks & Publications, Personal — plus a **Recent** block that auto-lists the latest posts from the `Others` category, and an **All** archive page.
- Folder-as-category content model (`content/Work`, `AI`, `Personal`, `Others` with `USE_FOLDER_AS_CATEGORY`): a post dropped into `Others/` surfaces under Recent until it's promoted into a group.
- Individual flat pages for each talk, paper, and the book; `/all/` and `/talks-and-publications/` index pages.
- Favicon (from `profile.png`); design tokens as CSS variables.

### Changed
- Flat, topic-named URLs (`/slug/`) everywhere; turned off category/tag/author/archive output.
- pycombo: modularity formula and the Zachary's-karate figure moved into the right margin (Tufte); added a Portugal community-detection figure credited to the MIT Senseable City Lab.
- Renamed "Ria Novosti" → "Data Journalism" (`/data-journalism/`).
- Collapsed the pre-2016 talks (2012–2016) into a single "Earlier talks" line linking their slides.

### Removed
- Trimmed Press & media to three entries; pulled NYC ViewShed, three Afisha pieces, and three Grasshopper3D brochures off the site (kept in `IDEAS.md` for re-synthesis).
- Retired the old combined `presentations` / `publications` list pages (now drafts) and the thin "Other Projects" page.
