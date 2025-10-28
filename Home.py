import streamlit as st
import os
import pickle
import gdown

# -------------------------------
# 🔧 Page Configuration
# -------------------------------
st.set_page_config(page_title="Home", layout="wide")

# -------------------------------
# ⚙️ Optional: Load ML Model (if needed)
# -------------------------------
MODEL_PATH = "pipeline.pkl"
DRIVE_FILE_ID = "https://drive.google.com/file/d/10bbMLeMF8HmdkQjzdrhwzXEANYoh0uh4/view?usp=sharing"  # Replace with actual ID if used

@st.cache_resource
def load_model():
    """Download and load the ML pipeline (only if needed)."""
    if not os.path.exists(MODEL_PATH):
        # Uncomment the next line once you have your model on Google Drive
        # gdown.download(f"https://drive.google.com/uc?export=download&id={DRIVE_FILE_ID}", MODEL_PATH)
        pass
    if os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        return model
    return None

# Optional: load model (comment out if not used on home page)
# model = load_model()

# -------------------------------
# 🏡 Main Page
# -------------------------------
st.title("🏡 Welcome to Apartment Finder")

st.write(
    """
    This platform helps you:
    - 📊 **Analyze** apartment price trends  
    - 🤖 **Predict** apartment prices  
    - 🏢 **Recommend** the best options for you  

    Use the sidebar to navigate to different sections of the app.
    """
)

# -------------------------------
# 🖼️ Banner Image
# -------------------------------
st.image(
    "https://images.unsplash.com/photo-1568605114967-8130f3a36994",
    use_container_width=True
)

# -------------------------------
# 💡 Feature Highlights
# -------------------------------
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

# -------------------------------
# 🚀 Call to Action
# -------------------------------
if st.button("👉 Get Started"):
    st.sidebar.success("Select a page from the sidebar!")

# -------------------------------
# 📘 Footer (optional)
# -------------------------------
st.markdown(
    """
    <hr>
    <center>
    Built with ❤️ using Streamlit
    </center>
    """,
    unsafe_allow_html=True
)
