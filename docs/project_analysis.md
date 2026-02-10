# Retail Analytics Project – Group Work Analysis

## 1. Project Overview
The Retail Analytics project was developed as a group effort to analyze customer behavior using transactional retail data. The primary objective of this project was to segment customers based on their purchasing patterns and provide actionable insights for business decision-making.

We implemented an end-to-end analytics pipeline that covers data storage, processing, visualization, and automation. The project demonstrates how raw transactional data can be transformed into meaningful business insights using modern data analytics tools.

---
## 2. Problem Statement
Retail businesses often face challenges in identifying high-value customers, retaining existing customers, and detecting customers who are likely to churn. Traditional approaches rely on manual analysis or static reports, which are time-consuming and not scalable.

The goal of this project was to:
- Segment customers based on their purchasing behavior
- Identify valuable, loyal, and at-risk customers
- Automate the analytics process to reduce manual intervention
- Present insights through an interactive dashboard for business users

---

## 3. Data Source and Storage
The transactional retail data was stored in a PostgreSQL database hosted on Aiven Cloud. Cloud-based storage was chosen to ensure scalability, availability, and reliability.

DBeaver was used as a database management tool to:
- Explore tables
- Validate data quality
- Create views required for analysis

Database views were created to simplify downstream analytics and ensure a clean separation between raw data and analytical logic.

---

## 4. Data Processing and RFM Analysis
The core analytical component of the project is the RFM (Recency, Frequency, Monetary) analysis.

- **Recency** measures how recently a customer made a purchase
- **Frequency** measures how often a customer purchases
- **Monetary** measures how much revenue a customer generates

Using Python, transactional data was processed to calculate RFM metrics for each customer. Customers were scored using quantile-based segmentation, ensuring balanced distribution across segments.

Based on the combined RFM scores, customers were classified into meaningful segments such as:
- Champions
- Loyal Customers
- Potential Loyalists
- At-Risk Customers
- Hibernating Customers

This segmentation enables targeted marketing and customer retention strategies.

---

## 5. Visualization and Business Insights
Power BI was used to design an interactive dashboard that presents key metrics and customer segments in a business-friendly manner.

The dashboard allows users to:
- View segment-wise customer distribution
- Analyze revenue contribution by segment
- Identify high-value and at-risk customers
- Filter insights by region and other dimensions

This visualization layer bridges the gap between technical analysis and business decision-making.

---

## 6. Automation and Pipeline Integration (Week 4)
A major enhancement in this project was the automation of the analytics pipeline.

The automated workflow follows this sequence:
PostgreSQL Database → Python RFM Pipeline → CSV Output → Power BI Dashboard

A Python script was scheduled using Windows Task Scheduler to run periodically. This script:
- Extracts updated data from the database
- Recalculates RFM metrics
- Updates the output dataset automatically

As a result, the Power BI dashboard always reflects the latest insights with minimal manual effort.

---

## 7. Security and Best Practices
To maintain security and professionalism:
- Database credentials were stored using environment variables
- Sensitive files were excluded using `.gitignore`
- No credentials or confidential data were pushed to GitHub
- A structured project layout was followed for clarity and maintainability

---

## 8. Team Collaboration and Contribution
This project was completed as a collaborative team effort:
- Data extraction, cleaning, and RFM logic were implemented using Python
- Dashboard creation and visualization were developed using Power BI
- Automation and integration were implemented in the final phase
- Documentation and version control were managed using GitHub

Each phase was integrated carefully to ensure consistency across the pipeline.

---

## 9. Challenges and Learnings
During the project, several challenges were encountered:
- Aligning file paths across Python and Power BI
- Handling Power BI version compatibility
- Ensuring automation reliability
- Managing collaboration through GitHub

These challenges improved our understanding of real-world data engineering workflows, debugging techniques, and teamwork.

---

## 10. Conclusion and Future Scope
The Retail Analytics project successfully demonstrates an end-to-end data analytics solution with automation. It combines database management, data processing, visualization, and scheduling into a single workflow.

Future enhancements could include:
- Direct database connections to Power BI
- Real-time data updates
- Advanced machine learning-based customer segmentation
- Cloud-based orchestration tools

This project provided valuable hands-on experience in building scalable, automated analytics solutions.
