import streamlit as st
import requests

st.title("Real Estate Price Prediction")

# Input fields for property data
number_of_bedrooms = st.number_input("Number of Bedrooms", min_value=0)
living_area_m2 = st.number_input("Living Area (m²)", min_value=0)
equipped_kitchen = st.selectbox("Equipped Kitchen", ["Yes", "No"])
furnished = st.selectbox("Furnished", ["Yes", "No"])
swimming_pool = st.selectbox("Swimming Pool", ["Yes", "No"])
building_condition = st.selectbox("Building Condition", ["To be done up", "To restore", "To renovate", "Good", "As new"])
region = st.selectbox("Region", ["Flanders", "Wallonia", "Brussels"])
property_type = st.selectbox("Type of Property", ["apartment", "house"])

# Convert selections to expected format
data = {
    "Number_of_bedrooms": number_of_bedrooms,
    "Living_area_m2": living_area_m2,
    "Equipped_kitchen": 1 if equipped_kitchen == "Yes" else 0,
    "Furnished": 1 if furnished == "Yes" else 0,
    "Swimming_pool": 1 if swimming_pool == "Yes" else 0,
    "Building_condition": building_condition,
    "Region": region,
    "Property_type": property_type
}

# Predict button
if st.button("Get Prediction"):
    try:
        # Send request to API
        response = requests.post("http://localhost:8000/predict", json=data)  # Replace with your deployed API URL
        if response.status_code == 200:
            prediction = response.json().get("prediction", "Error in prediction")
            st.write(f"Predicted Price: {prediction}")
        else:
            st.write("Error in retrieving prediction:", response.json().get("detail"))
    except requests.exceptions.RequestException as e:
        st.write("Connection error with API:", e)

