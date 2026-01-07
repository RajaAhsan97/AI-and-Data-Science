import streamlit as st
import pickle
import joblib

st.title('Churn Prediction - Gradient Boosting')

with open('churn_prediction_gradient_boosting.pkl', mode='rb') as f:
    model = pickle.load(f)

encoders = joblib.load('label_encoders.pkl')


# get features as input
credit_score = st.number_input('Enter Credit Score', value=100)

geography_options = ['France', 'Germany', 'Spain']
selected_geo_option = st.selectbox('Select', geography_options, key='geography')
geography = encoders['Geography'].transform([selected_geo_option])[0]


gender_options = ['Male', 'Female']
selected_gender_option = st.selectbox('Select', gender_options, key='gender')
gender = encoders['Gender'].transform([selected_gender_option])[0]

age = st.number_input('Enter Age', value=24)

tenure = st.number_input('Enter Tenure', value=1)

balance = st.number_input('Enter Balance', value=100000)

num_of_products = st.number_input('Enter No. of products', value=4)

options = [1, 0]
hasCard = st.selectbox('has Card', options, key='card')

is_active = st.selectbox('is Active', options, key='active')

estimated_salary = st.number_input('Enter Estimated Salary', value=70000)

credit_utilize = balance/credit_score

interact_score = num_of_products + hasCard + is_active

Balance_to_salary = balance/estimated_salary


# Button to get prediction from the model
predict = st.button('Predict')

if predict:
    # get predictions from model
    prediction = model.predict([[credit_score, geography, gender, age, tenure, balance, num_of_products, hasCard, is_active, estimated_salary, credit_utilize, interact_score, Balance_to_salary]])
    print(prediction)

    # display prediction from the model
    st.success(f"Performance Index: {prediction[0]}")