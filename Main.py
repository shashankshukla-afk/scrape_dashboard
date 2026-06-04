import pandas as pd
import random

restaurants = [
    "Tunday Kababi", "Sharma Ji Ka Dhaba", "Moti Mahal","Royal Cafe", 
    "Wahid Biryani", "Idris Biryani","Bajpai Kachori", "Chowdhary Lassi", 
    "Dastarkhan","Zaheer Ahmed Biryani", "Peter Cafe", "Aryan Restaurant"
    ]

categories = ["North Indian", "Mughlai", "Fast Food", 
"South Indian", "Chinese", "Street Food"]

areas = ["Hazratganj", "Aminabad", "Gomti Nagar", 
         "Chowk", "Aliganj", "Indira Nagar"]

data = []
for i in range(500):
    data.append({
        "business_name": random.choice(restaurants) + f" {i+1}",
        "category": random.choice(categories),
        "city": "Lucknow",
        "address": f"{random.randint(1,100)}, {random.choice(areas)}",
        "phone": f"98{random.randint(10000000, 99999999)}",
        "source": "Justdial"
    })

df = pd.DataFrame(data)
df.to_csv("listings.csv", index=False)
print(f"Created {len(df)} listings!")
print(df.head())
