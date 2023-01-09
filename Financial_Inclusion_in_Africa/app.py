import pickle
import streamlit as st
import pandas as pd
import numpy as np


# Create a app title with title method
st.title("Financial Inclusion in Africa")

# Create a subheader with subheader method
st.subheader("Get your financial inclusion status")

# Create a text with text method
st.text("Please fill the form below")


# Load the pickled model
with open('fin-inclusion.pkl', 'rb') as f:
    model = pickle.load(f)

# We created selectbox for categorical columns and used slider 
# numerical values ,specified range and step 

# Create a selectbox for the location
locations = ('Rwanda', 'Tanzania', 'Kenya', 'Uganda', 'Burundi')
location_type = st.selectbox('Location', locations)

# cell phone access
cellphone_access = st.selectbox('Cell Phone Access', ('Yes', 'No'))

# Create a slider for the household size
household_size = st.slider('Household Size', 1, 20, 1)

# Create a slider for the age of the respondent
respondent_age = st.slider('Respondent Age', 16, 100, 16)


# in order to recieved client inputs appended these inputs (created above) 
# into dictionary as we mentioned before. And We returned into dataframe.
data = {"location_type": location_type, 
        "cellphone_access": cellphone_access,
        "household_size": household_size}

# Convert data into dataframe
df = pd.DataFrame.from_dict([data])

# And appended column names into column list. 
# We need columns to use with reindex method as we mentioned before.
columns = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36
]
df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
prediction = model.predict(df)

# Submited button to predict
if st.button('Predict'):
    if prediction == 0:
        st.write('You are not financially included')
    else:
        st.write('Hello, you are financially included')
