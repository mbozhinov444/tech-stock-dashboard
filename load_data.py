# -*- coding: utf-8 -*-
"""
Created on Mon May 12 04:08:09 2025

@author: Admin
"""
import os
import sys
import yaml

# ✅ Add parent directory to path to allow utils import
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.helpers import load_all_stocks, save_to_sqlite

# Load configuration
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.yaml"))
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

TICKERS = config["tickers"]
START_DATE = config["start_date"]
END_DATE = config["end_date"]
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", config["database_path"]))
TABLE_NAME = "stock_data"

# Create database folder if needed
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Run ETL
full_df = load_all_stocks(TICKERS, START_DATE, END_DATE)
save_to_sqlite(full_df, DB_PATH, TABLE_NAME)