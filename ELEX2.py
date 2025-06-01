import streamlit as st
import pandas as pd
import pydeck as pdk

# Load data
df = pd.read_csv("Predicted_HIV_Cases_Each_Region.csv")

# Set page config
st.set_page_config(page_title="HIV Cases Prediction", layout="wide")

# Define region coordinates (sample approximate lat/lon for visualization)
region_coords = {
    "CAR": [16.4, 120.6],
    "1": [16.0, 120.3],
    "2": [17.0, 121.8],
    "3": [15.5, 120.8],
    "4A": [14.0, 121.3],
    "4B": [9.9, 118.7],
    "5": [13.0, 123.3],
    "6": [11.0, 122.5],
    "7": [10.3, 123.9],
    "8": [11.5, 125.0],
    "9": [7.8, 123.5],
    "10": [8.2, 124.2],
    "11": [7.1, 125.6],
    "12": [6.9, 124.9],
    "NCR": [14.6, 121.0]
}

# Add coordinates to dataframe
df["lat"] = df["Region"].map(lambda x: region_coords.get(x, [None, None])[0])
df["lon"] = df["Region"].map(lambda x: region_coords.get(x, [None, None])[1])

# Sidebar region selector
st.sidebar.title("🗺️ Select a Region")
selected_region = st.sidebar.selectbox("Region", list(region_coords.keys()))

# Filter data
region_data = df[df["Region"] == selected_region]

# Main title
st.title("🧪 HIV Cases Prediction Dashboard")

# Display data
st.subheader(f"📊 Predicted HIV Cases for Region {selected_region}")
st.write(region_data)
st.bar_chart(region_data[["Cases_2024", "Cases_2025", "Cases_2026"]].T)

# Interactive map
st.subheader("🗺️ Philippine Regions Overview")

layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    get_position='[lon, lat]',
    get_color='[200, 30, 0, 160]',
    get_radius=10000,
    pickable=True,
)

view_state = pdk.ViewState(
    latitude=12.8797,
    longitude=121.7740,
    zoom=5,
    pitch=0,
)

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    layers=[layer],
    initial_view_state=view_state,
    tooltip={"text": "{Region}"}
))
