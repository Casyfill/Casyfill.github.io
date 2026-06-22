Title: A short foray in Data Journalism (2012–2015)
Date: 2020-05-02 00:20
Slug: data-journalism

*Almost an accidental, formative detour into data journalism — what we built, what it taught me, and how it ended.*

---

<div class="marginnote"><img src="/static/data_journalism/my_moscow.jpg" alt="My movements around Moscow — a personal data-mapping experiment.">
<strong>My movements around Moscow.</strong> A personal experiment in "quantifying thyself" — in the spirit of my Strelka work, and of <a href="http://feltron.com/">Nicholas Felton</a>.</div>

In 2012, while wrapping up my year at the Strelka Institute — where I'd taken to turning data into pictures, down to mapping a year of my own movements around the city — I got an unexpected request: to present my team's work at a small gathering at Ria Novosti, one of the country's big news agencies at the time. Their chief editor came too. As always, I was happy to present.

It was a rare event where the stars aligned, and the audience was both genuinely interested and warm. Only later did the meaning of that presentation become clear: a few months on, just before our graduation, I received a job offer I hadn't asked for and hadn't even imagined — to continue my data-driven experiments as part of the agency's infographics department. It was completely off my radar, but after some thought, I agreed. Only later did I learn the name for what I was about to do — _data journalism_.

To this day I believe this was (one of) my luckiest, most pivotal moments. I started working with fantastic people, and the work broadened my understanding of the world around me by orders of magnitude. It sounds almost funny, but a few days before I started, I was asked whether I wanted to be an _editor_ or a _designer_ in the team's nomenclature. To this day, I'm glad I picked _editing_.

The studio was a good place to think. A small room of developers, designers, and editors on fast turnaround, building one explanatory graphic after another — which sounds like a grind and was in fact the opposite. We had room to pick our own topics, or to put our own spin on whatever was on the agenda. Every week, there was pitching. It was a proper infographics studio: people were genuinely curious, open to the world, trying to make out the bigger picture — not just the facts of the day.

What my new boss, Maya, and I were bringing in was something new: data, not just information. Until then the work was mostly done by hand, and "data" usually meant a curated list of points and facts. The programmers built front-end visualizations; no real data analysis (and nothing larger than a few rows in a table, let alone "big data") was happening.

And I was about to change that — except for one detail: I knew I wanted to do data analysis, but I didn't yet know how to code, at least not efficiently.

## Duma's tax declarations

<div class="marginnote"><img src="/static/data_journalism/deputy_tax_declarations.jpeg" alt="A configurator plotting each Russian deputy by income and activity, with a detail panel of one deputy's declared property.">
<strong>The Duma, by declaration.</strong> Income against activity; click a deputy for the full filing.</div>

<div class="marginnote"><img src="/static/data_journalism/duma_prototype.png" alt="The same scatterplot of Russian deputies — a Grasshopper 3D prototype.">
<strong>Same scatterplot, Grasshopper 3D prototype.</strong></div>

This was one of our first big projects — essentially one giant scatterplot of every deputy. Each one files an income-and-property declaration, and almost no one reads them. They were a mess, of course: no single structure, no standards. I spent ages parsing and sifting through them, and for every car we had to attach a price tag, quantifying as much as we could. It was monumental work, and it taught me a great deal about data cleaning — and about scoping. We turned a stack that was designed to be scattered and unreadable into something you could actually explore: each official a point, income against activity, the full holdings a click away. In hindsight we could have done more with the material — but we turned plenty of heads as it was.

## Country Budget

<div class="marginnote"><img src="/static/data_journalism/budget_calculator.jpeg" alt="A Sankey-style budget calculator flowing a year of personal taxes into federal spending categories.">
<strong>Budget calculator.</strong> Your year of taxes, flowed into where the state spends it — and the country that spends most like you would.</div>

Our next big project wasn't about big data per se, but the subject was complex: the entire budget of a country. And again — this is information that isn't designed to be approachable; it's a plethora of nuance, reasoning, and history. To give it a more entertaining spin — or so we thought — we added a "choose your own <del>adventure</del> budget" game: you could change how the budget was distributed and see which country your ratios most resembled. The match was rarely what people expected. It was a good lesson: the piece was meant as a kind of edutainment — open-ended, with no critical commentary of our own — and yet every interaction nudged people toward an uncomfortable question of their own.

## 20 Years of Russian Duma

<div class="marginnote"><img src="/static/data_journalism/vis-gosduma-20.png" alt="Alluvial diagram tracing the alignment of Russian parties across 20 years of the State Duma.">
<strong>20 years of the State Duma.</strong> Every party and alignment, traced across two decades. <em>Code:</em> Michail Dunayev · <em>Design:</em> Valeriy Borisov · <em>Editor/analyst:</em> Philipp Kats · <em>Director:</em> Maya Stravinskaya.</div>

Perhaps my favorite work from this era. In theory it was a small spin on our first project: again, every deputy is a colored dot — except now we traced how they moved, election to election, between parties. What began as a diverse, picturesque mix of parties settled into an anemic gathering of four large, bureaucratized ones. Yes, that's more than the two in the US — but there was no real competition. The same people kept the same seats; they wanted no change, and represented no one.

The data processing itself was simple: parse the (very nicely built) Duma website, match names and party affiliations, double-check for surname changes, and we were done. As with so many of these, it started as a thought exercise, a small experiment — and only once we had the visualization did we realize we had a story.

