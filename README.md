# PENGUIN

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
