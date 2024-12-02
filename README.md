# Data Cleaning Master

**Data Cleaning Master** is a Python-based application designed to clean datasets efficiently. It handles duplicates, missing values, and ensures clean output in seconds. This tool is highly performant, user-friendly, and tested on large datasets to ensure accuracy and speed. It’s particularly useful in the early stages of data analysis or machine learning projects, where data quality is crucial to building reliable models and insights.

---

https://github.com/user-attachments/assets/02b33e6b-def3-4882-8e66-2c2ab3466be4

---


## Why It's Useful

Data cleaning is one of the most time-consuming tasks in data science and analytics. **Data Cleaning Master** automates this process by providing a simple yet powerful solution to handle common issues like duplicate entries and missing values. This tool streamlines the preparation of datasets, allowing data scientists and analysts to focus on analysis rather than manual cleaning tasks.

The application:

- **Removes duplicate records** and saves a backup for further review.
- **Handles missing values** by filling numeric columns with the mean and removing rows with missing non-numeric values.
- **Supports CSV and Excel files**, making it versatile for a variety of projects.

## Key Features

- **Fast & Efficient**: Cleans datasets with thousands of rows in seconds.
- **Duplicate Backup**: Saves a backup of duplicate records before removal.
- **Missing Values Handling**: Replaces missing numeric values with column means and drops rows with missing non-numeric values.
- **User-Friendly**: Clear prompts guide users through the process step-by-step.
- **Multiple Format Support**: Handles both CSV and Excel files seamlessly.

## Skills Required

### Technical Skills:
- **Python 3.x**: For writing the data cleaning logic.
- **Pandas**: To handle data manipulation and cleaning.
- **NumPy**: For numerical operations like calculating the mean of columns.
- **Streamlit**: To create the interactive UI for file upload and data cleaning.
- **OS Library**: To manage file operations and system paths.

### Soft Skills:
- **Attention to Detail**: Ensuring accurate cleaning of data, such as correctly handling duplicates and missing values.
- **Problem Solving**: Identifying data issues and finding effective solutions, like filling missing numeric values or removing invalid entries.
- **Communication**: Providing clear and concise user prompts and messages to guide users through the process.
- **Time Management**: Ensuring the data cleaning process is completed efficiently, even with large datasets.
- **Adaptability**: The ability to adapt to different data formats and handle various data types appropriately.

## Objectives

- Clean datasets in various formats (CSV, Excel).
- Remove duplicates and store them separately.
- Handle missing values:
  - Replace missing numeric values with the mean of the column.
  - Remove rows with missing non-numeric values.
- Save and export the cleaned dataset with an option to download.

## Step-by-Step Process

1. **Input & File Verification**  
   Upload a CSV or Excel file. The app verifies the file format and reads the data.

2. **Duplicate Detection**  
   The app checks for duplicate rows, saves them in a separate file (`XYZ.csv`), and removes them from the main dataset.

3. **Handle Missing Values**  
   - For numeric columns: Fills missing values with the mean of the respective column.
   - For non-numeric columns: Removes rows containing missing values.

4. **Export Clean Data**  
   After cleaning, the dataset is saved as `XYZ.csv` and made available for download.

5. **Testing & Performance**  
   The app has been tested on datasets with over 10,000 rows, handling large datasets in seconds without errors. It performs reliably in both standalone and Jupyter Notebook environments.

## Usage

1. Run the app using Streamlit:
   ```bash
   streamlit run app.py
