import pandas as pd

def load_data():
    ev_url = "https://api.iea.org/evs?parameters=EV-sales&category=Historical&mode=Cars&csv=true"

    ev_df = pd.read_csv(ev_url)

    ev_df = ev_df[['region', 'parameter', 'powertrain', 'year', 'unit', 'value']]

    # split the dataframe into two based on the parameter
    ev_sales_df = ev_df[ev_df['parameter'] == 'EV sales']
    ev_sales_share_df = ev_df[ev_df['parameter'] == 'EV sales share']

    # drop the parameter and unit columns
    ev_sales_share_df = ev_sales_share_df.drop(columns=['parameter', 'unit'])
    ev_sales_df = ev_sales_df.drop(columns=['parameter', "unit"])

    # rename the value column to sales
    ev_sales_df.rename(columns={'value': 'sales'}, inplace=True)
    ev_sales_share_df.rename(columns={'value': 'sales_share'}, inplace=True)

    # reset the index
    ev_sales_df.reset_index(drop=True, inplace=True)
    ev_sales_share_df.reset_index(drop=True, inplace=True)

    return ev_sales_df, ev_sales_share_df


def sales_by_region():
    ev_url = "https://api.iea.org/evs?parameters=EV-sales&category=Historical&mode=Cars&csv=true"

    ev_df = pd.read_csv(ev_url)

    ev_df = ev_df[['region', 'parameter', 'powertrain', 'year', 'unit', 'value']]

    exclude_list = ['Europe', 'EU27', 'Rest of the world', 'World']
    ev_sales_by_region_df = ev_df[~ev_df['region'].isin(exclude_list)]

    ev_sales_by_region_df = ev_sales_by_region_df[ev_sales_by_region_df['parameter'] == "EV sales"]

    ev_sales_by_region_df.rename(columns={'value': 'sales'}, inplace=True)

    ev_sales_by_region_df = ev_sales_by_region_df.drop(columns=['parameter', 'unit'])

    return ev_sales_by_region_df


def load_charging_points_data():
    ev_charging_points_url = "https://api.iea.org/evs?parameters=EV-charging-points&category=Historical&mode=EV&csv=true"

    ev_charging_points_df = pd.read_csv(ev_charging_points_url)

    ev_charging_points_df = ev_charging_points_df[['region', 'powertrain', 'year', 'value']]
    ev_charging_points_df.rename(columns={'value': 'charging_points'}, inplace=True)

    exclude_list = ['Europe', 'EU27', 'Rest of the world', 'World']
    ev_charging_points_df = ev_charging_points_df[~ev_charging_points_df['region'].isin(exclude_list)]

    return ev_charging_points_df


def load_world_data():
    ev_charging_points_url = "https://api.iea.org/evs?parameters=EV-charging-points&category=Historical&mode=EV&csv=true"

    powertrain_years_df = pd.read_csv(ev_charging_points_url)

    powertrain_years_df = powertrain_years_df[powertrain_years_df['region'] == 'World']    

    powertrain_years_df = powertrain_years_df.drop(columns=['region', 'category', 'parameter', 'unit', 'mode'])

    powertrain_years_df.rename(columns={'value': 'charging_points'}, inplace=True) 

    return powertrain_years_df
