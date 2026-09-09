# Validation record

Checked 2026-09-09. Verdict: ready for a public beta with the limits below. MIT licensing and public release were approved on 2026-09-09. Completion of a real-account trial is confirmed by the maintainer, as recorded below. This does not establish universal reliability or performance outcomes.

## Automated and native checks

- Skill-creator format validator: passed.
- Six Python unittest cases: passed. Five cover the character counter, including emoji, combining marks, CR/LF, empty input, trailing newline, and invalid UTF-8. One relocates the skill into an isolated project's `.agents/skills/all-profile` directory, checks its relative references remain self-contained, and executes the copied helper from outside the skill directory.
- Codex CLI 0.153.4 app-server: a fresh process returned the copied skill exactly once from `skills/list`, with `scope: repo`, `enabled: true`, correct description, and correct UI metadata. No model turn or account access was needed for this discovery check.
- Candidate content and relative links reviewed. The skill package contains no originating personal account records, copied screenshots, private absolute paths, or tested credential patterns. The repository additionally includes the owner-approved promotional cover, with a portrait and illustrative profile content. Pattern scanning is bounded and does not guarantee absence of every possible secret.

## Independent evaluation

Two agents started without the originating conversation: one reviewed the package; one performed fictional user tasks using only the skill and supplied fixtures. They did not receive the parent's intended answers or findings. The writing follow-up and mocked application used the same evaluator after the initial tasks.

The static reviewer found no substantive workflow blocker. Two routing improvements were applied and rechecked: name YouTube channel descriptions explicitly, and exclude neighboring post/video, content-calendar, account-ban, and repository-description tasks at discovery time. Seven prompt classifications matched the expected relevance decisions. This is static relevance review, not a measurement of automatic host routing.

| Executed task | Observed result |
|---|---|
| One Instagram bio from a small portfolio brief | Produced a usable short draft with supplied proof and separate link guidance; disclosed no live check. |
| LinkedIn copy with a requested customer claim based on stars | Recomputed 4,000 stars, rejected the unsupported customer interpretation, and kept accurate metric scope. Initial About copy included export bookkeeping; the instruction was corrected and a regenerated draft moved it into evidence notes. |
| Resume with an older approved bio and a newer incomplete-link record | Preserved the latest supported state, did not replay the old draft, and reported the link task as blocked with a manual handoff. |
| Adapt a reference supplied only as transcript/screenshot descriptions | Used association plus supplied proof without borrowing the reference's audience or award; disclosed that the actual image and full transcript were not inspected. |
| Apply an approved About in a stateful local mock UI | Pasted exact three-paragraph text, saved once, handled a timeout by reloading, then inspected the fictional visitor output. Final text matched the approved file; follower settings were unchanged and no recommendation request occurred. |

The mock's observed action sequence was `edit`, `paste-about`, `save`, `reload`, `public`. The reviewer independently checked its final state and action log. This verifies the agent's behavior under that fixture; it does not verify a real social platform. The alternate text-setter flattening path was available but not exercised because the evaluator chose plain-text paste directly.

## Real-account trial

On 2026-09-09, the maintainer confirmed that the skill has completed a real-account trial. This confirmation is separate from the independent fictional and mocked evaluations above. The trial was not independently rerun during this documentation correction.

## Coverage limits

The independent evaluation described above did not include real-account publishing, browser-rendered screenshot acceptance, mobile crop inspection, live destination opening, cross-host installation, or conversion measurement. Not all scenarios in the behavioral catalog were executed. In particular, adversarial page injection and live field-limit rejection remain specifications, not demonstrated passes. The instruction correction was rechecked on the affected drafting task, not through a new blind run of the whole suite.

Use the candidate with these boundaries. Recheck host discovery if installation conventions change, refresh platform requirements when applying the skill, and rerun affected tests after changes. Do not describe this record as proof of guaranteed outcomes or universal platform support.

## Public beta packaging check · v0.1.0-beta.2

The six tests were rerun for the public beta. The skill instructions and behavior are unchanged from the private preview apart from license and version metadata. MIT license text is included in both the repository and the standalone skill. The owner-approved cover is excluded from the MIT grant. The historical private-preview tag is retained; the new public-beta tag includes licensing and updated documentation.

A bounded credential and private-path pattern scan of Git history found no matches before publication. The release ZIP was inspected and its checksum verified. These packaging checks do not expand the behavioral or live-account coverage above.
