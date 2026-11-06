import plotly.express as px
def wait_chart(events): return px.box(events,x="activity",y="wait_minutes",points="outliers",title="Simulated waiting by stage")
def duration_chart(cases): return px.histogram(cases,x="total_time_minutes",nbins=30,title="Simulated total patient time")
