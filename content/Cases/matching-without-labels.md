Title: The same sale, twice, and no way to know
Date: 2026-08-28 12:00
Modified: 2026-10-02 15:00
Slug: matching-without-labels
Status: draft
Category: Cases
Image: /static/cases/calibration-two-populations.png
Description: Deciding whether two records describe the same real-world sale, with no labels, no stated cost of a wrong answer, and products downstream that break quietly.

*A sale happens once in the world and arrives twice in your data. Deciding that the two records are the same event turns out to be a question about who owns the risk.*

---

A sale happens once. It reaches you twice: once from the marketplace where the property was listed, once from the public record filed after the deal closed. The two arrive weeks or months apart, from systems that were never designed to agree, and neither carries a key that points at the other. Somebody has to decide they describe the same event.

In the median case this is easy, and it was already solved before I got to it by a rule set that demanded the two records be close on every axis at once. That rule set was excellent at what it accepted and silent about everything else. The interesting population is the remainder: an address written two defensible ways, a unit label that one side reads as an apartment and the other as a floor, a filing lag long enough that "around the same time" stops being a usable phrase.

Which makes this less a similarity problem than a liability one. You are asserting something irreversible about the world, *these two things are one thing*, on evidence that never quite settles it, and other people's numbers inherit the assertion.

## The constraint nobody warns you about

Everyone expects the no-labels part. The part that cost me months is subtler: the closest thing to labels you have is the output of the strict rule set that came before, and that isn't ground truth, it's a record of what the old system was willing to accept. It was willing to accept the easy cases. So every label you own is drawn from the part of the distribution you have already solved. Fit your gates to that sample and you will reproduce the previous system's blind spot with real fidelity, then report a strong validation number, because you evaluated on the cases it was already good at.

Then there's the cost, and I had the shape of it wrong for a while. Recall is the objective — the entire point of the project is the matches you don't have. But the constraint that actually binds is precision, and it binds because a false match is not a cheap error. A miss is a gap: an absent number, a listing with no closing attached. A false match is confidently wrong instead of absent, and it travels — it can credit the wrong person with someone else's sale, or make one property's history contradict itself. When one of those reaches a customer, somebody undoes it by hand, and afterwards that pair lives on a blocklist forever, because nobody trusts the system not to make the same call twice.

What makes this genuinely hard rather than merely unpleasant is that the two pressures are both real and point opposite ways. Measured precision on a label set like this is a pessimistic lower bound: a pair you score as wrong may just be a match the old strict rules never admitted, so the number on your slide understates you and you should loosen. Meanwhile every error you do make is expensive, so you should tighten. Nobody is going to settle that for you by naming a price, and waiting for someone to name one is how a project sits still for a quarter.

## The decision was to stop making it

For a while I treated picking the threshold as my job, on the reasoning that I was the one who understood the score. Wrong reasoning. Understanding the score is why I was the worst person to choose where it cut: the choice is a bet on how much wrongness a team can absorb inside numbers they report, and I didn't own any of those numbers.

What made handing it over an argument rather than a dodge was doing the expensive thing first — hand-labelling a stratified sample across the entire score range, on production data rather than the conservative legacy set. That buys a curve you can stand behind, so the conversation stops being a defence of my judgment and becomes a choice between two rows of a table: at this bar you gain about this many matches, and about this share of them are wrong. Consumers chose. They chose more conservatively than I would have, which was itself worth knowing. On the order of twenty thousand matches came back, and the bar never moved.

The better answer arrived later, and by force rather than by design. One global bar stopped serving anyone, because the team publishing a number to a customer and the team computing an internal aggregate have no business being held to the same confidence. What replaced it is a handful of named policies over a score — same decision, different floors, each one attached to a use case and arguable on its own terms — instead of one verdict issued centrally. That reads like a configuration detail and it's the actual resolution: the model gets out of the business of holding opinions about other people's risk tolerance.

One rule stayed hand-written and outside the model, on purpose: two records can't describe the same sale if they name incompatible units of the same building. The model could learn that perfectly well. I kept it as an explicit veto applied after scoring anyway, because a veto is inspectable one case at a time, sweepable against a labelled set, and reversible without rebuilding anything upstream. A learned feature is none of those things at the moment someone asks why one specific pair was rejected. On a system that feeds attribution, someone always eventually asks.

