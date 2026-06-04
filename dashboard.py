import streamlit as st
import requests
import plotly.express as pe
import pandas as pd

st.title("Business Listings Dashboard")
st.subheader("Lucknow Restaurants Data")

# Category wise chart
cat_data = requests.get("http://127.0.0.1:8000/category-count").json()
cat_df = pd.DataFrame(cat_data)
st.subheader("Category Wise Count")
fig1 = pe.bar(cat_df, x="category", y="count", color="category")
st.plotly_chart(fig1)

# Source wise chart
src_data = requests.get("http://127.0.0.1:8000/source-count").json()
src_df = pd.DataFrame(src_data)
st.subheader("Source Wise Count")
fig2 = pe.pie(src_df, names="source", values="count")
st.plotly_chart(fig2)

# City wise chart
city_data = requests.get("http://127.0.0.1:8000/city-count").json()
city_df = pd.DataFrame(city_data)
st.subheader("City Wise Count")
fig3 = pe.bar(city_df, x="city", y="count", color="city")
st.plotly_chart(fig3)

# Show raw data
st.subheader("All Listings")
all_data = requests.get("http://127.0.0.1:8000/listings").json()
all_df = pd.DataFrame(all_data)
st.dataframe(all_df)