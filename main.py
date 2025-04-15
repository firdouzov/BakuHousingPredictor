import pickle
import streamlit as st
from streamlit_folium import st_folium
import folium
import numpy as np

knn_model = pickle.load(open('knn_model.sav', 'rb'))
st.title('Housing Predictor of new buildings')
area=st.number_input('Area: ', min_value=35, max_value=1500, value=35, step=1)
rooms=st.number_input('Rooms: ', min_value=1, max_value=15, value=1, step=1)
bill = st.radio(
    "Has Bill? :",
    ["Yes", "No"])
repair = st.radio(
    "Is repaired? :",
    ["Yes", "No"])

bill_value = 1 if bill == "Yes" else 0
repair_value = 1 if repair == "Yes" else 0
curfloor=st.number_input('Current floor: ', min_value=1, max_value=500, value=1, step=1)
maxfloor=st.number_input('Max floor: ', min_value=1, max_value=500, value=1, step=1)

def get_pos(lat, lng):
    return lat, lng


latitude = 40.453703
longitude = 49.922476

# Create the map centered at the provided coordinates with zoom level 9
m = folium.Map(location=[latitude, longitude], zoom_start=9)

m.add_child(folium.LatLngPopup())

map = st_folium(m, height=350, width=700)

def predict():
    row=np.array([[area,rooms,bill_value,repair_value,curfloor,maxfloor,latitude,longitude]])
    answer=knn_model.predict(row)
    st.write(f'Predicted price is {answer[0]}')

data = None
if map.get("last_clicked"):
    data = get_pos(map["last_clicked"]["lat"], map["last_clicked"]["lng"])
    latitude=map["last_clicked"]["lat"]
    longitude=map["last_clicked"]["lng"]
    st.button('Predict',on_click=predict)
