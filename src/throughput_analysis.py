def throughput_by_period(df,frequency="D"):
 d=df.copy(); d["timestamp"]=__import__("pandas").to_datetime(d.timestamp,utc=True,errors="coerce")
 d=d.sort_values("timestamp").drop_duplicates("case_id"); d["period"]=d.timestamp.dt.to_period(frequency).astype(str)
 return d.groupby("period").case_id.nunique().reset_index(name="arrivals")
