Title: Working with AI, or "Sometimes, LLM is just a banana"
Date: 2026-07-21 12:00
Slug: banana-is-just-a-banana
Description: Is it fruit, or is it art? I nearly built a clever feature for the cases my model gets wrong — then measured, and used the LLM as a workhorse instead.

*Is it fruit, or is it art? Is an LLM's real value as an advisor, or as a workhorse?*

---

<!-- review note: domain deliberately abstracted; no product, dataset, or figures named. -->

<div class="marginnote"><strong><a href="https://www.vogue.com/article/the-120000-art-basel-banana-explained-maurizio-cattelan">Comedian</a> (2019).</strong> Maurizio Cattelan duct-taped a banana to a wall and it sold for $120,000. Sometimes the idea is the whole point. Sometimes it's just a banana.</div>

One of those rainy summer days with a thunderstorm, I sat at my coworking; I was looking at the fairly complex and important model I built a while ago — and had just migrated to the new infrastructure. A good opportunity to re-diagnose the performance. As I already knew, the model struggled with co-ops, where the financial situation is both obscure and not publicly available, and disentangling it is a story of its own. We had been trying to pull that data for a while, pretty much to no avail. So I thought — can we train the model on its own mistakes, at \(t-1\), the way a Kalman filter works for robotic sensors, or, say, weather stations ([2006](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005JD006311), [2011](https://journals.ametsoc.org/view/journals/mwre/139/11/2011mwr3653.1.xml))? We could keep the feature from hollowing out by calibrating the "residual" feature against itself (shrink or increase the residual bias while it persists, keep it when the resulting bias is zero). Yes, yes, I was quite proud of myself in anticipation.

But of course, before rushing to implementation, we need to measure the impact. How many buildings do indeed have a _systemic_ error, asked I. And the answer was… not so many; as Claude put it, casually: "at this number, someone should just look into those buildings, not build a feature". And with that, a bulb turned on in my head. For me to go over the financial history of even a dozen big, historic buildings would take more than a week. It was simply not worth it. But now — could I treat my LLM as a workhorse, not just a partner in dialogue? And that's what I did.

<div class="marginnote"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/I_Ritz_Tower%2C_New_York_City%2C_NY%2C_USA_%283%29.jpg/960px-I_Ritz_Tower%2C_New_York_City%2C_NY%2C_USA_%283%29.jpg" alt="The Ritz Tower, a setback skyscraper on Park Avenue, Manhattan.">
<strong>The kind of case.</strong> A landmark like the Ritz Tower can trade at a steep discount for reasons the data never states outright: a land lease, say, with the ground rent buried in an old filing. The market prices it in; the model can't. Photo: <a href="https://commons.wikimedia.org/wiki/User:Elisa.rolle">Elisa.rolle</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</div>

An hour later, I submitted my first tickets to fix data quality: a few land leases, a couple of other nuances. And that was my, perhaps not-so-shiny, moral. It could have been a fancy technique; instead, I ran a "brute force" investigation, and that was it. Sometimes an LLM is just a machine, winning at scale, not at complexity. Sometimes a banana is just a banana.