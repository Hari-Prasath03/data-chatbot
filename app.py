import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="AI Data Assistant V2", layout="wide")
st.title("🤖 AI Data Assistant (Gemini Powered)")

# -------------------------
# Gemini Configuration
# -------------------------
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.0-pro")

# -------------------------
# File Upload
# -------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Basic Statistics")
    st.dataframe(df.describe())

    st.subheader("🤖 Ask AI about your data")

    question = st.text_input("Type your question:")

    if question:

        prompt = f"""
        You are a professional data analyst.
        The dataframe is named df.
        The columns are: {list(df.columns)}.
        Convert the user's question into a single valid Pandas expression.
        Only return Python code.
        Do NOT explain anything.
        Do NOT use print().
        Question: {question}
        """

        response = model.generate_content(prompt)
        pandas_code = response.text.strip()

        st.code(pandas_code, language="python")

        try:
            result = eval(pandas_code)
            st.success("✅ Result:")
            st.write(result)
        except Exception as e:
            st.error("⚠️ Error executing generated code.")
