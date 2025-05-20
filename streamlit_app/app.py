import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data, get_available_countries

st.set_page_config(page_title="Solar Dashboard", layout="wide")

st.title("☀️ Solar Energy Dashboard")
st.markdown("Explore and compare solar metrics across African countries")

# Sidebar
country = st.sidebar.selectbox("Select Country", get_available_countries())
df = load_data(country)

if df is not None:
    metric = st.sidebar.selectbox("Metric to Visualize", ['GHI', 'DNI', 'DHI', 'Tamb', 'ModA', 'ModB'])

    st.subheader(f"{country.title()} - {metric} over Time")
    fig = px.line(df, x='Timestamp', y=metric, title=f'{metric} Trend')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Summary Statistics")
    st.dataframe(df[[metric]].describe())

    st.subheader("Correlation Heatmap")
    corr = df[['GHI', 'DNI', 'DHI', 'Tamb', 'ModA', 'ModB']].corr()
    st.dataframe(corr.round(2))

    st.subheader("Scatter Plot")
    x_axis = st.selectbox("X-axis", df.columns[1:-1])
    y_axis = st.selectbox("Y-axis", df.columns[1:-1])
    fig2 = px.scatter(df, x=x_axis, y=y_axis, color=metric)
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("Data not found.")