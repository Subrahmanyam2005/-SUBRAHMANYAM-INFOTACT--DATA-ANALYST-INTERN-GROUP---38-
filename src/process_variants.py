def discover_variants(df,top_n=20):
 v=df.sort_values(["case_id","timestamp"]).groupby("case_id").activity.agg(lambda x:" → ".join(map(str,x)))
 r=v.value_counts().head(top_n).rename_axis("variant").reset_index(name="cases"); r["share_percent"]=r.cases/max(len(v),1)*100
 return r
