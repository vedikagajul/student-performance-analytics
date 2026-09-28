# Student Performance Analytics & Risk Analysis

An end-to-end **data analytics and visualization project** that explores student academic performance, identifies patterns associated with performance, analyzes potentially at-risk students using a project-defined rule, and presents insights through an interactive **Streamlit dashboard**.

The project demonstrates practical application of **Python, Pandas, NumPy, Matplotlib, Seaborn, statistical analysis, exploratory data analysis (EDA), feature engineering, and Streamlit**.

> **Note:** This project uses a synthetic dataset created for educational and portfolio purposes. The findings should not be interpreted as real-world educational or causal conclusions.

## Project Overview

Educational performance data can contain patterns related to factors such as study time, attendance, previous academic performance, sleep, and other student characteristics.

This project analyzes a synthetic dataset containing **500 student records** to explore questions such as:

* What is the overall academic performance of the students?
* How do Math, Science, and English scores compare?
* How is study time associated with average academic performance?
* How is attendance distributed across different performance levels?
* How is previous academic performance associated with current performance?
* Which students are flagged as potentially at risk using a predefined analytical rule?
* Are there unusual performance values that may require further investigation?
* Which numerical variables show stronger or weaker linear associations with average score?

The primary goal is to demonstrate a complete **data analysis workflow**, from dataset generation and cleaning to visualization, statistical analysis, risk analysis, and dashboard development.

## Objectives

The main objectives of this project are:

1. Generate and work with a structured student dataset.
2. Perform data cleaning and validation.
3. Conduct exploratory data analysis using Pandas.
4. Perform numerical analysis using NumPy.
5. Engineer meaningful analytical features.
6. Analyze relationships between student attributes and performance.
7. Detect potential outliers using the IQR method.
8. Define and analyze a project-specific risk rule.
9. Create meaningful visualizations using Matplotlib and Seaborn.
10. Build an interactive dashboard using Streamlit.
11. Present analytical results in a clear and accessible format.

## Dataset

The project uses a **synthetically generated dataset containing 500 students**.

### Original Features

| Feature              | Description                                 |
| -------------------- | ------------------------------------------- |
| `Student_ID`         | Unique student identifier                   |
| `Gender`             | Student gender                              |
| `Study_Hours`        | Approximate study hours                     |
| `Attendance_Percent` | Attendance percentage                       |
| `Math_Score`         | Mathematics score                           |
| `Science_Score`      | Science score                               |
| `English_Score`      | English score                               |
| `Previous_Score`     | Previous academic score                     |
| `Parent_Education`   | Parent education level                      |
| `Extracurricular`    | Participation in extracurricular activities |
| `Sleep_Hours`        | Approximate daily sleep duration            |

### Engineered Features

| Feature               | Description                                 |
| --------------------- | ------------------------------------------- |
| `Average_Score`       | Mean of Math, Science, and English scores   |
| `Overall_Performance` | Performance category based on average score |
| `Study_Hour_Group`    | Grouped study-hour range                    |
| `Attendance_Group`    | Grouped attendance range                    |
| `Risk_Status`         | Project-defined risk classification         |

## Performance Classification

Students are categorized according to their average score:

| Average Score | Performance Level |
| ------------: | ----------------- |
|   80 or above | Excellent         |
|      60–79.99 | Good              |
|      40–59.99 | Average           |
|      Below 40 | Poor              |

These categories are created specifically for this project and are not official academic grading standards.

## Risk Analysis

The project uses a simple analytical rule to identify students who may require further investigation.

A student is classified as **At Risk** when either condition is satisfied:

```text
Average Score < 40
OR
Attendance < 60%
```

Otherwise, the student is classified as:

```text
Not At Risk
```

### Important

This is a **project-defined analytical rule**, not a validated educational risk model.

It does not predict student outcomes and should not be used to make real-world decisions about students.

## Exploratory Data Analysis

The project performs exploratory analysis across several dimensions.

### Academic Performance

* Overall average score
* Subject-wise performance
* Performance-level distribution
* Score distributions
* Summary statistics

### Study Behavior

* Study hours vs average score
* Study-hour group analysis
* Distribution of study hours

### Attendance

* Attendance vs average score
* Attendance groups
* Attendance distribution across performance levels

### Previous Performance

* Previous score vs current average score
* Correlation between previous and current performance

### Other Factors

* Sleep hours vs performance
* Parent education vs performance
* Extracurricular participation vs performance
* Gender-based performance analysis

## Statistical Analysis

The project applies several statistical and analytical techniques:

* Mean
* Median
* Minimum and maximum
* Standard deviation
* Percentiles
* Correlation analysis
* GroupBy aggregation
* Value counts
* Proportional analysis
* IQR-based outlier detection

These techniques are used to summarize the dataset and investigate relationships between variables.

## Correlation Analysis

Correlation analysis is used to examine **linear associations** between numerical variables.

For example, the project analyzes the relationship between:

* Study hours and average score
* Previous score and average score
* Attendance and average score
* Sleep hours and average score

### Important Interpretation

Correlation indicates an association between variables. It **does not establish causation**.

Because this project uses synthetic data, observed relationships should be treated as demonstrations of analytical techniques rather than real-world evidence.

## Outlier Detection

The project uses the **Interquartile Range (IQR)** method to identify potentially unusual average-score values.

The method is based on:

```text
IQR = Q3 - Q1
```

Potential outliers are identified using standard IQR boundaries:

```text
Lower Bound = Q1 - 1.5 × IQR
Upper Bound = Q3 + 1.5 × IQR
```

Outliers are treated as values that may require further investigation rather than automatically being considered errors.

## Streamlit Dashboard

The project includes an interactive dashboard built with **Streamlit**.

### Dashboard Sections

#### Overview

Provides a high-level summary including:

* Number of students
* Average score
* Average attendance
* Average study hours
* Subject-wise performance
* Performance distribution

#### Performance Analysis

Explores relationships between:

* Study hours and average score
* Attendance and average score
* Parent education and average score
* Previous score and current average score

#### Risk Analysis

Includes:

* Number of potentially at-risk students
* Risk distribution
* At-risk student records
* Outlier analysis

#### Correlation Analysis

Includes:

* Correlation matrix
* Correlation heatmap
* Numerical factors associated with average score

#### Student Data

Allows users to:

* Search by Student ID
* Apply filters
* View student records
* Download filtered data as CSV

## Interactive Filtering

The dashboard allows users to filter the dataset based on available student attributes such as:

* Gender
* Overall performance
* Risk status

This makes it possible to explore specific groups interactively rather than relying only on static analysis.

## Project Workflow

```text
Synthetic Data Generation
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
```

## Technologies Used

| Technology       | Purpose                                      |
| ---------------- | -------------------------------------------- |
| Python           | Core programming language                    |
| Pandas           | Data manipulation and analysis               |
| NumPy            | Numerical operations and feature engineering |
| Matplotlib       | Data visualization                           |
| Seaborn          | Statistical visualization                    |
| Streamlit        | Interactive dashboard                        |
| Jupyter Notebook | Exploratory analysis and experimentation     |
| Git & GitHub     | Version control and project hosting          |

## Project Structure

```text
student-performance-analytics/
│
├── data/
│   └── student_performance.csv
│
├── nb/
│   └── student_performance_analysis.ipynb
│
├── screenshots/
│   ├── overview.png
│   ├── performance.png
│   ├── risk_analysis.png
│   └── correlation.png
│
├── app.py
├── generate_data_
```
