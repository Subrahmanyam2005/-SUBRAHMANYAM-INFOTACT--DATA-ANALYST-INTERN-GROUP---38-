def save_scenario(state,name,result):
 if not name.strip(): raise ValueError("Scenario name required")
 state.setdefault("careflow_scenarios",{})[name.strip()]=result
 return name.strip()
def list_scenarios(state): return list(state.get("careflow_scenarios",{}))
