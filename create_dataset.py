
# STUDENT PERFORMANCE ANALYSIS
# Pandas + NumPy + Matplotlib
# 1. IMPORT LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 2. CREATE DATASET

np.random.seed(42)
n = 500
student_id = [f"STU{i:03d}" for i in range(1, n + 1)]
gender = np.random.choice(["Female", "Male"],size=n)
study_hours = np.random.uniform(1, 10, n).round(1)

attendance = np.random.uniform(
    50, 100, n
).round(1)

previous_score = np.random.uniform(
    35, 95, n
).round(0)

sleep_hours = np.random.uniform(
    4, 10, n
).round(1)

parent_education = np.random.choice(
    ["High School", "Diploma", "Bachelor's", "Master's"],
    size=n
)

extracurricular = np.random.choice(
    ["Yes", "No"],
    size=n
)


# ============================================================
# 3. CREATE SUBJECT SCORES
# ============================================================

noise = np.random.normal(0, 7, n)

base_score = (
    0.30 * previous_score
    + 2.8 * study_hours
    + 0.18 * attendance
    + 0.8 * sleep_hours
)

math_score = np.clip(
    base_score + noise + 3,
    0,
    100
).round(0)

science_score = np.clip(
    base_score + noise,
    0,
    100
).round(0)

english_score = np.clip(
    base_score + noise - 2,
    0,
    100
).round(0)


# ============================================================
# 4. CREATE DATAFRAME
# ============================================================

df = pd.DataFrame({
    "Student_ID": student_id,
    "Gender": gender,
    "Study_Hours": study_hours,
    "Attendance_Percent": attendance,
    "Math_Score": math_score,
    "Science_Score": science_score,
    "English_Score": english_score,
    "Previous_Score": previous_score,
    "Parent_Education": parent_education,
    "Extracurricular": extracurricular,
    "Sleep_Hours": sleep_hours
})


# ============================================================
# TASK 1–10: BASIC PANDAS
# ============================================================

# View first 5 rows
print(df.head())


# View last 5 rows
print(df.tail())


# Number of rows and columns
print(df.shape)


# Column names
print(df.columns)


# Basic information
df.info()


# Statistical summary
print(df.describe())


# Check missing values
print(df.isnull().sum())


# Check duplicate rows
print(df.duplicated().sum())


# Select one column
print(df["Math_Score"])


# Select multiple columns
print(
    df[
        [
            "Student_ID",
            "Math_Score",
            "Science_Score",
            "English_Score"
        ]
    ].head()
)


# ============================================================
# TASK 11–20: FILTERING AND SORTING
# ============================================================

# Students with Math Score greater than 80
print(
    df[df["Math_Score"] > 80]
)


# Students studying more than 7 hours
print(
    df[df["Study_Hours"] > 7]
)


# Students with attendance above 80%
print(
    df[df["Attendance_Percent"] > 80]
)


# Female students
print(
    df[df["Gender"] == "Female"]
)


# Students with Math Score between 60 and 80
print(
    df[df["Math_Score"].between(60, 80)]
)


# Sort by Math Score
print(
    df.sort_values(
        "Math_Score",
        ascending=False
    ).head()
)


# Sort by Study Hours
print(
    df.sort_values(
        "Study_Hours",
        ascending=False
    ).head()
)


# ============================================================
# TASK 21–30: VALUE COUNTS + GROUPBY
# ============================================================

# Gender distribution
print(
    df["Gender"].value_counts()
)


# Parent education distribution
print(
    df["Parent_Education"].value_counts()
)


# Extracurricular distribution
print(
    df["Extracurricular"].value_counts()
)


# Gender proportions
print(
    df["Gender"].value_counts(
        normalize=True
    )
)


# Average Math Score
print(
    df["Math_Score"].mean()
)


# Maximum Math Score
print(
    df["Math_Score"].max()
)


# Minimum Math Score
print(
    df["Math_Score"].min()
)


# Average score by gender
print(
    df.groupby("Gender")["Math_Score"].mean()
)


# Maximum score by gender
print(
    df.groupby("Gender")["Math_Score"].max()
)


# Average score by parent education
print(
    df.groupby(
        "Parent_Education"
    )["Math_Score"].mean()
)


# ============================================================
# TASK 31–40: NUMPY ANALYSIS
# ============================================================

