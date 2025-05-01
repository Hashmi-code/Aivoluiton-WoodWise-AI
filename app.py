import streamlit as st
import numpy as np
import plotly.graph_objects as go
from openai import AzureOpenAI
from datetime import datetime

# --- Setup ---
st.set_page_config(page_title="WoodWise AI", layout="wide")

# Azure OpenAI setup
client = AzureOpenAI(
    api_key=st.secrets["AZURE_API_KEY"],
    api_version="2024-12-01-preview",
    azure_endpoint="https://ai-jadewright8967ai215099010767.openai.azure.com/"
)
deployment = "gpt-4.1"

# Load data
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

# --- Header ---
st.markdown("""
### WoodWise AI: Forecast. Adjust. Act.
##### Client: MapleBuild Ltd. | Forecast Model: NeuralNet v1.0 | Last Updated: {date}
""".format(date=datetime.today().strftime('%Y-%m-%d')))

# --- Tabs ---
tabs = st.tabs(["Overview", "Adjust Forecast", "AI Report", "Scenario Simulation"])

# --- Tab 1: Overview ---
with tabs[0]:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### Avg Forecast (Units/Week)")
        st.markdown(f"**{int(np.mean(forecast_values))}**")
    with col2:
        st.markdown("#### Model Confidence Level")
        st.markdown(f"**{confidence}**")
        with st.expander("What does this mean?"):
            st.markdown("""
            **High** Confidence: Model predictions strongly align with past data and current conditions.
            
            **Low** Confidence: Uncertainty is higher due to limited data, volatility, or conflicting indicators.
            """)
    with col3:
        st.markdown("#### Inventory Plan")
        st.markdown(inventory_strategy)

    # Graph
    st.markdown("""
    ### 📊 Actual vs. Predicted Sales
    """)
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=y_true, name="Actual Sales", mode='lines+markers'))
    fig.add_trace(go.Scatter(y=y_pred, name="Predicted Sales", mode='lines+markers'))
    fig.update_layout(xaxis_title="Weeks", yaxis_title="Sales Units", height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Meet Your Agents 
    st.markdown("## 🤝 Meet Your Agents")
    st.markdown("""
    - **📈 Forecasting Agent**: Generates weekly sales forecasts using historical trends and AI modeling.  
    - **✍️ Adjustment Agent (HITL)**: Allows users to modify forecasts and inventory plans manually.  
    - **🌐 Scenario Agent**: Simulates external factors like tariffs, weather, and construction activity.  
    - **📄 Reporting Agent**: Compiles final insights and recommendations into business-friendly reports.  
    """)

# --- Tab 2: Adjust Forecast ---
with tabs[1]:
    st.markdown("### 📜 Forecasted Sales (Next 4 Weeks)")
    st.markdown("Your forecasted sales for the next 4 weeks based on current industry conditions. Adjust as needed.")
    new_forecast = []
    for i, val in enumerate(forecast_values):
        new_val = st.number_input(f"Week {i+1}", value=val, step=10, key=f"week_{i+1}")
        new_forecast.append(int(new_val))

    st.markdown("### 📦 Adjust Inventory Strategy")
    user_strategy = st.text_area("Inventory Strategy. Adjust based upon forecasted sales results.", value=inventory_strategy)

# --- Tab 3: AI Report ---
with tabs[2]:
    st.markdown("## 🤖 Final Forecast Report Generator")
    if st.button("Generate Final Forecast Report"):
        adjusted_message = f"""
Using a neural network trained on multiple industry factors, generate a 4-week lumber sales forecast report for MapleBuild Ltd. Include:
- Bullet points for demand expectations
- Inventory strategy summary (based on: {user_strategy})
- Key risks to monitor
- Why the forecast is reliable (confidence: {confidence})

Use this forecasted sales: {new_forecast}
"""
        with st.spinner("Generating..."):
            response = client.chat.completions.create(
                model=deployment,
                messages=[
                    {"role": "system", "content": "You are a helpful forecasting assistant for a manufacturing company."},
                    {"role": "user", "content": adjusted_message},
                ]
            )
            final_report = response.choices[0].message.content
            final_report = final_report.replace("Let me know if you need this in a specific format or with more detail!", "")
            st.success(final_report.strip())

# --- Tab 4: Scenario Simulation Agent ---
with tabs[3]:
    st.markdown("## Scenario Simulation Agent")

    scenario_map = {
        "Tariff Change": -1,
        "Construction Activity": 1,
        "Industrial Output": 1,
        "Weather Disruption": -0.5,
    }

    driver = st.selectbox("Choose a driver to simulate", list(scenario_map.keys()))
    impact_percent = st.slider("Adjust percentage (+/-)", -50, 50, 0)

    if st.button("Recalculate Forecast"):
        weight = scenario_map[driver]
        new_vals = [int(x * (1 + (impact_percent/100) * weight)) for x in forecast_values]
        st.success(f"New adjusted forecast based on {impact_percent}% change in {driver}: {new_vals}")
