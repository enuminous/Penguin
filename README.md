# PENGUIN

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Penguin) · This repository is linked through its source; GitHub Pages is not enabled.

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>
<!-- ENUMINOUS-NETWORK:END -->

**Predictive Evaluation of Network Gradients under Uncertainty and Information Noise**

PENGUIN is an EFMW-derived framework for identifying the **noise ceiling** of predictive systems.

Its narrow question is:

> At what point does additional model complexity stop extracting useful structure because uncertainty and noise overwhelm recoverable information?

## Intended uses

- sensor networks
- AI-agent monitoring
- distributed systems
- industrial telemetry
- logistics
- forecasting
- anomaly detection
- control systems
- noisy human-organization data

## Core signal path

```text
signal state
→ gradient structure
→ uncertainty
→ noise estimate
→ calibration drift
→ signal-to-noise ratio
→ information-loss regime
→ PENGUIN noise-ceiling score
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
penguin.py
features.py
baselines.py
metrics.py
freeze.py
noise_schema.json
example_config.yaml
example_data.csv
example_run.py
test_penguin.py
MANIFEST.sha256
```

## Scientific hypothesis

> Predictive advantage from structured relational models should rise while recoverable structure dominates, then diminish as observation noise or irreducible uncertainty approaches a regime-specific ceiling.

PENGUIN does not assume this pattern is universal.

## Example signals

- rolling variance
- gradient instability
- local entropy proxy
- disagreement
- missingness
- calibration drift
- signal-to-noise ratio
- noise concentration
- multiscale uncertainty
- regime transition

## Baselines

Included:

- raw-state logistic model
- variance-only model
- SNR-only model
- uncertainty-only model
- base-rate predictor

## Primary endpoint

> Does PENGUIN improve prediction of future failure/noise-regime transitions over matched raw-state models?

Primary metric:

- Brier score

Secondary metrics:

- log loss
- ROC-AUC
- average precision
- performance stratified by noise regime

## Habitat test

PENGUIN is especially useful as a negative-control framework.

A candidate EFMW mechanism should not be expected to improve indefinitely as noise increases.

A plausible habitat pattern is:

```text
low noise        → limited need for extra complexity
moderate noise   → possible structured advantage
high noise       → advantage degrades
extreme noise    → no recoverable signal
```

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Freeze discipline

Freeze before serious evaluation:

- uncertainty definition
- noise estimator
- SNR definition
- horizons
- target
- regime thresholds
- baseline models
- split
- metrics
- exclusions
- seeds

## Negative results

If PENGUIN adds no value over simple variance/SNR baselines, the richer noise-ceiling representation has not demonstrated incremental utility.

## Status

Research software. Experimental.
