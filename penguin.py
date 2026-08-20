from dataclasses import dataclass
import pandas as pd

from features import build_penguin_features
from baselines import LogisticModel, BaseRateModel, variance_feature, snr_feature, uncertainty_feature
from metrics import binary_metrics, noise_strata

@dataclass
class PENGUINExperiment:
    time_column: str
    target_column: str
    feature_columns: list
    horizons: tuple = (3,7,23)
    train_fraction: float = 0.65
    random_state: int = 23

    def run(self, df):
        df=df.sort_values(self.time_column).reset_index(drop=True).copy()
        cut=max(20,int(len(df)*self.train_fraction))
        y=df[self.target_column].astype(int).to_numpy()

        pf=build_penguin_features(df,self.feature_columns,self.horizons)
        raw=df[self.feature_columns].astype(float).ffill().fillna(0.0)
        full=pd.concat([raw,pf],axis=1).fillna(0.0)

        variance=variance_feature(df,self.feature_columns,max(self.horizons))
        snr=snr_feature(df,self.feature_columns,max(self.horizons))
        uncertainty=uncertainty_feature(df,self.feature_columns)

        models={
            "penguin":(LogisticModel(self.random_state),full),
            "raw_state":(LogisticModel(self.random_state),raw),
            "variance_only":(LogisticModel(self.random_state),variance),
            "snr_only":(LogisticModel(self.random_state),snr),
            "uncertainty_only":(LogisticModel(self.random_state),uncertainty),
            "base_rate":(BaseRateModel(),raw),
        }

        results={}
        for name,(model,X) in models.items():
            model.fit(X.iloc[:cut],y[:cut])
            p=model.predict_proba(X.iloc[cut:])
            results[name]={
                "overall":binary_metrics(y[cut:],p),
                "by_noise_regime":noise_strata(
                    y[cut:],p,pf["penguin_noise_score"].to_numpy()[cut:]
                )
            }

        return {
            "n_total":len(df),
            "train_n":cut,
            "test_n":len(df)-cut,
            "results":results,
            "primary_delta_brier_raw_minus_penguin":(
                results["raw_state"]["overall"]["brier"]
                - results["penguin"]["overall"]["brier"]
            ),
            "interpretation":(
                "Positive delta favors PENGUIN over the matched raw-state model. "
                "The framework is primarily for identifying where predictive structure degrades as noise rises."
            )
        }
