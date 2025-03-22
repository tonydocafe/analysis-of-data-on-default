# Data Analysis with the "Adult" Dataset 🚀

Welcome to the data analysis project for the "Adult" dataset! This repository is the starting point for exploring, processing, and evaluating classification models on income data, revolving around predicting whether a person earns more or less than 50K based on several characteristics.

##Project Structure 🎯

The heart of this project is the `main.py` file, which organizes the execution of the data and model pipeline. Here's what each script does:

### File: `main.py`
**Purpose**: This is the entry point for the data analysis project. It coordinates the execution of auxiliary scripts and ensures that everything works in harmony.

**Main Functionalities**:
- Calls the auxiliary scripts:
- `data_loader.py`: Loads and processes the dataset.
- `model_trainer.py`: Trains and evaluates the classification models.
- `visualization.py`: Generates performance comparison graphs.
- Coordinates the steps of the data and model pipeline.

### File: data_loader.py
**Purpose** Manages the loading, cleaning and balancing of the "Adult" dataset.

**Main features**:

- Load the data file (adult.data) and remove missing values.

- Converts categorical variables into numeric values ​​with LabelEncoder.

- Apply the SMOTE algorithm to balance the classes (note that, in the original dataset, we have an imbalance between the classes).

### File: model_trainer.py
**Purpose** Trains and evaluates classification models on the processed dataset.

**Main Features**::

- Trains three models:

- Perceptron

- Decision Tree

- Neural Networks

- Displays performance metrics (precision, recall, and f1-score) for each model.

### File: visualization.py
**Purpose**: Generates comparative performance graphs between classification models.

**Main Features**:

- Creates bar charts comparing the accuracy of each model.

- Interactive display of graphs using matplotlib and seaborn.

### Data Summary 📊
**Records:**
- 32,561

**Columns:**
- 15

**Missing Values:** Some columns have missing values:

- job class: 1,836 missing values.

- occupation: 1,843 missing values.

- country of origin: 583 missing values.

**Data Types:**

- Numeric (int64): 6 columns

- Categorical (object): 9 columns

**Memory:**

Size: 3.7 MB

### Recommended Action 🛠️
**Missing Values:** Decide how to treat this data, either by filling with the mode or mean or by removing the rows.

**Class Balancing:** The dataset was balanced using techniques such as SMOTE, ensuring that the classes "income <=50K" and "income >50K" have the same number of records.

### Model Performance 💪
**Overall Accuracy:** 90%

**Metrics by Class:**

**Class 0 (income <=50K):** Needs 90% precision and recall.

**Class 1 (income >50K):** Similar results, with results and recall of 89-90%.

### Dependencies 📦
Make sure you have the necessary dependencies installed:

- pandas

- scikit-learn

- xgboost

- matplotlib

- seaborn

- imbalanced-learn

**How ​​to run**:
```bash
$ python3 main.py
