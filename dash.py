import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales data.csv")

df["total"] = df["Quantity_Sold"] * df["Sales_Amount"]

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("Sales Dashboard")

st.markdown("#### This is a collection of all the charts from the sales record")

# Calculating the KPIs
col1, col2,col3 = st.columns(3)

with col1:
    st.metric(label="Total Quantity Sold", value=df["Quantity_Sold"].sum())


with col2:
    st.metric(label="Total Revenue Generated", value=round(df["total"].sum()))

with col3:
    st.metric(label="The Most Sold Product", value=df["Product_Category"].mode()[0])

st.markdown("#### Charts")

chart1, chart2 = st.columns(2)

# Total Revenue per Product Category
product_revenue = df.groupby("Product_Category")["total"].sum()
with chart1:
    fig, ax = plt.subplots()
    product_revenue.plot(kind="bar", color="blue", ax=ax)
    plt.title("Total Revenue per Product")
    plt.xlabel("Products")
    plt.xticks(rotation=45)
    plt.ylabel("Total Revenue")
    st.pyplot(fig)

# Total Revenue per sales rep
salesrep_revenue = df.groupby("Sales_Rep")["total"].sum()
with chart2:
    fig, ax = plt.subplots()
    salesrep_revenue.plot(kind="line", color="green", marker="o", ax=ax)
    plt.title("Revenue per Sales Rep")
    st.pyplot(fig)

chart3, chart4 = st.columns(2)

# Most popular payment method
payment_method = df.groupby("Payment_Method")["Payment_Method"].count()
with chart3:
    fig, ax = plt.subplots()
    payment_method.plot(kind="pie", autopct="%.2f%%")
    plt.title("Payment Method Distribution")
    plt.ylabel("")
    st.pyplot(fig)

# Sales per Region
with chart4:
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="Region", ax=ax, hue="Region")
    plt.title("Total Sales per Region")
    plt.xlabel("Region")
    plt.ylabel("Total Sales")
    st.pyplot(fig)


st.markdown("#### Data Preview")
st.dataframe(df.head(10))

