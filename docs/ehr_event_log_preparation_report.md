CareFlow EHR Event Log --- Dataset Preparation Report

1. Project Details
- Project: CareFlow --- Clinical Pathway Process Mining
- Workstream: Member 1 --- Dataset Selection, Preparation, and
  Documentation
- Dataset type: Public Emergency Department (ED) event log
- Preparation status: Public dataset cleaned and prepared for
  process-mining use
- Approval: The project official approved using a public dataset
  instead of generating a synthetic EHR dataset.

2. Purpose
CareFlow analyzes clinical pathways and aims to identify workflow
patterns, delays, and potential bottlenecks. The team selected a
publicly available Emergency Department event log. Its event records can
be organized into chronological activity sequences for process mining.

3. Dataset Source
- Repository:
  https://github.com/HzyBetty/emergency-department-operations
- Dataset file: event_log_ED_MMA_2026.csv
- Source type: Public dataset
- Use in CareFlow: Patient-pathway and operational-workflow
  analysis
Retain attribution to the original source and follow the repository's
applicable license and usage terms.

4. Dataset Preparation
The public dataset was selected and preprocessed for CareFlow. The
prepared event-log schema reported for the project contains these
fields:
  Field                Description
  case_id            Identifier for a patient visit/case
  activity           Activity or event performed during the visit
  timestamp          Date and time at which the event occurred
  sequence           Event order within a case
  triage_code        Triage category/code from the source data
  initial_zone       Initial Emergency Department zone/category
  disposition_code   Code representing the visit outcome
  disposition_desc   Readable description of the visit outcome
  age                Patient age recorded in the source data
  gender             Gender value recorded in the source data
The field mappings reported during preparation included visit_id to
case_id and event to activity. The sequence field was derived
from event timestamps to represent event order within each case.

5. Reported Data Validation
The following results were reported after preprocessing:
  Validation check                           Reported result
  Total event records                                 90,965
  Unique patient cases                                16,011
  Distinct activities                                      9
  Missing values in required fields                        0
  Duplicate case_id + sequence keys                    0
  Negative time differences within cases                   0
These figures reflect results reported during project preparation.
Re-run the validation notebook or script against the final committed CSV
before treating them as independently verified release statistics.

6. Why This Dataset Was Chosen
- It provides event-level records that can be grouped into patient
  cases.
- Activities and timestamps support chronological pathway
  reconstruction.
- The prepared structure is suitable for activity-frequency,
  pathway-variant, and waiting-time analyses.
- The project official approved use of a public dataset, so a separate
  synthetic EHR event generator is not required for the current
  project approach.

7. How the Dataset Supports CareFlow
The prepared event log can support:
1. Activity analysis: Count how frequently each activity occurs.
2. Pathway discovery: Reconstruct ordered activities for each
   patient case.
3. Waiting-time analysis: Calculate elapsed time between
   consecutive events.
4. Bottleneck exploration: Identify transitions or activities
   associated with longer delays.
5. Data-quality reporting: Summarize missing values, duplicate
   event-order keys, and timestamp consistency.
These are analysis opportunities; report results only after the relevant
analyses have actually been run.

8. Member 1 Scope and Handoff
Member 1 (Me) responsibilities documented here
- Select and document the public ED dataset.
- Clean and prepare the event-log structure.
- Define the prepared field names and meanings.
- Run and document data-quality checks.
- Hand off the prepared dataset and documentation to the team