A different rule earned its place the harder way. Time runs one direction, and a listing cannot close long after the deed it supposedly corresponds to was filed. Nothing in the training signal ever gave the model a reason to care, so it scored a batch of those pairs confidently, and every one of them was wrong. A single condition removed the lot. I don't read that as the model losing. It's what a hard physical constraint looks like when you make it compete with a learned score instead of simply stating it.

## What surprised me

Candidate coverage turned out not to be recoverable recall, and I had built a plan on the assumption that it was. Blocking here is geographic, and in a dense market almost every unmatched sale has *some* nearby candidate, so coverage read as a promise. Most unmatched sales did have a candidate scored. Almost none of those candidates cleared any bar worth using, because what the blocker had found was a plausible neighbour rather than the counterpart. I'd been reading a measure of how much work the blocker was doing as a measure of how much recall was sitting there waiting, and those are different quantities.

The one I'd tell a junior colleague about first: calibration is a property of a population, not of a model. Average precision on its own validation set was about as high as it goes, and on an older population the model had never been asked about, its highest-confidence band was wrong far more often than that score implied. Nothing was broken. The score meant exactly what it had been fit to mean, on the distribution it had been fit on, and that distribution was the biased label set from earlier. A calibrated probability is a claim about a population. Move the population and the claim is void, silently, while every metric on the dashboard keeps reporting that things are fine.

<figure>
<svg id="calib-fig" role="img" aria-label="Reliability diagram: two populations, one model" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 518.4 331.2" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <defs>
  <style type="text/css">#calib-fig *{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 331.2 
L 518.4 331.2 
L 518.4 0 
L 0 0 
L 0 331.2 
z
" style="fill: none; opacity: 0"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 49.85 287.02 
L 507.6 287.02 
L 507.6 10.8 
L 49.85 10.8 
L 49.85 287.02 
z
" style="fill: none"/>
   </g>
   <g id="line2d_1">
    <path d="M 58.652885 281.708077 
