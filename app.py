import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


st.set_page_config(
    page_title="Student Performance Analytics",
    page_icon="📊",
    layout="wide"
)


@st.cache_data
def create_dataset():

    np.random.seed(42)

    n = 500

    student_id = [f"STU{i:03d}" for i in range(1, n + 1)]

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
        0, 7, n
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

    return df


def engineer_features(df):

    df = df.copy()

    df["Average_Score"] = df[
        [
            "Math_Score",
            "Science_Score",
            "English_Score"
        ]
    ].mean(axis=1)

    conditions = [
        df["Average_Score"] >= 80,
        (df["Average_Score"] >= 60) &
        (df["Average_Score"] < 80),
        (df["Average_Score"] >= 40) &
        (df["Average_Score"] < 60),
        df["Average_Score"] < 40
    ]

    choices = [
        "Excellent",
        "Good",
        "Average",
        "Poor"
    ]

    df["Overall_Performance"] = np.select(
        conditions,
        choices,
        default="Unknown"
    )

    df["Study_Hour_Group"] = pd.cut(
        df["Study_Hours"],
        bins=[0, 3, 6, 9, 10],
        labels=[
            "1-3",
            "3-6",
            "6-9",
            "9-10"
        ],
        include_lowest=True
    )

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

    df["Risk_Flag"] = np.where(
        (
            (df["Average_Score"] < 40) |
            (df["Attendance_Percent"] < 60)
        ),
        "At Risk",
        "Normal"
    )

    return df


def calculate_outliers(df):

    q1 = df["Average_Score"].quantile(0.25)
    q3 = df["Average_Score"].quantile(0.75)

    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = df[
        (df["Average_Score"] < lower_bound) |
        (df["Average_Score"] > upper_bound)
    ]

    return outliers, lower_bound, upper_bound


