# -SUBRAHMANYAM-INFOTACT--DATA-ANALYST-INTERN-GROUP---38-
THIS IS MY OFFICIAL REPOSITORY CONNECTED TO INFOTACT SOLUTIONS DASHBOARD.


## Project Description

**CareFlow – Clinical Pathway Process Mining** is a data-driven healthcare analytics project designed to analyze patient journeys and understand how clinical processes flow through emergency department operations.

The project uses a structured healthcare event log to track patient cases across different clinical activities. By analyzing activity sequences, timestamps, and patient visit information, CareFlow aims to identify common clinical pathways, detect process bottlenecks, measure waiting times, and highlight variations in patient flow.

The project combines **Python, Pandas, Streamlit, Plotly, Google BigQuery, dbt, and process mining techniques** to prepare healthcare event data, transform it into an analytics-ready format, and present meaningful insights through an interactive dashboard.

### Project Objectives

- Analyze patient journeys using event log data.
- Discover and visualize common clinical pathways.
- Identify bottlenecks and delays in emergency department workflows.
- Examine variations in activity sequences and patient flow.
- Validate and transform healthcare data for reliable analysis.
- Present key findings through an interactive analytics dashboard.

### Expected Outcome

CareFlow aims to provide a clear, data-driven view of clinical workflows, helping users understand how patients move through different stages of care and where process improvements may be possible.

