# Pakistani Diabetes Dataset — EDA & Classification

## 🚀 Live Demo
👉 [Click here to try the app](https://pakistani-diabetes-eda-mebhfrxbvqsgojruuiwxag.streamlit.app)

Exploratory Data Analysis and Logistic Regression classification on a clinical diabetes dataset from Pakistan.

---

## Dataset

| | |
|---|---|
| **Source** | [Kaggle — mshoaibishaaq](https://www.kaggle.com/datasets/mshoaibishaaq/pakistani-diabetes-dataset) |
| **Rows** | 909 (after cleaning) |
| **Features** | 17 + 1 target (Outcome) |
| **Target** | Outcome — 1 = Diabetic, 0 = Non-Diabetic |

---

## Key EDA Findings

- **Class balance:** 53% diabetic / 47% non-diabetic — no oversampling required
- **Strongest predictor:** HbA1c Level (correlation: 0.81 with Outcome)
- **Age risk:** Diabetes rate jumps from 6% (under 30) to 74% (30–40 age group)
- **Exercise:** 61% of non-exercisers are diabetic; 52% of all diabetics do zero exercise
- **HDL:** Only negative predictor — higher good cholesterol associated with lower diabetes risk
- **Multicollinearity:** HbA1c and Blood Sugar Random correlate at 0.79 — monitored during model selection
- **Data issue found:** BMI outlier (max 233) removed; filtered to BMI < 60

---

## Modeling Approach

### Model 1 — All Features (Baseline)
Trained on all 17 features including lab test results.

| Metric | Score |
|---|---|
| Accuracy | 100% |
| Precision | 100% |
| Recall | 100% |
| F1 Score | 100% |

⚠ **Perfect score = red flag.** Model was using leaky features:
`HbA1c_Level`, `Blood_Sugar_Random`, `Diabetes_Duration_Years` —
columns that already confirm diabetes. Discarded.

---

### Model 2 — Home User Risk Predictor ✅
Retrained using only features a person knows **without any lab test.**

**Selected Features:**
`Age`, `Gender`, `Weight_kg`, `BMI`, `Systolic_BP`, `Diastolic_BP`,
`Family_History`, `Exercise_Duration`, `Polydipsia_Excessive_Thirst`,
`Polyuria_Frequent_Urination`

| Metric | Score |
|---|---|
| Accuracy | 93.96% |
| Precision | 93.00% |
| Recall | 95.88% |
| F1 Score | 94.42% |

**Top predictors:** Excessive thirst (2.47), Age (2.05), Frequent urination (1.65)

**Recall (95.88%) is the key metric** — the model catches 96% of actual
diabetic patients, missing only 4%. Critical for a screening tool.

---

## Real World Use Case

This model is designed for **home-based diabetes risk screening** in Pakistan,
where many people cannot afford lab tests (HbA1c costs Rs. 800–1500)
but want to assess their risk before visiting a doctor.

> ⚠ This is a risk indicator — not a medical diagnosis.
> Anyone flagged as high risk should consult a doctor.

---

## Project Structure

| File | Description |
|---|---|
| `Pakistani_Diabates_Dataset.ipynb` | EDA + Data Cleaning |
| `Model_Training.ipynb` | Logistic Regression — Model 1 & Model 2 |
| `data/Pakistani_Diabetes_Dataset.csv` | Raw dataset |
| `data/Pakistani_Diabetes_Dataset_Cleaned.csv` | Cleaned dataset for model training |
| `plots/` | Saved visualizations |

---

## Tools

Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn

---

## Author

Maria — Data Science Student
