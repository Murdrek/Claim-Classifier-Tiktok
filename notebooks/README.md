📓 Notebooks: Data Preparation & Inspection
This directory contains the core Python development for the Automatidata project, focused on the NYC Taxi & Limousine Commission (TLC) dataset.

📑 Project Context
The primary goal of these notebooks is to transform raw, historical taxi data into a structured format ("Tidy Data") to build a reliable fare estimation tool.

🛠️ Main Notebook
Activity_Course 2 Automatidata project lab.ipynb
This notebook covers the Plan and Analyze phases of the PACE framework:

Data Loading & Structuring: Initial inspection of 18 variables from the TLC dataset.

Anomaly Detection: Identification of critical data inconsistencies, such as trips with 0.00 miles but fares as high as $450.00.

Exploratory Data Analysis (EDA): Preliminary statistical review of trip distances and fare amounts, which are heavily right-skewed.

🧪 Technical Stack
Python: Primary language for data manipulation.

Pandas & NumPy: For data cleaning and matrix operations.

PACE Framework: Methodology used to ensure an ethical and structured analytical workflow.

📈 Next Steps in the Pipeline
Deep-Dive EDA: Visualizing correlations between time of day and total fare.

Feature Engineering: Refining variables like duration estimates and peak hour indicators.

Model Selection: Testing XGBoost and Multiple Linear Regression.
