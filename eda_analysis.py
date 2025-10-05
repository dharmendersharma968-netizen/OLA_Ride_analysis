import pandas as pd
df = pd.read_csv("OLA_Cleaned.csv")
print ("Shape(rows,column): " , df.shape)
print("\ncolums:\n", df.columns.to_list())
print("\nDataset_Sample:" , df.head())
print("\nSummary Stastics:", df.describe())
print("\nBooking Status Count:\n", df["Booking_Status"].value_counts())
print("\nVehicle Type Count:\n", df["Vehicle_Type"].value_counts())
print("\nPayment Method count:\n", df["Payment_Method"].value_counts())