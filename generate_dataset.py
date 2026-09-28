import numpy as np
import pandas as pd


np.random.seed(42)

n = 500

student_id = [
    f"STU{i:03d}"
    for i in range(1, n + 1)
]

gender = np.random.choice(
    ["Female", "Male"],
    size=n
)

study_hours = np.random.uniform(
    1, 10, n
).round(1)

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
    [
        "High School",
        "Diploma",
        "Bachelor's",
        "Master's"
    ],
    size=n
)

extracurricular = np.random.choice(
    ["Yes", "No"],
    size=n
)

noise = np.random.normal(
    0,
    7,
    n
)

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

df.to_csv(
    "data/student_performance.csv",
    index=False
)

print("Dataset created successfully.")
print("Rows:", len(df))
print("Columns:", len(df.columns))
print(df.head())