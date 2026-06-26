Title: Structure of 311 service requests as a signature of urban location
Date: 2017-10-17
Slug: structure-of-311-requests

*A city's 311 complaint calls carry more than the complaint. The mix of what people report — noise, heat, a blocked driveway — turns out to be a fairly reliable signature of where they live.*

---

**Lingjing Wang, Cheng Qian, Philipp Kats, Constantine Kontokosta, Stanislav Sobolevsky** · *PLOS ONE* 12(10): e0186314, 2017 · [Read the paper →](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0186314)

This was a [CUSP](https://cusp.nyu.edu/) paper out of Stanislav Sobolevsky's group — the lab whose urban-network work later pushed me toward [pycombo](/pycombo/) — and, as best I recall, my first time on an academic paper. My part was the cluster analysis. The question behind it is an old one for anyone who studies cities: planning, policy, and real estate all lean on *local context* — the character of a single neighborhood — yet the signals that capture it are expensive, slow, or sparse. A census is rich but comes once a decade. We wanted to know whether a city already reveals its context, for free, in the data it collects every day.

It does, through **311** — the non-emergency line a resident calls about a noisy bar, a broken heater, a blocked driveway, a pothole. New York alone logs more than a million of these a year, each stamped with a type and a place. The idea was that the *mix* of complaints in a neighborhood — not how many, but which kinds, in what proportion — is a signature of the place itself: "the unique way people use 311," as we put it in the paper.

## A signature made of complaints

For each census tract we turned its 311 record into that signature — a vector of the relative frequency of every request type — and let a clustering algorithm sort the city's ~2,000 tracts by signature alone, with no map and no demographics in the loop. Four clear classes emerged in New York.

<figure><img src="/static/311/new_york.png" alt="New York City: census tracts colored into four 311-complaint clusters (left) and a radar plot of those clusters' socioeconomic features (right).">
<figcaption><strong>New York, by its complaints.</strong> Left: ~2,000 census tracts sorted into four clusters from the mix of 311 requests alone — no demographics in the loop. Right: the same clusters' socioeconomic profiles — income, schooling, race, insurance — which the clustering never saw. <em>From</em> Wang et&nbsp;al., <em>PLOS&nbsp;ONE</em> 2017 (CC&nbsp;BY), Figs&nbsp;1 &amp; 5.</figcaption></figure>

The clusters mapped onto the city in ways that were easy to recognize. One was the loud, dense core — Midtown, downtown Brooklyn, and, oddly, the airports — defined by noise. A more residential Brooklyn–Queens stood out for blocked driveways. Heating complaints marked one set of tracts; rough streets another.

<div class="marginnote"><img src="/static/311/ny_cluster_distribution.png" alt="Bar chart of the share of each 311 request type within the four New York clusters.">
<strong>What sets them apart.</strong> The share of each request type within the four clusters — noise, heating, blocked driveways, and street conditions each dominate a different group. <em>Fig 2.</em></div>

## It tracked the census

We had clustered on complaints alone — not a single income, education, or race figure went into it. So we pulled the census (the 2014 ACS) and asked whether these complaint-based groups lined up with anything in it. They did. Income, education, unemployment, insurance coverage, and racial composition all separated clearly across groups the algorithm had drawn without ever seeing them — the radar plot above is that comparison.

From there it was a short step to prediction: regression models that read a neighborhood's socioeconomic profile, and even relative real-estate price trends, from its 311 signature alone (for prices we used Zillow's data, years before I'd end up working there). And it wasn't a New York quirk — Boston and Chicago gave back the same kind of structure.

<div class="marginnote"><img src="/static/311/chicago.png" alt="Chicago: census tracts in four 311-complaint clusters (left) and a radar plot of their socioeconomic features (right).">
<strong>Not only New York.</strong> Chicago, the same method: four clusters (left) with their own distinct socioeconomic profiles (right). Boston behaved much the same. <em>Figs 3 &amp; 6.</em></div>

## What I took from it

What I liked about this work is how little it needed: no new sensors, no survey budget — just the ordinary civic data a city already keeps, read as a portrait of itself. That a place's everyday data exhaust can be a low-cost lens on it is the throughline from my [data-journalism years](/data-journalism/) into CUSP.

The limits are the interesting part. A 311 signature measures *who calls about what*, so it carries the bias of who picks up the phone — and real-estate prices lag, recording decisions made months earlier. None of that sinks the idea; it marks where to be careful. The claim was never that complaints replace the census, only that a city, observed closely, already signals where it's changing — often early enough to act.
