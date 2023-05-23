import streamlit as st
import pickle
from streamlit_option_menu import option_menu


#loading the model 
with open("C:\\Users\\AMANDEEP KAUR\\Desktop\\Credit Card\\Fraud_Detection.sav", 'rb') as file:
    fraud_detection_model = pickle.load(file)

#creating the side bar
with st.sidebar:
    selected = option_menu("Created by -  Amandeep Kaur",['Fraud Detection'])

if (selected == 'Fraud Detection'):

    st.title("Credit Card Fraud Detection System")

    # Input fields for feature values
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    # Input fields for feature values
    with col1:
        try:
            V1 = float(st.text_input("Enter the value of V1"))
        except ValueError:
            V1 = 0.0
        
    with col2:
        try:
            V2 = float(st.text_input("Enter the value of V2"))
        except ValueError:
            V2 = 0.0

    with col3:
        try:
            V3 = float(st.text_input("Enter the value of V3"))
        except ValueError:
            V3 = 0.0
        
    with col4:
        try:
            V4 = float(st.text_input("Enter the value of V4"))
        except ValueError:
            V4 = 0.0
    
    with col5:
        try:
            V5 = float(st.text_input("Enter the value of V5"))
        except ValueError:
            V5 = 0.0
        
    with col6:
        try:
            V6 = float(st.text_input("Enter the value of V6"))
        except ValueError:
            V6 = 0.0

    with col7:
        try:
            V7 = float(st.text_input("Enter the value of V7"))
        except ValueError:
            V7 = 0.0
        
    with col1:
        try:
            V8 = float(st.text_input("Enter the value of V8"))
        except ValueError:
            V8 = 0.0

    with col2:
        try:
            V9 = float(st.text_input("Enter the value of V9"))
        except ValueError:
            V9 = 0.0

    with col3:
        try:
            V10 = float(st.text_input("Enter the value of V10"))
        except ValueError:
            V10 = 0.0
        
    with col4:
        try:
            V11 = float(st.text_input("Enter the value of V11"))
        except ValueError:
            V11 = 0.0
    
    with col5:
        try:
            V12 = float(st.text_input("Enter the value of V12"))
        except ValueError:
            V12 = 0.0
        
    with col6:
        try:
            V13 = float(st.text_input("Enter the value of V13"))
        except ValueError:
            V13 = 0.0

    with col7:
        try:
            V14 = float(st.text_input("Enter the value of V14"))
        except ValueError:
            V14 = 0.0

    with col1:
        try:
            V15 = float(st.text_input("Enter the value of V15"))
        except ValueError:
            V15 = 0.0

    with col2:
        try:
            V16 = float(st.text_input("Enter the value of V16"))
        except ValueError:
            V16 = 0.0

    with col3:
        try:
            V17 = float(st.text_input("Enter the value of V17"))
        except ValueError:
            V17 = 0.0
        
    with col4:
        try:
            V18 = float(st.text_input("Enter the value of V18"))
        except ValueError:
            V18 = 0.0
    
    with col5:
        try:
            V19 = float(st.text_input("Enter the value of V19"))
        except ValueError:
            V19 = 0.0
        
    with col6:
        try:
            V20 = float(st.text_input("Enter the value of V20"))
        except ValueError:
            V20 = 0.0

    with col7:
        try:
            V21 = float(st.text_input("Enter the value of V21"))
        except ValueError:
            V21 = 0.0
    
    with col1:
        try:
            V22 = float(st.text_input("Enter the value of V22"))
        except ValueError:
            V22 = 0.0

    with col2:
        try:
            V23 = float(st.text_input("Enter the value of V23"))
        except ValueError:
            V23 = 0.0

    with col3:
        try:
            V24 = float(st.text_input("Enter the value of V24"))
        except ValueError:
            V24 = 0.0
        
    with col4:
        try:
            V25 = float(st.text_input("Enter the value of V25"))
        except ValueError:
            V25 = 0.0
    
    with col5:
        try:
            V26 = float(st.text_input("Enter the value of V26"))
        except ValueError:
            V26 = 0.0
        
    with col6:
        try:
            V27 = float(st.text_input("Enter the value of V27"))
        except ValueError:
            V27 = 0.0

    with col7:
        try:
            V28 = float(st.text_input("Enter the value of V28"))
        except ValueError:
            V28 = 0.0


    # Perform fraud detection when button is clicked
    if st.button("Detect Fraud"):
        features = [[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28]]  
        result = fraud_detection_model.predict(features)

        if result[0] == 1:
            st.write("Fraudulent Transaction Detected!")
        else:
            st.write("Transaction is Safe.")

