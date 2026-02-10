# Retail Analytics Project

##  Project Overview
This project is an end-to-end **Retail Analytics system** developed as part of an internship program.  
The goal is to analyze customer purchasing behavior using **RFM Analysis**, visualize insights using **Power BI**, and automate data refresh pipelines.

---

##  Project Structure
Retail-Analytics/
│
├── data/ # Raw and processed CSV files
├── scripts/ # Python scripts for RFM processing
├── automation/ # Week 4 automation documentation
├── docs/ # Detailed project analysis
├── powerbi/ # Power BI dashboard (.pbix)
├── python_to_postgres.py # PostgreSQL integration script
├── rfm_analysis_results.csv # Final RFM output
├── .gitignore
└── README.md


---

## Week-wise Breakdown

###  Week 2 – RFM Analysis (Python)
- Cleaned retail transaction data
- Calculated:
  - **Recency**
  - **Frequency**
  - **Monetary**
- Generated R, F, M scores
- Assigned customer segments:
  - Champions
  - Loyal
  - Potential Loyalists
  - Hibernating
  - At Risk
- Exported final results as CSV

---

###  Week 3 – Power BI Dashboard
- Built interactive dashboard using Power BI
- Visualized:
  - Customer segmentation
  - Revenue contribution by segment
  - RFM score distribution
- Enabled refresh from CSV source

---

###  Week 4 – Automation & Integration
- Automated RFM pipeline using Python
- Integrated PostgreSQL (Aiven Cloud)
- Enabled repeatable data refresh
- Ensured Power BI updates on new data

 **Automation details:**  
👉 [Week 4 Automation](automation/week4_automation.md)

---

 📘 Detailed Project Analysis
A complete explanation of the project workflow, tools used, challenges, and outcomes:

👉 [Project Analysis Documentation](docs/project_analysis.md)

---

🛠️ Tech Stack
- Python (Pandas, NumPy)
- PostgreSQL (Aiven Cloud)
- Power BI
- Git & GitHub
- DBeaver

---

##  Team Collaboration
This project was completed collaboratively with clear task division:
- Data processing
- RFM Analysis
- Dashboard creation
- Automation & cloud integration
- Documentation & version control

---

## Outcome
- Built a scalable retail analytics pipeline
- Converted raw data into actionable business insights
- Delivered a professional, production-style analytics project

