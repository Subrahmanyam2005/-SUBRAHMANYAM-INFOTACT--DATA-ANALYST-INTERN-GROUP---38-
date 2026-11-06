def transition_analysis(df):
 import pandas as pd
 d=df.sort_values(["case_id","timestamp"]).copy()
 d["next_activity"]=d.groupby("case_id").activity.shift(-1); d["next_timestamp"]=d.groupby("case_id").timestamp.shift(-1)
 d["gap_minutes"]=(d.next_timestamp-d.timestamp).dt.total_seconds()/60
 return d.dropna(subset=["next_activity"]).groupby(["activity","next_activity"],as_index=False).agg(transitions=("case_id","count"),cases=("case_id","nunique"),mean_gap_minutes=("gap_minutes","mean"),median_gap_minutes=("gap_minutes","median"))