This project won us a **silver medal** at the prestigious [Malofiej competition](https://en.wikipedia.org/wiki/Malofiej_Awards) (Spain).

## How Deputies vote

<div class="marginnote"><img src="/static/data_journalism/clusters_prototype.jpg" alt="Cluster analysis of Russian deputies' votes — Gephi prototype">
<strong>Initial prototype.</strong> Almost every project began with one — not just a guide for the designer, but a base to find the story and narrative in.</div>

<div class="marginnote"><img src="/static/data_journalism/vis-gosduma-cluster.png" alt="Cluster analysis of Russian deputies' votes — a dot grid showing how each deputy voted on the Dima Yakovlev law, colored by party.">
<strong>Politics of parties — clustering deputies by their votes.</strong> Each deputy is a dot; the grid shows one decisive vote. Cluster the votes and the real factions fall out of the data on their own. <em>Code:</em> Evgeny Panov · <em>Design:</em> Alexey Novichkov, Valeriy Borisov · <em>Editor/analyst:</em> Philipp Kats · <em>Director:</em> Maya Stravinskaya. <a href="https://ria.ru/20130708/948263330.html">Original writeup</a> (the interactive itself is now offline).</div>

This was another piece in the "Duma" series — how do they actually vote? It was also me growing, technically and professionally, without quite realizing it. On the same government website I'd used before, I found an open database of the votes — every one of them, every deputy. The sobering part was that by then we had no shortage of high-profile laws to anchor attention, like the one banning American families from adopting Russian orphans — a law whose cost was concrete and countable: adoptions frozen mid-process, and, by some accounts, children who didn't survive the wait.

But that was only the start. Using the full record for the sitting assembly, I ran what I called _cluster analysis_ — what science would more properly call _community detection on networks_. I built a dense graph of all the deputies, weighted every edge by how often two of them voted the same way, and let a force layout ("spring pull") do the rest. In seconds, deep, hidden structures and partitions inside the party lines emerged.

It was a real challenge: our first attempt to run the spring physics in the browser failed outright, so we fell back to precomputing the layout and animating only the transitions. I presented the project at a Network Science conference, and later heard it was being discussed in political-science circles. Looking back, I'm proud of it — I'd reinvented community detection on my own and made something people argued about. I can also see its limits now: I was rediscovering methods that already existed, without the scientific grounding or mentorship to recognize it. That gap, more than anything, is what would later point me toward graduate school.

## Global trends challenging cities

This was one of the last things I made at the studio: a set of four posters for a local urban-development conference. The subject — cities — was near and dear to me, and it was a rare print commission. The project made the longlist for an Information is Beautiful award.

<div class="marginnote"><img src="/static/data_journalism/muf.png" alt="Global trends challenging cities — radial infographics on urbanization made for the Moscow Urban Forum.">
<strong>Global trends challenging cities.</strong> Four posters on urbanization for the Moscow Urban Forum. <em>Design:</em> Nadezhda Andrianova, Maria Miahaylova · <em>Data &amp; content:</em> Philipp Kats. <a href="https://www.informationisbeautifulawards.com/showcase/563-global-trends-challenging-cities">Information is Beautiful — longlist</a>.</div>

## How it ended, and what I took from it

As I hinted, some of those projects turned heads — and not everyone was happy with what the agency was doing. In late 2013 it was abruptly dissolved and folded into a new, more state-aligned holding (you may know the name: "Russia Today"). The brief, relatively liberal window we'd been working in was closing — the end of a somewhat liberal epoch, as we'd only understand later.

Our team seemed to land on its feet: by mutual agreement, we moved together to Rambler & Co — home of _Afisha_ and _Lenta.ru_, then one of the best independent newsrooms in the country. But just weeks before we arrived, Lenta's editor-in-chief and senior staff were dismissed; much of that team regrouped abroad and founded what became [Meduza](https://meduza.io/en). We'd signed on to a very different place than the one we joined.

In a way, I was lucky to be close to history in the making — and luckier still not to get too close. It was a short chapter, but a dense one: more than a hundred pieces in all, most ephemeral, a few I still point to — a series of stories on art and the state since the 1990s, a long-read on Stalin's legacy with the "Memorial" NGO, experiments piping musicians' and critics' brain activity off an "EMOTIV EPOC" sensor, and many, many others. That first one was a particular gift: chasing down and verifying each story sent me down a rabbit hole I happily got lost in, and introduced me to dozens of Russian artists along the way.

I learned an enormous amount — and not only the obvious. Technical skill, yes: I bent [Grasshopper 3D](https://www.grasshopper3d.com/), meant for architectural generative design, into a makeshift data-wrangling rig, leaned on the era's toolkit — [TileMill](https://tilemill-project.github.io/tilemill/), [Tabula](https://tabula.technology/), [Gephi](https://gephi.org/), and my beloved [OpenRefine](https://openrefine.org/) — and by 2014 had taught myself Python and R. But the larger lesson was how to _work_: to combine creativity, experimentation, and project management, and to move fast in a small team — to compromise, to ask, to bring people along.

And I learned where my limits were. I'd begun to feel a ceiling: I wanted to take on more than my self-taught, unmentored skills could yet carry. That, more than anything, sent me to New York in 2015, to NYU CUSP for my master's.

<div class="marginnote"><img src="/static/data_journalism/photo_from_police.jpg" alt="Held at a police precinct after a protest, with Boris Nemtsov and Ilya Yashin — a year before Nemtsov's assassination.">
<strong>Held at a police precinct</strong>, after a protest on Manezhnaya Square — in good company with Ilya Yashin, Boris Nemtsov, and dozens of others. A year before Nemtsov's assassination.</div>
