# CareFlow – Member 1 Week 1 Progress Report

**Project:** CareFlow – Clinical Pathway Process Mining  
**Role:** Member 1 – Dataset Selection, Preparation, and Documentation  
**Duration:** Week 1 (Day 1–Day 5)

## Day 1 – Dataset Research and Selection

- Reviewed the project requirements and identified the need for an event log suitable for clinical pathway process mining.
- Explored publicly available Emergency Department event-log datasets.
- Selected the public dataset `event_log_ED_MMA_2026.csv` from the Emergency Department Operations repository.
- Reviewed the dataset structure and its suitability for analyzing patient activities and clinical workflows.

**Outcome:** Selected a suitable public ED event-log dataset for CareFlow.

## Day 2 – Dataset Inspection and Schema Understanding

- Inspected the dataset columns and event-log structure.
- Identified important fields related to patient cases, activities, timestamps, triage, and visit outcomes.
- Planned the transformation of the source fields into a consistent schema for process-mining analysis.
- Identified the need to organize events chronologically within each patient case.

**Outcome:** Established the target event-log schema and preparation requirements.

## Day 3 – Data Cleaning and Preprocessing

- Cleaned and preprocessed the selected public dataset using Python in Google Colab.
- Mapped `visit_id` to `case_id` and `event` to `activity`.
- Prepared timestamp values for chronological event ordering.
- Created the `sequence` field to represent event order within each case.
- Organized the prepared data into a consistent event-log format.

**Outcome:** Prepared the dataset for clinical pathway analysis.

## Day 4 – Data Validation and Quality Checks

- Checked the prepared dataset for missing values in required fields.
- Checked for duplicate combinations of `case_id` and `sequence`.
- Validated chronological event ordering within patient cases.
- Reviewed the number of event records, cases, and distinct activities.

**Reported validation results:**
- Total event records: 90,965
- Unique patient cases: 16,011
- Distinct activities: 9
- Missing values in required fields: 0
- Duplicate `case_id` and `sequence` combinations: 0
- Negative time differences within cases: 0

**Outcome:** Recorded data-quality validation results for the prepared event log.

*Note: These figures are the results reported during preprocessing and should be confirmed against the final prepared CSV before formal submission.*

## Day 5 – Documentation and Team Handoff

- Documented the dataset source, preparation process, schema, and validation results.
- Prepared the EHR Event Log Preparation Report for the project repository.
- Recorded the decision to use a public dataset instead of generating synthetic EHR data, following approval from the project official.
- Prepared the dataset documentation for coordination with the remaining team members.
- Identified the next steps for supporting process-mining analysis and dashboard integration.

**Outcome:** Completed the initial dataset preparation documentation and prepared the work for team handoff.

## Week 1 Summary

During Week 1, Member 1 selected a publicly available Emergency Department event log, cleaned and preprocessed the data, prepared a consistent event-log schema, recorded data-quality validation results, and documented the dataset for CareFlow.

The prepared dataset is intended to support patient pathway reconstruction, activity analysis, waiting-time analysis, and bottleneck identification.

## Deliverables

1. Selected public ED event-log dataset.
2. Cleaned and preprocessed event-log data.
3. Prepared schema containing `case_id`, `activity`, `timestamp`, `sequence`, `triage_code`, `initial_zone`, `disposition_code`, `disposition_desc`, `age`, and `gender`.
4. Data-quality validation results.
5. EHR Event Log Preparation Report.

## Next Steps

- Maintain the prepared dataset and documentation.
- Coordinate the dataset handoff with the team.
- Support process-mining and dashboard integration by clarifying the event-log schema and data-quality checks.
