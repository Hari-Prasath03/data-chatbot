import streamlit as st
import pandas as pd

st.set_page_config(page_title="CSV Statistical Summary", layout="wide")

st.title("📊 CSV Statistical Summary Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Dataset Shape")
    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    st.subheader("🧮 Statistical Summary (Numeric Columns)")
    st.dataframe(df.describe())

    st.subheader("🔎 Missing Values")
    missing = df.isnull().sum()
    st.dataframe(missing[missing > 0])

    st.subheader("📈 Correlation Matrix")
    numeric_df = df.select_dtypes(include="number")
    if not numeric_df.empty:
        st.dataframe(numeric_df.corr())
    else:
        st.write("No numeric columns available for correlation.")
