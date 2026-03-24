import streamlit as st
import numpy as np
import pickle

# -------------------------------
# Load model and columns
# -------------------------------
model = pickle.load(open("bangalore_model.pkl", "rb"))
columns = pickle.load(open("model_columns.pkl", "rb"))

# -------------------------------
# Extract locations for dropdown
# -------------------------------
locations = [col.replace("location_", "") for col in columns if col.startswith("location_")]
locations = sorted(locations)

# -------------------------------
# UI Title
# -------------------------------
st.title("🏠 Bangalore House Price Predictor")

# -------------------------------
# User Inputs
# -------------------------------
location = st.selectbox("Select Location", locations)
sqft = st.number_input("Total Sqft", min_value=300, value=1000)
bath = st.number_input("Bathrooms", min_value=1, value=2)
bhk = st.number_input("BHK", min_value=1, value=2)

# -------------------------------
# Prediction Button
# -------------------------------
if st.button("Predict Price"):
    
    # Create input array
    x = np.zeros(len(columns))
    
    # Fill numerical values
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    # Handle location encoding
    loc_col = "location_" + location
    if loc_col in columns:
        x[columns.index(loc_col)] = 1

    # Predict price
    price = model.predict([x])[0]

    # Show result
    st.success(f"Estimated Price: ₹ {price:.2f} Lakhs")