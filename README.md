# 🌦 Climate Pattern Intelligence Dashboard – Power BI
## Overview
The Climate Pattern Intelligence Dashboard is a time-series analytics system built using OpenWeather API data and Power BI.
The project integrates hourly multi-city weather data and applies advanced DAX modeling to analyze temperature trends, volatility patterns, and behavioral climate dynamics.
The dashboard is structured to support both real-time operational monitoring and deeper analytical intelligence.

## Project Objectives
Monitor real-time temperature trends across multiple cities
Detect peak temperature hours and cooling efficiency patterns
Analyze hourly volatility and temperature shifts
Compare multi-city climate behavior using time-series modeling
Build structured KPI-driven insights using advanced DAX
## Dashboard Architecture
The system is divided into two analytical layers:
### 1. Operational Monitoring Layer
Focused on real-time city-level tracking.
* Live temperature tracking by city
* Peak hour detection
* Cooling efficiency metrics
* Current temperature ranking
* 48-hour stability index
* Operational city snapshot table
This layer supports immediate climate observation and short-term analysis.
### 2. Pattern Intelligence Layer
Focused on behavioral and trend analysis.
* Multi-city time-series comparison
* 3-hour rolling average smoothing
* Day vs Night Cooling Index
* Wind–Temperature correlation analysis
* Custom Change Intensity Index (volatility metric)
This layer transforms raw hourly data into structured analytical insights.
## Key Analytical Features
Hourly time-series modeling
Rolling average smoothing using DAX
KPI engineering for volatility measurement
Multi-city comparative analytics
Trend and stability detection
Correlation analysis between wind speed and temperature
## Tech Stack
* Power BI
* DAX (Data Analysis Expressions)
* Power Query
* OpenWeather API
* Time-Series Data Modeling
## Data Engineering Approach
* Integrated hourly weather data using OpenWeather API
* Structured and transformed data using Power Query
* Built time-based analytical measures using DAX
* Engineered calculated KPIs for volatility and intensity tracking
* Designed layered dashboard architecture for clarity and usability
## Custom Metrics Implemented
* 3-Hour Rolling Average
* Change Intensity Index (Hourly Volatility)
Cooling Efficiency Metric
Temperature Stability Index
Peak Temperature Hour Detection
