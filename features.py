import numpy as np
import pandas as pd

EPS = 1e-8

def build_penguin_features(df, feature_columns, horizons=(3,7,23)):
    x = df[feature_columns].astype(float).ffill().fillna(0.0)
    out = pd.DataFrame(index=df.index)

    grad_cols = []
    var_cols = []
    for c in feature_columns:
        g = f"{c}__gradient"
        v = f"{c}__variance"
        out[g] = x[c].diff().fillna(0.0)
        out[v] = x[c].rolling(max(horizons), min_periods=2).var().fillna(0.0)
        grad_cols.append(g)
        var_cols.append(v)

    out["gradient_instability"] = out[grad_cols].std(axis=1).fillna(0.0)
    out["noise_variance"] = out[var_cols].mean(axis=1)

    signal_mean = x.abs().mean(axis=1)
    out["signal_strength"] = signal_mean
    out["snr_proxy"] = signal_mean / (np.sqrt(out["noise_variance"]) + EPS)

    # disagreement/uncertainty proxy across channels
    out["cross_channel_disagreement"] = x.std(axis=1).fillna(0.0)

    # entropy-like uncertainty proxy from normalized absolute channel magnitudes
    mag = x.abs() + EPS
    shares = mag.div(mag.sum(axis=1), axis=0)
    entropy = -(shares * np.log(shares)).sum(axis=1)
    out["entropy_proxy"] = entropy.fillna(0.0)

    # calibration drift proxy: recent scale vs longer-run scale
    short = x.abs().mean(axis=1).rolling(3, min_periods=1).mean()
    long = x.abs().mean(axis=1).rolling(max(horizons), min_periods=1).mean()
    out["scale_drift"] = ((short-long).abs()/(long.abs()+EPS)).fillna(0.0)

    for h in horizons:
        out[f"noise_mean_{h}"] = out["noise_variance"].rolling(h, min_periods=1).mean()
        out[f"snr_mean_{h}"] = out["snr_proxy"].rolling(h, min_periods=1).mean()
        out[f"entropy_mean_{h}"] = out["entropy_proxy"].rolling(h, min_periods=1).mean()
        out[f"gradient_mean_{h}"] = out["gradient_instability"].rolling(h, min_periods=1).mean()

    # High score = closer to noise ceiling
    components = [
        out["noise_variance"],
        out["gradient_instability"],
        out["cross_channel_disagreement"],
        out["entropy_proxy"],
        out["scale_drift"],
        1.0/(out["snr_proxy"]+EPS),
    ]
    for h in horizons:
        components.extend([
            out[f"noise_mean_{h}"],
            1.0/(out[f"snr_mean_{h}"]+EPS),
            out[f"entropy_mean_{h}"],
            out[f"gradient_mean_{h}"],
        ])

    ranked = pd.concat(components, axis=1).replace([np.inf,-np.inf], np.nan).fillna(0.0).rank(pct=True)
    out["penguin_noise_score"] = ranked.mean(axis=1).fillna(0.0)

    return out.replace([np.inf,-np.inf], np.nan).fillna(0.0)
