Interim Submission: Customer Experience Analytics for Fintech Apps
Project: Customer Experience Analytics for Fintech Apps Role: Data Analyst, Omega Consultancy Date: November 30, 2025 Status: Task 1 & 2 (Completed), Task 3 (In Progress - Database Setup) Submission Requirement: Interim Report 
1. Executive Summary & Project Status
The objective of this project is to enhance customer retention for Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank by transforming raw Google Play Store feedback into actionable business intelligence. The initial phases (Data Collection and Analysis) are complete, setting the stage for database implementation (Task 3).
The end-to-end pipeline facilitates three key business scenarios: identifying pain points to Retain Users, extracting needs to Enhance Features, and clustering complaints for Managing Support.
Key Performance Indicator (KPI): Statistical Rigor. Quantified features (Sentiment Scores and Thematic Categories) are ready for PostgreSQL persistence and final visualization.
2. Completed Work: Data and Analytical Foundation
The full scope of Task 1 (Data Collection) and Task 2 (Sentiment and Thematic Analysis) is complete, establishing the necessary analytical features on a clean and comprehensive dataset.
2.1. Task 1: Data Collection & Quality
Data acquisition met the project volume KPI, and quality checks confirmed the dataset's readiness for analysis.
Finding Category
Summary of Observation
Actionable Insight
Data Volume & Coverage
Collected 1,200 reviews (400 per target bank: CBE, BOA, Dashen). KPI met.
Data Set Complete: Sufficient volume for statistically significant analysis.
Data Quality
Minimal missing data (<5% error); dates normalized.
Preprocessing Complete: Dataset is clean and ready for feature engineering (Task 2).
Rating Distribution
Highly bipolar distribution (Avg. 4.25): $\approx$ 70% 5-star vs. 12.5% 1-star reviews.
Focus: The 1-star reviews ($\approx$ 150 total) will be isolated for deep thematic analysis to identify core pain points (Scenario 1).

Visual Support for Task 1
Table 2.1: Initial Review Volume and Rating Distribution (N=1,200)
Bank
Reviews Collected
Avg. Rating
% 1-Star Reviews
CBE
400
4.10
16.0%
BOA
400
4.30
11.0%
Dashen
400
4.35
10.5%
Total
1,200
4.25
12.5%


Figure 1. Rating distribution across all 1,200 collected reviews (1-5 Stars) grouped by bank. This confirms the high volume of critical 1-star reviews requiring further investigation.
2.2. Task 2: Sentiment and Thematic Feature Engineering
User opinion was quantified (Sentiment) and feedback was categorized (Themes) to create the analytical features necessary for final insight generation.
Sentiment: VADER lexicon successfully provided a quantifiable sentiment_score for 100% of the 1,200 reviews.
Thematic: Initial keyword extraction and n-gram analysis generated preliminary thematic groupings for each bank, confirming the high-level thematic approach is feasible.
Visual Support for Task 2
Figure 2. Comparison of Average VADER Sentiment Score by Bank. This chart visually establishes the baseline performance of each bank's app experience before deeper thematic drilling.

Figure 3. Top 10 High-Frequency Keywords Word Cloud, filtered for 1-star reviews. This immediately highlights recurring negative language (e.g., 'crash', 'login', 'slow').
Table 2.2: Preliminary Thematic Groupings (Derived from Initial Keywords)
Bank
High-Frequency Positive Themes (Drivers)
High-Frequency Negative Themes (Pain Points)
CBE
Utility & History (good application time)
Mixed Service (bad like, best cbe bank)
BOA
Speed & Quality (nice excellent amazing fast)
Account Access (login issue, password problem)
Dashen
Functionality (good app job, nice fast work)
Transaction Errors (transfer fail, money gone)

3. Next Steps and Deliverable Focus
The project now enters the data engineering phase (Task 3) and final synthesis (Task 4).
3.1. Immediate Next Steps (Focus on Task 3 Completion)
PostgreSQL Database Setup: Implement the data persistence layer. This is the critical next step.
Action: Create the bank_reviews database, define the schema, and execute the Python script to insert all 1,200 processed entries, ensuring data integrity for final querying.
Sentiment Refinement:
Action: Implement the planned distilbert-base-uncased-finetuned-sst-2-english model to refine VADER scores, providing a more robust sentiment baseline.
Targeted Thematic Deep Dive:
Action: Cross-reference refined sentiment scores against 1- and 2-star ratings to precisely identify the specific keywords driving negative sentiment.
3.2. Pending Work (Task 4)
Insight Derivation: Identify and quantify 2+ drivers and 2+ pain points for each bank using generated sentiment and thematic features.
Visualization: Generate remaining stakeholder-friendly plots (e.g., Sentiment Trends over Time).
Final Report: Synthesize findings into the comprehensive report with actionable recommendations.

