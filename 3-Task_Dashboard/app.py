import pandas as pd 
import os
import  plotly.express as px 
import plotly.graph_objects as go
import streamlit as st 

pwd = os.getcwd()
file_path = os.path.join(pwd, "exisiting_customer_data.xlsx" )

df = pd.read_excel(file_path)


st.set_page_config(page_title = " Sales Dashboard", 
                   page_icon=":bar_chart:", 
                   layout="wide")


st.sidebar.header("Please Filter Here:")
state = st.sidebar.multiselect(
    "Select the city:", 
    options= df["state"].unique(),
    default= df["state"].unique(),
)
gender = st.sidebar.multiselect(
    "Select the gender:", 
    options= df['gender'].unique(),
    default= df['gender'].unique(),
)
wealth_segment = st.sidebar.multiselect(
    "Select the wealth_segment:", 
    options= df['wealth_segment'].unique(),
    default= df['wealth_segment'].unique(),
)
Customer_segment = st.sidebar.multiselect(
    "Select the Customer_segment:", 
    options= df['Customer_segment'].unique(),
    default= df['Customer_segment'].unique(),
)

def_selection = df.query(
    "state == @state & gender == @gender & wealth_segment == @wealth_segment & Customer_segment == @Customer_segment"
)
#st.dataframe(def_selection)



#--------------------------- Mainpage ---------------------------
st.title(":bar_chart: Sales Dasboard")
st.markdown("##")

rupee_symbol = "₹"
st.write(f"Price: {rupee_symbol}500")

#   KPI's


total_sales = int(def_selection["list_price"].sum())
#avg_rating  = ":star:" * int(round(def_selection["rating"].mean(), 1))
avg_sales = round(def_selection["list_price"].mean(), 2)

left_col , middle_col, right_col = st.columns(3)

with left_col:
    st.subheader("Total sales :")
    st.subheader(f"INR ₹ {total_sales: ,}")
with middle_col:
    st.subheader("Average sales :")
    st.subheader(f"INR ₹ {avg_sales}")

st.markdown("---")


sales_online_orders = (
    def_selection.groupby(['online_order']).agg({ 'customer_id' :'count', 'Profit': 'sum'})
    )
fig_sales_online_orders = px.bar(
    sales_online_orders,
    x=['Profit','customer_id'],
    y=sales_online_orders.index,
    orientation="h",
    title = '<b>Scales by Product Line</b>',
    color_discrete_sequence = ['#C70039'] * len(sales_online_orders),
    template = 'plotly_white',
)
st.plotly_chart(fig_sales_online_orders)



