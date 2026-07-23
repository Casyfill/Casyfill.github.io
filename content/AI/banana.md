Title: Working with AI, or "Sometimes, LLM is just a banana"
Date: 2026-07-21 12:00
Slug: banana-is-just-a-banana

*Work in progress: is it fruit, or is it art? Is an LLM's real value as an advisor, or as a workhorse?*

---

<!-- review note: domain deliberately abstracted; no product, dataset, or figures named. -->

<div class="marginnote"><img src="https://assets.vogue.com/photos/5deec22ee52fbd00086eb689/master/w_800,c_limit/01-%2010492891h.jpg" alt="A banana duct-taped to a white wall — Maurizio Cattelan's artwork Comedian.">
<strong><a href="https://www.vogue.com/article/the-120000-art-basel-banana-explained-maurizio-cattelan">Comedian</a> (2019).</strong> Maurizio Cattelan's banana, duct-taped to a wall and sold for $120,000. Sometimes the idea is the whole point. Sometimes it's just a banana. Photo: Rhona Wise / EPA-EFE / Shutterstock.</div>

One of those rainy summer days with a thunderstorm, I sat at my coworking; I was looking at the fairly complex and important model I built a while ago - and just migrated to the new infrastructue. This was a good opportunity to re-diagnose the performance. As I already knew, model struggled with coops, where financial situation is always both obscure and not plublicly awailable, and disentangling it is a story of it's own. We were trying to pull this data for a while, but pretty much to no avail. So I thought - can we train the model on it's own mistakes, at \(t-1\), like Kalman filter works for the robotic sensors - or, say, weather stations ([2006](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2005JD006311), [2011](https://journals.ametsoc.org/view/journals/mwre/139/11/2011mwr3653.1.xml))? We could prevent the feature for hallowing-out by calibrating "residual" feature by itself (e.g. shrink/increase residual bias while it persists, and keep it when resulting bias is zero). Yes, yes, I was quite proud of my self in anticipation.

But of course, before rushing to implementation, we need to measure the impact. How many buildings indeeed have a _sistemic_ error, asked I. And the answer was... not so many; as Claude put it, casually: "at this number, someone should just look into those buildings, not build a feature". And with that, bulb turned on in my head. Of course, for me to go over a financial history for even a dozen of big, historic buildings, would take more than a week. It was simply not worth it. But now, I can treat my LLM as a workhorse - not just a partner in a dialogue? And that's what i did. 

<div class="marginnote"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/I_Ritz_Tower%2C_New_York_City%2C_NY%2C_USA_%283%29.jpg/960px-I_Ritz_Tower%2C_New_York_City%2C_NY%2C_USA_%283%29.jpg" alt="The Ritz Tower, a setback skyscraper on Park Avenue, Manhattan.">
<strong>The kind of case.</strong> A landmark like the Ritz Tower can trade at a steep discount for reasons the data never states outright: a land lease, say, with the ground rent buried in an old filing. The market prices it in; the model can't. Photo: <a href="https://commons.wikimedia.org/wiki/User:Elisa.rolle">Elisa.rolle</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>.</div>

An hour later, I submitted my first tickets to fix data quality: few land leases, couple of other nuances. And that was my, perhaps not-so-shiny, moral; It could have been a fancy technique; Instead, I ran with a "brute force" investigation, and that was it. Sometimes, LLM is just a machine, winning at scale, not complexity. Sometimes, banana is just a banana.