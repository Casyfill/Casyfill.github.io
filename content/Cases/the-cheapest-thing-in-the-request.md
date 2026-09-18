Title: The model was the cheapest thing in the request
Date: 2026-09-18 12:00
Slug: the-cheapest-thing-in-the-request
Status: draft
Description: A hard latency budget on a prediction service, and the discovery that the model spent almost none of it — the budget was going to fetching, not to thinking.

*I kept arguing about which model. The budget was being spent somewhere else entirely.*

---

A prediction is only worth what someone can do with it, and what someone can do with it usually depends on getting it inside a page load. So at some point the model stops being a model and becomes a field on an API response, sitting next to a dozen other fields, resolved by a dozen other teams, all of them assembling one screen for one impatient person.

That API had a hard budget. Not a target, not a nice-to-have — a number in a document, agreed with the people who own the page, and the page is slow if any one of us is slow. A hundred milliseconds. A few thousand requests a minute, all day, every day. Everything I'd shipped over several years was reachable through that one door.

I came to it thinking about it the way a modeller thinks about it: which model can I afford. A bigger one is more accurate and more expensive to run, so somewhere there's a curve and I should find the point on it where accuracy stops being worth the milliseconds. That's the conversation the literature is set up for, it's the conversation in every system-design interview, and I had it with myself several times.

## The constraint

Then I measured where the time actually went, which I should have done first.

Server-side compute — the actual prediction, the thing I'd been agonising over — was a couple of hundred *micro*seconds. The request's p95 was around fifty milliseconds. The budget was a hundred. So the model was using something on the order of a third of one percent of the time available to it, and the other ninety-nine-and-change percent was the service going and getting things.

That ratio is the whole case, and it inverts the question. I could have doubled the model's cost, or quadrupled it, and no dashboard anywhere would have twitched. The curve I'd been trying to find the optimum on was flat across the entire range I could plausibly want. Meanwhile a single call out to the service that authoritatively owns one of the input fields cost more, on its own, than everything else on the path put together. The expensive thing was never the arithmetic. It was the fetching.

That's an uncomfortable finding if you arrived as a modeller, because it means the interesting decision isn't yours by training. It's a decision about where data lives.

## The decision

The clean design is that each service owns its data and you ask it. Every architecture review will tell you this and every architecture review is right: one authoritative copy, one team responsible for it, nobody serving a stale answer because nobody has a second copy to go stale. It's correct, and under a hundred-millisecond budget with fan-out, it doesn't fit.

So I stopped asking and started keeping. A stream carrying every change to the fields I needed, landing them in an in-memory store that sits next to the serving path, and a read that never leaves the neighbourhood. Cache, compute, or precompute is the actual decision underneath most serving work, and it gets made on latency and re-litigated on cost and correctness forever after.

What you give up is not obvious until you've operated it for a while. You don't give up accuracy. You give up *authority*: you're now serving a copy, and the copy is behind by however long the pipeline takes. Which means somebody has to answer how stale is acceptable, and that turns out to be a product question wearing an infrastructure costume. It isn't one answer, either. A description that's a few minutes out of date is invisible to everyone. A listing that has come off the market and still reads as available is a customer complaint and possibly worse. Content staleness you can cache through. Availability staleness you cannot, ever, and the freshness requirement for the whole service is set by that one field rather than by an average across fields.

The other thing you give up is that you now run a stateful system. I'd written a model. I now operated a store, with a memory ceiling, an eviction policy, and a failure mode.

## What surprised me

The first surprise is the ratio, and I've never fully got over it. Every conversation I'd had about this system, mine included, was a conversation about models — which one, how big, how often retrained — and all of them were arguments about a rounding error inside a budget dominated by data movement. Owning both ends is the only reason I know that. From the model side you can't see it, because the profiler stops at your function boundary and reports that you're fast. From the serving side you can't see it either, because to a backend engineer the prediction is an opaque call that might cost anything, and nobody tells you it's basically free. The thing worth knowing lives exactly on the seam, and it's visible from neither room.

The second surprise cost me a day of production degradation and I'd rather have learned it cheaply.

I resized that store down. Before doing it I did real, careful work on the risk I could see: the smaller instance class has a different CPU behaviour under sustained load, and I wanted proof it would hold the traffic. I got the proof. The analysis was sound, the load was fine, CPU never came close. It was also entirely beside the point. The constraint that actually bound was memory, against a store whose contents can double when an upstream replays, and I had sized against the amount of data in it *after* I'd just pruned it rather than against the amount it can hold. I gave the interesting question my full attention and the binding question a glance, and I'm fairly sure I did that because one of them looked like a problem and the other looked like a lookup.

There was a third, smaller one worth the sentence: a substantial share of the reads turned out to be for records the design had quietly assumed almost nobody would ask about. What a cache is *for* is an empirical question and I'd answered it from the architecture diagram.

## What I'd do differently

Put the safety valve in even when the reasoning says it's redundant. I'd decided against expiring entries because a separate job already removed the cold ones, so expiry added nothing — which was true for the steady state, and the steady state was not the thing that hurt me. I optimised for the expected case and left no behaviour at all for the unexpected one, which is a habit worth naming because it doesn't feel like a shortcut while you're doing it; it feels like removing a redundancy. And I shipped the change before the alarms that would have caught it, having told myself, in writing, in that same week, that "I'll notice" is not a control. Alarms first, then the risky change. That ordering is free and I got it backwards.

<!-- [confirm] before shipping: this piece publishes a production incident, abstracted — no service names, no vendor, no dates, no figures, and framed entirely as my own error. Read it once with that in mind. If it's too close, the section can be cut to the ratio + the traffic-shape surprise and the piece still stands, ~250 words shorter. -->
