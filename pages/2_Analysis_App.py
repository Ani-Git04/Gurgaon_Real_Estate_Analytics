import pickle

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st
from wordcloud import WordCloud

st.set_page_config(page_title="Plotting Demo")

st.title("Analytics")

new_df = pd.read_csv("Dataset/data_viz1.csv")
# st.dataframe(new_df)

feature_text = pickle.load(open('Dataset/feature_text.pkl','rb'))


group_df = new_df.groupby(by = 'sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200, height=700,
                        hover_name=group_df.index)
st.plotly_chart(fig, use_container_width=True)

st.header("Feature WordCloud")

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords={'s'},  # Customize as needed
    min_font_size=10
).generate(feature_text)

# Create a new figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")  # Turn off axis
plt.tight_layout(pad=0)

# Display in Streamlit
st.pyplot(fig)


st.header('Area vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom")
    st.plotly_chart(fig1, use_container_width=True)


st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'Overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'Overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)


st.header('Side-by-Side BHK Price Comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4 ], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)


st.header('Side-by-Side Price Distribution: House vs Flat')

fig4, ax = plt.subplots(figsize=(10, 6))

# KDE plots only (no histogram)
sns.kdeplot(data=new_df[new_df['property_type'] == 'house']['price'],label='House',fill=True,ax=ax)
sns.kdeplot(data=new_df[new_df['property_type'] == 'flat']['price'],label='Flat',fill=True,ax=ax)

ax.set_title('KDE Plot of Prices for House vs Flat')
ax.set_xlabel('Price')
ax.set_ylabel('Density')
ax.legend()

# Display in Streamlit
st.pyplot(fig4)






