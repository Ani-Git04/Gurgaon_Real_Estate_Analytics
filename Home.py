import streamlit as st

# Page config
st.set_page_config(page_title="Home", layout="wide")

# Main title
st.title("🏡 Welcome to Apartment Finder")

# Subtitle / intro
st.write(
    """
    This platform helps you:
    - 📊 **Analyze** apartment price trends  
    - 🤖 **Predict** apartment prices  
    - 🏢 **Recommend** the best options for you

    Use the sidebar to navigate to different sections of the app.
    """
)

# Optional: Add a nice banner image
st.image("https://images.unsplash.com/photo-1568605114967-8130f3a36994", use_column_width=True)

# Add three columns with feature highlights
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📈 Price Predictor")
    st.write("Predict the price of apartments based on features like area, location, and amenities.")

with col2:
    st.subheader("📊 Analysis Dashboard")
    st.write("Explore real-estate trends and insights through interactive visualizations.")

with col3:
    st.subheader("🏠 Recommend Apartment")
    st.write("Get personalized apartment recommendations based on your preferences.")

# Add a simple CTA button
if st.button("👉 Get Started"):
    st.sidebar.success("Select a page from the sidebar!")
