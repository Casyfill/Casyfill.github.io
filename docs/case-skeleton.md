# Case skeleton

Template for a `/cases/` write-up. Lives in `docs/` so Pelican never builds it.
Copy into `content/Cases/<slug>.md`, fill in, add the entry to
`content/pages/cases.md` and `content/pages/all.md`.

Source of truth for what to write and what not to: the Case Bank note in the
vault (`SPC Case Bank — Shipped Work to Publishable Cases`). Every case has a
**Leak line** there — read it before drafting.

---

```markdown
Title: <the problem, stated as a problem — not the project name>
Date: YYYY-MM-DD 12:00
Slug: <kebab-slug>
Description: <one sentence, ~150 chars, reused as the meta description and the share card>
Image: /static/cases/<slug>/<card>.png   # optional, only if there's a real visual

*<the dek — one italic line, same sentence in a different key than the Description>*

---

<!-- 1. THE PROBLEM (2–3 paragraphs)
     Abstract the object, keep the constraint. Open on the constraint, not on
     context-setting. No internal product, service, dataset or table names. -->

<!-- 2. THE CONSTRAINT THAT MADE IT HARD (1–2 paragraphs)
     The thing a reader wouldn't guess. Usually: no labels, a hard budget, an
     asymmetric cost nobody will quote you, or a downstream consumer that
     breaks quietly. -->

<!-- 3. THE DECISION (2–3 paragraphs)
     Publish the decision, not the configuration. The reasoning about why that
     *class* of decision is hard, and how the tradeoff got resolved. No feature
     lists, thresholds, model families, prompts, or architecture diagrams. -->

<!-- 4. WHAT SURPRISED ME (1–2 paragraphs)
     Non-negotiable. This is the paragraph that makes the piece more than common
     knowledge. If nothing surprised you, write a different case. -->

<!-- 5. WHAT I'D DO DIFFERENTLY (1 paragraph)
     Concrete, not humble-bragging. Ends the piece on substance. -->
```

## Checks before it ships

- **Seam test.** What did owning both sides of this boundary let me see that a
  specialist wouldn't? If the piece doesn't answer that, it's a fine post but
  it isn't doing positioning work.
- **Anti-trite test, per paragraph.** Could a competent person who has never
  done this have written this paragraph? If yes, cut it.
- **One number, and only from the Career inventory.** Round it. Never restate a
  number that isn't already there.
- **Build passes and the page has a card.**
  `PATH="$HOME/.local/bin:$PATH" pelican content -o /tmp/out -s publishconf.py`,
  then confirm `og:title` and `<meta name="description">` in
  `/tmp/out/<slug>/index.html`.
- Added to `content/pages/cases.md`, `content/pages/all.md`, and `NAV_GROUPS`.
