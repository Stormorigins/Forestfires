import streamlit as st
import pickle
import numpy as np
import sklearn

def predict_selling_price(Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region):

    #change the datatypes "string" to "int"
    Temperature= float(Temperature)
    RH= float(RH)
    RH= float(RH)
    RH= float(RH)
    RH= float(RH)
    DMC= float(DMC)
    ISI= float(ISI)
    Classes= float(Classes)
    Region= float(Region)
    #modelfile of the classification
    with open("C:/Users/Aishwarya MMPL/Documents/GUVI_PYTHON/Udemy/ML/Complete-Data-Science-With-Machine-Learning-And-NLP-2024-main/4-Ridge Lasso And Elasticnet/Ridge Lassso Elastic Regression Practicals/ridge.pkl","rb") as f:
        model_regg=pickle.load(f)
    
    with open("C:/Users/Aishwarya MMPL/Documents/GUVI_PYTHON/Udemy/ML/Complete-Data-Science-With-Machine-Learning-And-NLP-2024-main/4-Ridge Lasso And Elasticnet/Ridge Lassso Elastic Regression Practicals/scaler.pkl","rb") as f1:
        standard=pickle.load(f1)

    data=standard.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
    
    y_pred= model_regg.predict(data)

    # ac_y_pred= np.exp(y_pred[0])

    return y_pred


st.header("**PREDICT SELLING PRICE**")
st.write(" ")

col1,col2= st.columns(2)



with col1:
    Temperature= st.number_input(label="Enter the Temperature")
    RH= st.number_input(label="Enter the Relative Humidity")
    Ws= st.number_input(label="Enter the Wind speed")
    Rain= st.number_input(label="Enter the Rain")
    FFMC= st.number_input(label="Enter the Fine Fuel Moisture Code")

with col2:
    DMC= st.number_input(label="Enter the Duff Moisture Code")
    ISI= st.number_input(label="Enter the Drought Code")
    Classes= st.number_input(label="Enter the Classes")
    Region= st.number_input(label="Enter the Region")
    
    

button= st.button(":violet[***PREDICT THE SELLING PRICE***]",use_container_width=True)
if button:
    price= predict_selling_price(Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region)    
st.write(f"## :green[**The Selling Price is :**{price}]")