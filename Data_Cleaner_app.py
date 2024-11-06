import os
import pandas as pd
import streamlit as st

def data_cleaning_master(data):
    st.write("Thank you for giving the details!")

    # Print data types of each column
    st.write("Data types of each column:")
    st.write(data.dtypes)


    # Data cleaning steps: check for duplicates
    duplicates = data.duplicated().sum()
    st.write(f"Dataset has {duplicates} duplicate rows.")
    if duplicates > 0:
        st.write("Duplicates have been removed.")
    data.drop_duplicates(inplace=True)


    # Check for missing values and show the count of missing values
    st.write("Checking for missing values...")
    missing_values = data.isnull().sum()
    st.write("Missing values count for each column:")
    st.write(missing_values)

    
    # Handling missing values (fill numeric columns with mean and round to 1 decimal)
    for col in data.columns:
        if data[col].dtype in (float, int):
            # Round to 1 decimal place when filling missing values
            data[col].fillna(data[col].mean().round(1), inplace=True)
        else:
            data.dropna(subset=[col], inplace=True)


    # Ensure data types are consistent
    for col in data.columns:
        if pd.api.types.is_integer_dtype(data[col]):
            data[col] = data[col].astype(int)
        elif pd.api.types.is_float_dtype(data[col]):
            data[col] = data[col].astype(float)
        elif pd.api.types.is_datetime64_any_dtype(data[col]):
            data[col] = pd.to_datetime(data[col], errors='coerce')
        elif pd.api.types.is_string_dtype(data[col]):
            data[col] = data[col].astype(str)

    # Show cleaned dataset preview
    st.write(f"Cleaned dataset preview:")
    st.write(data.head())

    return data

# Streamlit UI
def main():
    st.title("Data Cleaning Master")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

    # Load the file and store it in session_state
    if uploaded_file is not None:
        if 'uploaded_data' not in st.session_state:
            st.session_state.uploaded_data = uploaded_file
            st.session_state.cleaned_data = None  # Reset cleaned data

        # Read the uploaded file
        if uploaded_file.name.endswith('.csv'):
            st.write("Dataset is csv!")
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            st.write("Dataset is an Excel file!")
            data = pd.read_excel(uploaded_file)
        else:
            st.error("Unknown file type!")
            return

        st.write(f"Dataset has {data.shape[0]} rows and {data.shape[1]} columns.")
        
        # Text input for custom filename (initialize session state)
        custom_filename = st.text_input(
            "Enter the name you want for the cleaned file",
            value="Cleaned_data.csv"
        )

        # Data cleaning button
        if st.button("Clean Data"):
            # Clean the data and store it in session_state
            cleaned_data = data_cleaning_master(data)
            st.session_state.cleaned_data = cleaned_data  # Store cleaned data in session_state
            st.session_state.custom_filename = custom_filename  # Store custom filename

            # Save cleaned dataset with the custom filename
            st.session_state.cleaned_data.to_csv(custom_filename, index=False)

            # Provide a download link for the cleaned dataset
            with open(custom_filename, "rb") as f:
                st.download_button(
                    label="Download Cleaned Data",
                    data=f,
                    file_name=custom_filename,  # Ensure the filename is the custom one entered
                    mime="text/csv"
                )
                st.balloons()

if __name__ == "__main__":
    main()