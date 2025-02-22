import streamlit as st
from utils import load_data

###################################### Page Config #####################################
st.set_page_config(
    layout="centered",
    initial_sidebar_state="collapsed",
    page_title="EV Sales and Sales Share",
    page_icon=":electric_plug:",
)


###################################### Load Data #####################################
ev_sales_df, ev_sales_share_df = load_data()


###################################### Header #####################################
st.title("Global EV Sales Summary")

expander = st.expander("About this app", expanded=True)
expander.markdown("This app is a summary of the global EV sales data using the [International Energy Agency (IEA)](https://www.iea.org/data-and-statistics/data-tools/global-ev-data-explorer) EV Sales dataset.")


###################################### Goblal EV Sales Summary ########################

st.subheader("Total EV Sales")
st.divider()

# Summary Metrics
col1, col2, col3 = st.columns([1, 1, 1])

col1.metric("EV Sales", 12354546)
col2.metric("EV Sales Growth", 12354546)
col3.metric("Charging Points", 12354546)

# Add vertical space
st.markdown("\n")
st.markdown("\n")
st.markdown("\n")

# Bar Chart of Global EV Sales
st.subheader("Global EV Sales")
st.divider()

# Filter ev_sales_df to only include World sales
world_sales_df = ev_sales_df[ev_sales_df["region"] == "World"]

# Create a bar chart of the sales by year
st.bar_chart(world_sales_df, x="year", y="sales", color="powertrain")





