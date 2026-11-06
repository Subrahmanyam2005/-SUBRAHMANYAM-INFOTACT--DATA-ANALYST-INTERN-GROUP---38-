def analyze_resource_utilization(sim_events):
 if sim_events.empty: return sim_events.copy()
 return sim_events.groupby("activity",as_index=False).agg(busy_minutes=("service_minutes","sum"),cases=("case_id","nunique"))
def observed_resource_summary(df,column="resource"):
 if column not in df: return None,f"Missing source column: {column}"
 return df.groupby(column).agg(events=("activity","size"),cases=("case_id","nunique")).reset_index(),None
