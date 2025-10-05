import pandas as pd

# Step 1: Load CSV
df = pd.read_csv("OLA_Cleaned.csv")

# Step 2: Convert date columns to MySQL-friendly format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True).dt.strftime("%Y-%m-%d %H:%M:%S")
df["Ride_DateTime"] = pd.to_datetime(df["Ride_DateTime"], dayfirst=True).dt.strftime("%Y-%m-%d %H:%M:%S")

# Step 3: Save new file
df.to_csv("OLA_Cleaned_MySQL.csv", index=False)

print("✅ File saved as OLA_Cleaned_MySQL.csv with correct datetime format.")
