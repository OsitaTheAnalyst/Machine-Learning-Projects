import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved model

Diabetes_model = pickle.load(open('Diabetes_prediction_model.sav','rb'))
Breast_Cancer_model = pickle.load(open('Breast_Cancer_Prediction_model.sav','rb'))
Heart_Disease_model = pickle.load(open('Heart_Disease_Prediction_model.sav','rb'))
Parkinsons_model = pickle.load(open('Parkinsons_Disease_Prediction_model.sav','rb'))
Cardio_Disease_model = pickle.load(open('Cardio_Disease_Prediction_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Detection System',
                          ['Diabetes Detection',
                           'Breast Cancer Detection',
                           'Heart Disease Detection',
                           "Parkinson's Disease Detection",
                           'Cardiovascular Disease Detection'],
                           
                           icons = ['activity','bookmark-star','heart','person-check','postage-heart'],
                          default_index = 0)
    
# Diabetes Prediction Page
if (selected == 'Diabetes Detection'):
    
    #title page
    st.title('Diabetes Detection Model')
    
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level') 
    with col3:
        BloodPressure = st.text_input('BloodPressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Values')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age Of Patient')
        
        
    #code for prediction
    diab_diagnosis =''
    
    #creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = Diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,
                                        BMI,DiabetesPedigreeFunction,Age]])
        if diab_prediction[0]==0:
            diab_diagnosis = 'Patient is not Diabetic'
        else:
            diab_diagnosis = 'Patient is Diabetic'
        
        
    st.success(diab_diagnosis)    
    
# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Detection'):
    
    #title page
    st.title('Breast Cancer Detection Model')
    
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        mean_radius = st.text_input('Mean Radius')
    with col2:
        mean_texture = st.text_input('Mean Texture') 
    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')
    with col1:
        mean_area = st.text_input('Mean Area')
    with col2:
        mean_smoothness = st.text_input('Mean Smoothness')
    with col3:
        mean_compactness = st.text_input('Mean Compactness')
    with col1:
        mean_concavity = st.text_input('Mean Concavity')
    with col2:
        mean_concave_points = st.text_input('Mean Concave Points')
    with col3:
        mean_symmetry = st.text_input('Mean Symmetry')
    with col1:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension') 
    with col2:
        radius_error = st.text_input('Radius Error')
    with col3:
        texture_error = st.text_input('Texture Error')
    with col1:
        perimeter_error = st.text_input('Perimeter Error')
    with col2:
        area_error = st.text_input('Area Error')
    with col3:
        smoothness_error = st.text_input('Smoothness Error')
    with col1:
        compactness_error = st.text_input('Compactness Error')    
    with col2:
        concavity_error = st.text_input('Concavity Error')
    with col3:
        concave_points_error = st.text_input('Concave Points Error') 
    with col1:
        symmetry_error = st.text_input('Symmetry Error')
    with col2:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
    with col3:
        worst_radius = st.text_input('Worst Radius')
    with col1:
        worst_texture = st.text_input('Worst Texture')
    with col2:
        worst_perimeter = st.text_input('Worst Perimeter')
    with col3:
        worst_area = st.text_input('Worst Area')
    with col1:
        worst_smoothness = st.text_input('Worst Smoothness') 
    with col2:
        worst_compactness = st.text_input('Worst Compactness')
    with col3:
        worst_concavity = st.text_input('Worst Concavity')
    with col1:
        worst_concave_points = st.text_input('Worst Concave Points')
    with col2:
        worst_symmetry = st.text_input('Worst Symmetry')
    with col3:
        worst_fractal_dimension = st.text_input('Worst Fractal Dimension')
        
    
    #code for prediction
    breast_cancer_diagnosis =''
    
    #creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction = Breast_Cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,
                                                           mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,
                                                           mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,
                                                           smoothness_error,compactness_error,concavity_error,concave_points_error,
                                                           symmetry_error,fractal_dimension_error,worst_radius,worst_texture,
                                                           worst_perimeter,worst_area,worst_smoothness,worst_compactness,
                                                           worst_concavity,worst_concave_points,worst_symmetry,
                                                           worst_fractal_dimension]])
        if breast_cancer_prediction[0]==0:
            breast_cancer_diagnosis = 'Breast Cancer is Malignant'
        else:
            breast_cancer_diagnosis = 'Breast Cancer is Benign'
        
        
    st.success(breast_cancer_diagnosis)
        
