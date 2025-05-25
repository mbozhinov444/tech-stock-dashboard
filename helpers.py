# -*- coding: utf-8 -*-
"""
Created on Mon May 12 19:54:31 2025

@author: Admin
"""

import pandas as pd
import yfinance as yf
from sqlalchemy import create_engine
from typing import List

def download_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download historical stock data using yfinance.
    """
    df = yf.Ticker(ticker).history(start=start_date, end=end_date)
    df = df.reset_index()
    df = df[["Date", "Close", "Volume"]].copy()
    df["Stock"] = ticker
    df["Return"] = df["Close"].pct_change()
    return df

def load_all_stocks(tickers: List[str], start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download and concatenate data for multiple stocks.
    """
    all_data = []
    for ticker in tickers:
        print(f"Downloading {ticker}...")
        df = download_stock_data(ticker, start_date, end_date)
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)

def save_to_sqlite(df: pd.DataFrame, db_path: str, table_name: str = "stock_data") -> None:
    """
    Save DataFrame to a SQLite database.
    """
    engine = create_engine(f"sqlite:///{db_path}")
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print("✅ Data loaded into database:", db_path)
    print("🧾 Table:", table_name)
    print(df.head())
