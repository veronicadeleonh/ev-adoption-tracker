import streamlit as st
from utils import sales_by_region
import matplotlib.pyplot as plt
import plotly.express as px 
import pandas as pd

st.set_page_config(
    page_title="🚗 EV Sales and Sales Share",
    page_icon=":electric_plug:",
)

st.title("🚗 EV Sales Data")

## subheader
st.subheader("EV Sales by Country")

##### LOAD DATA #####
ev_sales_by_region_df = sales_by_region()


# create a filter to select the region
region_filter = st.selectbox("Select Country", ev_sales_by_region_df["region"].unique())

# filter the dataframe by the selected region
ev_sales_region_labels = ev_sales_by_region_df[ev_sales_by_region_df["region"] == region_filter]

# create a bar chart of the sales by year and units sold without stacking by region
st.bar_chart(ev_sales_region_labels, x="year", y="sales", color="powertrain")

# divider
st.divider()

#subheader
st.subheader("Top Sales by Country")

# create dataframe with top 10 sales by country
top_sales_by_country_df = ev_sales_by_region_df.groupby("region")["sales"].sum().nlargest(10).reset_index()

col1, col2 = st.columns([2, 1])

with col1:
    # draw a pie chart of the top 10 sales by country
    fig = px.pie(top_sales_by_country_df, values='sales', names='region', title='Top 10 EV Sales by Country')
    st.plotly_chart(fig)
    

with col2:
    # draw a dataframe of the top 10 sales by country and dont show the index
    st.dataframe(top_sales_by_country_df, hide_index=True)

    
#divider
st.divider()

#subheader
st.subheader("Top Sales by Country")

# add a multiselect to select the country
country_filter = st.multiselect("Select Country", ev_sales_by_region_df["region"].unique())

# filter the dataframe by the selected country
ev_sales_country_labels = ev_sales_by_region_df[ev_sales_by_region_df["region"].isin(country_filter)]

# add a powertrain filter
powertrain_filter = st.multiselect("Select Powertrain", ev_sales_country_labels["powertrain"].unique())

# filter the dataframe by the selected powertrain
ev_sales_country_labels = ev_sales_country_labels[ev_sales_country_labels["powertrain"].isin(powertrain_filter)]

# create a line chart of the sales by year for the selected countries and powertrains
if not ev_sales_country_labels.empty:
    sales_by_year_region = ev_sales_country_labels.groupby(['year', 'region'])['sales'].sum().reset_index()

    # Pivot the DataFrame to have years as index and regions as columns
    sales_pivot = sales_by_year_region.pivot(index='year', columns='region', values='sales')

    # Create the line chart
    st.line_chart(sales_pivot)
else:
    st.warning("Please select at least one country and one powertrain to display the sales data.")


