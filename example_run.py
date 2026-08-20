import json
import pandas as pd
from penguin import PENGUINExperiment

df=pd.read_csv("example_data.csv")

exp=PENGUINExperiment(
    time_column="time",
    target_column="noise_regime_event",
    feature_columns=["signal_a","signal_b","signal_c"],
    horizons=(3,7,23),
    random_state=23,
)

result=exp.run(df)
print(json.dumps(result,indent=2))
