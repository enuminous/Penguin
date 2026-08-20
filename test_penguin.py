import pandas as pd
from features import build_penguin_features
from penguin import PENGUINExperiment

FEATURES=["signal_a","signal_b","signal_c"]

def test_features():
    df=pd.read_csv("example_data.csv")
    pf=build_penguin_features(df,FEATURES)
    assert len(pf)==len(df)
    assert "penguin_noise_score" in pf.columns
    assert pf["penguin_noise_score"].between(0,1).all()

def test_experiment_runs():
    df=pd.read_csv("example_data.csv")
    exp=PENGUINExperiment(
        time_column="time",
        target_column="noise_regime_event",
        feature_columns=FEATURES,
    )
    out=exp.run(df)
    assert "results" in out
    assert "penguin" in out["results"]
    assert "snr_only" in out["results"]
