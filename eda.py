import pandas as pd

# 1. Read dataset
df = pd.read_excel("OLA_DataSet.xlsx")

# 2. Drop unnecessary columns
if "Vehicle Images" in df.columns:
    df.drop(columns=["Vehicle Images"], inplace=True)

# 3. Create Ride_DateTime (Date + Time)
if "Date" in df.columns and "Time" in df.columns:
    df["Ride_DateTime"] = pd.to_datetime(
        df["Date"].astype(str) + " " + df["Time"].astype(str),
        errors="coerce"
    )
    # Drop Time column after combining
    df.drop(columns=["Time"], inplace=True)

# 4. Fill missing values
df["Payment_Method"] = df["Payment_Method"].fillna("Unknown")
df["Driver_Ratings"] = df["Driver_Ratings"].fillna(df["Driver_Ratings"].mean())
df["Customer_Rating"] = df["Customer_Rating"].fillna(df["Customer_Rating"].mean())
df["Incomplete_Rides_Reason"] = df["Incomplete_Rides_Reason"].fillna("Not_Applicable")

# 5. Create Incomplete Flag
df["Incomplete_Flag"] = df["Incomplete_Rides"].notna().astype(int)
if "Incomplete_Rides" in df.columns:
    df.drop(columns=["Incomplete_Rides"], inplace=True)

# 6. Create Cancel Flags from Booking_Status
df["Canceled_By_Customer"] = df["Booking_Status"].str.contains("customer", case=False, na=False).astype(int)
df["Canceled_By_Driver"] = df["Booking_Status"].str.contains("driver", case=False, na=False).astype(int)

# 7. Print Summary
print("Shape after cleaning:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing values after cleaning:\n", df.isnull().sum())
print("\nBooking Status Counts:\n", df["Booking_Status"].value_counts())
print("\nCancel Flags Distribution:")
print("Canceled_By_Customer:", df["Canceled_By_Customer"].value_counts().to_dict())
print("Canceled_By_Driver:", df["Canceled_By_Driver"].value_counts().to_dict())
print("Incomplete_Flag:", df["Incomplete_Flag"].value_counts().to_dict())
print("\nFirst 5 rows:\n", df.head())

# 8. Save cleaned dataset
df.to_csv("OLA_Cleaned.csv", index=False)
print("\n✅ Cleaned dataset saved as OLA_Cleaned.csv")

