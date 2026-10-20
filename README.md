# Diabetes Healthcare Data Analytics Dashboard

An exploratory healthcare data analytics project using **Python, Pandas, Matplotlib, and Microsoft Power BI** to investigate patterns between diabetes status and selected health indicators in public health survey data.

## Project Overview

This project explores the relationship between diabetes categories and health indicators such as Body Mass Index (BMI), high blood pressure, high cholesterol, and age groups. It uses the Diabetes Health Indicators Dataset derived from the **2015 Behavioral Risk Factor Surveillance System (BRFSS)**.

The project combines Python-based data exploration with Power BI visualization to transform a raw CSV dataset into meaningful charts and an interactive healthcare analytics dashboard.

This project was developed as part of my **Healthcare Data Analyst Internship at YuvaIntern**.

## Objectives

- Load and inspect a public healthcare dataset using Python.
- Understand dataset structure, data types, missing values, and duplicate records.
- Analyse the distribution of diabetes categories.
- Compare average BMI across diabetes categories.
- Explore diabetes-status patterns among respondents with and without high blood pressure.
- Examine patterns involving high cholesterol and age groups.
- Build a Power BI dashboard for visual exploration and reporting.
- Practise data analysis, visualization, and responsible interpretation of healthcare data.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Loading, inspecting, and summarizing data |
| Matplotlib | Creating exploratory charts |
| VS Code | Writing and running Python scripts |
| Microsoft Power BI Desktop | Building the healthcare analytics dashboard |
| CSV | Dataset storage and data exchange |

## Dataset

**Dataset:** Diabetes Health Indicators Dataset  
**Underlying source:** CDC Behavioral Risk Factor Surveillance System (BRFSS), 2015

Dataset download: [Diabetes Health Indicators Dataset — Kaggle](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

Official source documentation: [CDC BRFSS 2015](https://www.cdc.gov/brfss/annual_data/annual_2015.html)

The project uses the file:

`diabetes_012_health_indicators_BRFSS2015.csv`

The selected dataset contains 253,680 records and 22 columns.

### Important Features

| Feature | Description |
|---|---|
| `Diabetes_012` | Diabetes status category: 0 = no diabetes, 1 = prediabetes, 2 = diabetes |
| `BMI` | Body Mass Index |
| `HighBP` | Indicator for reported high blood pressure |
| `HighChol` | Indicator for reported high cholesterol |
| `Age` | Encoded age-group category |

The dataset contains additional demographic, lifestyle, and health-indicator variables that can be explored in future analysis.

**Note:** The dataset is survey-derived. The `Age` field represents coded age groups rather than exact ages in years.

## Project Structure

```text
Healthcare-Data-Analytics/
│
├── data/
│   └── diabetes_012_health_indicators_BRFSS2015.csv
│
├── outputs/
│   ├── diabetes_distribution.png
│   ├── average_bmi.png
│   └── blood_pressure_comparison.png
│
├── analysis.py
├── Diabetes_Healthcare_Analytics.pbix
└── README.md
```

The Power BI file and output images should be included in the repository after verifying their filenames. The dataset itself may be kept locally rather than committed to GitHub.

## Python Analysis

The Python analysis script performs initial data inspection and exploratory visualization.

### Data Inspection

- Loads the CSV dataset using Pandas.
- Displays the number of records and columns.
- Prints sample records and column names.
- Checks data types.
- Identifies missing values.
- Counts exact duplicate rows.
- Summarizes the diabetes-status categories.

### Exploratory Data Visualization

**1. Distribution of Diabetes Status**

A bar chart showing the number of survey records in the no-diabetes, prediabetes, and diabetes categories.

**2. Average BMI by Diabetes Status**

A comparison of average BMI across the three diabetes categories.

**3. Diabetes Status by High Blood Pressure**

A percentage-based comparison of diabetes categories between respondents with and without reported high blood pressure.

These charts help identify descriptive patterns in the dataset.

## Power BI Dashboard

The Power BI report is designed to present healthcare indicators through clear and interactive visualizations.

Planned and initial dashboard components include:

- Diabetes-status distribution chart
- Average BMI by diabetes category
- High blood pressure comparison
- High cholesterol comparison
- Diabetes-status distribution across age groups
- Diabetes category share
- Summary cards for total records and diabetes categories
- Interactive slicers for age group, high blood pressure, and high cholesterol

The dashboard is being refined to improve category labels, field aggregations, readability, and consistency with the Python analysis.

### Suggested Dashboard Layout

1. **Overview:** Summary cards showing record counts.
2. **Diabetes Distribution:** Counts across the three diabetes categories.
3. **Health Indicators:** BMI, blood pressure, and cholesterol comparisons.
4. **Age Group Analysis:** Distribution across encoded age groups.
5. **Interactive Exploration:** Slicers for filtering the report.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Healthcare-Data-Analytics.git
cd Healthcare-Data-Analytics
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Set Up Python

Install Python and open the project folder in VS Code.

Install the required libraries:

```bash
python -m pip install pandas matplotlib seaborn
```

### 3. Download the Dataset

Download the dataset from Kaggle and place the CSV file inside the `data/` folder.

Ensure the filename matches the one used in `analysis.py`.

### 4. Run the Analysis

```bash
python analysis.py
```

The script should display the initial inspection results and generate the charts configured in the Python code. Output filenames depend on the save paths used in the script.

### 5. Open the Power BI Report

Open `Diabetes_Healthcare_Analytics.pbix` in Microsoft Power BI Desktop after saving the report to your repository folder.

If the dataset is stored in a different location, update the data source path in Power BI when prompted.

## Data Quality and Limitations

The initial Python inspection reported missing-value and exact-duplicate counts. Duplicate records should be investigated before deciding whether to remove them; they should not be automatically deleted without documenting the rationale.

Other limitations include:

- The diabetes categories are imbalanced, so raw counts alone may not give a complete picture.
- Age is represented by encoded age groups.
- The data is observational and survey-derived.
- Reported associations do not establish cause and effect.
- The analysis is exploratory and is not a validated clinical prediction or diagnostic system.

## Future Improvements

- Improve the Power BI dashboard design and interactive filtering.
- Add percentage-based KPIs and clearly labelled summary cards.
- Validate Power BI aggregations against Python results.
- Investigate duplicate records and document data-cleaning decisions.
- Explore additional lifestyle and demographic indicators.
- Add a correlation analysis where appropriate.
- Develop a reproducible data-cleaning pipeline.
- Extend the project with statistical analysis or a carefully validated machine-learning model.

## Learning Outcomes

Through this project, I am developing practical skills in:

- Healthcare data exploration
- Python programming for data analysis
- Data quality inspection
- Exploratory data visualization
- Power BI dashboard development
- Data interpretation and reporting
- Responsible handling and presentation of public health data

## Acknowledgements

- [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/brfss/annual_data/annual_2015.html) for the underlying BRFSS survey data and documentation.
- [Kaggle — Diabetes Health Indicators Dataset](https://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset) for the ready-to-use dataset.

## Disclaimer

This project is intended for educational and exploratory data analytics purposes only. It does not provide medical advice, diagnose diabetes, or establish causal relationships between health indicators and diabetes.

---

**Project:** Diabetes Healthcare Data Analytics Dashboard  
**Tools:** Python · Pandas · Matplotlib · Power BI  
**Internship:** Healthcare Data Analyst Intern — YuvaIntern
