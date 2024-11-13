import streamlit as st
import requests

st.title("Прогноз ціни нерухомості")

# Поля для введення даних
living_area = st.number_input("Living Area (м²)", min_value=0)
property_type = st.selectbox("Type of Property", ["apartment", "house", "land", "office", "garage"])
bedrooms = st.number_input("Number of Bedrooms", min_value=0)
postal_code = st.number_input("Postal Code", min_value=1000, max_value=9999)
surface_of_good = st.number_input("Surface of Good (optional)", min_value=0)
garden = st.checkbox("Garden")
garden_area = st.number_input("Garden Area (optional)", min_value=0)
swimming_pool = st.checkbox("Swimming Pool")
furnished = st.checkbox("Furnished")
openfire = st.checkbox("Openfire")
terrace = st.checkbox("Terrace")
number_of_facades = st.number_input("Number of Facades (optional)", min_value=0)
construction_year = st.number_input("Construction Year (optional)", min_value=1800, max_value=2024)
building_condition = st.selectbox("Building Condition", ["to be done up", "to restore", "to renovate", "good", "as new"])
kitchen = st.selectbox("Kitchen", ["not installed", "usa not installed", "installed"])

# Кнопка для прогнозу
if st.button("Отримати прогноз"):
    # Формуємо дані для запиту
    data = {
        "Living area m²": living_area,
        "Property type": property_type,
        "Number of bedrooms": bedrooms,
        "Postal code": postal_code,
        "Surface of good": surface_of_good,
        "Garden": garden,
        "Garden area": garden_area,
        "Swimming pool": swimming_pool,
        "Furnished": furnished,
        "Openfire": openfire,
        "Terrace": terrace,
        "Number of facades": number_of_facades,
        "Construction year": construction_year,
        "Building condition": building_condition,
        "Kitchen": kitchen
    }

    # Надсилаємо запит до API
    try:
        response = requests.post("http://localhost:8000/predict", json=data)  # Заміни URL на свій, якщо API розгорнутий в іншому місці
        if response.status_code == 200:
            prediction = response.json().get("prediction", "Помилка в прогнозі")
            st.write(f"Прогнозована ціна: {prediction}")
        else:
            st.write("Помилка в отриманні прогнозу:", response.json().get("detail"))
    except requests.exceptions.RequestException as e:
        st.write("Помилка з'єднання з API:", e)
