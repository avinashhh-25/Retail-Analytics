# Week 4 – Automation & Handoff

## Objective
Automate the RFM analysis pipeline and integrate it with the Power BI dashboard.

## End-to-End Flow
PostgreSQL (Aiven Cloud)
→ Python Script (rfm_pipeline.py)
→ CSV Output
→ Power BI Dashboard

## Automation Method
- Windows Task Scheduler is used to automate execution
- Python script runs on a scheduled interval
- CSV file is regenerated automatically
- Power BI reflects updated data on refresh

## Tools Used
- PostgreSQL (Aiven Cloud)
- Python (pandas, psycopg2)
- Power BI
- Windows Task Scheduler
- GitHub for version control

## Outcome
The RFM analysis pipeline runs without manual intervention and provides updated insights through Power BI.