math_scores = df["Math_Score"].to_numpy()


# Mean
print(
    np.mean(math_scores)
)


# Minimum
print(
    np.min(math_scores)
)


# Maximum
print(
    np.max(math_scores)
)


# Standard deviation
print(
    np.std(math_scores)
)


# Median
print(
    np.median(math_scores)
)


# 25th percentile
print(
    np.percentile(
        math_scores,
        25
    )
)


# 50th percentile
print(
    np.percentile(
        math_scores,
        50
    )
)


# 75th percentile
print(
    np.percentile(
        math_scores,
        75
    )
)


# ============================================================
# TASK 41–50: MATPLOTLIB VISUALIZATION
# ============================================================

# Histogram
plt.hist(df["Math_Score"])

plt.title("Distribution of Math Scores")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")

plt.show()


# Scatter plot
plt.scatter(
    df["Study_Hours"],
    df["Math_Score"]
)

plt.title("Study Hours vs Math Score")
plt.xlabel("Study Hours")
plt.ylabel("Math Score")

plt.show()


# Average Math Score by Gender
gender_avg = (
    df.groupby("Gender")["Math_Score"].mean()
)

plt.bar(
    gender_avg.index,
    gender_avg.values
)

plt.title("Average Math Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Math Score")

plt.show()


# Average Math Score by Parent Education
education_avg = (
    df.groupby("Parent_Education")["Math_Score"].mean()
)

plt.bar(
    education_avg.index,
    education_avg.values
)

plt.title("Average Math Score by Parent Education")
plt.xlabel("Parent Education")
plt.ylabel("Average Math Score")

plt.xticks(rotation=20)

plt.show()


# Gender distribution pie chart
gender_counts = df["Gender"].value_counts()

plt.pie(
    gender_counts.values,
    labels=gender_counts.index,
    autopct="%1.1f%%"
)

plt.title("Gender Distribution")

plt.show()


# ============================================================
# TASK 51: CORRELATION MATRIX
# ============================================================

correlation = df[
    [
        "Study_Hours",
        "Attendance_Percent",
        "Math_Score",
        "Science_Score",
        "English_Score",
        "Previous_Score",
        "Sleep_Hours"
    ]
].corr()

print(correlation)


# ============================================================
# TASK 52: CORRELATION HEATMAP
# ============================================================

plt.figure(figsize=(10, 7))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title(
    "Correlation Matrix of Student Performance"
)

plt.show()


# ============================================================
# TASK 53: MEANINGFUL FACTORS
# ============================================================

meaningful_corr = df[
    [
        "Study_Hours",
        "Attendance_Percent",
        "Math_Score",
        "Previous_Score",
        "Sleep_Hours"
    ]
].corr()

print(meaningful_corr)


# ============================================================
# TASK 54: MATH SCORE CORRELATIONS
# ============================================================

math_corr = df[
    [
        "Study_Hours",
        "Attendance_Percent",
        "Math_Score",
        "Previous_Score",
        "Sleep_Hours"
    ]
].corr()["Math_Score"]

print(math_corr)


# ============================================================
# TASK 55: SORT CORRELATIONS
# ============================================================

math_corr = df[
    [
        "Study_Hours",
        "Attendance_Percent",
        "Previous_Score",
        "Sleep_Hours"
    ]
].corrwith(
    df["Math_Score"]
)

math_corr = math_corr.sort_values(
    ascending=False
)

print(math_corr)


# ============================================================
# TASK 56: CORRELATION BAR CHART
# ============================================================

plt.bar(
    math_corr.index,
    math_corr.values
)

plt.title(
    "Factors Correlated with Math Score"
)

plt.xlabel("Factor")
plt.ylabel("Correlation")

plt.show()


# ============================================================
# TASK 57: FEATURE ENGINEERING
# ============================================================

conditions = [
    df["Math_Score"] >= 80,
    df["Math_Score"].between(60, 79),
    df["Math_Score"].between(40, 59),
    df["Math_Score"] < 40
]

choices = [
    "Excellent",
    "Good",
    "Average",
    "Poor"
]

