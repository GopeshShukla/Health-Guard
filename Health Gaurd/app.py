import os 
import pickle
import streamlit as st
from streamlit_option_menu  import option_menu

#set page configuration

st.set_page_config(page_title="Health Gaurd",layout= "wide") 

# getting the working directory of the .py file

working_dir = os.path.dirname(os.path.abspath(__file__))

# loading of the saved models

diabetes_model = pickle.load(open('diabetes.pkl','rb'))
heart_model = pickle.load(open('heart.pkl','rb'))
parkinson_model = pickle.load(open('parkinson.pkl','rb'))
stroke_model = pickle.load(open('stroke.pkl','rb'))
#Header
st.title("Multiple Disease Prediction System")
#sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Stroke Prediction'],menu_icon='hospital-fill',icons=['activity', 'heart', 'person', 'lightning'],default_index=0)
if selected == 'Diabetes Prediction':
	st.header('Welcome to the Diabetes Prediction Model'.title())
	col1,col2,col3 = st.columns(3)
	glucose = col1.slider('Glucose Level',0,500,120)
	bp  = col1.slider('Blood Pressure Level',0,200,120)
	skthic = col3.slider('Skin Thickness Value',0,100,20)
	insulin =col1.slider('Insulin Level',0,900,30)
	bmi= col2.slider('BMI Value',0.0,70.0,25.0)
	dpf= col3.slider('Diabetes Pedigree Function Value',0.0,2.5,0.5)
	age = col2.slider('Age',0,100,25)	
	
	if st.button('Diabetes Test Result'):
		user_input = [glucose,bp,skthic,insulin,bmi,dpf,age]
		pred = diabetes_model.predict([user_input])[0]
		diab_diagnosis = 'The Person Is Diabetic' if pred == 1 else 'The Person Is Not Diabetic'
		st.success(diab_diagnosis)
       
elif selected == 'Heart Disease Prediction':
    st.header('Welcome to the Heart Disease Prediction Model'.title())
    col1,col2,col3 = st.columns(3)
    
    age = col1.slider("Age",0,100,25)
    gender = col2.radio("Gender",["Male","Female"])
    cp = col3.selectbox('Chest Pain Type',['Type1','Type2','Type3','Type4'])
    trestbps = col1.slider('Resting Blood pressure',0,200,120)
    chol = col2.slider('Serum Cholestrol in mg/dl',50,600,200)
    fbs = col3.radio('Fasting Blood Pressure > 120',['Yes','No'])
    restecg = col1.radio('Resting Electrocardiograph Result',['Normal','Abnormal'])
    mhra = col2.slider('Maximum Heart Rate Achieved',50,200,80)
    ang = col3.radio('Exercise Include Angina',['Yes','No']) #exercise karte samaya hone wala dil ka dard
    oldpeak = col1.slider('ST depression include by exercise',0.0,10.0,1.0)
    slope = col2.selectbox('Slope of the peakexercise ST segment',['Upsloping','Flat','Downsloping'])
    cf = col3.slider('Major vessels colored by flourosopy',0,4,0)
    thal = col1.selectbox('Thalassemia',['Normal','Fixed Defect','Reversable Defect'])
    
    #mapping categorical data ("Vo data jisme ek se aadhik value ho sakti hai jaise ki selectbox ki values.")
    
    cp_mapping = {'Type1':0,'Type2':1,'Type3':2,'Type4':3}
    slope_mapping = {'Upsloping':0,'Flat':1,'Downsloping':2}
    thal_mapping = {'Normal':0,'Fixed Defect':1,'Reversable Defect':2}
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, 1 if gender == 'Male' else 0,cp_mapping[cp],trestbps,chol,1 if fbs == 'Yes' else 0,1 if restecg == 'Normal' else 0,mhra,1 if ang == 'Yes' else 0,oldpeak,slope_mapping[slope],cf,thal_mapping[thal]]
        pred = heart_model.predict([user_input])[0]
        heart_diagnosis = 'The person is having Heart Disease.' if pred == 1 else 'The person does not having Heart Disease.'
        st.success(heart_diagnosis)
            

elif selected == 'Parkinsons Prediction':
    st.header('Welcome to the Parkinson Disease Prediction Model'.title())
    
# Streamlit layout with three columns
    col1, col2, col3 = st.columns(3)

