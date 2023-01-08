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

def predict_financial_inclusion(
    country, year, location_type, cellphone_access, 
    houselhold_size, age_of_respondent, marital_status, education_level, job_type):

    # country
    if country == "Rwanda":
        country = 0
    elif country == "Tanzania":
        country = 1
    elif country == "Uganda":
        country = 2
    elif country == "Kenya":
        country = 3
    else:
        country = 4

    # year
    if year == "2016":
        year = 0
    elif year == "2017":
        year = 1
    else:
        year = 2

    # location_type
    if location_type == "Rural":
        location_type = 0
    else:
        location_type = 1

    # cellphone_access
    if cellphone_access == "Yes":
        cellphone_access = 1
    else:
        cellphone_access = 0

    # marital_status
    if marital_status == "Married/Living together":
        marital_status = 0
    elif marital_status == "Widowed":
        marital_status = 1
    elif marital_status == "Divorced/Seperated":
        marital_status = 2
    elif marital_status == "Single/Never Married":
        marital_status = 3
    else:
        marital_status = 4

    # education_level
    if education_level == "No formal education":
        education_level = 0
    elif education_level == "Primary education":
        education_level = 1
    elif education_level == "Secondary education":
        education_level = 2
    elif education_level == "Vocational/Specialised training":
        education_level = 3
    elif education_level == "Tertiary education":
        education_level = 4
    else:
        education_level = 5

    # job_type
    if job_type == "Farming and Fishing":
        job_type = 0
    elif job_type == "Formally employed Government":
        job_type = 1
    elif job_type == "Formally employed Private":
        job_type = 2
    elif job_type == "Informally employed":
        job_type = 3
    elif job_type == "Remittance Dependent":
        job_type = 4
    elif job_type == "Self employed":
        job_type = 5
    elif job_type == "Other Income":
        job_type = 6
    else:
        job_type = 7

# Let's style the app
st.markdown(
    """
<style>
body {
    color: #fff;
    background-color: #111;
}
</style>
""",
    unsafe_allow_html=True,
)

# add sidebar
st.sidebar.header("User Input Parameters")

# add a selectbox to the sidebar
def user_input_features():
    country = st.sidebar.selectbox("Country", ("Kenya", "Rwanda", "Tanzania", "Uganda"))
    year = st.sidebar.selectbox("Year", ("2016", "2017", "2018"))
    location_type = st.sidebar.selectbox("Location Type", ("Rural", "Urban"))
    cellphone_access = st.sidebar.selectbox("Cellphone Access", ("Yes", "No"))
    houselhold_size = st.sidebar.slider("Houselhold Size", 1, 21, 3)
    age_of_respondent = st.sidebar.slider("Age of Respondent", 16, 100, 25)
    marital_status = st.sidebar.selectbox(
        "Marital Status", (
            "Married/Living together", "Widowed", "Divorced/Seperated",
            "Single/Never Married", "Dont know"
        )
    )
    education_level = st.sidebar.selectbox(
        "Education Level", (
            "No formal education", "Primary education", "Secondary education",
            "Vocational/Specialised training", "Tertiary education", "Other/Dont know/RTA"
        )
    )
    job_type = st.sidebar.selectbox(
        "Job Type", (
            "Farming and Fishing", "Formally employed Government", "Formally employed Private",
            "Informally employed", "Remittance Dependent", "Self employed", "Other Income",
            "No Income"
        )
    )

    # load the model
    model = joblib.load("fin-inclusion.pkl")

    # create a dataframe
    df = pd.DataFrame(
        columns=[
            "country", "year", "location_type", "cellphone_access",
            "houselhold_size", "age_of_respondent", "marital_status", "education_level", "job_type"
        ],
        data=[
            [

                country, year, location_type, cellphone_access, houselhold_size, 
                age_of_respondent, marital_status, education_level, job_type
            ]
        ],
    )

    # predictions
    prediction = model.predict(df)
    probability = model.predict_proba(df)

# Submit button
if st.sidebar.button("Predict"):
    prediction = predict_financial_inclusion(
        "country", "year", "location_type", "cellphone_access", 
        "houselhold_size", "age_of_respondent", "marital_status", "education_level", "job_type"
    )
    st.subheader("Prediction")
    if prediction == 1:
        st.success("The person is likely to have or use a bank account")
    else:
        st.success("The person is unlikely to have or use a bank account")

    st.subheader("Probability")
    st.write(prediction)

# add footer
st.markdown(
    """
<style>
footer {
    color: #fff;
    background-color: #111;
}
</style>
""",
    unsafe_allow_html=True,
)
