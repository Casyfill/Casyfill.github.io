Title: This is not a pipe
Date: 2026-07-21 12:00
Slug: banana-is-just-a-banana
Description: Two cases of working with an LLM on our own tools — and how, each time, the AI ended up somewhere other than where I planned to put it.

*Working with a tool, on a tool — and where the line between them moved.*

---

<!-- review note: domain deliberately abstracted; no product, dataset, or figures named. -->

In *Systems Thinking*, Jamshid Gharajedaghi writes that "dissolving a problem transforms it and generates a whole new set of concerns." Solving a major constraint does not just expose the next bottleneck in an otherwise unchanged system. The conditions of success change, and the system has to change with them.

I keep coming back to this now that much of my work is done together with an LLM. We build tools, and we build them with a tool. The two cases below are small, but in both, the constraint I had planned around disappeared — and <mark>what replaced it was not the next item on the same list</mark>. Where the AI belonged changed, who knew what changed, and so did what was worth building at all.

<figure class="column"><img src="/static/cases/magritte-pipe.jpg" style="max-width:378px;width:100%" alt="Magritte's painting of a pipe, with the words Ceci n'est pas une pipe written beneath it">
<figcaption>René Magritte, <a href="https://en.wikipedia.org/wiki/The_Treachery_of_Images"><em>The Treachery of Images</em></a> (1929). <em>Ceci n'est pas une pipe</em> — this is not a pipe. It is a picture of one. © René Magritte estate; shown for commentary.</figcaption></figure>

## Just look at the buildings

<div class="marginnote"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/I_Ritz_Tower%2C_New_York_City%2C_NY%2C_USA_%283%29.jpg/960px-I_Ritz_Tower%2C_New_York_City%2C_NY%2C_USA_%283%29.jpg" alt="The Ritz Tower, a setback skyscraper on Park Avenue, Manhattan.">
<strong>The kind of case.</strong> A landmark like the Ritz Tower can trade at a steep discount for reasons the data never states outright: a land lease, say, with the ground rent buried in an old filing. The market prices it in; the model can't. Photo: <a href="https://commons.wikimedia.org/wiki/User:Elisa.rolle">Elisa.rolle</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</div>

I was reviewing a valuation model I had built a while ago and had just migrated to new infrastructure — a good moment to re-diagnose it. I already knew one weak spot: some buildings had a big, one-sided error, consistent from sale to sale — which was a signal in itself.

So I set out to fix it as a model improvement: a rolling calibration that would estimate each building's persistent bias from its past prediction errors and correct for it, inspired by the way a Kalman filter updates its estimate as new observations arrive. I was quite proud of myself, and already thought of presenting the fix to the team.

Before building anything, I asked the agent to investigate whether my hypothesis held up. Instead of approval, it suggested investigating those twenty or so buildings online — and so I asked it to do just that.

Two hours and hundreds of legal documents, newspaper articles and forum posts later, I had enough evidence to file my first CS ticket. When I was done, the next day, half of those buildings turned out to be land-leased, and the other half had their own tricky legal issues.

I had been trying to make up for missing information with another layer of modeling. But that information was not hidden in a statistical pattern; it was written down, in documents too expensive for me to read. <mark>The constraint had been my time. Once that disappeared, the model I had planned to build no longer made sense.</mark>

## A regex, written by the model

The second case went the other way.

We needed to normalize apartment unit strings — the "4A" or "PH4A" part of an address. It looks like an easy problem, but our data has a long tail of specific cases, and the existing packages handled them badly.

<div class="marginnote"><img src="/static/cases/unit-parsing-flow.png" alt="Diagram of one unit string, Apt. #PH4A/B (terrace), going through clean, classify, split and read steps to exact keys PH4A and PH4B and partial keys 4A and 4B; grey boxes show the branches it did not take">
<strong>One unit string, split and diced.</strong> Blue is the path this string takes; grey is every branch it could have taken.</div>

My plan was to put AI in the product: let a model parse the strings at runtime and make sense of them. Instead, the agent wrote a plain regex package, end to end. It stayed in the workshop, and what shipped was ordinary code.

<mark>I delegated the implementation, but not the architecture.</mark> Three things were fixed up front: a two-function interface as the only public surface; a basic test set the agent could not change without my approval, which I checked in every commit; and ADRs — short architecture decision records — specifying the normalization rules and edge-case policies, as the contract between developers, the LLM included.

Here the constraint was writing and maintaining many fiddly rules. Once that was cheap, the hard part moved somewhere else.

## Who knows what

Constraints are one side of these stories. Knowledge is another: where it came from, and who was right when we disagreed.

In the first case, the model contradicted my *method*, and it was right: my knowledge came from general experience, while it had looked at the actual buildings. In the second, it contradicted my *facts*, and it was wrong — for a good reason. It insisted that "PH 4A" and "4A" are different units, because in our data they are; they should have been merged and never were. <mark>The model was faithful to the data; the data was not faithful to the world.</mark> Like Magritte's pipe, a string in our records is a picture of an apartment, not the apartment. I overruled it, and the merge is my next task.

## What moved

In the first case I planned a model, and the AI did the research instead. In the second I planned AI in the product, and it became the builder. Each time, removing one constraint did more than reveal the next one. <mark>It changed what was worth building</mark>: once looking is cheap, a model can be unnecessary; once code is cheap, the questions are about data, specification and judgment. And it changed my part in the work: less writing, more choosing which problem is worth solving, where the agent's work ends, and which source of knowledge to trust.

I don't have answers here, but I have questions:

- **What is the real constraint?** Do we truly lack the information, or is it just too unstructured to collect — scattered across filings, newspaper articles and forum posts?
- **What actually needs reasoning at runtime?** Which problems need dynamic, context-aware judgment on every call, and which are deterministic rules — regex trees, state machines — too tedious for a person to build and maintain, but not for a machine?
- **Whose knowledge is right?** The patterns in the actual data, or the common sense in a person's head? Probably neither, fully.

The line between the tool we build and the tool that helps us build it keeps getting harder to draw. I don't yet know how to draw it clearly — only that I keep needing to.

---

**References**

- Jamshid Gharajedaghi, *Systems Thinking: Managing Chaos and Complexity*, 3rd ed., Morgan Kaufmann, 2011 — §1.4 "Change of the Game," pp. 6–8. His example is Ford: success at mass production moved the challenge to markets and diversity, and the strategy that won became a liability.
