import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Low-Risk Asset Allocation Portfolio",
    page_icon="💹",
    layout="wide"
)

# -----------------------------
# TITLE & DESCRIPTION
# -----------------------------
st.title("💹 Asset Allocation Portfolio (Low-Risk Profile)")
st.subheader("Age Group: 45–65 years")

st.markdown("""
This portfolio is designed for investors with a **low-risk tolerance**, focusing on **capital protection, moderate returns**, and **reduced volatility**.  
""")

# -----------------------------
# DATA
# -----------------------------
data = {
    "Asset class": [
        "Equity (Stocks / Equity MFs)",
        "Debt / Fixed Income",
        "Gold / Commodities",
        "Real Estate",
        "Cash / Liquid Funds"
    ],
    "Allocation (%)": [15, 50, 20, 10, 5],
    "Risk": ["Moderate", "Low", "Moderate", "Low moderate", "Very low"],
    "Reward (%)": ["9-11", "6-7", "8-9", "6-8", "3-4"],
    "Time period": ["5-7 YRS", "3-5 YRS", "7-10 YRS", "3-5 YRS", "0-1 YRS"],
    "Portfolio Weight Impact (%)": [15, 50, 20, 10, 5],
    "LOGIC": [
        "Stock market fluctuates; you can lose 20–30% short term, but since only 15% is invested, overall impact is ~10%.",
        "Safer because returns are fixed. Risk comes only if interest rates change or issuer defaults (rare).",
        "Moves opposite to equity — protects during crises (like 2020).",
        "Property isn’t easy to sell quickly; market cycles take years. Physical asset = long-term safety.",
        "Almost risk-free, but inflation slowly reduces its real value."
    ],
    "SUMMARY": [
        "Keeps inflation protection & long-term growth, but limits volatility.",
        "Main stability pillar — predictable cash flow. Acts as a ‘shock absorber’.",
        "Protects capital during downturns; hedge against equity risk.",
        "Illiquid but steady; useful as diversification for long-term wealth.",
        "Liquidity for emergencies or reinvestment when markets dip."
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# DISPLAY PORTFOLIO TABLE
# -----------------------------
st.markdown("### 🧾 Portfolio Breakdown")
st.dataframe(df, use_container_width=True)

# -----------------------------
# PIE CHART FOR ALLOCATION
# -----------------------------
st.markdown("### 📊 Allocation Overview")
fig = px.pie(df, values="Allocation (%)", names="Asset class",
             color_discrete_sequence=px.colors.sequential.Blues_r,
             title="Portfolio Allocation by Asset Class")
st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# PORTFOLIO PERFORMANCE METRICS
# -----------------------------
st.markdown("### 📈 Portfolio Performance Summary")

metrics = {
    "Expected Annual Return": "7.95% realistic long-term average",
    "Portfolio Risk (Std. Dev.)": "9.90% → portfolio’s value could swing ±10% in a year",
    "Worst-Case (95% confidence)": "11% possible fall in bad year",
    "Best-Case (95% confidence)": "27% gain in a very good year",
    "Risk-Adjusted Return (Sharpe-like)": "0.80% → healthy for low-risk investors"
}

# Display metrics nicely
for k, v in metrics.items():
    st.markdown(f"**{k}:** {v}")

# -----------------------------
# FOOTER DISCLAIMER
# -----------------------------
st.markdown("""
---
**Disclaimer:**  
This app is for **educational purposes only**. The data and calculations shown represent 
a hypothetical portfolio designed for low-risk investors. Always consult a certified financial planner 
before making investment decisions.
""")
