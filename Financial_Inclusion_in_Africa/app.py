#import packages 
import streamlit as st
import joblib
import xgboost as xgb
import pandas as pd

# add banner image
st.header("Financial Inclusion in Africa")
st.subheader(
    """
How likely is it for one to have a bank acccount?.
"""
)

# form to collect user information
my_form = st.form(key="financial_form")
country = my_form.selectbox("select country", ("Tanzania", "kenya", "Uganda", "Rwanda"))
location_type = my_form.selectbox("select location", ("Rural", "Urban"))
year = my_form.number_input("Inter year", min_value=2000, max_value=2100)
cellphone_access = my_form.selectbox("Do you have a cellphone?", ("Yes", "No"))
gender_of_respondent = my_form.selectbox("Gender", ("Female", "Male"))
relationship_with_head = my_form.selectbox(
    "what is your relationship with the head of the family",
    (
        "Spouse",
        "Head of Household",
        "Other relative",
        "Child",
        "Parent",
        "Other non-relatives",
    ),
)
marital_status = my_form.selectbox(
    "Your marital status",
    (
        "Married/Living together",
        "Widowed",
        "Single/Never Married",
        "Divorced/Seperated",
        "Dont know",
    ),
)
education_level = my_form.selectbox(
    "Your education level",
    (
        "Secondary education",
        "No formal education",
        "Vocation/Specialised training",
        "Primary education",
        "Tertiary education",
        "Other/Dont know/RTA",
    ),
)
job_type = my_form.selectbox(
    "Your job type",
    (
        "Self employed",
        "Government Dependent",
        "Formally employed Private",
        "Informally employed",
        "Formally employed Government",
        "Farming and Fishing",
        "Remittance Dependent",
        "Other Income",
        "Dont Know/Refuse to answer",
        "No Income",
    ),
)
household_size = my_form.number_input(
    "How many people are living in the house?", min_value=1, max_value=100
)

age_of_respondent = my_form.number_input("Your age", min_value=18, max_value=120)

submit = my_form.form_submit_button(label="make prediction")


# load the model and one-hot-encoder and scaler

with open("Financial_Inclusion_in_Africa/fin-inclusion.pkl",
    "rb",
) as f:
    model = joblib.load(f)

@st.cache
# function to clean and tranform the input


if submit:

    # collect inputs
    input = {
        "country": country,
        "year": year,
        "location_type": location_type,
        "cellphone_access": cellphone_access,
        "household_size": household_size,
        "age_of_respondent": age_of_respondent,
        "gender_of_respondent": gender_of_respondent,
        "relationship_with_head": relationship_with_head,
        "marital_status": marital_status,
        "education_level": education_level,
        "job_type": job_type,
    }

          
    # create a dataframe
    data = pd.DataFrame(inputs, columns=["country",
        "year",
        "location_type",
        "cellphone_access",
        "household_size",
        "age_of_respondent",
        "gender_of_respondent",
        "relationship_with_head",
        "marital_status",
        "education_level",
        "job_type"], index=[0])
    
    
    # perform prediction
    prediction = model.predict(data)
    output = int(prediction[0])
    probas = model.predict_proba(data)
    probability = "{:.2f}".format(float(probas[:, output]))

    # Display results
    st.header("Results")
    if output == 1:
        st.write(
            "You are most likely to have a bank account with probability of {} 😊".format(
                probability
            )
        )
    elif output == 0:
        st.write(
            "You are most likely not to have a bank account with probability of {} 😔".format(
                probability
            )
        )


url = "https://twitter.com/ashioyajotham"
st.write("Developed by [Victor Jotham Ashioya](%s)" % url)
