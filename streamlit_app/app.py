import streamlit as st
import pandas as pd
import plotly.express as px
from utils.data_loader import load_data, get_available_countries

# Streamlit page configuration
st.set_page_config(page_title="Solar Dashboard", layout="wide")

# Page title
st.title("☀️ Solar Energy Dashboard")
st.markdown("Explore and compare solar metrics across African countries")

# Sidebar controls
country = st.sidebar.selectbox("Select Country", get_available_countries())
df = load_data(country)

# Main content
if df is not None:
    metric = st.sidebar.selectbox("Metric to Visualize", ['GHI', 'DNI', 'DHI', 'Tamb', 'ModA', 'ModB'])

    st.subheader(f"{country.title()} - {metric} over Time")
    fig = px.line(df, x='Timestamp', y=metric, title=f'{metric} Trend in {country.title()}')
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📊 Summary Statistics")
    st.dataframe(df[[metric]].describe().T)

    st.subheader("📈 Correlation Heatmap")
    corr = df[['GHI', 'DNI', 'DHI', 'Tamb', 'ModA', 'ModB']].corr()
    st.dataframe(corr.style.background_gradient(cmap='coolwarm').format("{:.2f}"))

    st.subheader("🔍 Scatter Plot Explorer")
    x_axis = st.selectbox("X-axis", df.columns[1:-1], index=0)
    y_axis = st.selectbox("Y-axis", df.columns[1:-1], index=1)
    fig2 = px.scatter(df, x=x_axis, y=y_axis, color=metric, title=f'{y_axis} vs {x_axis}')
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.warning("⚠️ Data not found for this country. Please ensure the cleaned CSV is available.")
