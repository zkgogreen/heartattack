import pickle
import streamlit as st

# membaca model
diabetes_model = pickle.load(open('heart.sav', 'rb'))
st.title("Predection and Analysis of Heart Attack")

col1, col2 = st.columns(2)

with col1:
    age = st.text_input("Age")
    sex = st.selectbox("sex",["Male","Female"])
    cp = st.slider("Chest Pain type chest pain type",0,4)
    trtbps = st.text_input("resting blood pressure (in mm Hg)")
    chol = st.text_input("cholestoral in mg/dl fetched via BMI sensor")
    fbs = st.checkbox("fasting blood sugar")
    restecg = st.slider("resting electrocardiographic results",0,2)

with col2:
    thalachh = st.text_input("maximum heart rate achieved")
    exng = st.checkbox("exercise induced angina")
    oldpeak = st.text_input("Previous peak")
    slp = st.text_input("Slope")
    caa = st.slider("number of major vessels",0,3)
    thall = st.text_input("Thal rate")

diab_diagnosis = ''
sex = 0 if sex == "Male" else 1
if st.button("Predict"):
    diab_prediction = diabetes_model.predict([[
       age,sex,cp,trtbps,chol,fbs,restecg,thalachh,exng,oldpeak,slp,caa,thall
       ]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = "You are potentialy get heart attact"
    else:
        diab_diagnosis = "You're fine, be safe"

    st.success(diab_diagnosis)
