Title: Declarative visualization with Vega
Date: 2018-01-01
Slug: nyc-dataviz-2018
Subtitle: NYC Data Visualization Meetup · 2018

[slides](https://docs.google.com/presentation/d/1kc4VsezCkqwyPURjf3Hhp8pxO1cqGmJaXmm4QmPEH7g/edit)

<!-- TODO: video — confirm whether a recording exists (the Dropbox nyc_datavis_all.mp4 file was previously misattributed to "Find your spot"); re-link once recovered -->

A talk at the [NYC Data Visualization Meetup](https://www.meetup.com/datavisualization/) in 2018, the group then run by Naomi B. Robbins, about one family of tools — Vega, Vega-Lite, and Altair, the Python binding for them. Vega and Vega-Lite came out of the [Interactive Data Lab at the University of Washington](https://idl.uw.edu/). It's easy to mistake them for yet another plotting library. Vega does sit on top of D3 and a few other existing pieces, but the rendering isn't the interesting part. What sets it apart is that it's *declarative*, in the spirit of ggplot's grammar of graphics.

## Charts as specifications

<!-- <figure><img src="/static/presentations_talks/2018_dataviz/diagram.png" alt="Diagram of the Vega ecosystem: Python (pdvega, Altair) compiling to Vega-Lite and Vega specs, rendered by Vega.js on top of D3, surrounded by related engines, tools, and environments.">
<figcaption><strong>The Vega family.</strong> Python (pdvega, Altair) compiles to a Vega-Lite spec, then a Vega spec, then Vega.js on top of D3, with a wide ecosystem of engines, tools, and environments around it.</figcaption></figure> -->

<figure>
<img src="/static/presentations_talks/2018_dataviz/editor.png" alt="The Vega editor: a JSON chart specification on the left, the rendered US map it produces on the right.">
<figcaption><strong>Spec to chart.</strong> The Vega Editor: a JSON specification on the left, the chart it produces on the right. You change the spec, not the pixels.</figcaption>
</figure>

The idea is simple: you say what you want to see, not how to draw it. You write a specification of the chart, and an engine executes it. One can compare it to SQL — a shared specification accepted by multiple engines, each working differently under the hood. Spelled out, a spec reads almost like a letter:

> Dear chart,
>
> Please show me points with X on a linear scale over "Height" and Y on a linear scale over "Weight," size on a log scale by population, and color by gender, using the dataset I'm passing you.

That framing buys a clean separation of concerns, on more than one level. The spec lives outside the data, so when the data changes the chart simply re-renders. It lives outside the visuals too: a theme can be defined once, even externally, so the same chart restyles itself when you swap themes. As an analyst you stay on the meaning, and let the styling be settled once, elsewhere.

<!-- <div class="marginnote"><img src="/static/presentations_talks/2018_dataviz/editor.png" alt="The Vega editor: a JSON chart specification on the left, the rendered US map it produces on the right.">
<strong>Spec to chart.</strong> The Vega Editor: a JSON specification on the left, the chart it produces on the right. You change the spec, not the pixels.</div> -->

And because the thing in the middle is just a specification, a JSON file, it travels between languages and engines. That's exactly how Altair works: Python emits the spec, and the Vega engine renders it in the browser.

## From notebook to live page

That portability turned out to matter well beyond a notebook. At StreetEasy I wanted one place to host embedded charts, themed consistently, where adding a new one cost almost no development, and Vega fit exactly.

<div class="marginnote"><strong>vega-embed.</strong> The standard helper for dropping a Vega or Vega-Lite view into a page: give it a spec (inline or by URL) plus a theme, and it renders, export menu included.</div>

The hosting was a few small pieces. A public S3 bucket, later behind a CDN, though any static host would do. A single page that uses [vega-embed](https://github.com/vega/vega-embed) to render a spec with our house theme. And the detail that made it click: that page reads a `spec_path` parameter from its own URL, so one deployed page can render any specification I point it at.

That indirection is the whole point. Publishing a chart never touches code or a deploy — I add a spec file and change a query parameter. Every chart is just a data file, so a new or broken one can't take down the page or disturb the ones already live. The theme is set once and shared, the data lives in the spec and can be swapped underneath, and the page is static, so it caches and scales for free. One page served any number of charts, and nothing was ever at risk.

An analyst builds the chart in a notebook with Altair, and to shave off the last step I wrote a small Python helper that exported and published it in a single line, without leaving the analysis.

<figure><img src="/static/presentations_talks/2018_dataviz/schema.png" alt="App scheme: a Jupyter notebook with Altair and an internal package produces specs and data, pushed to an S3 bucket, where Vega.js and Vega-Lite.js render them with an external theme.">
<figcaption><strong>App scheme.</strong> Build in a Jupyter notebook with Altair and our internal package, push the spec and data to an S3 bucket, and let Vega render it in the browser, with the theme kept separate and specs pulled in by URL.</figcaption></figure>

In the CMS, WordPress for us, going live was then just pasting an embed pointed at the new URL.

What lands on the page is live: interactive, themed to the brand, with the rich interactivity that normally takes real front-end work included by default.

<figure><img src="/static/presentations_talks/2018_dataviz/use_at_streeteasy.png" alt="A published StreetEasy blog post, 'Top Neighborhoods for Night Shift Workers in NYC,' with an interactive map embedded in the page.">
<figcaption><strong>Live on the site.</strong> The result in our CMS: an interactive, brand-themed StreetEasy piece, embedded straight from a spec.</figcaption></figure>

Years on, the bet still reads as the right one. Separating what from how, and treating the chart itself as data, is what let a small team ship interactive graphics without standing up a front-end project behind every one. It went over well on the night, too, though I pitched it wide — more a tour of a way of thinking than a hands-on session, which asked a lot of a mixed, non-technical room.

## What changed since

The tools didn't stand still. Altair picked up a prefix and is now [Vega-Altair](https://altair-viz.github.io/), and the whole family sits under [NumFOCUS](https://numfocus.org/project/vega), the nonprofit behind NumPy and pandas, as a sponsored project — about as clear a signal of staying power as open source offers. Altair is on version 6 now, several major releases past what I demoed in 2018, still built on the Vega-Lite grammar underneath.

<!-- TODO (June 2026): the report you uploaded (vega-viz-since-2018.md) came through empty — re-share it and I'll fold in the specific changes you want to highlight here. -->

## Where it went

My own path drifted away from this kind of work. The team I'm on moved from economics and day-to-day editorial content to a data-product team building actual features, so public-facing visualization isn't the daily craft anymore, and I miss it more than I'd expected. The app I built to serve these specs is still running. The engineering held up; the harder problem, which I underrated at the time, was getting non-technical colleagues to use the full range of what it offered. A spec is elegant to people who think in specs; for everyone else, the distance between *possible* and *actually used* turned out to be the real design work, and the part I'd take a different run at today.
