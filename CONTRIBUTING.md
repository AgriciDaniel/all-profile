# Contributing

Help make All-profile clearer, more useful, and easier to trust.

Useful contributions include a confusing instruction, a reproducible platform change, a better handoff, or a test case that exposes a real failure. Describe what you asked the agent to do, what happened, and what should have happened. Include the skill version and agent host where relevant.

Use fictional or anonymized examples. Do not include passwords, cookies, session tokens, private account history, or screenshots containing personal information. Use current official sources for platform requirements and state when you checked them.

Keep changes focused. Preserve the distinction between drafting, approved account changes, and verified results. Do not replace an evidence gap with a confident assumption or add a guarantee of growth.

To check a change locally, run this from the repository folder:

```bash
python3 -m unittest discover -s tests -v
```

The tests need Python 3.9 or later and no extra packages. For instruction changes, also try the relevant [behavioral cases](tests/behavioral-cases.md) using fictional inputs. Record what was actually tested; a mock result is not a live-platform result.

The skill, code, and documentation are MIT-licensed. Contributions to those files are provided under the same license. The cover artwork and third-party branding are excluded; see [artwork and branding](assets/README.md).
