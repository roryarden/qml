---
description: "Pull the latest arXiv QML papers: run get_digest.py to update the ledger and regenerate the digest. Does not review or summarize anything."
name: "Refresh Digest"
argument-hint: "Refresh the QML ledger and digest from arXiv"
agent: "agent"
tools: [execute]
---

Refresh my quantum-machine-learning feed from arXiv. This task **only** pulls new
data; it does not score, sync, or summarize papers.

## Step

Run exactly:

```sh
uv run scripts/get_digest.py
```

This updates the rolling ledger (`papers/ledger.json`) and regenerates the daily
snapshot (`papers/digest.md`).

## Report

Report the script's summary line (how many new / revised / in ledger / in
digest). If it says nothing changed, say so. Then remind me I can review the
digest with `/review-digest`.

## Constraints

- Only run the `get_digest.py` command above — no other commands, no file edits.
