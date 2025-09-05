# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import folium
from streamlit_folium import st_folium

# -------------------------
# Load Data
# -------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("airbnbst.csv")   
    return df

df = load_data()

st.title("🏡 Airbnb Analysis Dashboard")

# -------------------------
# Sidebar Filters
# -------------------------
st.sidebar.header("Filters")

country = st.sidebar.selectbox("Select Country", df["Country"].dropna().unique())
property_type = st.sidebar.multiselect("Property Type", df["Property_type"].dropna().unique())
room_type = st.sidebar.multiselect("Room Type", df["Room_type"].dropna().unique())

filtered_df = df[df["Country"] == country]
if property_type:
    filtered_df = filtered_df[filtered_df["Property_type"].isin(property_type)]
if room_type:
    filtered_df = filtered_df[filtered_df["Room_type"].isin(room_type)]

# -------------------------
# Geospatial Map
# -------------------------
st.subheader("🌍 Geospatial Distribution of Listings")

map_df = filtered_df.dropna(subset=["Latitude", "Longitude"])

if not map_df.empty:
    m = folium.Map(
        location=[map_df["Latitude"].mean(), map_df["Longitude"].mean()],
        zoom_start=11
    )
    for _, row in map_df.iterrows():
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=3,
            popup=f"{row['Name']} - ${row['Price']}",
            color="blue",
            fill=True,
            fill_opacity=0.6,
        ).add_to(m)

    st_folium(m, width=700, height=500)
else:
    st.warning("⚠️ No valid listings available for the selected filters.")

# -------------------------
# Price Analysis
# -------------------------
st.subheader("💲 Price Analysis")

st.markdown("**Avg Price in each Room type**")
if not filtered_df.empty:
    avg_price_room = filtered_df.groupby("Room_type")["Price"].mean().reset_index()
    fig_room = px.bar(avg_price_room, x="Room_type", y="Price", 
                      color="Price", 
                      color_continuous_scale="Blues",
                      title="Avg Price in each Room type")
    st.plotly_chart(fig_room, use_container_width=True)
else:
    st.info("No data available for the selected filters.")

# -------------------------
# Availability Analysis
# -------------------------
st.subheader("📅 Availability by Season")

if not filtered_df.empty and "Availability_365" in filtered_df.columns:
    filtered_df["season"] = pd.cut(filtered_df["Availability_365"],
                                   bins=[0, 90, 180, 270, 365],
                                   labels=["Low", "Moderate", "High", "Full Year"])
    fig_avail = px.histogram(filtered_df, x="season", color="Room_type",
                             title="Seasonal Availability of Listings")
    st.plotly_chart(fig_avail, use_container_width=True)
else:
    st.info("No availability data for the selected filters.")

# -------------------------
# Location-Based Insights
# -------------------------
st.subheader("👨‍💼 Top 10 Hosts by Number of Listings")

if not filtered_df.empty:
    top_hosts = filtered_df["Host_name"].value_counts().head(10).reset_index()
    top_hosts.columns = ["Host_name","Listings"]

    fig_hosts = px.bar(
        top_hosts, 
        x="Host_name", 
        y="Listings", 
        title="Top 10 Hosts with Most Listings",
        color="Listings", 
        color_continuous_scale="Cividis"
    )
    st.plotly_chart(fig_hosts, use_container_width=True)
else:
    st.info("No host data available for the selected filters.")

# -------------------------
# Review Scores
# -------------------------
st.subheader("⭐ Review Scores Distribution")

if not filtered_df.empty and "Review_scores" in filtered_df.columns:
    fig_review = px.histogram(filtered_df, x="Review_scores", nbins=20, 
                              title="Distribution of Review Scores")
    st.plotly_chart(fig_review, use_container_width=True)
else:
    st.info("No review score data available for the selected filters.")
