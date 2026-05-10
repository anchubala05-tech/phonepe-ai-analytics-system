AI-Powered PhonePe Transaction Intelligence System
An advanced Machine Learning and Business Analytics project built using Python, SQL, Streamlit, and the official PhonePe Pulse dataset.

Project Overview
This project performs comprehensive analysis of large-scale digital payment transaction data from PhonePe and delivers actionable insights through:

Transaction Analytics
Fraud and Anomaly Detection
State-wise Clustering
Transaction Trend Forecasting
Interactive Business Intelligence Dashboard
Regional Performance Insights


Key Features
Data Engineering

Automated JSON data extraction pipeline
Data preprocessing and transformation
MySQL database integration
Advanced feature engineering

Machine Learning

Isolation Forest for anomaly/fraud detection
K-Means clustering for state segmentation
Prophet model for time-series forecasting

Dashboard

Executive KPI cards
Interactive Plotly visualizations
Fraud detection analytics
State-wise filtering and drill-down
Forecast visualization with confidence intervals


Technologies Used
Technology,Purpose
Python,Core Programming Language
Pandas,Data Processing & Analysis
NumPy,Numerical Computations
MySQL,Relational Database
SQLAlchemy,Database Connectivity
Scikit-learn,Machine Learning Algorithms
Prophet,Time Series Forecasting
Streamlit,Interactive Dashboard Framework
Plotly,Advanced Data Visualization

Project Structure
textPhonePe_ML_Project/
│
├── data/                 # Raw and processed data
├── database/             # SQL scripts and schema
├── src/                  # ETL, preprocessing and ML scripts
├── dashboard/            # Streamlit application
├── models/               # Trained machine learning models
├── reports/              # Analysis reports and visualizations
├── requirements.txt
└── README.md

Machine Learning Models
Anomaly Detection

Algorithm: Isolation Forest
Purpose: Identifies suspicious transaction spikes and abnormal patterns

State Clustering

Algorithm: K-Means Clustering
Purpose: Groups states based on transaction volume, user base, and growth patterns

Forecasting

Algorithm: Facebook Prophet
Purpose: Predicts future transaction amounts and counts with trend and seasonality analysis


Dashboard Features

Executive KPI Metrics
Transaction Trends Analysis
Fraud Detection Dashboard
State Segmentation & Clustering View
Interactive Forecasting Charts
Dynamic Filters (State, Year, Quarter, Payment Category)


How to Run Locally
1. Clone the Repository
Bashgit clone https://github.com/anchubala05-tech/phonepe-ai-analytics-system.git
2. Install Dependencies
Bashpip install -r requirements.txt
3. Run the Streamlit Application
Bashstreamlit run dashboard/app.py

Deployment
The project is deployed and accessible via Streamlit Community Cloud.

Dataset
Source: PhonePe Pulse Dataset (Official GitHub Repository)


Future Enhancements

Real-time data streaming and analytics
Deep learning models for advanced fraud detection
Live fraud alerting system
Cloud database integration (AWS RDS / GCP)
Enhanced geospatial visualization using interactive India map
