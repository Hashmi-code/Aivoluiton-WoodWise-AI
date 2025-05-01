## **WoodWise AI Multi-Agent**
WELCOME TO WOODWISE AI AGENT 👋:
![images-WoodWise Ai Agent](6.jpeg)
## **Introduction**
This repository outlines the foundation of our artificial intelligence forecasting model tailored specifically
to the lumber and manufacturing industry. This system is composed of four agents: Forecasting, Adjustment (HITL), Scenario Simulation, and Reporting. They work together to help businesses make smarter, data-driven decisions while embracing responsible AI practices.

## **Problem Statement**
The lumber industry faces significant uncertainty due to fluctuating demand, seasonal trends, and supply chain disruptions. Traditional forecasting methods often fail to capture complex patterns in price movements and inventory levels, leading to:

1. Overstocking or Stockouts: Inefficient inventory levels increase holding costs or disrupt production schedules.

2. Missed Revenue Opportunities: Inaccurate price and demand forecasts can lead to lost sales or inability to capitalize on market upswings.

3. Manual Decision Bottlenecks: Supply chain managers rely on manual spreadsheet analysis, which is time-consuming and error-prone.

## **Solution**
The WoodWise Forecasting AI Agent leverages a multi-agent system built with Python and Azure OpenAI to forecast lumber demand, inventory requirements, and simulate economic scenarios, several weeks into the future. Key capabilities include:

Time-Series Forecasting: Uses historical sales and pricing data to train models like Random Forests and Gradient Boosting for accurate predictions.

Scenario Analysis: Simulates "what-if" scenarios (e.g., tariff changes, production disruptions) to assess impact on inventory and revenues.

Automated Reporting: Generates dynamic dashboards and natural-language summaries to keep stakeholders informed.

## **Features**
1. Confidence Level: Model confidence is surfaced to guide decision-makers on how reliable a prediction is.
             ![images-WoodWise Ai Agent](1.jpeg)
2. Time-Series Forecasting: Uses historical data to forecast weekly sales for 4 weeks.
             ![images-WoodWise Ai Agent](2.jpeg)
3. Scenario Testing: Users can simulate changes in key drivers and instantly visualize demand shifts.
             ![images-WoodWise Ai Agent](3.jpeg)
4. Human-in-the-Loop: Managers can manually adjust forecasts and inventory plans.
             ![images-WoodWise Ai Agent](4.jpeg)
5. Streamlit Dashboard: All agents are deployed in a single interactive UI.
             ![images-WoodWise Ai Agent](5.jpeg)
## **Responsible AI**
We prioritize transparency through: 
- Confidence Reporting: Each forecast includes a model confidence score (High or Low), derived from performance trends.
- Human Oversight: A HITL interface ensures users can override or adjust AI outputs.
- No Black Box Outputs: Key model explanations and assumptions are shared through an interactive UI.

## **Technologies Used**
- Python
- Streamlit
- Azure OpenAI (GPT-4.1)
- Plotly

## **Getting Started**
1. Clone the repository
2. Install dependencies with 'pip install -r requirements.txt'
3. Run the app using 'streamlit run app.py'
4. https://aivoluiton-woodwise-ai.streamlit.app/

## **Acknowledgements**
Built for the Microsoft AI Agents Hackathon 2025.

![images-WoodWise Ai Agent](7.jpeg)
