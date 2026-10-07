def human_approval_node(state)::
  decision = state["decision"]
  approval_data = {
    "allocation": {
      "solar_used_kw": decision.get ("solar_used_kw" , 0),
      "battery_used_kw": decision.get("battery_used_kw" , 0),
      "grid_used_kw": decision.get("grid_used_kw", 0),
    },
    "safety_results" : { 
      "critical_load_kw": state["critical_load_kw"],
      "battery_soc_pct" : state["battery_soc_pct"],
      "alerts" : state["alerts"],
    },
    "deviations" : {
      "deviation_detected" : state ["deviation_detected"],
           "replanned": state.get("replanned", False),
    },
    "metrics" : {
      "grid_price_per_kwh" : state ["grid_price_per_kwh"],
      "forecast_solar_kw": state["forecast_solar_kw"],
      "flexible_loads_deferred" : [l["name"] for l in state["flexible_loads"] if l.get("deferred")],
    },
    "reasoning" : state.get("reasoning", ""),
  }
  return{
    **state,
    "approval_pending" : True,
    "approval_data" : approval_data,
    "approval_decision" : None,
    "approval_modifications" : {},
    "reviewer_notes": "",
  }


