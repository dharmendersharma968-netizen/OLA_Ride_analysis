import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("OLA_Cleaned.csv")
plt.figure(figsize=(6,4))
sns.countplot(x = "Booking_Status", data= df, order=df["Booking_Status"].value_counts().index)
plt.title("Booking Status DIstribution")
plt.xticks(rotation=30)
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x= "Payment_Method", data= df, order=df["Payment_Method"].value_counts().index)
plt.title("Payment Method Distribution")
plt.xticks(rotation = 30)
plt.show()

plt.figure(figsize= (7,4))
order = df["Vehicle_Type"].value_counts().index
sns.countplot(x="Vehicle_Type", data= df, order=order, palette= "viridis")
plt.title("Vehicle Type Distribution")
plt.xticks(rotation = 30)
plt.show()

plt.figure(figsize=(8,5))
top_pickups = df["Pickup_Location"].value_counts().head(10)
sns.barplot(x=top_pickups.index, y=top_pickups.values, palette="pastel")
plt.title("Top 10 Pickup Location")
plt.xticks(rotation = 45)
plt.ylabel("Number of Rides")
plt.xlabel("Pickup Location")
plt.show()

plt.figure(figsize=(8,5))
top_drops = df["Drop_Location"].value_counts().head(10)
sns.barplot(x=top_drops, y=top_drops.values, palette= "muted")
plt.title("Top 10 Drops ")
plt.xticks(rotation = 45)
plt.ylabel("Number of RIdes")
plt.xlabel("Drop Location")
plt.show()

# 4. Cancel by Customer Flag
plt.figure(figsize=(5,4))
sns.countplot(x="Canceled_By_Customer", data=df, palette="coolwarm")
plt.title("Canceled by Customer (0 = No, 1 = Yes)")
plt.show()

# 5. Cancel by Driver Flag
plt.figure(figsize=(5,4))
sns.countplot(x="Canceled_By_Driver", data=df, palette="coolwarm")
plt.title("Canceled by Driver (0 = No, 1 = Yes)")
plt.show()
