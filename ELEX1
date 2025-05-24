import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns  # For color palette

# 📂 File uploader
st.title("📊 3D Forecast of HIV Cases in the Philippines (2022–2026)")
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Define years and regions
    years = [2022, 2023, 2024, 2025, 2026]
    regions = df["Region"].values

    # Generate 3D data points
    X = np.tile(years, len(df))
    Y = np.repeat(np.arange(len(regions)), len(years))
    Z = df[["Cases_2022", "Cases_2023", "Cases_2024", "Cases_2025", "Cases_2026"]].values.flatten()

    # Generate colors
    palette = sns.color_palette("hsv", len(regions))
    colors = np.repeat(palette, len(years), axis=0)

    # Define bar widths
    dx = np.ones_like(X) * 0.4
    dy = np.ones_like(Y) * 0.4
    dz = Z

    # Create 3D bar chart
    fig = plt.figure(figsize=(16, 12))
    ax = fig.add_subplot(111, projection='3d')

    ax.bar3d(X, Y, np.zeros_like(Z), dx, dy, dz, color=colors, alpha=0.8)

    ax.set_xticks(years)
    ax.set_xticklabels(years, fontsize=12)
    ax.set_yticks(np.arange(len(regions)))
    ax.set_yticklabels(regions, fontsize=10)

    ax.set_xlabel("Year")
    ax.set_ylabel("Region")
    ax.set_zlabel("HIV Cases")
    ax.set_title("3D Forecast of HIV Cases in the Philippines (2022–2026)")

    ax.view_init(elev=30, azim=130)

    # 📊 Show plot in Streamlit
    st.pyplot(fig)
else:
    st.info("👆 Please upload a CSV file to generate the 3D chart.")
