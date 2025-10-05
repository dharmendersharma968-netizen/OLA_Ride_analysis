import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

st.title("OLA RIDE DASHBOARD")

# ✅ MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dharam@123",
    database="ola_project"
)

# ✅ Sidebar filters
st.sidebar.title("Filters")
vehicle_filter = st.sidebar.selectbox(
    "Select Vehicle Type", ["All", "Bike", "Auto", "Mini", "Prime Sedan", "Prime SUV", "Prime Plus", "eBike"]
)

status_filter = st.sidebar.selectbox(
    "Select Booking Status", ["All", "Success", "Canceled by Customer", "Canceled by Driver", "Driver Not Found"]
)

#date slicer


# ✅ Base query
query = "SELECT * FROM ola_rides"

# ✅ Add conditions
conditions = []
if vehicle_filter != "All":
    conditions.append(f"Vehicle_Type = '{vehicle_filter}'")
if status_filter != "All":
    conditions.append(f"Booking_Status = '{status_filter}'")

if conditions:
    query += " WHERE " + " AND ".join(conditions)

query += " LIMIT 50;"

df = pd.read_sql(query, conn)


st.sidebar.subheader("Select Date Range")
if "Ride_DateTime" in df.columns:
    min_date = pd.to_datetime(df["Ride_DateTime"]).min().date()
    max_date = pd.to_datetime(df["Ride_DateTime"]).max().date()
    date_range = st.sidebar.date_input("Choose Date Range", [min_date,max_date], min_value= min_date, max_value= max_date)
    if len(date_range) == 2:
        start_date, end_date = date_range
        df = df[
            (pd.to_datetime(df["Ride_DateTime"]).dt.date >= start_date) &
            (pd.to_datetime(df["Ride_DateTime"]).dt.date <= end_date)
    ]







#kpi cards
col1, col2, col3, col4 = st.columns(4)

total_rides = len(df)
col1.metric("Total Rides", total_rides)

success_ride = len(df[df["Booking_Status"]== "Success"])
col2.metric("Successful RIdes", success_ride)

cancel_rides = len(df[df["Booking_Status"].str.contains("Canceled")])
col3.metric("Cancel Rides", cancel_rides)

total_revenue = df["Booking_Value"].sum()
col4.metric("Total Revenue", f"{total_revenue}")

st.subheader("Booking Status Breakdown")
status_counts = df["Booking_Status"].value_counts()

fig, ax = plt.subplots()
ax.pie(status_counts, labels = status_counts.index, autopct= "%1.1f%%" , startangle = 90)
ax.axis("equal")

st.pyplot(fig)

#bar graph
st.subheader("Rides per Vehicle type ")
vehicle_counts = df["Vehicle_Type"].value_counts()
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(vehicle_counts.index, vehicle_counts.values, color = "skyblue")

ax.set_xlabel("Vehicle Type")
ax.set_ylabel("Number Of Rides")
ax.set_title("Rides By Vehicle Type")
plt.xticks(rotation=30)
st.pyplot(fig)

st.subheader("Revenue by Payment Method")

payment_revenue = df.groupby("Payment_Method")["Booking_Value"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(6,4))
ax.bar(payment_revenue.index, payment_revenue.values, color="orange")

ax.set_xlabel("Payment Method")
ax.set_ylabel("Total Revenue (₹)")
ax.set_title("Revenue by Payment Method")

plt.xticks(rotation=30)

st.pyplot(fig)

st.subheader("Ratings Distribution")

rating_col = st.sidebar.selectbox(
    "Select Rating Column",
    [col for col in df.columns if "Rating" in col]  # auto-detect rating columns
)

if rating_col in df.columns:
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df[rating_col].dropna(), bins=10, color="green", edgecolor="black")
    ax.set_xlabel(rating_col)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Distribution of {rating_col}")
    st.pyplot(fig)
else:
    st.info("No rating column found in the data.")

# ✅ Show results
st.write("### Filtered Rides Data")
st.dataframe(df)
