# Business Listings Dashboard

A full-stack data dashboard built with FastAPI, Streamlit and MySQL.

## Tech Stack
- Python
- FastAPI
- Streamlit
- MySQL
- Pandas
- Plotly

## Project Structure
- Main.py - Web scraping code
- api.py - FastAPI backend
- dashboard.py - Streamlit dashboard
- insert.py - Insert data into MySQL
- listings.csv - Mock business data

## Setup Instructions

### Step 1 - Install dependencies
pip install fastapi uvicorn mysql-connector-python streamlit pandas plotly requests

### Step 2 - Setup MySQL
- Create database: business_listings
- Create table: listing_master
- Run insert.py to insert 500 records

### Step 3 - Run FastAPI
uvicorn api:app --reload

### Step 4 - Run Dashboard
streamlit run dashboard.py

## Features
- City wise business count
- Category wise business count
- Source wise business count
- Interactive charts
- Full data table view

## Author
Shashank Shukla
