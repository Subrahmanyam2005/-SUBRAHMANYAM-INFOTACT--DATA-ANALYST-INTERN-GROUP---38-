# CareFlow Week 3 – Python Analytics Execution Guide

## Objective

Develop Python analytics to calculate patient journey durations, elapsed time between consecutive clinical activities, and potential workflow bottlenecks.

## Prerequisites

- Python 3.10 or a compatible Python version
- pandas
- numpy
- matplotlib
- A cleaned event-log CSV
- The CareFlow GitHub repository

## Required Input Columns

The event log must contain:

- `case_id`: patient journey identifier
- `activity`: recorded clinical or operational activity
- `timestamp`: event timestamp

An optional `sequence` column can help order events that share a timestamp.

## Execution Steps

1. Obtain the validated event log from the data engineering team member.
2. Check the source CSV column names and timestamp format.
3. Run `calculate_metrics.py` against the cleaned event log.
4. Inspect the generated CSV files.
5. Validate elapsed-time calculations against manually checked sample cases.
6. Generate the bottleneck visualization using `plot_metrics.py`.
7. Share the validated outputs with the dashboard developer.
8. Update the Week 3 analysis report with actual results.

## Expected Outputs

- `outputs/case_duration_metrics.csv`
- `outputs/transition_time_metrics.csv`
- `outputs/bottleneck_summary.csv`
- `outputs/data_quality_summary.csv`
- `outputs/bottleneck_p90_chart.png`

## Validation Checklist

- Confirm the input file path is correct.
- Confirm required columns exist.
- Verify event ordering within each case.
- Investigate missing timestamps and duplicate records.
- Check that negative time intervals are not included in timing summaries.
- Verify that elapsed-time values use minutes consistently.
- Compare calculated metrics with manually checked cases.
- Confirm dashboard values match the exported CSV files.

## Interpretation Notes

Elapsed time between two recorded activities is not necessarily pure waiting time. It can include service time, waiting, documentation gaps, and unrecorded activities.

A potential bottleneck flag is an initial screening indicator, not proof of a clinical problem.

Do not claim results have been validated until the scripts have been executed and the outputs checked.

## Week 3 Completion Criteria

- Analytics script created and reviewed.
- Output CSV files generated successfully.
- Sample calculations manually validated.
- Dashboard integration completed or documented as pending.
- Analysis report updated.
- Changes committed to GitHub.
