import streamlit as st
import pandas as pd

st.title("📊 Data Chatbot")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(df.head())

    question = st.text_input("Ask a question about your data:")

    if question:
        question = question.lower()

        if "average" in question:
            column = question.split("average")[-1].strip()
            if column in df.columns:
                st.write(f"Average of {column}:", df[column].mean())
            else:
                st.write("Column not found.")

        elif "total" in question:
            column = question.split("total")[-1].strip()
            if column in df.columns:
                st.write(f"Total of {column}:", df[column].sum())
            else:
                st.write("Column not found.")

        elif "rows" in question:
            st.write("Number of rows:", len(df))

        else:
            st.write("Sorry, I can't understand that question yet.")
