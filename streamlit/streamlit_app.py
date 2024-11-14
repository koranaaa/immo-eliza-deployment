import streamlit as st
import requests

st.title("Real Estate Price Prediction")

# Input fields for property data
number_of_bedrooms = st.number_input("Number of Bedrooms", min_value=0)
living_area_m2 = st.number_input("Living Area (m²)", min_value=0)
equipped_kitchen = st.selectbox("Equipped Kitchen", ["Yes", "No"])
furnished = st.selectbox("Furnished", ["Yes", "No"])
swimming_pool = st.selectbox("Swimming Pool", ["Yes", "No"])
building_condition = st.selectbox("Building Condition", ["As new", "Good", "To be done up", "To restore", "To renovate"])
region = st.selectbox("Region", ["Flanders", "Wallonia", "Brussels"])
property_type = st.selectbox("Type of Property", ["apartment", "house"])

# Convert selections to expected format
data = {
    "Number of bedrooms": number_of_bedrooms,  # Change key to match FastAPI expectation
    "Living area m²": living_area_m2,         # Change key to match FastAPI expectation
    "Equipped kitchen": 1 if equipped_kitchen == "Yes" else 0,
    "Furnished": 1 if furnished == "Yes" else 0,
    "Swimming pool": 1 if swimming_pool == "Yes" else 0,
    "Building condition": building_condition,
    "Region": region,
    "Property type": property_type
}

# Predict button
if st.button("Get Prediction"):
    try:
        # Send request to API
        response = requests.post("http://127.0.0.1:8000/predict", json=data)  
        if response.status_code == 200:
            prediction = response.json().get("prediction", "Error in prediction")
            st.write(f"Predicted Price: {prediction}")
        else:
            st.write("Error in retrieving prediction:", response.json().get("detail"))
    except requests.exceptions.RequestException as e:
        st.write("Connection error with API:", e)
