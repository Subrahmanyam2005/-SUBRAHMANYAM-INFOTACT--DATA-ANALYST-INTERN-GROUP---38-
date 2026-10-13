CareFlow — Data Dictionary

Overview

This document describes the columns in the prepared Emergency Department event log used in the CareFlow Clinical Pathway Process Mining project.

Column Name| Data Type| Description| Purpose
"case_id"| String| Unique identifier for a patient visit or encounter.| Groups events belonging to the same visit.
"activity"| String| Name of the activity or process step recorded during a visit.| Identifies the steps performed in the clinical pathway.
"timestamp"| Timestamp / DateTime| Date and time at which an event was recorded.| Establishes event order and supports waiting-time analysis.
"sequence"| Integer| Sequence number used to order events within a visit.| Helps determine the order of events, particularly when timestamps are equal.
"triage_code"| String| Triage category or code recorded in the source dataset.| Supports pathway comparisons by triage category, subject to the source code definitions.
"initial_zone"| String| Code identifying the initial Emergency Department zone recorded for the visit.| Supports analysis by initial zone, subject to the source documentation.
"disposition_code"| String| Code representing the recorded visit disposition or outcome.| Supports analysis of visit outcomes.
"disposition_desc"| String| Text description associated with the recorded disposition.| Makes disposition categories easier to interpret and report.
"age"| Integer| Age recorded for the patient visit.| Supports age-group analysis when appropriate.
"gender"| String| Gender category recorded in the source dataset.| Supports demographic summaries when appropriate.

Key Fields for Process Mining

Field| Role
"case_id"| Case identifier
"activity"| Event or activity label
"timestamp"| Event timestamp
"sequence"| Event ordering field, where available

Data Quality Considerations

- Each event should have a valid case identifier, activity, and timestamp.
- Events should be ordered by timestamp and, where available, sequence.
- Repeated activities within a visit should not automatically be removed because they may represent genuine revisits or repeated process steps.
- Missing values, duplicate event keys, and invalid timestamps should be checked and documented.
- Triage, zone, and disposition codes should be interpreted using the source dataset's documentation.
- Age and gender should only be used for analyses relevant to the project and permitted by the dataset's usage conditions.

Notes

This dictionary describes the prepared CareFlow event-log schema. Confirm the actual column names, data types, and meanings against the final CSV and source documentation before production use. The "sequence" field should be documented as derived if it was calculated during preprocessing rather than supplied by the original dataset.

