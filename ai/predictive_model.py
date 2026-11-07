def train_duration_model(case_metrics,target="observed_duration_minutes"):
 from sklearn.ensemble import RandomForestRegressor
 from sklearn.model_selection import train_test_split
 from sklearn.metrics import mean_absolute_error,r2_score
 from sklearn.impute import SimpleImputer
 from sklearn.pipeline import make_pipeline
 import pandas as pd
 cols=["event_count","unique_activities"]
 d=case_metrics.dropna(subset=[target])
 if len(d)<10: raise ValueError("Need at least 10 cases for demo model")
 Xtr,Xte,ytr,yte=train_test_split(d[cols],d[target],test_size=.2,random_state=42)
 model=make_pipeline(SimpleImputer(strategy="median"),RandomForestRegressor(n_estimators=150,random_state=42))
 model.fit(Xtr,ytr); pred=model.predict(Xte)
 return model,{"mae":float(mean_absolute_error(yte,pred)),"r2":float(r2_score(yte,pred)),"test_cases":len(yte)}
