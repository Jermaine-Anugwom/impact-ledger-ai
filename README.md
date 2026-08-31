# Impact Ledger AI

**Measure whether an AI deployment improves the operation it joined.**

> All people, organizations, records, measurements, and outcomes in this
> repository are synthetic.

## The operational problem

Model accuracy alone does not reveal adoption, overrides, failure cost, or workflow improvement.

## The proof

Outcome events, baseline comparisons, adoption and override metrics, experiment notes, and transparent assumptions.

## Why this is forward deployed

The project begins with the operator's decision, uncertainty, failure cost,
integration boundary, and handoff—not with a model demo. It makes policy and
evidence inspectable, preserves human authority for consequential cases, and
remains useful when the optional model layer is unavailable.

## Architecture

```mermaid
flowchart LR
  A[Workflow events] --> B[Adoption + acceptance]
  A --> C[Overrides + errors]
  A --> D[Cycle time]
  B --> E[Deployment scorecard]
  C --> E
  D --> E
  E --> F[Baseline comparison]
  F --> G[Experiment decision]
```

## Quickstart

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
pytest -q
impact_ledger
```

No API key or network connection is required.

## Evaluation and limitations

Run `pytest -q` for the reproducible evaluation. The fixture set is deliberately
synthetic and cannot establish production performance. A real deployment would
require operator observation, representative data, policy review, privacy review,
security testing, and a monitored rollout.

## Project documents

- [Field discovery and handoff](FIELD_NOTES.md)
- [Security boundaries](SECURITY.md)
- [Operating runbook](RUNBOOK.md)
- [Development provenance](DEVELOPMENT.md)
- [Release history](CHANGELOG.md)

## Topics

`ai-metrics`, `product-analytics`, `experimentation`, `llmops`, `python`
