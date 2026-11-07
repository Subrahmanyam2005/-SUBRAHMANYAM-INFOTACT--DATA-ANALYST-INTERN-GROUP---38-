def generate_recommendations(bottlenecks,threshold_minutes=30):
 out=[]
 for _,r in bottlenecks.iterrows():
  w=float(r.get("mean_wait_minutes",r.get("mean_gap_minutes",0)))
  if w>=threshold_minutes: out.append({"finding":f"{r.activity} → {r.next_activity}: {w:.1f} min mean gap","suggestion":"Review timestamps, staffing, scheduling and handoffs with workflow owners.","caution":"Not a clinical recommendation."})
 return out or [{"finding":"No transition exceeded the configured threshold.","suggestion":"Review lower-ranked transitions and data quality.","caution":"Threshold is configurable, not a clinical standard."}]
