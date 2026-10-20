
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Locate and load the dataset
file_path = Path("data/diabetes_012_health_indicators_BRFSS2015.csv")
df = pd.read_csv(file_path)

# 1. Understand the dataset
print("DATASET OVERVIEW")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nFIRST FIVE ROWS")
print(df.head())

# 2. Check data quality
print("\nMISSING VALUES:", df.isnull().sum().sum())
print("DUPLICATE ROWS:", df.duplicated().sum())

# 3. Count each diabetes category
counts = df["Diabetes_012"].value_counts().sort_index()
labels = {
    0: "No diabetes",
    1: "Prediabetes",
    2: "Diabetes"
}

print("\nDIABETES CATEGORY COUNTS")
for category, count in counts.items():
    print(labels[int(category)], ":", count)

# 4. Calculate percentages
print("\nDIABETES CATEGORY PERCENTAGES")
print((counts / len(df) * 100).round(2))

# 5. Create a chart
Path("outputs").mkdir(exist_ok=True)

chart_counts = counts.copy()
chart_counts.index = [labels[int(x)] for x in chart_counts.index]

chart_counts.plot(kind="bar")
plt.title("Distribution of Diabetes Status")
plt.xlabel("Diabetes category")
plt.ylabel("Number of survey respondents")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("outputs/diabetes_distribution.png", dpi=200)
plt.show()

print("\nChart saved in the outputs folder.")


# STEP 5: EXPLORE HEALTH INDICATORS

# A. Diabetes status by age group
print("\nDIABETES STATUS BY AGE GROUP")
print(pd.crosstab(df["Age"], df["Diabetes_012"]))

# B. Average BMI by diabetes category
print("\nAVERAGE BMI BY DIABETES CATEGORY")
print(df.groupby("Diabetes_012")["BMI"].mean().round(2))

# C. Diabetes status and high blood pressure
print("\nDIABETES STATUS BY HIGH BLOOD PRESSURE")
print(pd.crosstab(df["HighBP"], df["Diabetes_012"]))

# STEP 6: CREATE CHARTS

labels = {
    0: "No diabetes",
    1: "Prediabetes",
    2: "Diabetes"
}

# Chart 1: Average BMI
bmi_average = df.groupby("Diabetes_012")["BMI"].mean()
bmi_average.index = [labels[int(x)] for x in bmi_average.index]

plt.figure(figsize=(8, 5))
bmi_average.plot(kind="bar")
plt.title("Average BMI by Diabetes Status")
plt.xlabel("Diabetes category")
plt.ylabel("Average BMI")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/average_bmi.png", dpi=200)
plt.show()

# Chart 2: High blood pressure comparison
bp_table = pd.crosstab(
    df["HighBP"],
    df["Diabetes_012"],
    normalize="index"
) * 100

bp_table.columns = [labels[int(x)] for x in bp_table.columns]
bp_table.index = ["No high BP", "High BP"]

bp_table.plot(kind="bar", figsize=(9, 5))
plt.title("Diabetes Status by High Blood Pressure Group")
plt.xlabel("High blood pressure")
plt.ylabel("Percentage of respondents")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("outputs/blood_pressure_comparison.png", dpi=200)
plt.show()

print("\nEDA completed. Charts saved in the outputs folder.")

print("NEW EDA CODE IS RUNNING")

print("\nAverage BMI by diabetes category:")
print(df.groupby("Diabetes_012")["BMI"].mean().round(2))

plt.figure(figsize=(8, 5))
df.groupby("Diabetes_012")["BMI"].mean().plot(kind="bar")
plt.title("Average BMI by Diabetes Status")
plt.xlabel("Diabetes category: 0 = No diabetes, 1 = Prediabetes, 2 = Diabetes")
plt.ylabel("Average BMI")
plt.tight_layout()
plt.savefig("outputs/average_bmi.png", dpi=200)
plt.show()

print("Chart saved to outputs/average_bmi.png")



# STEP 7: DATA QUALITY INVESTIGATION

print("\n--- DATA QUALITY REPORT ---")

print("Original number of rows:", len(df))
print("Exact duplicate rows:", df.duplicated().sum())

print("\nDuplicate percentage:")
print(round(df.duplicated().mean() * 100, 2), "%")

print("\nUnique values in important columns:")
for column in ["Diabetes_012", "HighBP", "HighChol", "BMI", "Age"]:
    print(column, ":", df[column].nunique())

print("\nData quality investigation completed.")


# STEP 8: HEALTH INDICATOR ANALYSIS

# Percentage of respondents in each diabetes category
print("\nDiabetes category percentages:")
print(
    df["Diabetes_012"]
    .value_counts(normalize=True)
    .sort_index()
    .mul(100)
    .round(2)
)

# Compare average BMI across categories
print("\nAverage BMI:")
print(df.groupby("Diabetes_012")["BMI"].mean().round(2))

# Compare reported high blood pressure
print("\nHigh blood pressure by diabetes category:")
print(
    pd.crosstab(
        df["Diabetes_012"],
        df["HighBP"],
        normalize="index"
    ).mul(100).round(2)
)

# Compare reported high cholesterol
print("\nHigh cholesterol by diabetes category:")
print(
    pd.crosstab(
        df["Diabetes_012"],
        df["HighChol"],
        normalize="index"
    ).mul(100).round(2)
)
