import pandas as pd
import numpy as np
import streamlit as st
import pickle

def process_input_data(input_data):
      # Convert categorical variables to numerical values
        if input_data["country"] == "Rwanda":
            country = 0
        elif input_data["country"] == "Tanzania":
            country = 1
        elif input_data["country"] == "Uganda":
            country = 2
        elif input_data["country"] == "Kenya":
            country = 3
        else:
            country = 4

        if input_data["year"] == "2016":
            year = 0
        elif input_data["year"] == "2017":
            year = 1
        else:
            year = 2

        if input_data["location_type"] == "Rural":
            location_type = 0
        else:
            location_type = 1

        if input_data["cellphone_access"] == "Yes":
            cellphone_access = 1
        else:
            cellphone_access = 0

        if input_data["marital_status"] == "Married/Living together":
            marital_status = 0
        elif input_data["marital_status"] == "Widowed":
            marital_status = 1
        elif input_data["marital_status"] == "Divorced/Seperated":
            marital_status = 2
        elif input_data["marital_status"] == "Single/Never Married":
            marital_status = 3
        else:
            marital_status = 4
        if input_data["education_level"] == "No formal education":
            education_level = 0
        elif input_data["education_level"] == "Primary education":
            education_level = 1
        elif input_data["education_level"] == "Secondary education":
            education_level = 2
        elif input_data["education_level"] == "Vocational/Specialised training":
            education_level = 3
        elif input_data["education_level"] == "Tertiary education":
            education_level = 4
        else:
            education_level = 5

        if input_data["job_type"] == "Farming and Fishing":
            job_type = 0    
        elif input_data["job_type"] == "Formally employed Government":
            job_type = 1
        elif input_data["job_type"] == "Formally employed Private":
            job_type = 2
        elif input_data["job_type"] == "Informally employed":
            job_type = 3
        elif input_data["job_type"] == "Remittance Dependent":
            job_type = 4
        elif input_data["job_type"] == "Self employed":
            job_type = 5
        elif input_data["job_type"] == "Other Income":
            job_type = 6
        else:
            job_type = 7

        # Return processed input data as a NumPy array
        return np.array([[
            country, year, location_type, cellphone_access,
            input_data["houselhold_size"], input_data["age_of_respondent"],
            marital_status, education_level, job_type
        ]])

# Load the model
pickle_in = open("Financial_Inclusion_in_Africa/fin-inclusion.pkl", "rb")
model = pickle.load(pickle_in)

# Define the main app
def main():
    # Add banner image and header
    st.header("Financial Inclusion in Africa")
    st.subheader(
        """
    How likely is it for one to have a bank acccount?.
    """
    )

    # Add a submit button
    if st.button("Predict"):
        # Get user input values
        input_data = {
            "country": st.sidebar.selectbox("Country", ("Kenya", "Rwanda", "Tanzania", "Uganda")),
            "year": st.sidebar.selectbox("Year", ("2016", "2017", "2018")),
            "location_type": st.sidebar.selectbox("Location Type", ("Rural", "Urban")),
            "cellphone_access": st.sidebar.selectbox("Cellphone Access", ("Yes", "No")),
            "houselhold_size": st.sidebar.slider("Houselhold Size", 1, 21, 3),
            "age_of_respondent": st.sidebar.slider("Age of Respondent", 16, 100, 25),
            "marital_status": st.sidebar.selectbox(
                "Marital Status", (
                    "Married/Living together", "Widowed", "Divorced/Seperated",
                    "Single/Never Married", "Dont know"
                )
            ),
            "education_level": st.sidebar.selectbox(
                "Education Level", (
                    "No formal education", "Primary education", "Secondary education",
                    "Vocational/Specialised training", "Tertiary education", "Other (specify)"
                )
            ),

            "job_type": st.sidebar.selectbox(
                "Job Type", (
                    "Farming and Fishing", "Formally employed Government", "Formally employed Private",
                    "Informally employed", "Remittance Dependent", "Self employed", "Other Income",
                    "No Income"
                )
            )
        }


        # Process input data
        processed_input_data = process_input_data(input_data)

        # Make predictions
        prediction = model.predict(processed_input_data, columns=['country', 'year', 'location_type', 'cellphone_access', 'houselhold_size', 
        'age_of_respondent', 'marital_status', 'education_level', 'job_type'])


        # Display the prediction
        st.subheader("Prediction")
        if prediction == 1:
            st.write("The respondent is likely to have a bank account")
        else:
            st.write("The respondent is unlikely to have a bank account")

# Run the main app

if __name__ == "__main__":
    main()
