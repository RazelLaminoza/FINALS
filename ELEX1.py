import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("Predicted_HIV_Cases_2024_2026.csv")

# Set page config
st.set_page_config(page_title="HIV Cases Prediction", layout="wide")

# Define regions
regions = ["CAR", "1", "2", "3", "4A", "4B", "5", 
           "6", "7", "8", "9", "10", "11", "12", "NCR"]

# Title
st.title("🧪 HIV Cases Prediction Dashboard")

# UI: Create a grid of buttons
cols = st.columns(8)
for idx, region in enumerate(regions):
    if cols[idx % 8].button(region):
        st.subheader(f"📊 Predicted Data for Region {region}")
        region_data = df[df["Region"] == region]
        st.write(region_data)
        st.bar_chart(region_data[["Cases_2024", "Cases_2025", "Cases_2026"]].T)

