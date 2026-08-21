Title: The same sale, twice, and no way to know
Date: 2026-08-21 12:00
Slug: matching-without-labels
Status: draft
Description: Deciding whether two records describe the same real-world sale, with no labels, no stated cost of a wrong answer, and products downstream that break quietly.

<!-- DRAFT — not published. Reads on a real page at /drafts/matching-without-labels/,
     which robots.txt disallows. Before shipping: remove `Status: draft`, bump the Date,
     resolve the three [confirm] items in the case bank, add the entry to
     content/pages/cases.md + content/pages/all.md, and uncomment the Cases nav group. -->

*A sale happens once in the world and arrives twice in your data. Deciding that the two records are the same event turns out to be a question about who owns the risk.*

---

A sale happens once. It reaches you twice: once from the marketplace where the property was listed, once from the public record filed after the deal closed. The two arrive weeks or months apart, from systems that were never designed to agree, and neither carries a key that points at the other. Somebody has to decide they describe the same event.

In the median case this is easy, and it was already solved before I got to it by a rule set that demanded the two records be close on every axis at once. That rule set was excellent at what it accepted and silent about everything else. The interesting population is the remainder: an address written two defensible ways, a unit label that one side reads as an apartment and the other as a floor, a filing lag long enough that "around the same time" stops being a usable phrase.

Which makes this less a similarity problem than a liability one. You are asserting something irreversible about the world, *these two things are one thing*, on evidence that never quite settles it, and other people's numbers inherit the assertion.

## The constraint nobody warns you about

Everyone expects the no-labels part. The part that cost me months is subtler: the closest thing to labels you have is the output of the strict rule set that came before, and that isn't ground truth, it's a record of what the old system was willing to accept. It was willing to accept the easy cases. So every label you own is drawn from the part of the distribution you have already solved. Fit your gates to that sample and you will reproduce the previous system's blind spot with real fidelity, then report a strong validation number, because you evaluated on the cases it was already good at.

Then there's the cost. Nobody will tell you what a wrong answer is worth. Ask what a false match costs relative to a missed one and every consumer says *it depends*, and they're right, because it depends on which of them is asking. A miss is a gap: an absent number, a listing with no closing attached. A false match is confidently wrong instead of absent, and it propagates — it can credit the wrong person with someone else's sale, or make one property's history contradict itself. Nobody can price that against a gap, and waiting for someone to price it is how a project sits still for a quarter.

<!-- [confirm] — the case bank flags that my own notes disagree on which direction the
     asymmetry actually ran on this project ("low-harm, caught downstream" vs "a false
     positive costs more than a miss"). The paragraph above deliberately states the
     structure of the problem without claiming which way I argued it. Resolve before shipping. -->

## The decision was to stop making it

For a while I treated picking the threshold as my job, on the reasoning that I was the one who understood the score. Wrong reasoning. Understanding the score is why I was the worst person to choose where it cut: the choice is a bet on how much wrongness a team can absorb inside numbers they report, and I didn't own any of those numbers.

What made handing it over an argument rather than a dodge was doing the expensive thing first — hand-labelling a stratified sample across the entire score range, on production data rather than the conservative legacy set. That buys a curve you can stand behind, so the conversation stops being a defence of my judgment and becomes a choice between two rows of a table: at this bar you gain about this many matches, and about this share of them are wrong. Consumers chose. They chose more conservatively than I would have, which was itself worth knowing.

The better answer got forced on us later. One accept/reject bar stopped serving anyone, because the team publishing a number to a customer and the team computing an internal aggregate have no business being held to the same confidence. So the system stopped emitting decisions and started emitting scores, and each consumer applies its own bar. That reads like an architectural detail and it's the actual resolution: the model gets out of the business of having opinions about other people's risk tolerance.

One rule stayed hand-written and outside the model, on purpose: two records can't describe the same sale if they name incompatible units of the same building. The model could learn that perfectly well. I kept it as an explicit veto applied after scoring anyway, because a veto is inspectable one case at a time, sweepable against a labelled set, and reversible without rebuilding anything upstream. A learned feature is none of those things at the moment someone asks why one specific pair was rejected. On a system that feeds attribution, someone always eventually asks.

## What surprised me

Candidate coverage turned out not to be recoverable recall, and I had built a plan on the assumption that it was. Blocking here is geographic, and in a dense market almost every unmatched sale has *some* nearby candidate, so coverage read as a promise. Most unmatched sales did have a candidate scored. Almost none of those candidates cleared any bar worth using, because what the blocker had found was a plausible neighbour rather than the counterpart. I'd been reading a measure of how much work the blocker was doing as a measure of how much recall was sitting there waiting, and those are different quantities.

The one I'd tell a junior colleague about first: calibration is a property of a population, not of a model. Average precision on its own validation set was about as high as it goes, and on an older population the model had never been asked about, its highest-confidence band was wrong far more often than that score implied. Nothing was broken. The score meant exactly what it had been fit to mean, on the distribution it had been fit on, and that distribution was the biased label set from earlier. A calibrated probability is a claim about a population. Move the population and the claim is void, silently, while every metric on the dashboard keeps reporting that things are fine.

## What I'd do differently

Build the hand-labelled stratified sample first — before the model, not to validate it. It cost a few days, it was the only unbiased thing in the project, and everything downstream of it (the curve, the conversation with consumers, the discovery that high confidence didn't travel) either came from it or would have arrived months earlier if it had existed on day one. I built the model first because building the model is the part that feels like the work. The sample was the work.

<!-- One number, from the inventory, if a receipt is wanted here:
     ~21k matches recovered, no threshold loosening. Round it; don't add a second. -->
