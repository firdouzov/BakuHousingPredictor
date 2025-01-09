Housing Price Predictor with Deployment

This project aims to predict housing prices in Baku, Azerbaijan, using machine learning models. It provides a user-friendly web application for users to estimate property prices based on features such as area, number of rooms, bill of sale availability, repair status, and location.

Overview

The housing market dataset was collected over a one-year period, focusing on properties in Baku. The dataset was used to train machine learning models to predict prices for two categories:

New Buildings

Old Buildings

The prediction is based on features such as:

Area (in square meters)

Number of rooms

Bill of sale availability (Yes/No)

Repair status (Yes/No)

Current floor

Maximum floors in the building

Geolocation (latitude and longitude)

The project includes the following components:

Data preprocessing and model training.

Deployment of the prediction system using Streamlit.

Interactive map integration for location selection.

Features

1. Interactive Web Application

Users can input property details like area, number of rooms, and repair status.

A dynamic map allows users to select the property’s location by clicking on the map.

2. Machine Learning Models

K-Nearest Neighbors (KNN) for predicting prices of new buildings.

Random Forest (RF) for predicting prices of old buildings.

3. Real-Time Predictions

The app instantly predicts the property price based on the provided inputs.

Installation

To run the project locally, follow these steps:

Clone the repository:

git clone https://github.com/your-username/housing-price-predictor.git
cd housing-price-predictor

Install dependencies:
Make sure you have Python 3.8 or later installed.

pip install -r requirements.txt

Run the application:

streamlit run app.py

Access the app:
Open your web browser and navigate to http://localhost:8501.

File Structure

|-- app.py                   # Main Streamlit application
|-- knn_model_binaAz.sav     # Trained KNN model for new buildings
|-- rf_model_old.sav         # Trained Random Forest model for old buildings
|-- requirements.txt         # Required Python libraries
|-- README.md                # Project documentation

Usage

Input Features

Category: Select either "New Building" or "Old Building."

Area: Enter the area in square meters (min: 35, max: 1500).

Rooms: Specify the number of rooms (min: 1, max: 15).

Bill of Sale: Indicate whether the property has a bill (Yes/No).

Repair Status: Indicate whether the property is repaired (Yes/No).

Current Floor: Specify the current floor (min: 1).

Max Floor: Specify the maximum number of floors (min: 1).

Interactive Map

Click on the map to select the latitude and longitude of the property.

Prediction

Click the "Predict" button to estimate the property price. The predicted price will be displayed below the button.

Deployment

This project is deployed using Streamlit, a Python framework for creating web apps. You can deploy it to platforms like Streamlit Cloud, Heroku, or AWS by following their respective deployment guides.

Future Enhancements

Adding more features like neighborhood rating, proximity to amenities, etc.

Expanding the dataset to include properties outside Baku.

Improving the user interface for better usability.

Incorporating additional machine learning models for better accuracy.

Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License

This project is licensed under the MIT License.

Acknowledgments

Special thanks to the contributors who helped in data collection and model training.

Libraries and tools used: Streamlit, Folium, Scikit-learn, NumPy, Pickle.

Screenshots

1. User Input Form



2. Interactive Map



3. Prediction Result



