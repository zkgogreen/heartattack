import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('heart.sav', 'rb'))
st.title("Predection and Analysis of Heart Attack")

col1, col2 = st.columns(2)

# with col1:
#     Pregnancies = st.text_input('Input nilai Pregnancies')
#     Glucose = st.text_input('Input nilai Glucose')
#     BloodPressure = st.text_input('Input nilai BloodPressure')
#     SkinThickness = st.text_input('Input nilai SkinThickness')

# with col2:
#     Insulin = st.text_input('Input nilai Insulin')
#     BMI = st.text_input('Input nilai BMI')
#     DiabetesPedigreeFunction = st.text_input('Input nilai DiabetesPedigreeFunction')
#     Age = st.text_input('Input nilai Age')

with col1:
    age = st.text_input("Age")
    sex = st.text_input("sex")
    cp = st.text_input("cp")
    trtbps = st.text_input("trtbps")
    chol = st.text_input("chol")
    fbs = st.text_input("fbs")
    restecg = st.text_input("restecg")

with col2:
    thalachh = st.text_input("thalachh")
    exng = st.text_input("exng")
    oldpeak = st.text_input("oldpeak")
    slp = st.text_input("slp")
    caa = st.text_input("caa")
    thall = st.text_input("thall")

diab_diagnosis = ''

if st.button("Predict"):
    diab_prediction = diabetes_model.predict([[
       age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall
       ]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = "You are potentialy get heart attact"
    else:
        diab_diagnosis = "You're fine, be safe"

    st.success(diab_diagnosis)