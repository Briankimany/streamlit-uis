import streamlit as st
from st_utils import fetch_data , generate_scatter_plot , generate_heatmap , generate_histogram , transform_to_df ,get_months_available
import os

st.set_page_config(layout="wide")
st.title("Odds Analysis")

col1, col2, col3 = st.columns(3)

url = "https://kimany.pythonanywhere.com/data"  


with col1:

    auth_key = st.text_input("Enter Auth Key")
    account_type = st.selectbox("Select Account Type", options=["DEMO_ACC ", "LIVE_ACC"])
    data_type = st.selectbox("Select Data Type", options=["Daily", "Monthly", "Weekly", "Custom Range"])

    if data_type == "Daily":
        daily = st.date_input("Select a Date")
        params = {'daily': daily.strftime("%Y-%m-%d")}
    elif data_type == "Monthly":
        response = get_months_available("https://kimany.pythonanywhere.com" ,auth_key)
        if response .status_code== 200:
                
            available_monthly_data = list(response.json()['data'].keys())
            available_years = set([int(i.split('-')[0]) for i in response.json()['data'].values()])

            year = st.selectbox("Select a year", options=available_years)
            monthly = st.selectbox("Select a Month", options=available_monthly_data)
            month_to_int = {
                "January": 1,
                "February": 2,
                "March": 3,
                "April": 4,
                "May": 5,
                "June": 6,
                "July": 7,
                "August": 8,
                "September": 9,
                "October": 10,
                "November": 11,
                "December": 12
            }
            params = {'monthly': f"{year}-{month_to_int[monthly]:02d}"}
        elif response.status_code == 401:
            st.error("Unauthorized access")
            params = None
        else:
            st.error("Error ")
            params= None
    elif data_type == "Weekly":
        weekly = st.date_input("Select a Week")
        params = {'weekly': weekly.strftime("%Y-%m")}
    else:
        start_date = st.date_input("Select a Start Date")
        end_date = st.date_input("Select an End Date")
        params = {'start_date': start_date.strftime("%Y-%m-%d"), 'end_date': end_date.strftime("%Y-%m-%d")}

    if st.button("Fetch Data"):
        if auth_key and data_type:
            data = None
            os.environ['account-type'] = account_type
            if params:
                data = fetch_data(url, auth_key, params)

            if data is not None:
                st.session_state.data = data
                st.warning("Fetching data ,please wait.")
                st.session_state.df=transform_to_df(data)
                st.success("Data fetched successfully!")
            else:
                st.error("No data found !")
                st.session_state.data = None
        else:
            st.warning("Please fill in all fields.")

with col2:
    data = st.session_state.get('data' , None)
    if data:
            df = st.session_state.df
            with st.expander('TABLE'):
                st.table(df[['date','time', 'value']])

with col3:
    data = st.session_state.get('data' , None)
    if data:
        df = st.session_state.df
        if st.button("Show Heatmap"):
            heatmap_fig = generate_heatmap(df)
            st.pyplot(heatmap_fig)

        
        if st.button("Show Scatter Plot"):
            scatter_fig = generate_scatter_plot(df)
            st.pyplot(scatter_fig)

        if st.button("Show Histogram"):
            histogram_fig = generate_histogram(df)
            st.pyplot(histogram_fig)
