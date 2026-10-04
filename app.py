import streamlit as st
import pandas as pd
import plotly.express as px

data = {
    "Product": [
        "Laptop", "Phone", "Tablet", "Monitor",
        "Laptop", "Phone", "Tablet", "Monitor",
        "Laptop", "Phone", "Tablet", "Monitor",
        "Laptop", "Phone", "Tablet", "Monitor"
    ],

    "Region": [
        "Lagos", "Lagos", "Lagos", "Lagos",
        "Abuja", "Abuja", "Abuja", "Abuja",
        "Kano", "Kano", "Kano", "Kano",
        "Port Harcourt", "Port Harcourt",
        "Port Harcourt", "Port Harcourt"
    ],

    "Sales": [
        1200000, 900000, 500000, 700000,
        800000, 700000, 400000, 600000,
        600000, 500000, 300000, 450000,
        950000, 750000, 420000, 580000
    ],

    "Profit": [
        250000, 180000, 100000, 140000,
        170000, 150000, 80000, 120000,
        120000, 100000, 60000, 90000,
        200000, 160000, 85000, 115000
    ],

    "Customers": [
        120, 180, 95, 80,
        90, 140, 75, 65,
        70, 110, 55, 50,
        100, 150, 72, 60
    ]
}

df = pd.DataFrame(data)


st.title("Sales Performance Dashboard")

st.write(
    "This dashboard provides an overview of sales, profit, and customer "
    "performance across different products and regions."
)

st.subheader("Sales Dataset")

st.dataframe(df)

#Create the 3 KPIs.
total_sales = df["Sales"].sum()
average_profit = df["Profit"].mean()
total_customers = df["Customers"].sum()

#creating coulumns
col1, col2, col3 = st.columns(3)

#Put a metric in each column
col1.metric("Total Sales", f"₦{total_sales:,.0f}")
col2.metric("Average Profit", f"₦{average_profit:,.0f}")
col3.metric("Total Customers", f"{total_customers:,}")

#Product vs Sales Chart

st.subheader("Sales by Product")

product_sales = df.groupby("Product", as_index=False)["Sales"].sum()

fig = px.bar(
    product_sales,
    x="Product",
    y="Sales",
    title="Total Sales by Product",
    labels={"Sales": "Total Sales (₦)", "Product": "Product"}
)

st.plotly_chart(fig, use_container_width=True)