L 498.797115 16.111923 
" clip-path="url(#p7e17ecc16d)" style="fill: none; stroke-dasharray: 2,3; stroke-dashoffset: 0; stroke: var(--hairline, #b6bbd1)"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_2">
      <defs>
       <path id="me244c36faf" d="M 0 0 
L 0 3 
" style="stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#me244c36faf" x="58.652885" y="287.02" style="fill: var(--hairline, #b6bbd1); stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <text style="font-size: 10px; font-family: inherit; text-anchor: middle; fill: var(--hairline, #b6bbd1)" x="58.652885" y="301.118437" transform="rotate(-0 58.652885 301.118437)">0</text>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <g>
       <use xlink:href="#me244c36faf" x="278.725" y="287.02" style="fill: var(--hairline, #b6bbd1); stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <text style="font-size: 10px; font-family: inherit; text-anchor: middle; fill: var(--hairline, #b6bbd1)" x="278.725" y="301.118437" transform="rotate(-0 278.725 301.118437)">0.5</text>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_4">
      <g>
       <use xlink:href="#me244c36faf" x="498.797115" y="287.02" style="fill: var(--hairline, #b6bbd1); stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <text style="font-size: 10px; font-family: inherit; text-anchor: middle; fill: var(--hairline, #b6bbd1)" x="498.797115" y="301.118437" transform="rotate(-0 498.797115 301.118437)">1</text>
     </g>
    </g>
    <g id="text_4">
     <text style="font-size: 11px; font-family: inherit; text-anchor: middle; fill: var(--muted, #68709a)" x="278.725" y="317.556406" transform="rotate(-0 278.725 317.556406)">what the model said</text>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_5">
      <defs>
       <path id="m3c128e0d4c" d="M 0 0 
L -3 0 
" style="stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m3c128e0d4c" x="49.85" y="281.708077" style="fill: var(--hairline, #b6bbd1); stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <text style="font-size: 10px; font-family: inherit; text-anchor: end; fill: var(--hairline, #b6bbd1)" x="43.35" y="285.507296" transform="rotate(-0 43.35 285.507296)">0</text>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_6">
      <g>
       <use xlink:href="#m3c128e0d4c" x="49.85" y="148.91" style="fill: var(--hairline, #b6bbd1); stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <text style="font-size: 10px; font-family: inherit; text-anchor: end; fill: var(--hairline, #b6bbd1)" x="43.35" y="152.709219" transform="rotate(-0 43.35 152.709219)">0.5</text>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_7">
      <g>
       <use xlink:href="#m3c128e0d4c" x="49.85" y="16.111923" style="fill: var(--hairline, #b6bbd1); stroke: var(--hairline, #b6bbd1); stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <text style="font-size: 10px; font-family: inherit; text-anchor: end; fill: var(--hairline, #b6bbd1)" x="43.35" y="19.911142" transform="rotate(-0 43.35 19.911142)">1</text>
     </g>
    </g>
    <g id="text_8">
     <text style="font-size: 11px; font-family: inherit; text-anchor: middle; fill: var(--muted, #68709a)" x="19.159219" y="148.91" transform="rotate(-90 19.159219 148.91)">how often it was right</text>
    </g>
   </g>
   <g id="line2d_8">
    <path d="M 72.790587 273.785746 
L 124.637409 240.545573 
L 167.244235 226.375545 
L 212.963181 195.475559 
L 256.961579 158.842266 
L 299.773864 142.00143 
L 343.976616 112.692343 
L 388.352162 88.547238 
L 433.857923 51.588666 
L 485.286205 23.851688 
" clip-path="url(#p7e17ecc16d)" style="fill: none; stroke: var(--muted, #68709a); stroke-width: 1.4; stroke-linecap: square"/>
   </g>
   <g id="line2d_9">
    <path d="M 72.072927 273.338021 
L 124.653921 230.452679 
L 168.150148 213.356126 
L 212.77487 196.516858 
L 256.300399 198.253924 
L 301.045289 179.252587 
L 345.802916 166.410522 
L 389.638263 165.073966 
L 433.894751 153.098437 
L 484.655706 130.454678 
" clip-path="url(#p7e17ecc16d)" style="fill: none; stroke: var(--accent, #2e7de9); stroke-width: 1.4; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 49.85 287.02 
L 49.85 10.8 
" style="fill: none; stroke: var(--hairline, #b6bbd1); stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 49.85 287.02 
L 507.6 287.02 
" style="fill: none; stroke: var(--hairline, #b6bbd1); stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="PathCollection_1">
    <path d="M 72.790587 280.343184 
C 74.52964 280.343184 76.1977 279.652251 77.427396 278.422555 
C 78.657092 277.192859 79.348025 275.524799 79.348025 273.785746 
C 79.348025 272.046693 78.657092 270.378633 77.427396 269.148936 
C 76.1977 267.91924 74.52964 267.228307 72.790587 267.228307 
C 71.051534 267.228307 69.383473 267.91924 68.153777 269.148936 
C 66.924081 270.378633 66.233148 272.046693 66.233148 273.785746 
C 66.233148 275.524799 66.924081 277.192859 68.153777 278.422555 
C 69.383473 279.652251 71.051534 280.343184 72.790587 280.343184 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 124.637409 244.923591 
C 125.798473 244.923591 126.912139 244.462296 127.733135 243.641299 
C 128.554131 242.820303 129.015427 241.706637 129.015427 240.545573 
C 129.015427 239.384509 128.554131 238.270843 127.733135 237.449847 
C 126.912139 236.628851 125.798473 236.167556 124.637409 236.167556 
C 123.476345 236.167556 122.362679 236.628851 121.541683 237.449847 
C 120.720687 238.270843 120.259391 239.384509 120.259391 240.545573 
C 120.259391 241.706637 120.720687 242.820303 121.541683 243.641299 
C 122.362679 244.462296 123.476345 244.923591 124.637409 244.923591 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 167.244235 230.270416 
C 168.277167 230.270416 169.267932 229.860028 169.998325 229.129635 
C 170.728718 228.399242 171.139107 227.408477 171.139107 226.375545 
C 171.139107 225.342613 170.728718 224.351848 169.998325 223.621455 
C 169.267932 222.891062 168.277167 222.480674 167.244235 222.480674 
C 166.211303 222.480674 165.220539 222.891062 164.490145 223.621455 
C 163.759752 224.351848 163.349364 225.342613 163.349364 226.375545 
C 163.349364 227.408477 163.759752 228.399242 164.490145 229.129635 
C 165.220539 229.860028 166.211303 230.270416 167.244235 230.270416 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 212.963181 199.28134 
C 213.972486 199.28134 214.940588 198.880339 215.654274 198.166653 
C 216.36796 197.452967 216.768961 196.484864 216.768961 195.475559 
C 216.768961 194.466255 216.36796 193.498152 215.654274 192.784466 
C 214.940588 192.07078 213.972486 191.669779 212.963181 191.669779 
C 211.953876 191.669779 210.985774 192.07078 210.272087 192.784466 
C 209.558401 193.498152 209.1574 194.466255 209.1574 195.475559 
C 209.1574 196.484864 209.558401 197.452967 210.272087 198.166653 
C 210.985774 198.880339 211.953876 199.28134 212.963181 199.28134 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 256.961579 162.552803 
C 257.945625 162.552803 258.889499 162.161837 259.585324 161.466012 
C 260.28115 160.770186 260.672116 159.826312 260.672116 158.842266 
C 260.672116 157.85822 260.28115 156.914346 259.585324 156.21852 
C 258.889499 155.522695 257.945625 155.131729 256.961579 155.131729 
C 255.977533 155.131729 255.033658 155.522695 254.337833 156.21852 
C 253.642007 156.914346 253.251042 157.85822 253.251042 158.842266 
C 253.251042 159.826312 253.642007 160.770186 254.337833 161.466012 
C 255.033658 162.161837 255.977533 162.552803 256.961579 162.552803 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 299.773864 145.651177 
C 300.741788 145.651177 301.670199 145.266617 302.354625 144.582191 
C 303.039051 143.897765 303.423611 142.969354 303.423611 142.00143 
C 303.423611 141.033505 303.039051 140.105094 302.354625 139.420668 
C 301.670199 138.736243 300.741788 138.351682 299.773864 138.351682 
C 298.80594 138.351682 297.877529 138.736243 297.193103 139.420668 
C 296.508677 140.105094 296.124116 141.033505 296.124116 142.00143 
C 296.124116 142.969354 296.508677 143.897765 297.193103 144.582191 
C 297.877529 145.266617 298.80594 145.651177 299.773864 145.651177 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 343.976616 116.230038 
C 344.914824 116.230038 345.814731 115.857284 346.478144 115.193871 
C 347.141557 114.530458 347.514311 113.63055 347.514311 112.692343 
C 347.514311 111.754135 347.141557 110.854227 346.478144 110.190814 
C 345.814731 109.527401 344.914824 109.154647 343.976616 109.154647 
C 343.038408 109.154647 342.138501 109.527401 341.475088 110.190814 
C 340.811675 110.854227 340.438921 111.754135 340.438921 112.692343 
C 340.438921 113.63055 340.811675 114.530458 341.475088 115.193871 
C 342.138501 115.857284 343.038408 116.230038 343.976616 116.230038 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 388.352162 92.562774 
C 389.417095 92.562774 390.438554 92.139672 391.191576 91.386651 
C 391.944597 90.63363 392.367699 89.612171 392.367699 88.547238 
C 392.367699 87.482305 391.944597 86.460846 391.191576 85.707825 
C 390.438554 84.954803 389.417095 84.531701 388.352162 84.531701 
C 387.28723 84.531701 386.26577 84.954803 385.512749 85.707825 
C 384.759728 86.460846 384.336626 87.482305 384.336626 88.547238 
C 384.336626 89.612171 384.759728 90.63363 385.512749 91.386651 
C 386.26577 92.139672 387.28723 92.562774 388.352162 92.562774 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 433.857923 56.007374 
C 435.029778 56.007374 436.153795 55.541791 436.982422 54.713164 
C 437.811049 53.884537 438.276631 52.760521 438.276631 51.588666 
C 438.276631 50.416811 437.811049 49.292794 436.982422 48.464167 
C 436.153795 47.635541 435.029778 47.169958 433.857923 47.169958 
C 432.686068 47.169958 431.562052 47.635541 430.733425 48.464167 
C 429.904798 49.292794 429.439215 50.416811 429.439215 51.588666 
C 429.439215 52.760521 429.904798 53.884537 430.733425 54.713164 
C 431.562052 55.541791 432.686068 56.007374 433.857923 56.007374 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    <path d="M 485.286205 30.324427 
C 487.002795 30.324427 488.64931 29.642418 489.863122 28.428606 
C 491.076935 27.214793 491.758944 25.568279 491.758944 23.851688 
C 491.758944 22.135098 491.076935 20.488584 489.863122 19.274771 
C 488.64931 18.060958 487.002795 17.37895 485.286205 17.37895 
C 483.569615 17.37895 481.9231 18.060958 480.709288 19.274771 
C 479.495475 20.488584 478.813466 22.135098 478.813466 23.851688 
C 478.813466 25.568279 479.495475 27.214793 480.709288 28.428606 
C 481.9231 29.642418 483.569615 30.324427 485.286205 30.324427 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
   </g>
   <g id="PathCollection_2">
    <path d="M 72.072927 279.842261 
C 73.797871 279.842261 75.452399 279.156933 76.672119 277.937213 
C 77.891839 276.717493 78.577166 275.062966 78.577166 273.338021 
C 78.577166 271.613077 77.891839 269.958549 76.672119 268.738829 
C 75.452399 267.519109 73.797871 266.833782 72.072927 266.833782 
C 70.347982 266.833782 68.693455 267.519109 67.473735 268.738829 
C 66.254015 269.958549 65.568687 271.613077 65.568687 273.338021 
C 65.568687 275.062966 66.254015 276.717493 67.473735 277.937213 
C 68.693455 279.156933 70.347982 279.842261 72.072927 279.842261 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 124.653921 234.753666 
C 125.794556 234.753666 126.888628 234.300487 127.695178 233.493936 
C 128.501729 232.687385 128.954908 231.593314 128.954908 230.452679 
C 128.954908 229.312044 128.501729 228.217973 127.695178 227.411422 
C 126.888628 226.604871 125.794556 226.151692 124.653921 226.151692 
C 123.513286 226.151692 122.419215 226.604871 121.612664 227.411422 
C 120.806113 228.217973 120.352934 229.312044 120.352934 230.452679 
C 120.352934 231.593314 120.806113 232.687385 121.612664 233.493936 
C 122.419215 234.300487 123.513286 234.753666 124.653921 234.753666 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 168.150148 217.271005 
C 169.188387 217.271005 170.184241 216.858509 170.918387 216.124364 
C 171.652532 215.390218 172.065028 214.394364 172.065028 213.356126 
C 172.065028 212.317887 171.652532 211.322033 170.918387 210.587887 
C 170.184241 209.853742 169.188387 209.441246 168.150148 209.441246 
C 167.11191 209.441246 166.116056 209.853742 165.38191 210.587887 
C 164.647765 211.322033 164.235269 212.317887 164.235269 213.356126 
C 164.235269 214.394364 164.647765 215.390218 165.38191 216.124364 
C 166.116056 216.858509 167.11191 217.271005 168.150148 217.271005 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 212.77487 200.286269 
C 213.77453 200.286269 214.73338 199.8891 215.440246 199.182234 
C 216.147112 198.475368 216.544281 197.516517 216.544281 196.516858 
C 216.544281 195.517198 216.147112 194.558348 215.440246 193.851482 
C 214.73338 193.144616 213.77453 192.747447 212.77487 192.747447 
C 211.775211 192.747447 210.81636 193.144616 210.109494 193.851482 
C 209.402628 194.558348 209.005459 195.517198 209.005459 196.516858 
C 209.005459 197.516517 209.402628 198.475368 210.109494 199.182234 
C 210.81636 199.8891 211.775211 200.286269 212.77487 200.286269 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 256.300399 202.1417 
C 257.331449 202.1417 258.320409 201.732059 259.049472 201.002997 
C 259.778535 200.273934 260.188175 199.284974 260.188175 198.253924 
C 260.188175 197.222874 259.778535 196.233914 259.049472 195.504851 
C 258.320409 194.775788 257.331449 194.366148 256.300399 194.366148 
C 255.269349 194.366148 254.280389 194.775788 253.551326 195.504851 
C 252.822264 196.233914 252.412623 197.222874 252.412623 198.253924 
C 252.412623 199.284974 252.822264 200.273934 253.551326 201.002997 
C 254.280389 201.732059 255.269349 202.1417 256.300399 202.1417 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 301.045289 182.883189 
C 302.008136 182.883189 302.931676 182.500646 303.612512 181.81981 
C 304.293347 181.138975 304.675891 180.215434 304.675891 179.252587 
C 304.675891 178.28974 304.293347 177.3662 303.612512 176.685364 
C 302.931676 176.004529 302.008136 175.621986 301.045289 175.621986 
C 300.082442 175.621986 299.158901 176.004529 298.478066 176.685364 
C 297.79723 177.3662 297.414687 178.28974 297.414687 179.252587 
C 297.414687 180.215434 297.79723 181.138975 298.478066 181.81981 
C 299.158901 182.500646 300.082442 182.883189 301.045289 182.883189 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 345.802916 170.243516 
C 346.819438 170.243516 347.794463 169.839647 348.513252 169.120858 
C 349.232042 168.402068 349.63591 167.427044 349.63591 166.410522 
C 349.63591 165.394 349.232042 164.418975 348.513252 163.700186 
C 347.794463 162.981396 346.819438 162.577528 345.802916 162.577528 
C 344.786394 162.577528 343.81137 162.981396 343.09258 163.700186 
C 342.373791 164.418975 341.969922 165.394 341.969922 166.410522 
C 341.969922 167.427044 342.373791 168.402068 343.09258 169.120858 
C 343.81137 169.839647 344.786394 170.243516 345.802916 170.243516 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 389.638263 169.031063 
C 390.687697 169.031063 391.694291 168.614118 392.436353 167.872056 
C 393.178415 167.129994 393.595359 166.123401 393.595359 165.073966 
C 393.595359 164.024532 393.178415 163.017939 392.436353 162.275877 
C 391.694291 161.533815 390.687697 161.11687 389.638263 161.11687 
C 388.588829 161.11687 387.582235 161.533815 386.840173 162.275877 
C 386.098111 163.017939 385.681167 164.024532 385.681167 165.073966 
C 385.681167 166.123401 386.098111 167.129994 386.840173 167.872056 
C 387.582235 168.614118 388.588829 169.031063 389.638263 169.031063 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 433.894751 157.48979 
C 435.059352 157.48979 436.17641 157.02709 436.999907 156.203593 
C 437.823404 155.380096 438.286105 154.263037 438.286105 153.098437 
C 438.286105 151.933836 437.823404 150.816778 436.999907 149.993281 
C 436.17641 149.169784 435.059352 148.707083 433.894751 148.707083 
C 432.730151 148.707083 431.613092 149.169784 430.789595 149.993281 
C 429.966098 150.816778 429.503397 151.933836 429.503397 153.098437 
C 429.503397 154.263037 429.966098 155.380096 430.789595 156.203593 
C 431.613092 157.02709 432.730151 157.48979 433.894751 157.48979 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    <path d="M 484.655706 137.012117 
C 486.394759 137.012117 488.062819 136.321184 489.292515 135.091487 
C 490.522212 133.861791 491.213145 132.193731 491.213145 130.454678 
C 491.213145 128.715625 490.522212 127.047565 489.292515 125.817869 
C 488.062819 124.588173 486.394759 123.89724 484.655706 123.89724 
C 482.916653 123.89724 481.248593 124.588173 480.018897 125.817869 
C 478.789201 127.047565 478.098268 128.715625 478.098268 130.454678 
C 478.098268 132.193731 478.789201 133.861791 480.018897 135.091487 
C 481.248593 136.321184 482.916653 137.012117 484.655706 137.012117 
z
" clip-path="url(#p7e17ecc16d)" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
   </g>
   <g id="patch_5">
    <path d="M 359.28636 31.207642 
Q 419.292787 27.704427 479.299213 24.201213 
" style="fill: none; stroke: var(--hairline, #b6bbd1); stroke-width: 0.7; stroke-linecap: round"/>
   </g>
   <g id="text_9">
    <text style="font-size: 10px; font-family: inherit; text-anchor: start; fill: var(--muted, #68709a)" x="243.513462" y="37.463029" transform="rotate(-0 243.513462 37.463029)">a 0.9 meant about 0.9</text>
   </g>
   <g id="patch_6">
    <path d="M 354.284768 215.348392 
Q 416.957748 174.537594 479.630728 133.726796 
" style="fill: none; stroke: var(--hairline, #b6bbd1); stroke-width: 0.7; stroke-linecap: round"/>
   </g>
   <g id="text_10">
    <text style="font-size: 10px; font-family: inherit; text-anchor: start; fill: var(--accent, #2e7de9)" x="265.520673" y="226.036298" transform="rotate(-0 265.520673 226.036298)">same score, roughly a coin flip</text>
   </g>
   <g id="legend_1">
    <g id="PathCollection_3">
     <path d="M 268.7125 264.798319 
C 269.550842 264.798319 270.35496 264.465242 270.947757 263.872445 
C 271.540555 263.279648 271.873631 262.475529 271.873631 261.637187 
C 271.873631 260.798846 271.540555 259.994727 270.947757 259.40193 
C 270.35496 258.809133 269.550842 258.476056 268.7125 258.476056 
C 267.874158 258.476056 267.07004 258.809133 266.477243 259.40193 
C 265.884445 259.994727 265.551369 260.798846 265.551369 261.637187 
C 265.551369 262.475529 265.884445 263.279648 266.477243 263.872445 
C 267.07004 264.465242 267.874158 264.798319 268.7125 264.798319 
z
" style="fill: var(--muted, #68709a); fill-opacity: 0.95"/>
    </g>
    <g id="text_11">
     <text style="font-size: 10px; font-family: inherit; text-anchor: start; fill: var(--text, #1f2f66)" x="282.7125" y="264.262187" transform="rotate(-0 282.7125 264.262187)">the population the model was fit on</text>
    </g>
    <g id="PathCollection_4">
     <path d="M 268.7125 279.495348 
C 269.555855 279.495348 270.364783 279.16028 270.961125 278.563937 
C 271.557467 277.967595 271.892536 277.158668 271.892536 276.315313 
C 271.892536 275.471957 271.557467 274.66303 270.961125 274.066688 
C 270.364783 273.470345 269.555855 273.135277 268.7125 273.135277 
C 267.869145 273.135277 267.060217 273.470345 266.463875 274.066688 
C 265.867533 274.66303 265.532464 275.471957 265.532464 276.315313 
C 265.532464 277.158668 265.867533 277.967595 266.463875 278.563937 
C 267.060217 279.16028 267.869145 279.495348 268.7125 279.495348 
z
" style="fill: var(--accent, #2e7de9); fill-opacity: 0.95"/>
    </g>
    <g id="text_12">
     <text style="font-size: 10px; font-family: inherit; text-anchor: start; fill: var(--text, #1f2f66)" x="282.7125" y="278.940313" transform="rotate(-0 282.7125 278.940313)">a population it had never been asked about</text>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p7e17ecc16d">
   <rect x="49.85" y="10.8" width="457.75" height="276.22"/>
  </clipPath>
 </defs>
</svg>
<figcaption><strong>One model, one score, two populations.</strong> Synthetic data, real shape. On the population the model was fit on, a 0.9 means about 0.9. On one it was never shown, the same 0.9 is roughly a coin flip, and nothing on the first population’s dashboard moves. Dot size is how many pairs landed in each bin.</figcaption>
</figure>

## What I'd do differently

Build the hand-labelled stratified sample first — before the model, not to validate it. It cost a few days, it was the only unbiased thing in the project, and everything downstream of it (the curve, the conversation with consumers, the discovery that high confidence didn't travel) either came from it or would have arrived months earlier if it had existed on day one. I built the model first because building the model is the part that feels like the work. The sample was the work.
