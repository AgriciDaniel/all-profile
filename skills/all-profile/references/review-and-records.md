# Review and durable handoff

## Review the right version

For a multi-platform job, keep a lightweight current record with the brief, source ledger, copy version, before-state, approved changes, after-state, and next actions. Use Markdown or JSON as appropriate. Store records outside the skill directory. Avoid building a large document hierarchy for a one-field request.

Suggested field record:

```json
{
  "platform": "example-platform",
  "account_url": "https://example.com/profile",
  "field": "bio",
  "before": null,
  "before_status": "not_captured",
  "proposed": "Fictional example text, not approved for use.",
  "version": "draft-1",
  "sources": [],
  "approval": null,
  "actual_after": null,
  "status": "draft",
  "verification": [],
  "remaining": ["Capture the current field before proposing a live edit."]
}
```

Use precise states: `draft`, `approved`, `save_reported`, `saved_reloaded`, `visitor_verified`, `blocked`, or `retained`. Record partial progress per field rather than hiding it behind an account-wide “complete.” Include timestamps, viewer surfaces, source references, and the authorization reference where applicable. An empty field and an uncaptured field are different.

On resume, read the newest field-specific observations and explicit owner decisions. Resolve contradictions by artifact version and evidence scope, not merely a shared date or a filename saying “final.” An old approval does not cover new wording. Preserve historical records but label them and point the start page to actual current state.

## Editorial review

Check clear association, audience relevance, proof, cross-platform consistency, field fit, visual clarity, and the next step. Inspect the exact artifact being delivered. For every substantive finding name the phrase or field, evidence, consequence, and concrete fix. Record the strongest objection to the recommended positioning and distinguish it from a factual blocker.

Reject unsupported achievements, misleading access promises, and borrowed credentials. Mark missing editor or visual evidence unresolved. Do not penalize unknown evidence with a zero. Preserve user-requested style when it works; a generic preference for fewer emojis is not evidence that a reference-driven design is wrong.

If a numerical editorial score helps the user, optional weights are association 25, audience 15, proof 20, consistency 10, field fit 10, visuals 10, next step 10. Rate observed dimensions 0-4. Compute earned points as weight times rating divided by 4; measured coverage is the sum of rated weights. Partial quality is earned points divided by measured coverage times 100. At zero coverage, quality is undefined. Show unrated dimensions and coverage alongside the score. Explain any not-applicable dimension and denominator adjustment.

These are local editorial weights, not an algorithmic ranking model. No score overrides unsupported claims, missing approval, or an unverified destination. A before/after score comparison needs equivalent evidence and criteria.

## Deliverables and exports

Keep one current copy source. Optional spreadsheets should provide platform, field, exact text, clearly labeled count method, placement, sources, and draft/applied status. Preserve unrelated sheets. After saving, reopen and compare every exported string with that source, inspect formula errors and proof arithmetic, and visually review wrapping and emoji. Spreadsheet previews do not prove social-app rendering.

If a live edit diverges from the draft, record the authorized actual value. Regenerate the current handoff or prominently mark an older export as historical with a pointer to the new record. Never claim a workbook is current because it opens successfully.

End with the observed outcome, actual changes or paste-ready proposal, validation performed, blocked fields, and next actions. For ongoing work, leave a restart note with exact account/field states and no secret values. Exporting to a separate vault must follow that vault's own contract and the user's authorization; this skill does not require a private knowledge system.

Only discuss performance gains when measured. Compare equivalent windows and preserve denominators, missing analytics, and confounders such as content changes. Better copy or a higher editorial score alone does not demonstrate lift.
