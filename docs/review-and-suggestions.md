# City Fish — content review & suggestions

_Review of the site as it stands (June 2026). Maps to `roadmap.md` → v2 → Stab 2._

## Snapshot: what's here now

A clean Pelican site on the Flex theme. Five things in the nav: **About** (the landing page), **Presentations**, **Publications**, **Projects**, **Blog**.

- **About** — short, warm, and the best-written thing on the site. "I make tools and draw pictures" + the architect → urban planner → data journalist → data scientist arc. Links to StreetEasy work, Branchpoint, and a CV.
- **Publications** — a genuinely strong record: a Packt book, five peer-reviewed papers on urban analytics, and a pile of data-journalism pieces. Buried in a plain list.
- **Presentations** — 8 talks, 2012–2022, with slides/video links. Also a plain list.
- **Projects** — four entries: DataFrame Schema (dfs), MosPlus, the RIA Novosti infographics, and an "Other Projects" stub.
- **Blog** — one dummy post: _"Ping ping! this is an initial dummy blogpost."_

The bones are good. The problem is the site undersells you, has real bugs, and reads as abandoned (newest dated content is 2022).

## What's good — keep it

- The **About voice**. "I make tools and draw pictures" and "the long way around" are memorable and human. This is the tone the rest of the site should match.
- The **substance** is unusually rich: a published book, real papers, an _Information is Beautiful_ award, open-source tools (pyCombo, pdvega, dfs), and a striking back-catalog of infographics.
- **Simple, fast, no-nonsense theme.** Don't over-design away from this.

## What's broken — fix now

These are live bugs, in rough priority order:

1. **Your homepage portrait is broken on deploy.** `about.md` is saved as root `index.html` but references `../static/photo.jpg`. From the site root that resolves _above_ the site (it only works locally by accident). The file lives at `static/photo.jpg`.
2. **Four of six images on the RIA Novosti page are broken:**
   - `deputy_tax_declaration.png` → actual file is `deputy_tax_declarations.jpeg` (plural, `.jpeg`)
   - `budget_calculator.png` → actual is `budget_calculator.jpeg`
   - `pension_calculator.png` → actual is `pension_calculator.jpeg`
   - `muf.png` → **doesn't exist at all** (the Singapore Urban Forum entry has no image). Add it or drop the reference.
   - Only `vis-gosduma-20.png` and `vis-gosduma-cluster.png` load.
3. **Root cause of 1 & 2: fragile `../static/` relative paths.** Switch to Pelican's `{static}/...` link syntax so paths resolve correctly regardless of the page's output location, and broken refs fail at build time instead of silently.
4. **`[pypi page](missing)`** on the dfs page — a link whose text and target are both literally "missing."
5. **Fragile CV link.** The CV is a Dropbox `?dl=0` URL that can vanish or change. Commit the PDF to `static/` and link locally.
6. **Typos to sweep:** "Cris Wong" → Chris Wong; "of of"; "Ria Novosty" → Novosti; "on the the interned" → internet; "Inforgraphics" → Infographics; "interchangable" → interchangeable.
7. **Empty footer/meta:** `COPYRIGHT`, `SITESUBTITLE`, and a site `DESCRIPTION` are all unset — the footer renders a bare "©" and there's no meta description or social-card image for sharing.

## What it lacks

- **Pictures — ironic for someone who "draws pictures."** There is no visual gallery anywhere. Your strongest, most distinctive assets (the Duma viz, pension/budget calculators, the award-winning Singapore posters) sit as broken thumbnails on a buried text page. This is the single biggest gap.
- **A real blog.** One dummy post is worse than no blog — it signals "abandoned." Either seed it with real content or hide the section.
- **A way to reach you.** Only social icons; no email, no contact line.
- **Recency / signs of life.** Everything dates to 2020–2022. Nothing says what you're up to now.
- **Depth on projects.** Three of four project pages are short and two openly say "more details later." They read as placeholders.
- **Discoverability niceties:** RSS is disabled, no OpenGraph image, thin SEO.

## Suggestions: good, quirky, and personal

The brief is "quirky and personal," and you have far more raw material for that than the site shows. Ideas, roughly highest-leverage first:

**1. Make it visual — a real portfolio/gallery.** You're a data-viz person; show the work. A simple grid of your infographics and maps (RIA calculators, the Duma clustering, Singapore posters, StreetEasy dashboard) with a sentence each. Fix the images first, then promote them from "buried project page" to a front-door gallery. Lead with pictures, not lists.

**2. Explain "City Fish."** The site name is delightfully odd and completely unexplained. A one-line origin story (a colophon, a footer hover, a tiny easter egg) turns a random name into personality.

**3. Tell your path as a map or timeline.** "Architect → urban planner → data journalist → data scientist," across Moscow, St. Petersburg, Singapore, NYC. You literally do spatial and temporal viz — do it to your own bio. An interactive map of "my cities" or a small career timeline would be the most _on-brand_ quirky thing on the site.

**4. Add a `/now` page.** A [nownownow.com](https://nownownow.com)-style "what I'm doing now" snippet kills the abandoned feel and matches your "perhaps one day I'll get back to it" voice. Cheap to maintain, high signal of life.

**5. A colophon / "how this is built" page.** You make tools — the uv + Pelican + GitHub Actions setup is itself a small story tool-makers love. Pairs naturally with a "/uses" page (editor, stack, hardware).

**6. Personality in the microcopy.** A custom 404 ("this page swam away"), a real footer line, hover states. Small touches, big character return.

**7. Show the teaching.** University + school teaching and Branchpoint are barely visible. A short "Teaching" section with the YakTak poster, slides, and a line on Branchpoint rounds out the picture.

## Suggested near-term punch list

A realistic sequence, not an aspirational one:

1. Fix the seven bugs above (broken images, paths, CV, typos, footer/meta). Half a day, and the site stops looking broken.
2. Delete or hide the dummy post.
3. Promote the visuals: fix the RIA images and build a simple gallery page; link it from the nav.
4. Add `SITESUBTITLE`, `COPYRIGHT`, `DESCRIPTION`, and an OG image.
5. Add a `/now` page and a contact line (email).
6. Pick the quirky win you'll actually enjoy — the "City Fish" story or the cities map — and ship one.

## A sane blog cadence

Don't promise daily. Seed 2–3 posts from things you already have, then go monthly-ish / "when there's something":

- A behind-the-scenes of one RIA infographic (the pension calculator is a great story).
- A short writeup of **pyCombo** or the **dfs** design philosophy (you've half-written these in the project pages already).
- One of your talks turned into a post (the "research cities through data" Yandex.Q talk converts cleanly).

The goal isn't volume — it's three real posts so the section reads as alive instead of empty.
