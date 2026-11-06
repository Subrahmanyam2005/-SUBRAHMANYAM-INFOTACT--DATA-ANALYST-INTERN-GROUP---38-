import pandas as pd
def filter_event_log(df,start=None,end=None,activities=None,case_ids=None):
 d=df.copy(); d["timestamp"]=pd.to_datetime(d.timestamp,utc=True,errors="coerce")
 if start is not None: d=d[d.timestamp>=pd.to_datetime(start,utc=True)]
 if end is not None: d=d[d.timestamp<=pd.to_datetime(end,utc=True)]
 if activities: d=d[d.activity.isin(activities)]
 if case_ids: d=d[d.case_id.astype(str).isin(map(str,case_ids))]
 return d.reset_index(drop=True)
