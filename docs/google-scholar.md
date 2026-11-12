# Google Scholar profile — set-up sheet

Not built by Pelican (lives in `docs/`). Twenty minutes, one time, needs you
signed in to Google. Why: seven papers including a PLOS ONE, and no profile
claims them. Scholar ranks on page one for your name and it's the cheapest
academic credibility on the list. The dblp entry
(<https://dblp.uni-trier.de/pid/203/8144.html>) is an index, not a profile.

## 1. Create the profile

<https://scholar.google.com/citations?view_op=new_profile>

| Field | Paste |
|---|---|
| Name | `Philipp Kats` |
| Affiliation | `Senior Applied Scientist, StreetEasy (Zillow Group)` |
| Email for verification | your `@zillowgroup.com` address (a verified institutional email is what makes the profile show up in search; a Gmail-only profile is indexed but ranks lower) |
| Areas of interest (five max) | `Machine Learning` · `Entity Resolution` · `Urban Informatics` · `Geospatial Data Science` · `Data Visualization` |
| Homepage | `https://casyfill.github.io/` |

Set the profile to **public**, and turn **on** "Automatically update the list
of articles" (the alternative is reviewing every suggestion by hand). Expect
near-namesake noise either way — Scholar matches on surname spelling, so
check the author line before accepting anything it suggests later.

## 2. Claim exactly these seven

Scholar will offer a candidate list after step 1. Tick these; untick anything
else.

| Year | Title | Venue |
|---|---|---|
| 2017 | Structure of 311 service requests as a signature of urban location | PLoS ONE 12(10): e0186314 |
| 2017 | Twitter Activity Timeline as a Signature of Urban Neighborhood | arXiv |
| 2017 | Geo-Tagged Social Media Data as a Proxy for Urban Mobility | Springer (AHFE proceedings) |
| 2018 | Digital Urban Sensing: A Multi-layered Approach | arXiv |
| 2018 | Twitter Connections Shaping New York City | HICSS |
| 2020 | Zoning of St. Petersburg Through the Prism of Social Activity Networks | Procedia Computer Science |
| 2021 | Social Activity Networks Shaping St. Petersburg | HICSS |

Same list as `/papers/` on the site, so the two surfaces agree. If Scholar
offers the Packt book (*Learn Python by Building Data Science Applications*),
take it too — it's yours and it carries citations.

## 3. Wire it into the site

Copy the profile URL (it looks like
`https://scholar.google.com/citations?user=XXXXXXXXXXXX`), then in
`pelicanconf.py` add one line to `SOCIAL`, after LinkedIn and before CV:

```python
    ('Scholar', 'https://scholar.google.com/citations?user=XXXXXXXXXXXX'),
```

That's the whole site change. The sidebar picks it up, and the homepage
JSON-LD `sameAs` block is built from `SOCIAL` (everything that isn't a `.pdf`),
so Google gets the site ↔ GitHub ↔ LinkedIn ↔ Scholar identity link for free.

Then rebuild and check:

```sh
PATH="$HOME/.local/bin:$PATH" pelican content -o /tmp/out -s publishconf.py
grep -o 'scholar.google.com[^"]*' /tmp/out/index.html
```

## Done looks like

Searching your name turns up the Scholar card above the contactout/rocketreach
scrapers, the profile lists seven papers and one book, and the site sidebar has
a fourth link. Tick it off in the strategy note's punch list.
