# CareFlow — Week 2 Progress Report

## 1. Overview

**Project:** CareFlow – Clinical Pathway Process Mining  
**Week:** Week 2  
**Contribution:** Member 3 – Process Mining Analytics and Interactive Scenario Analysis  

### Objective

The objective of Week 2 is to extend CareFlow beyond static dataset visualization by developing reusable process-mining analytics, an interactive clinical workflow dashboard, and a foundation for user-driven patient-flow scenario simulation.

The work focuses on helping users understand recorded patient pathways, investigate potential bottlenecks, and explore hypothetical operational changes using configurable parameters.

## 2. Work Areas

### 2.1 Process Mining and Workflow Analysis

The process-mining component focuses on transforming the validated event log into meaningful workflow insights.

**Planned and implemented components:**

- Shared event-log loading and validation utilities.
- Process discovery using PM4Py.
- Activity transition analysis.
- Patient pathway frequency analysis.
- Case-level duration calculations.
- Transition waiting-time analysis.
- Exportable process graph data for visualization.

**Expected deliverables:**

- `process_mining/common.py`
- `process_mining/discover_process.py`
- `process_mining/build_process_graph.py`
- `process_mining/pathway_analysis.py`
- `process_mining/bottleneck_analysis.py`

These components are intended to support reusable analytics and integration with the CareFlow dashboard.

### 2.2 Process Graph Visualization

An interactive process graph is being developed to represent transitions between clinical activities.

**Output files:**

- `outputs/careflow_interactive_process_graph.html` — interactive workflow graph.
- `outputs/process_graph_nodes.csv` — activity nodes and associated metrics.
- `outputs/process_graph_edges.csv` — transitions between activities and their frequencies.
- `outputs/careflow_process_map.png` — static process map generated through process discovery.

The visualizations aim to make patient-flow patterns easier to understand and help users investigate frequently occurring transitions.

### 2.3 Interactive Dashboard UI/UX

The dashboard design follows a light clinical theme with navy headings, teal accents, white cards, and interactive charts.

**Planned dashboard sections:**

1. **Overview** — key performance indicators and historical workflow summaries.
2. **Process Explorer** — activity transitions and process-map exploration.
3. **Scenario Simulator** — manual parameter entry and baseline-versus-scenario comparison.
4. **Data Quality** — event-log validation and metric definitions.
5. **About CareFlow** — project objectives, technology stack, and methodology.

The interface is being designed to distinguish historical observations from simulated estimates and future predictive outputs.

### 2.4 Parameter-Driven Scenario Simulation

A major Week 2 objective is to allow users to enter operational parameters rather than relying exclusively on values already present in the dataset.

**Candidate input parameters:**

- Mean patient arrivals per hour.
- Simulation duration.
- Number of staff members at each care stage.
- Assumed average service time.
- Baseline and proposed staffing configurations.

**Candidate outputs:**

- Simulated patient arrivals and completed journeys.
- Mean and median journey duration.
- 90th-percentile journey duration.
- Mean total waiting time.
- Stage-level waiting-time comparisons.
- Downloadable scenario comparison results.

The initial simulation design uses SimPy and a configurable sequence of care stages. It is a prototype and requires calibration against appropriate event-log statistics before its results can be used to support operational conclusions.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core analytics and application logic |
| Pandas and NumPy | Data processing and numerical calculations |
| PM4Py | Process discovery and process mining |
| NetworkX | Workflow graph construction |
| Plotly | Interactive charts and visualizations |
| Streamlit | Interactive dashboard interface |
| SimPy | Discrete-event patient-flow simulation |
| Pytest | Automated validation and testing |

## 4. Architecture and Data Flow

The intended workflow is:

1. Load and validate the prepared clinical event log.
2. Calculate historical workflow metrics and activity transitions.
3. Discover process patterns and identify potential bottlenecks.
4. Collect user-defined operational parameters through the dashboard.
5. Validate the submitted parameters.
6. Run the simulation or appropriate analytical method.
7. Compare the scenario outputs with the baseline.
8. Display interactive charts, metrics, assumptions, and downloadable results.

This architecture separates data processing, analytics, simulation, and presentation to improve maintainability and integration.

## 5. Validation and Testing Plan

The following checks are required before considering the implementation complete:

- Verify that the event log contains the required `case_id`, `activity`, and `timestamp` fields.
- Check invalid timestamps, missing identifiers, duplicate events, and event ordering.
- Compare transition counts with independently calculated sample results.
- Validate case-duration calculations against manually checked cases.
- Test simulation inputs, including invalid staffing levels and arrival rates.
- Verify repeatability for identical simulation configurations and random seeds.
- Confirm that changing a scenario parameter produces logically interpretable results.
- Test the Streamlit navigation and all dashboard sections.
- Confirm that CSV exports contain the expected columns and values.

## 6. Progress Status

Update this table to reflect the actual state of the repository at the end of Week 2.

| Task | Status |
|---|---|
| Event-log validation utilities | In progress / verify |
| PM4Py process discovery | In progress / verify |
| Interactive process graph | In progress / verify |
| Pathway frequency analysis | In progress / verify |
| Bottleneck analysis | In progress / verify |
| Light-theme dashboard UI | In progress / verify |
| Scenario simulation engine | Prototype / verify |
| Dashboard integration | In progress / verify |
| Automated tests | Pending / verify |
| Deployment validation | Pending / verify |

**Reporting note:** Mark a task as completed only after its code has been committed and tested. A proposed feature or code draft should not be reported as a completed, validated deliverable.

## 7. Challenges and Limitations

- The accuracy of historical metrics depends on the completeness and quality of the event log.
- Long elapsed times between events may indicate potential delays but do not automatically establish their cause.
- Hypothetical scenarios require explicit assumptions about arrivals, service times, staffing, and workflow rules.
- Simulation results may differ from real-world operational outcomes.
- Predictive machine learning requires a suitable target variable, representative training data, and independent evaluation.
- AI-generated explanations must be grounded in computed results rather than unsupported numerical claims.

## 8. Week 3 Plan

The next phase will focus on:

1. Completing and testing the process-mining modules.
2. Integrating the scenario simulator with the Streamlit application.
3. Connecting the dashboard to the validated dataset and, where available, the team's shared data pipeline.
4. Improving process-map interaction and global filtering.
5. Validating scenario outputs against known examples.
6. Adding multiple simulation runs and uncertainty summaries.
7. Preparing screenshots, documentation, and deployment evidence.

## 9. Expected Outcome

At the end of this development phase, CareFlow is intended to provide a clear, interactive view of clinical workflows and support exploratory analysis of hypothetical operating conditions.

The ultimate objective is to move beyond static dataset reporting toward a data-driven clinical workflow intelligence platform that combines observed process-mining results with clearly labelled simulation estimates and, where adequately validated, predictive analytics.


