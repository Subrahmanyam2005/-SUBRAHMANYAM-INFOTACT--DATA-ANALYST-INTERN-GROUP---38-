CareFlow — Data Source and Preparation

1. Dataset

Emergency Department Patient Flow event log.

2. Source

Repository: https://github.com/HzyBetty/emergency-department-operations

Source : [event_log_ED_MMA_2026.csv](https://github.com/user-attachments/files/33341555/event_log_ED_MMA_2026.csv)


3. Purpose

The dataset is used to study emergency department patient journeys, discover process flows, analyze activity transitions, and identify potential waiting-time bottlenecks.

4. Initial Dataset Statistics

- Event records: 90,965
- Unique patient visits: 16,011
- Distinct activities: 9

5. Preparation Performed

- Inspected column names and data types.
- Checked missing values and duplicate records.
- Standardized source columns to the CareFlow schema.
- Parsed timestamps and organized events chronologically.
- Generated event sequence numbers where required.
- Validated event ordering and duplicate case/sequence keys.

6. Validation Results

The initial validation reported:

- Missing values in required fields: 0
- Duplicate case_id + sequence keys: 0
- Negative time differences: 0

These results describe the prepared dataset at the time of validation. The raw source and final transformed row counts should be recorded separately.



7. Limitations

The source data may reflect specific recording conventions. Repeated activities and long elapsed times require investigation and should not automatically be classified as errors or inefficiencies.

All transformations and filtering decisions should be reproducible from the preparation notebook or Python script.