# Heart Disease Prediction Page
if (selected == 'Heart Disease Detection'):
    
    #title page
    st.title('Heart Disease Detection Model')
    
     #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex') 
    with col3:
        cp = st.text_input('Chest Pain Type (4 values)')
    with col1:
        trestbps = st.text_input('Resting blood pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (values 0,1,2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('Oldpeak = ST Depression induced By Exercise Relative To Rest') 
    with col2:
        slope = st.text_input('The slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Number of major vessels (0-3) colored by flourosopy')
    with col1:
        thal = st.text_input('Thal: 0 = Normal; 1 = Fixed defect; 2 = Reversable defect')
    
    
    #code for prediction
    heart_diagnosis =''
    
    #creating a button for Prediction
    if st.button('Heart Test Result'):
        heart_disease_prediction = Heart_Disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if heart_disease_prediction[0]==0:
            heart_diagnosis = 'Patient does not have a Heart Disease'
        else:
            heart_diagnosis = 'Patient has a Heart Disease'
        
        
    st.success(heart_diagnosis)
    
# Parkinson Prediction Page
if (selected == "Parkinson's Disease Detection"):
    
    #title page
    st.title("Parkinson's Disease Detection Model")
    
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        PPE = st.text_input('PPE') 
    with col3:
        spread2 = st.text_input('spread2')
    with col1:
        MDVPFo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVPFlo = st.text_input('MDVP:Flo(Hz)')
    with col3:
        MDVPShimmer = st.text_input('MDVP:Shimmer')
    with col1:
        MDVPAPQ = st.text_input('MDVP:APQ')
    with col2:
        HNR = st.text_input('HNR')
    with col3:
        ShimmerAPQ5 = st.text_input('Shimmer:APQ5')
    with col1:
        MDVPShimmer_dB = st.text_input('MDVP:Shimmer(dB)')   
    with col2:
        ShimmerAPQ3 = st.text_input('Shimmer:APQ3') 
    with col3:
        ShimmerDDA = st.text_input('Shimmer:DDA')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        MDVPJitter_abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        RPDE = st.text_input('RPDE')
    with col1:
        MDVPPPQ = st.text_input('MDVP:PPQ')
    with col2:
        MDVPJitter_percent = st.text_input('MDVP:Jitter(%)')
    with col3:
        MDVPRAP = st.text_input('MDVP:RAP') 
    with col1:
        JitterDDP = st.text_input('Jitter:DDP')
    with col2:
        DFA = st.text_input('DFA')
    with col3:
        NHR = st.text_input('NHR')
    with col1:
        MDVPFhi = st.text_input('MDVP:Fhi(Hz)')
    
    #code for prediction
    parkinsons_diagnosis =''
    
    #creating a button for Prediction
    if st.button('Parkinsons Disease Test Result'):
        parkinsons_disease_prediction = Parkinsons_model.predict([[spread1,PPE,spread2,MDVPFo,MDVPFlo,MDVPShimmer,MDVPAPQ,
                                                                  HNR,ShimmerAPQ5,MDVPShimmer_dB,ShimmerAPQ3,ShimmerDDA,D2,
                                                                  MDVPJitter_abs,RPDE,MDVPPPQ,MDVPJitter_percent,MDVPRAP,JitterDDP,
                                                                  DFA,NHR,MDVPFhi]])
        if parkinsons_disease_prediction[0]==0:
            parkinsons_diagnosis = 'Patient does not have Parkinsons Disease'
        else:
            parkinsons_diagnosis = 'Patient has Parkinsons Disease'
        
        
    st.success(parkinsons_diagnosis)
    
# Cardio Prediction Page
if (selected == 'Cardiovascular Disease Detection'):
    
    #title page
    st.title('Cardiovascular Disease Detection Model')
    
    #columns for input fields
    col1,col2,col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        gender = st.text_input('Gender 1: Female, 2: Male') 
    with col3:
        height = st.text_input('Height (cm)')
    with col1:
        weight = st.text_input('Weight (kg)')
    with col2:
        ap_hi = st.text_input('Systolic blood pressure')
    with col3:
        ap_lo = st.text_input('Diastolic blood pressure')
    with col1:
        cholesterol = st.text_input('Cholesterol 1: normal, 2: above normal, 3: well above normal')
    with col2:
        gluc = st.text_input('Glucose 1: normal, 2: above normal, 3: well above normal')
    with col3:
        smoke = st.text_input('Smoking 1: Yes, 0: No')
    with col1:
        alco = st.text_input('Alcohol intake 1: Yes, 0: No')
    with col2:
        active = st.text_input('Physical activity 1: Yes, 0: No')    
    #code for prediction
    cardio_disease_diagnosis =''
    
    #creating a button for Prediction
    if st.button('Cardio Disease Test Result'):
        input_data = (age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active)
        input_data_numpy = np.asarray(input_data)
        reshaped_data = input_data_numpy.reshape(1,-1)
        cardio_prediction = Cardio_Disease_model.predict(reshaped_data)
       # cardio_prediction = Cardio_Disease_model.predict([[age,gender,height,weight,ap_hi,ap_lo,cholesterol,gluc,smoke,alco,active]])
        if cardio_prediction[0]==0:
            cardio_disease_diagnosis = 'Patient does not have Cardiovascular Disease'
        else:
            cardio_disease_diagnosis = 'Patient has Cardiovascular Disease'
        
        
    st.success(cardio_disease_diagnosis)                                                                                                        