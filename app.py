import streamlit as st
import pandas as pd
from google import genai
import os

st.set_page_config(page_title="AI Data Assistant V2", layout="wide")
st.title("🤖 AI Data Assistant (Gemini Powered)")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📌 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("📊 Basic Statistics")
    st.dataframe(df.describe())

    question = st.text_input("Ask AI about your data:")

    if question:

        prompt = f"""
        You are a professional data analyst.
        The dataframe is named df.
        The columns are: {list(df.columns)}.
        Convert the user's question into a single valid Pandas expression.
        Only return Python code only.
        Question: {question}
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt,
        )

        pandas_code = response.text.strip()

        st.code(pandas_code, language="python")

        try:
            result = eval(pandas_code)
            st.success("✅ Result:")
            st.write(result)
        except:
            st.error("⚠️ Error executing generated code.")
