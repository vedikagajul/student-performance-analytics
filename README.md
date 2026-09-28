# Student Performance Analytics & Risk Analysis

An end-to-end data analytics project that explores student academic performance, identifies patterns associated with performance, analyzes potential risk groups, and presents the results through an interactive Streamlit dashboard.

The project demonstrates practical use of Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.

## Project Overview

Educational performance data can contain useful patterns related to study habits, attendance, previous academic performance, sleep, and other student characteristics.

This project analyzes a synthetic dataset of 500 students to answer questions such as:

- What is the average academic performance?
- How do Math, Science, and English scores compare?
- How is study time associated with academic performance?
- How does attendance vary across performance groups?
- Is previous academic performance associated with current performance?
- Which students are flagged as potentially at risk using a project-defined rule?
- Are there unusual student performance values that may require further investigation?

The goal is to demonstrate an end-to-end exploratory data analysis workflow rather than build a production educational prediction system.

## Features

### Data Generation

A synthetic dataset containing 500 student records is generated using NumPy and Pandas.

The dataset includes:

- Student ID
- Gender
- Study Hours
- Attendance Percentage
- Math Score
- Science Score
- English Score
- Previous Score
- Parent Education
- Extracurricular Activity
- Sleep Hours

### Feature Engineering

Additional analytical features are created:

- Average Score
- Overall Performance
- Study Hour Group
- Attendance Group
- Risk Flag

Performance levels are defined as:

| Average Score | Performance |
|---|---|
| 80 or above | Excellent |
| 60–79.99 | Good |
| 40–59.99 | Average |
| Below 40 | Poor |

## Risk Analysis

A student is flagged as `At Risk` when either:

- Average Score < 40

OR

- Attendance < 60%

This is a project-defined analytical rule and is not an official educational standard.

## Exploratory Data Analysis

The project includes analysis of:

- Overall performance distribution
- Subject-wise performance
- Study hours and performance
- Attendance and performance
- Previous score and current performance
- Sleep hours and performance
- Parent education and performance
- Extracurricular activity and performance
- Correlation between numerical variables
- Average score outliers

## Statistical Analysis

The project uses:

- Mean
- Median
- Standard deviation
- Percentiles
- Correlation
- GroupBy aggregation
- Value counts
- IQR-based outlier detection

## Dashboard

The Streamlit dashboard provides an interactive interface for exploring the dataset.

### Dashboard sections

#### Overview

Displays:

- Number of students
- Average score
- Average attendance
- Average study hours
- Subject performance
- Performance distribution

#### Performance Analysis

Includes:

- Study hours vs average score
- Attendance vs average score
- Parent education vs average score
- Previous score vs current average score

#### Risk Analysis

Includes:

- Number of at-risk students
- At-risk student table
- Risk distribution
- Outlier detection

#### Correlation Analysis

Includes:

- Correlation heatmap
- Factors associated with average score

#### Student Data

Allows users to:

- Search student IDs
- View filtered records
- Download filtered data as CSV

## Project Workflow

```text
Data Generation
      ↓
Data Validation
      ↓
Data Cleaning
      ↓
Feature Engineering
      ↓
Exploratory Data Analysis
      ↓
Statistical Analysis
      ↓
Correlation Analysis
      ↓
Outlier Detection
      ↓
Risk Identification
      ↓
Data Visualization
      ↓
Interactive Streamlit Dashboard