# Feature sliders based on dataset's statistical range
    with col1:
        MDVP_Fo = st.slider("Average Fundamental Frequency(Hz)", min_value=88.000, max_value=260.000, value=154.000)
        MDVP_Fhi = st.slider("Maximum Fundamental Frequency(Hz) ", min_value=102.000, max_value=592.000, value=197.000)
        MDVP_Flo = st.slider("Minimum Fundamental Frequency (Hz)", min_value=65.476, max_value=239.170, value=116.000)
        MDVP_Jitter = st.slider("Frequency Variation (Jitter %)", min_value=0.0017, max_value=0.0332, value=0.0062)
        MDVP_Jitter_Abs = st.slider("Absolute Frequency Variation", min_value=0.000007, max_value=0.00026, value=0.000044)
        MDVP_RAP = st.slider("Relative Average Perturbation (RAP)", min_value=0.000001, max_value=0.02144, value=0.0033)
        MDVP_PPQ = st.slider("Period Perturbation Quotient (PPQ)", min_value=0.000920, max_value=0.019580, value=0.0034)
        Jitter_DDP = st.slider("Frequency Perturbation (DDP)", min_value=0.002040, max_value=0.064330, value=0.0099)  

    with col2:
        MDVP_Shimmer = st.slider("Amplitude Variation (Shimmer %)", min_value=0.00954, max_value=0.11908, value=0.0297)
        MDVP_Shimmer_dB = st.slider("Amplitude Variation (dB)", min_value=0.085, max_value=1.302, value=0.282)
        Shimmer_APQ3 = st.slider("Amplitude Perturbation (APQ3)", min_value=0.00954, max_value=0.11908, value=0.0297)
        Shimmer_APQ5 = st.slider("Amplitude Perturbation (APQ5)", min_value=0.085, max_value=1.302, value=0.282)
        MDVP_APQ = st.slider("Amplitude Perturbation (APQ)", min_value=0.00068, max_value=0.02144, value=0.0033)
        Shimmer_DDA = st.slider("Amplitude Difference of Differences (DDA)", min_value=0.01364, max_value=0.16942, value=0.047)
        NHR = st.slider("Noise-to-Harmonics Ratio (NHR)", min_value=0.00065, max_value=0.31482, value=0.0248)
        HNR = st.slider("Harmonics-to-Noise Ratio (HNR)", min_value=8.441, max_value=33.047, value=21.9)

    with col3:
        RPDE = st.slider("Recurrence Period Density Entropy (RPDE)", min_value=0.256600, max_value=0.68520, value=0.4985)
        DFA = st.slider("Signal Complexity (DFA)", min_value=0.574300, max_value=0.825288, value=0.7181)
        spread1 = st.slider("Frequency Deviation (spread1)", min_value=-7.965, max_value=-2.434, value=-5.684)
        spread2 = st.slider("Frequency Irregularity (spread2)", min_value=0.006200, max_value=0.450500, value=0.2265)
        D2 = st.slider("Signal Complexity Measure (D2)", min_value=1.42300, max_value=3.67100, value=2.382)
        PPE = st.slider("Pitch Variation (PPE)", min_value=0.044500, max_value=0.527400, value=0.2066)

    # Button to run prediction
    if st.button('Parkinson’s Disease Test Result'):
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP,MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA,NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
    
    # Perform prediction using the loaded model
        prediction = parkinson_model.predict([user_input])[0]
        parkinsons_diagnosis = 'The person may have Parkinson’s disease.' if prediction == 1 else 'The person is unlikely to have Parkinson’s disease.'
        st.success(parkinsons_diagnosis) 
        
#UI of stroke prediction model

elif selected == 'Stroke Prediction':
    
    st.header("Welcome to the Stroke Prediction Model".title())
    # Creating a layout with three columns.
    col1,col2,col3 = st.columns(3)
    
    with col1:
        sex = st.radio("Sex", options=["Male", "Female"])
        age = st.slider("Age", min_value=1, max_value=120, value=30)
        hypertension = st.radio("Hypertension", options=["No", "Yes"])
        heart_disease = st.radio("Heart Disease", options=["No", "Yes"])    

    with col2:
        ever_married = st.radio("Ever Married", options=["No", "Yes"])
        work_type = st.selectbox("Work Type", options=["Private", "Self-employed", "Government", "Children", "Never worked"])
        Residence_type = st.radio("Residence Type", options=["Urban", "Rural"])
        avg_glucose_level = st.slider("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
            
    with col3:
        bmi = st.slider("BMI", min_value=10.0, max_value=100.0, value=25.0)
        smoking_status = st.radio("Smoking Status", options=["Smoker", "Non Smoker"])

    #mapping categorical data 
    #creating a dictionary for categorical data (work_type) 
    work_type_mapping = {"Private":0, "Self-employed":1, "Government":2, "Children":3, "Never worked":4}      
    
    if st.button('Heart Disease Test Result'):
        user_input = [
            1 if sex == "Male" else 0,
            age,
            1 if hypertension == "Yes" else 0,
            1 if heart_disease == "Yes" else 0,
            1 if ever_married == "Yes" else 0,
            work_type_mapping[work_type],
            1 if Residence_type == "Urban" else 0,
            avg_glucose_level,
            bmi,
            1 if smoking_status == "Smoker" else 0 
        ] 
            
        prediction = stroke_model.predict([user_input])[0]  
        result =  "The person may be at risk of a stroke." if prediction == 1 else "The person is unlikely to be at risk of a stroke."
        st.success(result)
        
    
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    






