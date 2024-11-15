# 🏠 Immo Eliza ML - Real Estate Price Prediction

## 📄 Project Description
This project involves deploying a machine learning model to predict real estate prices in Belgium. Built using FastAPI, the API provides developers access to model predictions and includes a Streamlit application for non-technical users such as managers or clients.


## 📂 Repository Structure
IMMO-ELIZA-DEPLOYMENT/
```
├── __pycache__/
├── .venv/                          
├── api/                
│   ├── app.py                      
│   ├── Dockerfile                  
│   └── predict.py                  
├── models/                         
│   ├── final_xgb_model_advanced.joblib   
│   ├── label_encoders.joblib             
│   ├── required_columns.joblib           
│   └── scaler.joblib                     
├── streamlit/                      
│   └── streamlit_app.py            
├── TEST/                           
│   └── __init__.py                
├── .gitignore                      
├── README.md                       
└── requirements.txt                
```


📂 Explanation of Structure
1. pycache/ - Compiled cache files for Python.
2. .venv/ - Virtual environment containing dependencies.
3. api/ - Folder with FastAPI files:
- app.py: The main FastAPI app.
- Dockerfile: For containerizing the FastAPI app.
- predict.py: Contains prediction logic and helper functions.
4. models/ - Folder for machine learning artifacts:
- final_xgb_model_advanced.joblib: Trained model file.
- label_encoders.joblib: Encoded labels for categorical variables.
- required_columns.joblib: Expected columns for model input.
- scaler.joblib: Scaler for standardizing input features.
5. streamlit/ - Folder with Streamlit app file:
- streamlit_app.py: Streamlit app for non-technical users.
6. TEST/ - Folder for test files, if applicable.
7. .gitignore - Excludes files/folders from version control.
8. README.md - Documentation file.
9. requirements.txt - Lists all project dependencies.


🛠️ Installation
Clone the repository:
```
git clone https://github.com/koranaaa/immo-eliza-deployment.git
cd immo-eliza-deployment
```
Set up a virtual environment:

```
python -m venv .venv
source .venv/bin/activate  # For MacOS/Linux
.venv\Scripts\activate     # For Windows
```

Install dependencies:

```
pip install -r requirements.txt
```

✔️ Usage
Run FastAPI:
To start the FastAPI server, navigate to the api directory:

```
cd api
uvicorn app:app --host 0.0.0.0 --port 8000
```
Access the API documentation at: http://127.0.0.1:8000/docs

Run the Streamlit Application:
To launch the Streamlit app:

```
streamlit run streamlit/streamlit_app.py
```

🧠 Models and Metrics
- XGBoost (R²: ~0.94, MAPE: ~7%)

The selected model is evaluated with metrics such as:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score


⏱️ Project Timeline
The project was completed in five stages:

Model preparation and initial API setup.
Docker configuration for FastAPI.
Streamlit application creation.
FastAPI deployment using Render.com.
Testing and performance optimization.


🔄 Planned Updates
Further model improvements for higher accuracy.
Addition of database integration for scalability.
Enhancements to the Streamlit app for a better user experience.

📌 Personal Note
This project was developed as part of the BeCode training program and highlights the practical application of data science and machine learning deployment.

📞 Contact Information
Lead Developer: [Korostelova Anastasiia]
LinkedIn: Anastasiia Korostelova
Email: nastiashosti@gmail.com

P.S. My READ.ME file was created as an ideal model of my project, but unfortunately I did not manage to implement everything.