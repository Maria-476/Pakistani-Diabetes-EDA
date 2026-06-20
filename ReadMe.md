# Pakistani Diabetes Dataset - EDA & Classification

Exploratory Data Analysis and Logistic Regression classification on a clinical diabetes dataset from Pakistan.

---

## Dataset

| | |
|---|---|
| **Source** | [Kaggle - mshoaibishaaq](https://www.kaggle.com/datasets/mshoaibishaaq/pakistani-diabetes-dataset) |
| **Rows** | 909 (after cleaning) |
| **Features** | 17 + 1 target (Outcome) |
| **Target** | Outcome: 1 = Diabetic, 0 = Non-Diabetic |

---

## Key Findings

- **Class balance:** 53% diabetic / 47% non-diabetic ,  no oversampling required
- **Strongest predictor:** HbA1c Level (correlation: 0.81 with Outcome)
- **Age risk:** Diabetes rate jumps from 6% (under 30) to 74% (30–40 age group)
- **Exercise:** 61% of non-exercisers are diabetic; 52% of all diabetics do zero exercise
- **HDL:** Only negative predictor , higher good cholesterol associated with lower diabetes risk
- **Multicollinearity:** HbA1c and Blood Sugar Random correlate at 0.79 , monitored during model selection
- **Data issue found:** BMI outlier (max 233) removed; filtered to BMI < 60

---

## Project Structure

| File | Description |
|---|---|
| `Pakistani_Diabates_Dataset.ipynb` | EDA + Data Cleaning |
| `Model_Training.ipynb` | Logistic Regression + Evaluation |
| `data/Pakistani_Diabetes_Dataset.csv` | Raw dataset |
| `plots/` | Saved visualizations |

---

## Tools

Python · Pandas · NumPy · Matplotlib · Seaborn · Scikit-learn

---

## Results

*(To be updated after model training)*

---

## Author

Maria Anwar - Data Science Student