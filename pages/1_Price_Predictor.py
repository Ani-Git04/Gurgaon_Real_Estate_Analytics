import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title="Price Predictor")
st.title("Price Predictor")

with open("/Users/anilsaini/PycharmProjects/PythonProject/real-estate/Models/df.pkl", "rb") as file:
    df = pickle.load(file)

with open("/Users/anilsaini/PycharmProjects/PythonProject/real-estate/Models/pipeline.pkl", "rb") as file:
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



