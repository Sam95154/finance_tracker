import streamlit as st
import pandas as pd
import plotly.express as px

st.title("💰 Personal Finance Tracker")

# User Input
amount = st.number_input("Enter Amount", min_value=0)

category = st.selectbox(
    "Select Category",
    ["Food", "Travel", "Shopping", "Bills"]
)

# Store Data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Amount", "Category"]
    )

# Add Expense
if st.button("Add Expense"):

    new_data = pd.DataFrame({
        "Amount": [amount],
        "Category": [category]
    })

    st.session_state.data = pd.concat(
        [st.session_state.data, new_data],
        ignore_index=True
    )

    st.success("Expense Added Successfully")

# Show Table
st.subheader("Expense Data")
st.dataframe(st.session_state.data)

# Pie Chart
if not st.session_state.data.empty:

    chart = px.pie(
        st.session_state.data,
        names="Category",
        values="Amount",
        title="Expense Distribution"
    )

    st.plotly_chart(chart)