df["Performance_Level"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

print(
    df[
        [
            "Student_ID",
            "Math_Score",
            "Performance_Level"
        ]
    ].head(10)
)


# ============================================================
# TASK 58: PERFORMANCE COUNTS
# ============================================================

performance_counts = (
    df["Performance_Level"].value_counts()
)

print(performance_counts)


# ============================================================
# TASK 59: PERFORMANCE DISTRIBUTION
# ============================================================

plt.bar(
    performance_counts.index,
    performance_counts.values
)

plt.title(
    "Student Performance Distribution"
)

plt.xlabel("Performance Level")
plt.ylabel("Number of Students")

plt.show()


# ============================================================
# TASK 60: AVERAGE SCORE BY PERFORMANCE LEVEL
# ============================================================

performance_avg = (
    df.groupby(
        "Performance_Level"
    )["Math_Score"].mean()
)

print(performance_avg)


# ============================================================
# TASK 61: EXTRACURRICULAR VS MATH SCORE
# ============================================================

extracurricular_avg = (
    df.groupby(
        "Extracurricular"
    )["Math_Score"].mean()
)

print(extracurricular_avg)


# ============================================================
# TASK 62: DIFFERENCE
# ============================================================

difference = (
    extracurricular_avg["Yes"]
    - extracurricular_avg["No"]
)

print(difference)


# ============================================================
# TASK 63: EXTRACURRICULAR BAR CHART
# ============================================================

plt.bar(
    extracurricular_avg.index,
    extracurricular_avg.values
)

plt.title(
    "Average Math Score by Extracurricular Activity"
)

plt.xlabel("Extracurricular")
plt.ylabel("Average Math Score")

plt.show()


# ============================================================
# TASK 64: STUDY HOUR GROUPS
# ============================================================

df["Study_Hour_Group"] = pd.cut(
    df["Study_Hours"],
    bins=[0, 3, 6, 9, 10],
    labels=[
        "1-3",
        "3-6",
        "6-9",
        "9-10"
    ]
)

print(
    df[
        [
            "Study_Hours",
            "Study_Hour_Group"
        ]
    ].head()
)


# ============================================================
# TASK 65: AVERAGE SCORE BY STUDY HOURS
# ============================================================

result = (
    df.groupby(
        "Study_Hour_Group",
        observed=False
    )["Math_Score"].mean()
)

print(result)


# ============================================================
# TASK 66: STUDY HOURS BAR CHART
# ============================================================

plt.bar(
    result.index,
    result.values
)

plt.title(
    "Average Math Score by Study Hours"
)

plt.xlabel("Study Hour Group")
plt.ylabel("Average Math Score")

plt.show()


# ============================================================
# TASK 67: ATTENDANCE GROUPS
# ============================================================

df["Attendance_Group"] = pd.cut(
    df["Attendance_Percent"],
    bins=[50, 65, 80, 100],
    labels=[
        "50%-65%",
        "65%-80%",
        "80%-100%"
    ],
    include_lowest=True
)

attendance_avg = (
    df.groupby(
        "Attendance_Group",
        observed=False
    )["Math_Score"].mean()
)

print(attendance_avg)


# ============================================================
# TASK 68: HIGHEST PERFORMING GROUPS
# ============================================================

highest_study_group = result.idxmax()

highest_attendance_group = (
    attendance_avg.idxmax()
)

print(
    "Highest study-hour group:",
    highest_study_group
)

print(
    "Highest attendance group:",
    highest_attendance_group
)


# ============================================================
# TASK 69: FINAL STUDY-HOUR VISUALIZATION
# ============================================================

plt.figure(figsize=(8, 5))

bars = plt.bar(
    result.index,
    result.values
)

plt.title(
    "Average Math Score by Study Hours"
)

plt.xlabel("Study Hour Group")
plt.ylabel("Average Math Score")

# Display values above bars
for bar in bars:

    height = bar.get_height()

    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center",
        va="bottom"
    )

plt.show()


# ============================================================
# TASK 70: FINAL INSIGHTS
# ============================================================

print("FINAL PROJECT INSIGHTS")
print("-" * 50)

print(
    "1. Study Hours had the strongest meaningful "
    "correlation with Math Score."
)

print(
    "2. Average Math Score increased as Study Hours "
    "increased."
)

print(
    "3. Attendance showed only a weak relationship "
    "with Math Score."
)

print(
    "4. Extracurricular participation showed almost "
    "no difference in average Math Score."
)

print(
    "5. Most students were classified as Average or Good "
    "based on Math Score."
)