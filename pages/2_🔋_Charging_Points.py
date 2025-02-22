import streamlit as st
from utils import load_charging_points_data, load_world_data

st.set_page_config(
    page_title="🔋 Charging Points",
    page_icon=":electric_plug:",
)

st.title("🔋 Charging Points")

#subheader
st.subheader("Charging Points by Country")  

## load data
ev_charging_points_df = load_charging_points_data() 
world_df = load_world_data()


######################### BAR CHART #########################
## create filter to select country
country_filter_bar_chart = st.selectbox("Select Country", ev_charging_points_df["region"].unique())

## filter dataframe by selected country
ev_charging_points_country_labels_bar_chart = ev_charging_points_df[ev_charging_points_df["region"] == country_filter_bar_chart]

## create a bar chart of the charging points by year    
st.bar_chart(ev_charging_points_country_labels_bar_chart, x="year", y="charging_points", color="powertrain")

# divider
st.divider()

######################### LINE CHART #########################
## subheader
st.subheader("Charging Points Growth through the years world wide")

# line chart of the charging points growth through the years in the world
st.line_chart(world_df, x="year", y="charging_points", color="powertrain")


# Divider
st.divider()

######################### TOP 10 COUNTRIES' CHARGING INFRASTRUCTURE #########################
## Subheader
st.subheader("Top 10 Countries' Charging Infrastructure")

# Calculate total charging points (fast and slow) for each country
ev_charging_points_df['total_charging_points'] = ev_charging_points_df['Publicly available fast'] + ev_charging_points_df['Publicly available slow']

# Group by region and sum the total charging points
top_countries_df = ev_charging_points_df.groupby('region')['total_charging_points'].sum().reset_index()

# Get the top 10 countries by total charging points
top_countries_df = top_countries_df.nlargest(10, 'total_charging_points')

# Create a bar chart for the total charging points
st.bar_chart(top_countries_df.set_index('region')['total_charging_points'])





















