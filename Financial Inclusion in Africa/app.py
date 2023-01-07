# Now we build a web app using Streamlit

import pickle
import streamlit as st
 
# loading the trained model
pickle_in = open('/home/ashioyajotham/Streamlit/Financial Inclusion in Africa/classifier.pkl', 'rb') 
classifier = pickle.load(pickle_in)

# defining the function which will make the prediction using the data which the user inputs
def prediction(Has a Bank account, Type of Location, Cell Phone Access, Household Size, Respondent) :
 
    # Pre-processing user input    
    if Has a Bank account == "Yes":
        Has a Bank account = 1
    else:
        Has a Bank account = 0
 
    if Type of Location == "Rural":
        Type of Location = 0
    elif Type of Location == "Urban":
        Type of Location = 1
    else:
        Type of Location = 2
 
    if Cell Phone Access == "Yes":
        Cell Phone Access = 1
    else:
        Cell Phone Access = 0
 
    if Respondent == "Yes":
        Respondent = 1
    else:
        Respondent = 0
 
    # Making predictions 
    prediction = classifier.predict(
        [[Has a Bank account, Type of Location, Cell Phone Access, Household Size, Respondent]])
     
    if prediction == 1:
        pred = 'Yes'
    else:
        pred = 'No'
    return pred

# this is the main function in which we define our webpage