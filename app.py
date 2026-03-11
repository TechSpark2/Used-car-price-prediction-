import streamlit as st
import numpy as np
import joblib

model = joblib.load("car_price_model.pkl")

st.title("Used Car Price Prediction")

year = st.number_input("Manufacturing Year",1990,2026)
km_driven = st.number_input("Kilometers Driven",0,500000)

fuel = st.selectbox("Fuel Type",["CNG","Diesel","Petrol","LPG","Electric"])
seller = st.selectbox("Seller Type",["Dealer","Individual"])
transmission = st.selectbox("Transmission",["Manual","Automatic"])
owner = st.selectbox("Owner Type",
["First Owner","Second Owner","Third Owner","Fourth Owner","Test Drive Car"])

car_age = 2026 - year

fuel_map = {"CNG":0,"Diesel":1,"Petrol":2,"LPG":3,"Electric":4}
seller_map = {"Dealer":0,"Individual":1}
transmission_map = {"Automatic":0,"Manual":1}
owner_map = {"First Owner":0,"Second Owner":1,"Third Owner":2,"Fourth Owner":3,"Test Drive Car":4}

fuel = fuel_map[fuel]
seller = seller_map[seller]
transmission = transmission_map[transmission]
owner = owner_map[owner]

if st.button("Predict Price"):

    data = np.array([[km_driven,fuel,seller,transmission,owner,car_age]])

    prediction = model.predict(data)

    st.success(f"Estimated Car Price: ₹ {round(prediction[0],2)}")
