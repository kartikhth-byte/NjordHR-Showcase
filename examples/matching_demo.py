"""Synthetic demonstration; not production matching code."""
import json
from pathlib import Path


def evaluate(candidate, plan):
    if not (candidate.get("approved") and candidate.get("current")):
        return "INELIGIBLE", "Facts are not approved and current."
    branch_states = []
    for branch in plan["branches"]:
        checks = [None if candidate.get(key) is None else candidate[key] == value
                  for key, value in branch.items()]
        branch_states.append(False if False in checks else None if None in checks else True)
    if True not in branch_states and None not in branch_states:
        return "NO_MATCH", "No nationality/rank branch matches."
    vessels = candidate.get("vessel_types")
    if vessels is not None and plan["shared"]["vessel_type"] not in vessels:
        return "NO_MATCH", "Shared vessel requirement is not satisfied."
    if vessels is None or True not in branch_states:
        return "NEEDS_REVIEW", "Required evidence is missing."
    return "MATCH", "A complete branch and the shared requirement match."


def main():
    data = json.loads(Path(__file__).with_name("synthetic_candidates.json").read_text())
    for candidate in data["candidates"]:
        status, reason = evaluate(candidate, data["plan"])
        print(f"{candidate['id']}: {status} — {reason}")


if __name__ == "__main__":
    main()
