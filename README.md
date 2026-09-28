# Student Performance Analytics & Risk Analysis

An end-to-end **Student Performance Analytics** project built using Python, Pandas, NumPy, Matplotlib, Seaborn, and Streamlit.

The project performs exploratory data analysis (EDA), statistical analysis, feature engineering, correlation analysis, outlier detection, and presents the results through an interactive dashboard.

## Project Objectives

* Analyze student academic performance.
* Identify relationships between study habits, attendance, previous scores, and performance.
* Compare performance across different subjects.
* Identify students who meet project-defined risk criteria.
* Detect outliers using the IQR method.
* Build an interactive Streamlit dashboard.

## Dataset

The dataset contains **500 synthetic student records**.

### Features

| Feature            | Description                   |
| ------------------ | ----------------------------- |
| Student_ID         | Unique student identifier     |
| Gender             | Student gender                |
| Study_Hours        | Daily study hours             |
| Attendance_Percent | Attendance percentage         |
| Math_Score         | Mathematics score             |
| Science_Score      | Science score                 |
| English_Score      | English score                 |
| Previous_Score     | Previous academic score       |
| Parent_Education   | Parent education level        |
| Extracurricular    | Extracurricular participation |
| Sleep_Hours        | Daily sleep hours             |

## Feature Engineering

Additional features were created using Pandas and NumPy:

* **Average_Score** — mean of Math, Science, and English scores.
* **Overall_Performance** — Excellent, Good, Average, or Poor.
* **Study_Hour_Group** — 1–3, 3–6, 6–9, and 9–10 hours.
* **Attendance_Group** — 50–65%, 65–80%, and 80–100%.
* **Risk_Flag** — identifies students meeting the project's risk criteria.

## Analysis Performed

### Exploratory Data Analysis

* Data inspection and cleaning
* Missing-value checks
* Descriptive statistics
* GroupBy analysis
* Frequency and proportion analysis
* Subject-wise performance comparison

### Statistical Analysis

* Mean
* Median
* Standard deviation
* Percentiles
* Minimum and maximum values

### Visualization

* Bar charts
* Histograms
* Scatter plots
* Correlation heatmap
* Performance distribution charts

### Correlation Analysis

The project analyzes correlations between:

* Study hours
* Attendance
* Previous score
* Sleep hours
* Subject scores
* Average score

**Note:** Correlation indicates association and does not establish causation. The dataset is synthetic, so the relationships should not be interpreted as real-world evidence.

### Outlier Detection

Outliers in `Average_Score` are detected using the **Interquartile Range (IQR)** method.

## Risk Analysis

A student is flagged as **At Risk** when:

* Average Score < 40 **OR**
* Attendance < 60%

This is a **project-defined analytical rule**, not an official educational standard.

## Streamlit Dashboard

The interactive dashboard provides:

* Performance overview
* Subject performance analysis
* Study hours analysis
* Attendance analysis
* Parent education analysis
* Previous score analysis
* Risk analysis
* Correlation analysis
* Student-level data search
* Interactive filtering
* Filtered data download

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* Jupyter Notebook

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
├── app.py
├── generate_dataset.py
├── project1_student_performance.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/vedikagajul/student-performance-analytics.git
cd student-performance-analytics
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit dashboard

```bash
streamlit run app.py
```

## Key Skills Demonstrated

* Data manipulation with Pandas
* Numerical analysis with NumPy
* Exploratory Data Analysis
* Statistical analysis
* Data visualization
* Feature engineering
* Correlation analysis
* Outlier detection
* Interactive dashboard development
* Data filtering and aggregation

## Limitations

* The dataset is synthetic.
* The risk classification is a project-defined rule.
* Correlation analysis does not imply causation.
* The project is focused on analytics and visualization rather than predictive machine learning.

## Future Improvements

* Add a machine learning model for performance prediction.
* Add automated report generation.
* Add database integration.
* Add more advanced student-level analytics.

## Author

**Vedika Gajul**

B.E. Artificial Intelligence & Data Science

[GitHub Repository](https://github.com/vedikagajul/student-performance-analytics?utm_source=chatgpt.com)
