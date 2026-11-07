SYSTEM_PROMPT="Explain workflow analytics, not diagnosis or treatment. Distinguish observed data from synthetic simulation and state limitations."
def insights_prompt(metrics,bottlenecks): return f"Summarize findings, validation questions and limitations. Metrics={metrics}; bottlenecks={bottlenecks}"
