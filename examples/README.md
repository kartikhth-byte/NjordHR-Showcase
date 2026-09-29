# Standalone matching example

[← Project overview](../README.md) · [View Python code](matching_demo.py) · [Synthetic fixtures](synthetic_candidates.json)

This example demonstrates paired OR branches, a shared tanker requirement, missing evidence, and approved/current eligibility. It uses only the Python standard library.

## Run locally

```bash
git clone https://github.com/kartikhth-byte/NjordHR-Showcase.git
cd NjordHR-Showcase
python3 examples/matching_demo.py
```

## Expected output

```text
DEMO-001: MATCH — A complete branch and the shared requirement match.
DEMO-002: MATCH — A complete branch and the shared requirement match.
DEMO-003: NO_MATCH — No nationality/rank branch matches.
DEMO-004: NEEDS_REVIEW — Required evidence is missing.
DEMO-005: INELIGIBLE — Facts are not approved and current.
```

## Scope

All five candidate records are synthetic. The plan is hand-authored to illustrate parser output: the example does not call an LLM or reproduce the production schema, rank ontology, or matching engine. The `tanker` label is simplified; production vessel subtype semantics require a richer catalog.
