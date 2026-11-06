def queue_summary(events):
 if events.empty: return {"mean_wait_minutes":0.0,"p95_wait_minutes":0.0,"total_wait_minutes":0.0}
 w=events.wait_minutes.clip(lower=0)
 return {"mean_wait_minutes":float(w.mean()),"p95_wait_minutes":float(w.quantile(.95)),"total_wait_minutes":float(w.sum())}
