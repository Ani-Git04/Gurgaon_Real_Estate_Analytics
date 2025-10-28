import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import requests


st.set_page_config(page_title="Price Predictor")
st.title("Price Predictor")

# -------------------------------
# Relative paths to your models
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # pages/.. = project root
df_path = os.path.join(BASE_DIR, "Models", "df.pkl")
pipeline_path = os.path.join(BASE_DIR, "Models", "pipeline.pkl")

# -------------------------------
# Google Drive File ID
DRIVE_FILE_ID = "1OHNfvc8cl6fERp9u7xv6f7nUuChUJt5s"  # Google Drive file ID

# Function to download model from Google Drive
def download_from_drive(file_id, save_path):
    download_url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(download_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        st.success(f"Model downloaded successfully to {save_path}")
    else:
        st.error("Failed to download the model from Google Drive.")
        return None

# -------------------------------
# Check if model file exists, if not download it
if not os.path.exists(pipeline_path):
    st.info("Downloading pipeline model from Google Drive…")
    download_from_drive(DRIVE_FILE_ID, pipeline_path)

# -------------------------------
# Load df.pkl
with open(df_path, "rb") as file:
    df = pickle.load(file)

# -------------------------------
# Load pipeline.pkl
with open(pipeline_path, "rb") as file:
    pipeline = pickle.load(file)

#st.dataframe(df)

st.header("Enter Your Input")

# property_type
property_type = st.selectbox('Property Type', ['flat','house'])

# sector
sector = st.selectbox('Sector',sorted(df['sector'].unique().tolist()))

# Bedroom
bedrooms = float(st.selectbox('Number of BedRoom',sorted(df['bedRoom'].unique().tolist())))

bathrooms = float(st.selectbox('Number of BathRooms',sorted(df['bathroom'].unique().tolist())))

balcony = st.selectbox('Balconies',sorted(df['balcony'].unique().tolist()))

property_age = st.selectbox('Property Age',sorted(df['agePossession'].unique().tolist()))

built_up_area = float(st.number_input('Built Up Area'))

servent_room = float(st.selectbox('Servent Room',[0.0,1.0]))

store_room = float(st.selectbox('Store Room',[0.0,1.0]))

furnishing_type = st.selectbox('Furnishing Type',sorted(df['furnishing_type'].unique().tolist()))

luxury_category = st.selectbox('Luxury Category',sorted(df['luxury_category'].unique().tolist()))

floor_category = st.selectbox('Floor Category',sorted(df['floor_category'].unique().tolist()))

if st.button('Predict'):
    # form a dataframe
    data = [[property_type, sector, bedrooms, bathrooms, balcony, property_age, built_up_area, servent_room, store_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'servant room', 'store room',
               'furnishing_type', 'luxury_category', 'floor_category']

    # Convert to DataFrame
    one_df = pd.DataFrame(data, columns=columns)

    # predict
    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = base_price - 0.22
    high = base_price + 0.22

    st.text("The price of the property is between {} Cr and {} Cr".format(round(low,2),round(high,2)))



