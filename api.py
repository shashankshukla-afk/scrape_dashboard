from fastapi import FastAPI
import mysql.connector

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password",
        database="business_listings"
    )

# API 1 - Get all listings
@app.get("/listings")
def get_listings():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM listing_master")
    data = cursor.fetchall()
    conn.close()
    return data

# API 2 - City wise count
@app.get("/city-count")
def city_count():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT city, COUNT(*) as count FROM listing_master GROUP BY city")
    data = cursor.fetchall()
    conn.close()
    return data

# API 3 - Category wise count
@app.get("/category-count")
def category_count():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT category, COUNT(*) as count FROM listing_master GROUP BY category")
    data = cursor.fetchall()
    conn.close()
    return data

# API 4 - Source wise count
@app.get("/source-count")
def source_count():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT source, COUNT(*) as count FROM listing_master GROUP BY source")
    data = cursor.fetchall()
    conn.close()
    return data