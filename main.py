import pickle
import streamlit as st
from streamlit_folium import st_folium
import folium
import numpy as np

# Load the KNN model
knn_model = pickle.load(open('knn_model_binaAz.sav', 'rb'))
rf_model_old = pickle.load(open('rf_model_old.sav', 'rb'))
st.title('Housing Predictor of new buildings')

category = st.radio("Category :", ["New Building", "Old Building"])

# Inputs for prediction
area = st.number_input('Area: ', min_value=35, max_value=1500, value=35, step=1)
rooms = st.number_input('Rooms: ', min_value=1, max_value=15, value=1, step=1)
bill = st.radio("Has Bill? :", ["Yes", "No"])
repair = st.radio("Is repaired? :", ["Yes", "No"])
bill_value = 1 if bill == "Yes" else 0
repair_value = 1 if repair == "Yes" else 0
curfloor = st.number_input('Current floor: ', min_value=1, max_value=500, value=1, step=1)
maxfloor = st.number_input('Max floor: ', min_value=1, max_value=500, value=1, step=1)

# Latitude and Longitude
latitude = 40.453703
longitude = 49.922476

# Function to get position from map click
def get_pos(lat, lng):
    return lat, lng

# Create map
m = folium.Map(location=[latitude, longitude], zoom_start=10)
m.add_child(folium.LatLngPopup())

# Streamlit map
map = st_folium(m, height=350, width=700)

# Prediction function
def predict(category):
    row = np.array([[area, rooms, bill_value, repair_value, curfloor, maxfloor, latitude, longitude]])
    if category=="New Building":
        answer = knn_model.predict(row)
    elif category=='Old Building':
        answer = rf_model_old.predict(row)
    st.write(f'Predicted price is {answer[0]}')

# Store map click position
if map.get("last_clicked"):
    latitude = map["last_clicked"]["lat"]
    longitude = map["last_clicked"]["lng"]

# Predict button and session state
if 'predicted' not in st.session_state:
    st.session_state.predicted = False

if st.button('Predict'):
    st.session_state.predicted = True
    predict(category)  # Trigger the prediction function
