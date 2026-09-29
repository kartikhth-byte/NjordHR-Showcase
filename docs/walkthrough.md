# Synthetic workflow walkthrough

[← Project overview](../README.md) · [View Python example](../examples/matching_demo.py)

This walkthrough describes the implemented product workflow using invented candidates. It is not a screenshot or recording of the live service.

## Recruiter

1. Enter: **Indian second officers or Filipino chief officers, with tanker experience.**
2. Inspect the interpreted plan: two alternative rank/nationality branches, each sharing the tanker requirement.
3. Review candidate evidence. In the standalone example, `DEMO-001` and `DEMO-002` match. `DEMO-003` has the wrong nationality/rank pairing. `DEMO-004` lacks vessel evidence and needs review. `DEMO-005` is pending and cannot enter search.
4. In the full application, refine a search, inspect saved results, verify selected candidates, and export shortlist records. The standalone example stops at filter evaluation.

## Operator

1. Monitor intake and extraction status; investigate failed processing.
2. Review candidate facts before approval/current promotion.
3. Inspect prompt diagnostics and matching ambiguity rather than silently treating uncertainty as success.
4. Use recurring issues to create regression cases and prioritize changes.
5. Compare evaluation artifacts before promoting parser/model changes.

## Try it

From the repository root, run:

```bash
python3 examples/matching_demo.py
```

It uses only the Python standard library and synthetic local fixtures. No credentials, network, GPU, or production data are required.
