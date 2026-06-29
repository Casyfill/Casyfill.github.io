Title: Find your spot. Custom boundaries
Date: 2018-01-01
Slug: find-your-spot
Subtitle: GeoNYC · 2018

[slides](https://docs.google.com/presentation/d/1SECOPRQB4gmTur-L67Q9TGDOBC7o5o-IJVgDdb1kDek/edit)

<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/se_ads_before.png" alt="A StreetEasy 'Find your place' subway ad: a building in cutaway with floors labeled hint of garbage, aroma of garbage, smell of garbage.">
<strong>The pitch, on the street.</strong> StreetEasy's "Find your place" campaign at the time — the right apartment is the one that fits you.</div>

<!-- TODO: video link — the previous link (Dropbox nyc_datavis_all.mp4) was incorrect and has been removed; add the correct recording once recovered -->

A talk at GeoNYC, New York's geospatial meetup, hosted that night by [Carto](https://carto.com/). I was about two years into StreetEasy, whose pitch then was that it helped you find what you were *actually* looking for, not just scroll an endless list — search you could shape to your own sense of the city. Custom boundaries were the literal version of that: find your spot, then look only there.


The tool itself is simple. Instead of accepting our official neighborhoods, anyone can draw their own area on the map, name it, and search inside it — one boundary or many.

<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/custom_boundary_tool.png" alt="StreetEasy's 'Create a Custom Boundary' tool: a polygon being drawn over a Manhattan street map inside the search interface.">
<strong>Draw your own.</strong> Sketch an area, name it, and it becomes a search filter.</div>

By 2018 our users had quietly drawn about forty thousand of them. That struck me as a gift: forty thousand hand-drawn polygons recording how New Yorkers really carve up their city, and marking every place our neat neighborhood map let them down.

## Mapping forty thousand polygons

It was also my excuse to solve a harder problem: how do you even draw forty thousand overlapping polygons on one map? Plot them the usual way and you get an ink-black smear. This is the quiet trouble with big-data visualization — the tools are few, the technique is fiddly, and the story is hard to compose — but it pays off, because a simple aggregate often hides the very thing you're after. The answer here was datashader, fairly new at the time, which I'll come back to.

<figure><img src="/static/presentations_talks/2018_geo_nyc/overall.png" alt="All ~40,000 custom search boundaries over New York City, rendered as a glowing density map; Manhattan blazes and the boroughs' structure emerges.">
<figcaption><strong>The city, drawn by its searchers.</strong> Every custom boundary at once. The shape of New York falls out on its own, brightest where people search the most. 2 Squares around union square - our default shape (see above).</figcaption></figure>

Even plotted as-is, the result was breath-taking. The structure of the city emerges on its own: people fence their searches along highways and big avenues. A few mega-polygons stretch clear across the map, drawn by people searching whole boroughs at once. And one spot in Queens lit up in a way I didn't expect.

<figure><img src="/static/presentations_talks/2018_geo_nyc/details.png" alt="The density map annotated: boxes mark a large boundary reaching toward New Jersey and a bright cluster at Forest Hills, with an arrow labeling the bright lines as highways and roads.">
<figcaption><strong>What you're looking at.</strong> The bright lines are highways and roads people bound their searches by; a mega-polygon reaches toward New Jersey; and one spot in Queens, Forest Hills, stands out.</figcaption></figure>

## What people draw, and what they call it

<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/walkable.png" alt="Density map of boundaries named 'walkable,' scattered across the city as rough circular shapes.">
<strong>"Walkable."</strong> Named by feel — people drew rough circles, a radius around a point.</div>

Does anyone agree with our map? Two ways to look: how far our outlines overlap what people actually draw, and what they name the places. The naming turned out to be the louder signal.

<!-- TODO: add an Upper West Side / Prospect Heights coverage-overlay slide here if you have one. -->



Map every boundary someone labeled "walkable" and you get a scatter of rough circles: people drew a radius around wherever they stood. Others name by anchor entirely, pinning an area to the one thing that matters to them.

<!-- <div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/prospect_park.png" alt="Density map of custom boundaries drawn around Prospect Park, Brooklyn.">
<strong>Prospect Park.</strong> Boundaries drawn around the park.</div>


<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/equinox.png" alt="Density map of custom boundaries near Equinox gym locations, scattered across Manhattan.">
<strong>Equinox.</strong> One cluster per location — the chain draws its own map.</div> -->

A park, a grocery, a gym: the boundary follows the anchor. It's a blunt, honest read on what people actually optimize for when they choose where to live.

## Forest Hills, two neighborhoods in one

<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/forest_hill.png" alt="Density map of custom boundaries in Forest Hills, Queens, forming two distinct clusters.">
<strong>Two clusters, one name.</strong> Forest Hills splits cleanly in the data. Color of the polygon defined by center of the polygon being below or above the railroad.</div>

Then the real disagreement: Forest Hills, in Queens. On our map it's one clean, well-defined neighborhood. In the data it splits in two — the historic Forest Hills on one side, and a newer section across the subway and the highway, long associated with the writer Sergei Dovlatov. Our customers treat them as two places; we still file them as one.

<figure><img src="/static/presentations_talks/2018_geo_nyc/forest_hill_photo.png" alt="Aerial view of Forest Hills: low-rise houses with gardens on one side, denser blocks on the other, divided by a rail line and highway corridor.">
<figcaption><strong>The split, from above.</strong> A rail line and highway cut Forest Hills apart — low houses and gardens on one side, denser blocks on the other. The map was wrong, and the people drawing on it knew it. (Apple Maps Satellite View)</figcaption></figure>

## Watching the market move

<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/bronx.png" alt="Density of custom boundaries for Bronx, over time.">
<strong>The map fills in.</strong> Custom-boundary density across the Bronx, over time.</div>


Boundaries carry a date, so you can watch the searching itself move. Played over the years, the density creeps outward, notably across the Bronx — tracing, I'd guess, the market opening up there.

## Why it took datashader

<div class="marginnote"><strong>datashader.</strong> A Python library that renders very large datasets by rasterizing — aggregating the data into a grid of pixels and coloring each by what lands there — instead of drawing every element as its own object.</div>

Back to the tool. Matplotlib and its kin draw each shape as an object, so forty thousand polygons either crawl or collapse into a blot. [datashader](https://datashader.org/) inverts that: it aggregates the data into a pixel grid and colors each cell by how much falls in it, so density itself becomes the picture — exactly what you want when the truth is in the overlap, not in any single shape.

A note on method, in fairness: everything here came from looking — drawing, adjusting, looking again — rather than from hard metrics. That's both the charm and the limit. There's a second layer still buried in this data for anyone who quantifies it: area overlap between drawn boundaries and our neighborhoods, naming frequencies, agreement scores, and more.

## What I took from it

<div class="marginnote"><img src="/static/presentations_talks/2018_geo_nyc/ads_later.jpeg" alt="A StreetEasy subway ad: a stylized map of Tribeca with the line 'places where I can still say I live in Tribeca,' and 'Find your place.'">
<strong>A year later.</strong> StreetEasy's advertising leaned into personal neighborhood lines — "places where I can still say I live in Tribeca."</div>

This stays one of my favorite pieces of work — a rare case where big, messy data became legible at a glance, with no summary table standing in for it. And a year on, custom-boundary search turned up as a headline feature in StreetEasy's advertising. I can't prove my analysis drove that, but the timing was close enough to enjoy.
