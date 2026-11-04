def compare_scenarios(baseline, alternative):
    b, a = baseline["summary"], alternative["summary"]
    keys = ["mean_total_time_minutes", "median_total_time_minutes",
            "mean_wait_minutes_per_stage", "total_wait_minutes"]
    rows = []
    for key in keys:
        before, after = float(b[key]), float(a[key])
        change = after - before
        pct = (change / before * 100) if before else None
        rows.append({"metric": key, "baseline": before, "alternative": after,
                     "absolute_change": change, "percentage_change": pct})
    return rows