def main():

    st.title("📊 Student Performance Analytics & Risk Analysis")

    st.write(
        "An interactive exploratory data analysis dashboard "
        "built using Python, Pandas, NumPy, Matplotlib, "
        "Seaborn and Streamlit."
    )

    df = create_dataset()
    df = engineer_features(df)

    st.sidebar.title("Dashboard Filters")

    selected_gender = st.sidebar.multiselect(
        "Gender",
        options=sorted(df["Gender"].unique()),
        default=sorted(df["Gender"].unique())
    )

    selected_performance = st.sidebar.multiselect(
        "Performance Level",
        options=[
            "Excellent",
            "Good",
            "Average",
            "Poor"
        ],
        default=[
            "Excellent",
            "Good",
            "Average",
            "Poor"
        ]
    )

    selected_risk = st.sidebar.multiselect(
        "Risk Status",
        options=[
            "At Risk",
            "Normal"
        ],
        default=[
            "At Risk",
            "Normal"
        ]
    )

    filtered_df = df[
        df["Gender"].isin(selected_gender) &
        df["Overall_Performance"].isin(selected_performance) &
        df["Risk_Flag"].isin(selected_risk)
    ]

    st.sidebar.write(
        f"Showing {len(filtered_df)} of {len(df)} students"
    )

    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "Overview",
            "Performance Analysis",
            "Risk Analysis",
            "Correlation",
            "Student Data"
        ]
    )

    with tab1:

        st.header("Overview")

        total_students = len(filtered_df)

        avg_score = filtered_df["Average_Score"].mean()

        avg_math = filtered_df["Math_Score"].mean()

        avg_science = filtered_df["Science_Score"].mean()

        avg_english = filtered_df["English_Score"].mean()

        avg_attendance = filtered_df[
            "Attendance_Percent"
        ].mean()

        avg_study_hours = filtered_df[
            "Study_Hours"
        ].mean()

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Students",
            total_students
        )

        col2.metric(
            "Average Score",
            f"{avg_score:.2f}"
        )

        col3.metric(
            "Average Attendance",
            f"{avg_attendance:.2f}%"
        )

        col4.metric(
            "Average Study Hours",
            f"{avg_study_hours:.2f}"
        )

        st.subheader("Subject Performance")

        subject_data = pd.DataFrame({
            "Subject": [
                "Math",
                "Science",
                "English"
            ],
            "Average Score": [
                avg_math,
                avg_science,
                avg_english
            ]
        })

        st.dataframe(
            subject_data,
            use_container_width=True
        )

        fig, ax = plt.subplots(
    figsize=(6, 3.5)

        )

        ax.bar(
            subject_data["Subject"],
            subject_data["Average Score"]
        )

        ax.set_title(
            "Average Score by Subject"
        )

        ax.set_xlabel("Subject")

        ax.set_ylabel(
            "Average Score"
        )

        st.pyplot(fig)

        performance_counts = (
            filtered_df[
                "Overall_Performance"
            ]
            .value_counts()
        )

        st.subheader(
            "Performance Distribution"
        )

        fig, ax = plt.subplots(figsize=(6, 3.5)

        )

        ax.bar(
            performance_counts.index,
            performance_counts.values
        )

        ax.set_title(
            "Student Performance Distribution"
        )

        ax.set_xlabel(
            "Performance Level"
        )

        ax.set_ylabel(
            "Number of Students"
        )

        st.pyplot(fig)

    with tab2:

        st.header("Performance Analysis")

        st.subheader(
            "Study Hours vs Average Score"
        )

        study_analysis = (
            filtered_df
            .groupby(
                "Study_Hour_Group",
                observed=False
            )["Average_Score"]
            .mean()
        )

        fig, ax = plt.subplots(figsize=(6, 3.5))

        ax.bar(
            study_analysis.index.astype(str),
            study_analysis.values
        )

        ax.set_title(
            "Average Score by Study Hours"
        )

        ax.set_xlabel(
            "Study Hour Group"
        )

        ax.set_ylabel(
            "Average Score"
        )

        st.pyplot(fig)

        st.subheader(
            "Attendance vs Average Score"
        )

        attendance_analysis = (
            filtered_df
            .groupby(
                "Attendance_Group",
                observed=False
            )["Average_Score"]
            .mean()
        )

        fig, ax = plt.subplots(figsize=(6, 3.5))

        ax.bar(
            attendance_analysis.index.astype(str),
            attendance_analysis.values
        )

        ax.set_title(
            "Average Score by Attendance Group"
        )

        ax.set_xlabel(
            "Attendance Group"
        )

        ax.set_ylabel(
            "Average Score"
        )

        st.pyplot(fig)

        st.subheader(
            "Parent Education Analysis"
        )

        parent_analysis = (
            filtered_df
            .groupby(
                "Parent_Education"
            )["Average_Score"]
            .mean()
            .sort_values(
                ascending=False
            )
        )

        fig, ax = plt.subplots(figsize=(6, 3.5))

        ax.bar(
            parent_analysis.index,
            parent_analysis.values
        )

        ax.set_title(
            "Average Score by Parent Education"
        )

        ax.set_xlabel(
            "Parent Education"
        )

        ax.set_ylabel(
            "Average Score"
        )

        plt.xticks(
            rotation=20
        )

        st.pyplot(fig)

        st.subheader(
            "Previous Score vs Current Score"
        )

        fig, ax = plt.subplots(figsize=(6, 3.5))

        ax.scatter(
            filtered_df["Previous_Score"],
            filtered_df["Average_Score"],
            alpha=0.6
        )

        ax.set_title(
            "Previous Score vs Average Score"
        )

        ax.set_xlabel(
            "Previous Score"
        )

        ax.set_ylabel(
            "Current Average Score"
        )

        st.pyplot(fig)

    with tab3:

        st.header("Risk Analysis")

        risk_counts = (
            filtered_df["Risk_Flag"]
            .value_counts()
        )

        col1, col2 = st.columns(2)

        col1.metric(
            "At-Risk Students",
            int(risk_counts.get(
                "At Risk",
                0
            ))
        )

        col2.metric(
            "Normal Students",
            int(risk_counts.get(
                "Normal",
                0
            ))
        )

        st.info(
            "Project-defined risk rule: a student is "
            "flagged as At Risk when Average Score is "
            "below 40 OR attendance is below 60%. "
            "This is an analytical rule for this project, "
            "not an official educational standard."
        )

        st.subheader(
            "At-Risk Students"
        )

        at_risk_students = filtered_df[
            filtered_df["Risk_Flag"] == "At Risk"
        ].sort_values(
            "Average_Score"
        )

        st.dataframe(
            at_risk_students[
                [
                    "Student_ID",
                    "Average_Score",
                    "Attendance_Percent",
                    "Study_Hours",
                    "Overall_Performance",
                    "Risk_Flag"
                ]
            ],
            use_container_width=True
        )

        st.subheader(
            "Performance vs Risk"
        )

        risk_performance = pd.crosstab(
            filtered_df["Overall_Performance"],
            filtered_df["Risk_Flag"]
        )

        st.dataframe(
            risk_performance,
            use_container_width=True
        )

        outliers, lower_bound, upper_bound = (
            calculate_outliers(filtered_df)
        )

        st.subheader(
            "Average Score Outliers"
        )

        st.write(
            f"Lower bound: {lower_bound:.2f}"
        )

        st.write(
            f"Upper bound: {upper_bound:.2f}"
        )

        st.write(
            f"Number of outliers: {len(outliers)}"
        )

        if len(outliers) > 0:

            st.dataframe(
                outliers[
                    [
                        "Student_ID",
                        "Average_Score",
                        "Study_Hours",
                        "Attendance_Percent",
                        "Overall_Performance"
                    ]
                ],
                use_container_width=True
            )

    with tab4:

        st.header("Correlation Analysis")

        numeric_columns = [
            "Study_Hours",
            "Attendance_Percent",
            "Math_Score",
            "Science_Score",
            "English_Score",
            "Previous_Score",
            "Sleep_Hours",
            "Average_Score"
        ]

        correlation = filtered_df[
            numeric_columns
        ].corr()

        fig, ax = plt.subplots(figsize=(6, 3.5))

        sns.heatmap(
            correlation,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            ax=ax
        )

        ax.set_title(
            "Correlation Matrix"
        )

        st.pyplot(fig)

        st.subheader(
            "Factors Associated with Average Score"
        )

        avg_score_corr = (
            correlation["Average_Score"]
            .drop("Average_Score")
            .sort_values(
                ascending=False
            )
        )

        fig, ax = plt.subplots(figsize=(6, 3.5))

        ax.bar(
            avg_score_corr.index,
            avg_score_corr.values
        )

        ax.set_title(
            "Correlation with Average Score"
        )

        ax.set_xlabel(
            "Factor"
        )

        ax.set_ylabel(
            "Correlation"
        )

        plt.xticks(
            rotation=30
        )

        st.pyplot(fig)

        st.warning(
            "Correlation shows association, not causation. "
            "The dataset is synthetic and the relationships "
            "should not be interpreted as real-world evidence."
        )

    with tab5:

        st.header("Student Data")

        search_student = st.text_input(
            "Search Student ID"
        )

        display_df = filtered_df.copy()

        if search_student:

            display_df = display_df[
                display_df["Student_ID"]
                .str.contains(
                    search_student,
                    case=False,
                    na=False
                )
            ]

        st.dataframe(
            display_df,
            use_container_width=True
        )

        csv = display_df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="Download Filtered Data",
            data=csv,
            file_name="filtered_student_data.csv",
            mime="text/csv"
        )

    st.markdown("---")

    st.caption(
        "Student Performance Analytics & Risk Analysis | "
        "Built with Python, Pandas, NumPy, Matplotlib, "
        "Seaborn and Streamlit"
    )


if __name__ == "__main__":
    main()