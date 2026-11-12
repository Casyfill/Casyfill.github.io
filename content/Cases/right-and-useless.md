Title: A flag that was right and useless
Date: 2026-09-11 12:00
Slug: right-and-useless
Status: draft
Category: Cases
Description: A listing flag with near-perfect recall that nobody could act on, and a language model that failed by rounding the hard cases up rather than by inventing anything.

*It caught everything it was supposed to catch. That turned out to be the problem.*

---

A listing has structured fields and it has a paragraph of prose, and the prose is where everything interesting hides. Whether the kitchen was redone. Whether a tenant is still in it. Whether the seller is in a hurry. None of that has a column, all of it is what a buyer actually wants to filter on, and people type those words into the search box every day.

So there was a flag. Somewhere upstream, a pattern read the description and set a boolean: this home has been renovated. It had close to perfect recall — if a listing said anything about a renovation, the flag caught it. By the only measure anyone had applied to it, it worked.

It was also close to useless, and it took reading a couple of hundred descriptions by hand to see why. The word was doing at least five jobs. The whole apartment was gut-renovated. The kitchen and one bathroom were done and nothing else was. The *building* was renovated — a new lobby, a roof deck, a gym — and the apartment was untouched. It was renovated, twenty years ago. Or the description mentioned a renovated park two blocks away, which is a sentence written for a search engine rather than for a person. Roughly two-thirds of what the flag caught were the first case, about a third were the second, and a small remainder weren't about the home at all. To a buyer those are not variations on a theme. The first and the third are opposite listings.

## The constraint

There was no ground truth, which everyone expects, and the usual answer is to go make some. That answer is right and it hides a trap I walked into.

You start by sampling at random from what the flag catches and labelling it by hand, because a random sample is the only thing that tells you what the population really looks like. It does that job well. It also cannot do the job you most need, and the reason is arithmetic rather than effort: the failure that embarrasses you — a listing flagged as renovated where nothing about the home was renovated — is rare. Sample a couple of hundred listings at random and you'll get one, perhaps two. You can label for a day and come away unable to say anything at all about whether the model catches the error you actually care about, while the accuracy number on your slide looks terrific, because it was computed almost entirely on easy cases.

The fix is to build a second set that is deliberately *not* representative: go hunting for the failure shapes on purpose, in rough quotas — building amenities rather than the home, negations and promises ("to be renovated", "renovation potential"), renovations dated far enough back to be irrelevant, plus a slice of ordinary positives as a control. Now you can measure the rare failure, because you went and concentrated it.

And now you own a number you must never quote. That set is enriched with failures by construction, so its headline accuracy is worse than reality and means nothing as an estimate of anything. Its composition is not the population's composition. It answers one question — does the model catch this failure — and it is silent on every other. I wrote that caveat into the notes in the strongest terms I could, because the set is genuinely useful and the number attached to it is genuinely misleading, and those two facts travel together into every meeting.

Two sets, then, each answering precisely what the other structurally cannot. I don't know a way around needing both.

## The decision

The obvious move is to ask the model the question you want answered: read this description, tell me whether the home is fully renovated, partly renovated, or not renovated at all. That version was mediocre, and it was mediocre in a specific direction I'll come back to.

What worked was taking the judgment away from it. The model gets asked only for plain facts that are either present in the text or not — what was renovated, when, whether it happened or is being promised. Then ordinary code, which I wrote and can read a year from now, applies the rules that turn those facts into a grade. Accuracy went up and the hard middle category nearly doubled its recall, and the gain came from the rules, not from a bigger model.

I've since come to think that's the general shape rather than a trick that worked once. A judgment call embeds a business definition — *how much of an apartment has to be new before a buyer would call it renovated* — and that definition is contested, it changes, and someone will eventually need to argue about it in a meeting. Bury it in a prompt and it becomes unversioned, untestable, and invisible to everyone who isn't reading prompts that week. Put the facts in the model and the definition in code and you can change your mind about the definition on a Tuesday without touching the extraction, and you can point at the line where the decision lives.

The check I trust most is cheap and I nearly skipped it. Grade the whole corpus — around a hundred and sixty-four thousand descriptions — and look at what share came back in the partial bucket, then compare that to the share in the hand-labelled random sample. They matched. That's not a precision or recall number and it doesn't replace either, but it's the one signal that comes from the whole population instead of from the couple of hundred rows you happened to look at. If those two had diverged, every clean metric I had would have been describing a sample rather than the corpus.

## What surprised me

The model never invented anything. I went in braced for fabrication, since that's the failure everybody writes about, and I found none of it — no imagined renovation, no hallucinated year, nothing asserted that wasn't in the text.

It failed by *rounding*. Handed a description of a kitchen and a bathroom and asked for one verdict, it called the apartment fully renovated most of the time. Not by inventing rooms. By resolving a genuinely ambiguous case toward the cleaner, more common, more confident-sounding answer — which is roughly what an unmotivated human skimming quickly would also do. The errors weren't scattered where a wrong guess would put them. They collapsed toward the majority label, which means the model had learned the shape of the answer without being able to hold the distinction that made the field worth having. That's a much quieter failure than a hallucination, and it survives every check that a hallucination trips: it's plausible, it's consistent, it agrees with itself, and it produces exactly the label a busy reviewer expects to see.

The second surprise came from being on the other side of the boundary. I owned the extraction and I also owned the contract this thing is published under, which meant I couldn't stop at a better model. A single boolean has no room to be right in. Two-thirds and one-third of a flagged population were being asked to share one bit, and no amount of accuracy fixes a field that can't represent the answer. The real change was to the schema — from a flag to something graded — and a model improvement alone would have gone on producing a well-measured number that no one downstream could act on. If I'd handed the classifier off at the model boundary I'd have shipped 0.87 and called it a good quarter.

## What I'd do differently

Label first. Two or three hundred rows per attribute, hand-read, both sets, *before* writing a single prompt — because the labelling is what taught me the category had five meanings, and I learned that after building something that assumed it had two. That ordering wasn't a nicety, it was the whole finding arriving late. And one honest gap: I never measured what this bought the models downstream. I know it's consumed, I believe the argument that one better field improves several models at once, and I have exactly no numbers for it — which, on a project whose entire premise was that a field nobody had measured properly was quietly degrading everything it touched, is a joke I should have seen coming.
