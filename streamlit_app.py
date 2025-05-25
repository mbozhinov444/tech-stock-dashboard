import os
import streamlit as st
import pandas as pd
import sqlite3
import yaml
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import requests
from bs4 import BeautifulSoup
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title="Tech Stock Dashboard", layout="wide")

# ✅ Load configuration from config.yaml
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.yaml"))
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

# ✅ Get absolute path to the database from config
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", config["database_path"]))
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM stock_data", conn)
conn.close()

# ✅ Add sector and company metadata (first join)
company_info = pd.DataFrame({
    "Stock": ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA"],
    "Company": ["Apple", "Microsoft", "Google", "Amazon", "NVIDIA"],
    "Sector": ["Consumer Tech", "Cloud & AI", "Internet", "E-commerce", "Semiconductors"]
})
df = df.merge(company_info, on="Stock", how="left")

# ✅ Add sector-level average returns (second join)
sector_return = pd.DataFrame({
    "Sector": ["Consumer Tech", "Cloud & AI", "Internet", "E-commerce", "Semiconductors"],
    "AvgSectorReturn": [0.0011, 0.0014, 0.0009, 0.0012, 0.0017]
})
df = df.merge(sector_return, on="Sector", how="left")
df["Date"] = pd.to_datetime(df["Date"])

# Sidebar controls
st.sidebar.header("Filter Options")
stocks = df["Stock"].unique().tolist()
selected_stock = st.sidebar.selectbox("Choose a stock:", stocks)

# Date range slider
date_min = df["Date"].min().to_pydatetime()
date_max = df["Date"].max().to_pydatetime()
date_range = st.sidebar.slider(
    "Select Date Range:",
    min_value=date_min,
    max_value=date_max,
    value=(date_min, date_max)
)

# 📘 About section
st.sidebar.markdown("---")
st.sidebar.title("ℹ️ About this App")
st.sidebar.info("""
This dashboard was built for the Applied Data Science in Finance course at Université Paris 1 Panthéon-Sorbonne.
It features interactive visualizations of major tech stocks including volatility, regression, and return analysis.
""")

# Filter the data
filtered_df = df[(df["Stock"] == selected_stock) &
                 (df["Date"] >= pd.to_datetime(date_range[0])) &
                 (df["Date"] <= pd.to_datetime(date_range[1]))].copy()

# 📈 Calculate volatility and Sharpe ratio
volatility = filtered_df["Return"].std()
mean_return = filtered_df["Return"].mean()
sharpe_ratio = mean_return / volatility if volatility != 0 else 0

# 📉 Perform linear regression: Close ~ Date
filtered_df = filtered_df.dropna(subset=["Close"])
filtered_df["DateOrdinal"] = filtered_df["Date"].map(pd.Timestamp.toordinal)
X = filtered_df[["DateOrdinal"]]
y = filtered_df["Close"]
model = LinearRegression()
model.fit(X, y)
predicted = model.predict(X)
slope = model.coef_[0]
r2 = r2_score(y, predicted)

# 🌐 Scrape latest headline from Yahoo Finance
def fetch_headline(ticker):
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}?p={ticker}&.tsrc=fin-srch"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        headline_section = soup.find("ul", class_="My(0) P(0) Wow(bw) Ov(h)")
        if headline_section:
            first_headline = headline_section.find("h3")
            if first_headline:
                return first_headline.get_text(strip=True)
        return "No recent headline found."
    except Exception as e:
        return f"Error fetching news: {e}"

latest_headline = fetch_headline(selected_stock)

# Show basic info
st.title(f"📊 {selected_stock} Stock Analysis")
st.markdown(f"**Period:** {date_range[0].date()} to {date_range[1].date()}")
st.markdown(f"**Company:** {filtered_df['Company'].iloc[0]} | **Sector:** {filtered_df['Sector'].iloc[0]}")
st.markdown(f"**Avg Sector Return:** {filtered_df['AvgSectorReturn'].iloc[0]:.4f}")
st.markdown(f"**Volatility (std dev):** {volatility:.4f}  |  **Sharpe Ratio:** {sharpe_ratio:.2f}")
st.markdown(f"**Regression Slope:** {slope:.4f}  |  **R² Score:** {r2:.3f}")
st.markdown(f"**📰 Latest Headline from Yahoo Finance:** _{latest_headline}_")

# Download CSV button
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name=f"{selected_stock}_data.csv",
    mime='text/csv'
)

# Summary statistics
st.subheader("Summary Statistics")
st.dataframe(filtered_df.describe(include=[np.number]))

# 📈 Plotly line chart for price
st.subheader("Stock Price Over Time")
fig_price = px.scatter(filtered_df, x="Date", y="Close", title=f"{selected_stock} Price with Regression Line")
fig_price.add_scatter(x=filtered_df["Date"], y=predicted, mode="lines", name="Linear Trend")
st.plotly_chart(fig_price, use_container_width=True)

# 📊 Plotly histogram of returns
st.subheader("Distribution of Daily Returns")
fig_hist = go.Figure()
fig_hist.add_trace(go.Histogram(
    x=filtered_df["Return"].dropna(),
    nbinsx=50,
    marker_color='skyblue',
    opacity=0.85
))
fig_hist.update_layout(
    title="",
    xaxis_title="Return",
    yaxis_title="Frequency",
    bargap=0.05,
    template="plotly_white"
)
st.plotly_chart(fig_hist, use_container_width=True)

# Show full data
with st.expander("Show raw data"):
    st.dataframe(filtered_df.reset_index(drop=True))











