from pathlib import Path
def export_tables(tables,output_dir="outputs/reports"):
 p=Path(output_dir); p.mkdir(parents=True,exist_ok=True); out=[]
 for name,df in tables.items():
  f=p/f"{name}.csv"; df.to_csv(f,index=False); out.append(f)
 return out
