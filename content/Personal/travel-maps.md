Title: Mapping my travels, again, but better
Date: 2026-11-18
Slug: travel-maps
Category: Personal
Description: Why I keep mapping my trips — from a hand-styled map of Costa Rica in 2014 to maps drawn from my Obsidian notes with Agate.
Image: /static/mapping_travel/costa-rica-2014-agate.png

*Why I keep drawing maps of my trips — and how my notes finally started drawing them for me.*

---

I was 14 when the first member of my family went abroad. It was my Mom — she got onto a government-sponsored trip to Turkish Cyprus. It took another five years for me to finally go abroad myself. Perhaps this delayed, long-awaited experience made me strive for each trip to be The Journey.

<div class="marginnote"><img src="/static/mapping_travel/costa-rica-2014-mapbox-studio.png" alt="A hand-styled map of Costa Rica with a wave-textured ocean, contour lines, and seven numbered stops from San José to Tortuguero">
<strong>Costa Rica, 2014.</strong> Made in Mapbox Studio, the successor to <a href="https://tilemill-project.github.io/tilemill/">TileMill</a>. One of my early attempts — naive and imperfect; checking it now, I even found a few destinations placed incorrectly, and I'm not sure how that happened.</div>

A month roving India, north to south. Two month-long trips roving Costa Rica, eleven years apart. Zigging and zagging through the Italian Alps. Those long travels do change your experience and sense of life, and provide an immense number of stories.

And planning trips, facing travel challenges and making decisions does feel empowering, somehow bringing me closer to the heroes of my childhood books: Cyrus Smith, Phileas Fogg, Richard Francis Burton. I guess that's why I've long been trying to record my travels and map them — not (only) as a visual testament, but also as an index, of sorts, linking all the stories, challenges, thoughts and emotions.

<div class="marginnote"><img src="/static/mapping_travel/photobook-costa-rica-2025.jpg" alt="An open photobook: a map of the southern Nicoya Peninsula on the left page; on the right, a list of each traveler's top three memories and photos of handwritten notebook pages">
<strong>Costa Rica, 2025.</strong> A spread from our family photobook: the map, made in QGIS, next to everyone's top three memories of the trip.</div>

Yet drawing those maps, while rewarding, took time, and I didn't have much of an audience to share them with. That changed when I became a father — from then on, maps became a part of the photobooks from our shared travels.

Of course, when I started using Obsidian to keep track of all my life in one place, travel plans and records were an obvious part of the migration. Details, arrangements, budgets, places to visit and travel logs — all were part of it from the start.

But the data visualisation part was lacking. With [Agate](/agate/), the plugin I built, that changed. With some tinkering, experimentation and inquiries to Claude, I was able to create a single map spec <del>to rule them all</del> that shows the itinerary of any trip I've had, on a map. Another spec, on top of the same data, shows the most important statistics.

<figure><img src="/static/mapping_travel/agate-costa-rica-and-georgia.png" alt="Two Obsidian notes side by side. Left: Travel - Costa Rica Summer 2025, a map of the Nicoya peninsula with two numbered stays, routes shaded from first to last leg, and icons for experiences like snorkeling, scuba diving and a turtle nursery, above a By the numbers block reading 38 days, $8,176 spent, 293 km travelled, with top highlights. Right: AT Georgia 2025, a hiking route over shaded terrain, above stacked charts of elevation, speed, heart rate, sun and temperature">
<figcaption>Two notes, drawn by Agate. Left: Costa Rica, summer 2025 — the route leg by leg with icons for experiences, and the trip by the numbers. Right: three days on the Appalachian Trail in Georgia, 2025 — the route over terrain, with elevation, speed, heart rate, sun and weather along the way. Tools: Obsidian, Agate · Basemap: MapTiler · Icons: custom CSS</figcaption></figure>

I am pretty happy with the result. Still, I am a bit concerned that the trips look almost cookie-cutter, and I am not fully satisfied with the free-tier MapTiler basemaps (labels get in the way). Perhaps another layer of information would help — iconography for experiences, top photos (that would require setting up private URLs and private image hosting within my network, a separate piece of work). All of it is yet to come.
