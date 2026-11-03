def generate_operational_insights(metrics, bottlenecks=None):
    insights = []
    patients = metrics.get("patients", 0)
    avg_duration = metrics.get("avg_observed_duration_minutes", 0)
    insights.append(f"The event log contains {patients:,} distinct patient cases.")
    insights.append(f"Mean observed first-to-last event duration is {avg_duration:.1f} minutes.")
    if bottlenecks is not None and not bottlenecks.empty:
        row = bottlenecks.iloc[0]
        insights.append(
            f"Review the {row['activity']} → {row['next_activity']} transition: "
            f"mean observed wait {row['mean_wait_minutes']:.1f} minutes."
        )
    insights.append("These are descriptive findings from the uploaded event log, not clinical recommendations.")
    return insights
