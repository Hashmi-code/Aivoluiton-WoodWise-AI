import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from openai import AzureOpenAI

# Azure OpenAI setup
client = AzureOpenAI(
    api_key=st.secrets["AZURE_API_KEY"],
    api_version="2024-12-01-preview",
    azure_endpoint="https://ai-jadewright8967ai215099010767.openai.azure.com/"
)
deployment = "gpt-4.1"

# Streamlit page config
st.set_page_config(page_title="WoodWise AI: Forecast. Adjust. Act.", page_icon="🌲")
st.title("WoodWise AI: Forecast. Adjust. Act.")

try:
    # Load forecast data
    with open("forecast_summary.txt", "r") as f:
        forecast_summary = f.read()

    with open("forecasted_values.txt", "r") as f:
        forecast_values = [int(x.strip()) for x in f.read().split(",")]

    with open("confidence.txt", "r") as f:
        confidence = f.read().strip()

    with open("strategy.txt", "r") as f:
        inventory_strategy = f.read().strip()

    y_true = np.loadtxt("y_true.txt")
    y_pred = np.loadtxt("y_pred.txt")

    # --- Confidence Level Display ---
    st.subheader("Forecast Confidence Level")
    st.markdown(f"`{confidence}`")
    if confidence == "Low":
        st.warning("⚠️ Forecast confidence is LOW. Manual adjustment is recommended.")

    # --- Actual vs. Predicted Sales ---
    st.subheader("📈 Actual vs. Predicted Sales (Test Set)")
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(y_true, label="Actual Sales")
    ax.plot(y_pred, label="Predicted Sales")
    ax.set_xlabel("Sample")
    ax.set_ylabel("Sales Units")
    ax.set_title("Actual vs. Predicted Lumber Sales")
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    # --- Forecasted Sales (Editable) ---
    st.subheader("📊 Forecasted Sales (Next 4 Weeks)")
    st.caption("Your forecasted sales for the next 4 weeks based on current industry conditions. Adjust as needed.")
    new_forecast = []
    for i, val in enumerate(forecast_values):
        new_val = st.number_input(f"Week {i+1}", value=val, step=10)
        new_forecast.append(int(new_val))

    # --- Inventory Strategy (Editable) ---
    st.subheader("📦 Adjust Inventory Strategy")
    user_strategy = st.text_area("Inventory Strategy", value=inventory_strategy)

    # --- Final Report ---
    if st.button("🧠 Generate Final Forecast Report"):
        adjusted_message = f"""
Using a neural network trained on multiple industry factors, the adjusted forecasted lumber sales units for the next 4 weeks are: {new_forecast}.
The forecast confidence level is: {confidence}.
The inventory strategy is: {user_strategy}.

Please generate a business-friendly forecast report that:
- Summarizes demand expectations
- Mentions confidence and its implication
- Highlights risks or external factors
- Justifies the inventory strategy
"""
        with st.spinner("Generating forecast report..."):
            response = client.chat.completions.create(
                model=deployment,
                messages=[
                    {"role": "system", "content": "You are a helpful forecasting assistant for the lumber industry."},
                    {"role": "user", "content": adjusted_message},
                ]
            )
            st.success("✅ Report Generated!")
            st.write(response.choices[0].message.content)

except FileNotFoundError as e:
    st.error("❌ Missing one or more forecast files. Please upload all necessary .txt files from Colab.")
