Title: Agate: an Obsidian plugin that turns Bases into data visualizations with Vega
Date: 2026-11-12
Slug: agate
Description: Agate is an Obsidian plugin that draws Vega and Vega-Lite charts from Bases — notes with properties, queried as a table.
Image: /static/agate/base-to-chart.jpg

<figure><img src="/static/agate/base-to-chart.jpg" alt="A base of book notes on the left; the same notes drawn as a chart on the right, with one row linked to its block">
<figcaption>The same notes, twice: as rows in a base, and as a chart. Each block is one book note; hovering it shows the note's properties.</figcaption></figure>

## What it is

[Agate](https://casyfill.github.io/Agate/) is a plugin for Obsidian that draws charts from your notes. It adds an **Agate chart** view to Bases: the base picks the notes, a Vega or Vega-Lite spec describes the picture, and the chart redraws when the notes or the base's filters change.

<div class="marginnote"><img src="/static/agate/obsidian-app.png" alt="Obsidian on desktop and phone: a folder of notes, an open note, and its link graph">
<strong>Obsidian.</strong> Notes, folders and the links between them, on desktop and mobile. <a href="https://obsidian.md">obsidian.md</a></div>

[Obsidian](https://obsidian.md) is a note-taking app that keeps notes as plain Markdown files in a local folder, called a vault. Notes can carry properties — a date, a rating, a place, a link to another note. **Bases**, a core Obsidian feature, queries notes by those properties and shows them as a table you can filter, sort and group, much like a small database.

<div class="marginnote"><img src="/static/agate/vega-lite-example.png" alt="A Vega-Lite bar chart of mean monthly precipitation in Seattle, next to the twelve-line JSON spec that draws it">
<strong>Vega-Lite.</strong> Twelve lines of JSON — data, mark, encoding — and the chart they draw. <a href="https://vega.github.io/vega-lite/examples/">Vega-Lite examples</a></div>

[Vega](https://vega.github.io/vega/) and [Vega-Lite](https://vega.github.io/vega-lite/) are languages for describing a chart as JSON, developed at the University of Washington's Interactive Data Lab. A spec says where the rows come from, which marks to draw, and which fields map to position, color and size; the library renders it. Vega-Lite is the short form for most charts, Vega the full language underneath.

!!! note "Install and links"
    In Obsidian: *Settings → Community plugins → Browse*, search **Agate**. Needs Obsidian 1.13+ with the core Bases plugin enabled; works on desktop and mobile.

    [Website](https://casyfill.github.io/Agate/) · [Quickstart](https://casyfill.github.io/Agate/quickstart.html) · [Gallery](https://casyfill.github.io/Agate/gallery.html) · [GitHub](https://github.com/Casyfill/Agate)

## What to use it for

To me, Obsidian's main value is its simplicity and flexibility: there is no declared structure or format for your notes. As a result, finding a structure that works is the user's own quest — a hard one, and never a one-time thing. That's why I wanted Vega here — a tool I've relied on since at least 2018, when I [gave a talk about it](/nyc-dataviz-2018/): freedom in how I visualize my notes, combined with charts I can reuse and that stay live as the notes and their structure change.

[Vega Visualizations](https://community.obsidian.md/plugins/obsidian-vega) already renders Vega in Obsidian, but with the data written into the spec. Agate connects it to Bases, and I now use it daily.

<div class="marginnote"><img src="/static/agate/hike-basemap.jpg" alt="A hiking route drawn over topographic map tiles, with named waypoints">
<strong>Outdoors.</strong> A three-day section of the Appalachian Trail over terrain tiles, camps and peaks labeled.</div>

<div class="marginnote"><img src="/static/agate/board-games.jpg" alt="Stacked bars of board-game plays per month by winner, next to a scatter of game length against complexity">
<strong>Collections.</strong> Game nights by winner, and the shelf by length and complexity — one note per game and per play.</div>

<div class="marginnote"><img src="/static/agate/brooklyn-1938.jpg" alt="Brooklyn's 1938 HOLC redlining map, neighborhoods colored by grade">
<strong>History.</strong> Brooklyn's 1938 HOLC redlining map, drawn from a GeoJSON file with hatched fills.</div>

<div class="marginnote"><img src="/static/agate/vault-links.jpg" alt="Arc diagram of links between notes, grouped by folder">
<strong>The vault itself.</strong> Links between notes, grouped by folder.</div>

- **Learning and practice.** I keep a note per interview problem, with scores before and after reading up; the chart shows which topics improve and which I keep avoiding.
- **Travel.** Place notes with coordinates, linked from trip notes, become routes on a globe — mine shows our Azores trip.
- **Work.** I track my goals and OKRs, as well as Jira tickets synced into the vault, thanks to two plugins: [Jira Issue](https://community.obsidian.md/plugins/obsidian-jira-issue) and [Jira Weaver](https://community.obsidian.md/plugins/jira-weaver).
- **Headline numbers.** Big numbers were almost an afterthought; they became the feature I use most.
- **Collections** — board games, books, records: what gets played or read, and what doesn't.
- **Habits and mood** — a few numbers in a daily note, accumulated into a year; [Habit Tracker 21](https://community.obsidian.md/plugins/habit-tracker-21) handles the daily check-ins.
- **The outdoors** — runs and hikes, with a multi-day route over a basemap.
- **Campaigns and worlds** — D&D sessions, characters and factions as linked notes.
- **History** — events with dates and places, or historical maps like Brooklyn's 1938 redlining.
- **The vault itself** — how notes link, and which folders take up space.

## How to start

The [quickstart](https://casyfill.github.io/Agate/quickstart.html) walks through a first chart in about fifteen minutes, with a starter set of 26 book notes. In short:

1. Give your notes consistent properties in the frontmatter — `genre`, `pages`, `status` — with numbers as numbers and dates as `YYYY-MM-DD`.
2. Create a base that picks those notes, e.g. every note with `type == "book"`.
3. Add a chart: in the base, add a view with the **Agate chart** layout, then pick one of thirteen recipes, ask an assistant (see below), or write a spec by hand. A spec can also live in any note, inside an ```` ```agate ```` code block:

```yaml
base: Reading/Books.base
spec:
  # Books per genre, colored by status. Edit a note and this redraws.
  mark: {type: bar, tooltip: true}
  encoding:
    y: {field: note.genre, type: nominal, sort: "-x"}
    x: {aggregate: count, title: Books}
    color: {field: note.status}
```

Fields are the property ids you see in the base (`note.genre`, `file.name`); the rest is plain Vega-Lite. The chart appears wherever a base does — its own tab, embedded in a note (`![[Books.base#Ratings]]`), the sidebar, a Canvas — and clicking a mark opens the note behind it.

The spec is a plain JSON or YAML file next to the notes: it syncs and versions like any other file, and still runs in the Vega editor outside Obsidian. Agate makes no network requests by default; remote data and map tiles load only once you allow them.

## Charting in the age of AI

Vega and Vega-Lite have been around for over a decade, with plenty of public specs and examples, so language models already know them well: describe a chart in plain words and any capable assistant writes a working spec. That shaped a deliberate choice — Agate has no chart-builder wizard with panels of options. Most people would ask an LLM anyway, so Agate helps the assistant instead:

- **Dynamic prompt.** *Copy prompt for an LLM* writes a prompt for the current base: its properties and their types, a few sample rows, and Agate's conventions. Paste it into any chat, add what you want, and *Paste spec* checks the reply and saves it as the view's chart ([guide](https://github.com/Casyfill/Agate/blob/main/docs/guide.md#2-your-first-chart-five-minutes)).
- **Theme prompt.** *Copy theme prompt* does the same for styling: it reads your current Obsidian theme, so an assistant can write a matching chart theme ([themes](https://github.com/Casyfill/Agate/blob/main/docs/themes.md)).
- **Skill.** For agents that work on the vault directly (Claude Code and similar), the [`agate-chart` skill](https://github.com/Casyfill/Agate/blob/main/skills/agate-chart/SKILL.md) teaches Agate's conventions and has the agent render a spec before handing it over.

## Extras on top of Vega

<div class="marginnote"><img src="/static/agate/5-rollup-numbers.jpg" alt="Big numbers rendered as note text">
<strong>Big numbers.</strong> Live totals and averages as note text rather than a chart. They follow the base's filters like any view.</div>

<div class="marginnote"><img src="/static/agate/horizon-table.jpg" alt="A cubism-style horizon chart: one row per market note, each with its own price series">
<strong>Per-note data.</strong> One row per note, each drawing its own time series as a cubism-style horizon chart.</div>

<div class="marginnote"><img src="/static/agate/themes.jpg" alt="The same board-game charts in four themes: Du Bois, FiveThirtyEight, dark Obsidian, and a hatched print style">
<strong>Themes.</strong> One spec, four looks. The theme lives apart from the spec and can follow your Obsidian theme, light or dark, as it changes.</div>

Plain Vega covers almost any picture, but a vault is not a CSV file: notes link to each other, sit in folders, and often stand for something measured elsewhere. A few extras make that available to a spec, without leaving the standard grammar — Agate's additions live under `usermeta`, which Vega ignores, so specs stay portable.

- **Big numbers** — headline figures (books this year, average rating, change from last year) shown as text.
- **The vault as data** — links between notes and the folder tree are available as datasets, for link graphs, arc diagrams and sunbursts.
- **Per-note data** — a note can point to its own CSV, JSON or URL, e.g. a price history per stock note.
- **Basemaps** — map tiles under routes and points, with API keys kept in Obsidian's secret storage.
- **Theme-aware** — the default theme follows the Obsidian theme and light or dark mode.

<!-- TODO: add real reports from other users (forum / GitHub / Reddit) as they come in — a quote or screenshot each, with permission. -->

Agate was built with heavy help from AI coding agents, with one demo vault that doubles as the test suite. <!-- TODO: link to the planned "how I built it" post once it exists --> Feedback and examples are welcome on [GitHub](https://github.com/Casyfill/Agate/issues).