**Dataset:** [Emergency Department Operations Dataset](https://github.com/HzyBetty/emergency-department-operations)

*Note: CareFlow is an academic analytics project. Its findings are intended for workflow analysis and educational purposes, not for making clinical decisions.*



## Week 1 – Project Setup and Data Preparation

### Overview

During Week 1, the CareFlow team focused on establishing the project foundation, understanding the emergency department event-log dataset, and preparing the data for subsequent process mining and dashboard development.

The main objective was to organize the project structure, inspect the available data, identify important event-log attributes, and establish the initial data-processing workflow.

### 1. Project Setup

The initial project setup included:

- Defining the CareFlow project objective and scope.
- Organizing the project repository and development files.
- Identifying the technology stack required for data analysis, process mining, and dashboard development.
- Establishing GitHub as the central location for source code and documentation.
- Planning individual responsibilities across the four-member team.

**Repository:** [CareFlow – Clinical Pathway Process Mining](https://github.com/krishna170-jpg/CareFlow-Clinical-Pathway)

### 2. Dataset Identification and Understanding

The team selected an emergency department patient-flow event log for analyzing patient journeys through clinical activities.

Initial data-understanding tasks included:

- Inspecting the dataset structure and column names.
- Identifying patient or case identifiers.
- Understanding activity labels and event timestamps.
- Checking the availability of event sequence information.
- Reviewing missing values, duplicate records, and timestamp formats.
- Identifying the fields required for patient-flow analysis.

**Expected core event-log fields:**

| Column | Description |
|---|---|
| `case_id` | Identifier for a patient journey or case |
| `activity` | Clinical or operational activity recorded |
| `timestamp` | Date and time of the recorded event |
| `sequence` | Optional event-order information |

*The actual dataset column names may differ. Confirm the data dictionary against the file committed to the repository.*

### 3. Data Cleaning and Preprocessing

The initial preprocessing workflow was planned and developed to prepare the event log for reliable analysis.

Key tasks included:

- Standardizing column names and data types.
- Converting timestamps into a consistent datetime format.
- Identifying records with missing case identifiers, activities, or timestamps.
- Checking duplicate event records.
- Sorting events chronologically within each case.
- Reviewing case-level activity sequences.
- Preparing a structured event log for process mining.

The purpose of these steps is to improve data consistency before calculating patient-flow metrics or discovering clinical pathways.

### 4. Initial Process Mining Preparation

The team identified the basic requirements for process mining and clinical pathway analysis.

Preparation activities included:

- Defining cases, activities, and timestamps.
- Establishing the event-log format needed by PM4Py.
- Planning process discovery and directly-follows transition analysis.
- Identifying potential metrics for pathway frequency and operational bottlenecks.

These activities establish the foundation for the process discovery and visualization work planned for Week 2.

### 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analytics |
| Pandas | Dataset inspection and cleaning |
| NumPy | Numerical operations |
| PM4Py | Process mining |
| GitHub | Version control and collaboration |
| Google Colab | Cloud-based development and experimentation |
| Streamlit | Planned interactive dashboard |

### 6. Week 1 Development Status

| Work area | Status |
|---|---|
| Project scope and objectives | Initial setup |
| GitHub repository | Established |
| Dataset identification | Initial review |
| Event-log structure | Identified / verify |
| Data cleaning | In progress / verify |
| Process mining preparation | Initial preparation |
| Dashboard development | Planned |
| Scenario simulation | Planned |

*Update the status column to reflect the work actually completed during Week 1.*

### 7. Challenges and Considerations

- Ensuring that the dataset contains the case, activity, and timestamp fields required for process mining.
- Handling missing or inconsistent event timestamps.
- Preserving the correct order of events within each patient journey.
- Distinguishing observed dataset metrics from later simulation estimates.
- Maintaining a clear and reproducible project structure for team collaboration.

### 8. Week 2 – Planned Work

- Develop process discovery and pathway analysis modules.
- Generate process graphs and transition-frequency summaries.
- Calculate patient-flow metrics and investigate potential bottlenecks.
- Enhance the Streamlit dashboard.
- Develop a configurable scenario simulator.
- Add testing and document the implementation.

### Detailed Progress Documentation

For the detailed Week 1 development report, refer to:

[Week 1 Progress Report](docs/WEEK1_PROGRESS.md)

---

**Project:** CareFlow – Clinical Pathway Process Mining  
**Development Phase:** Week 1 – Project Setup and Data Preparation



## Week 2 – Development Progress

### Overview

During Week 2, the CareFlow team focused on extending the initial data preparation work into process mining, clinical pathway analysis, interactive visualization, and scenario-based simulation.

The objective is to transform emergency department event logs into meaningful operational insights and support experimentation with different patient arrival rates, staffing levels, and service times.

### 1. Process Mining and Clinical Pathway Analysis

The process mining module is being developed to analyze patient journeys using event-log data.

Key development areas:

- Process discovery using PM4Py.
- Identification of frequently occurring clinical activities.
- Analysis of activity-to-activity transitions.
- Identification of common patient pathways.
- Bottleneck analysis using elapsed times between recorded events.

**Relevant files:**

- `process_mining/common.py`
- `process_mining/discover_process.py`
- `process_mining/build_process_graph.py`
- `process_mining/pathway_analysis.py`
- `process_mining/bottleneck_analysis.py`

### 2. Interactive Process Visualization

An interactive process graph is being developed to represent the movement of patients between clinical activities.

Planned or generated outputs include:

- `outputs/careflow_interactive_process_graph.html`
- `outputs/process_graph_nodes.csv`
- `outputs/process_graph_edges.csv`
- `outputs/careflow_process_map.png`

The visualizations are intended to help users understand activity relationships, transition frequencies, and overall clinical workflow patterns.

### 3. Streamlit Dashboard Development

The CareFlow dashboard is being enhanced to provide an interactive interface for exploring emergency department operations.

Key features under development:

- Overview dashboard with patient-flow metrics.
- Activity frequency and event-volume visualizations.
- Clinical process exploration.
- Date and activity filters.
- Event-log data quality information.
- CSV export functionality.
- Integration of scenario simulation.

**Main application:** `app.py`

**Live application:** [CareFlow Dashboard](https://careflow-clinical-pathway-gecwrps8ze2pscptvnavfp.streamlit.app/)

### 4. Parameter-Driven Scenario Simulation

A scenario simulation module is being developed to evaluate hypothetical emergency department configurations.

Users can configure:

- Patient arrival rate (patients per hour).
- Simulation duration.
- Number of staff members at each stage.
- Average service time for each stage.
- Baseline and proposed operational scenarios.

The simulator is designed to estimate:

- Total simulated patient arrivals.
- Completed patient journeys.
- Average patient journey duration.
- Average waiting time.
- Stage-level performance.
- Differences between baseline and proposed scenarios.

**Relevant files:**

- `simulation/engine.py`
- `simulation/scenario_page.py`
- `tests/test_simulation.py`

**Important:** Simulation results are estimates based on model assumptions, not observed clinical outcomes or validated machine-learning predictions.

### 5. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend analytics |
| Pandas and NumPy | Data processing |
| PM4Py | Process discovery |
| NetworkX | Process graph analysis |
| Plotly | Interactive visualizations |
| Streamlit | Web dashboard |
| SimPy | Discrete-event simulation |
| Pytest | Automated testing |

### 6. Week 2 Development Status

| Module | Status |
|---|---|
| Event-log preprocessing | Carried forward from Week 1 |
| Process discovery | In progress |
| Clinical pathway analysis | In progress |
| Interactive process graph | Implementation / verification |
| Dashboard enhancement | In progress |
| Scenario simulation | Prototype / verification |
| Automated testing | Pending verification |

*Update these statuses to reflect the actual implementation and test results before committing.*

### 7. Week 3 – Planned Work

- Integrate the process mining modules into the Streamlit dashboard.
- Validate process discovery and pathway metrics against the event log.
- Improve the interactive clinical process graph.
- Test baseline and proposed simulation scenarios.
- Refine dashboard UI/UX and navigation.
- Perform integration testing and resolve deployment issues.
- Prepare the project demonstration and technical documentation.

### Detailed Progress Documentation

For the complete Week 2 development report, refer to:

[Week 2 Progress Report](docs/WEEK2_PROGRESS.md)

---

**Project:** CareFlow – Clinical Pathway Process Mining  
**Development Phase:** Week 2 – Process Mining, Visualization and Simulation
