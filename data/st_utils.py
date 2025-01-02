import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

import streamlit as st
import os
def fetch_data(url, auth_key, params):
    headers = {
        'Authorization': f'Bearer {auth_key}' ,
        'account-type':os.environ.get('account-type',None)
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get("data" , None)
        if data == {} or data == None:
            return None

        return response.json()  
    
    if response.status_code == 401:
        st.error("Unauthorized access")

    else:
        st.error("Failed to fetch data from the server.")
    return None

def get_months_available(url , auth_key):
	headers = {
	'Authorization': f'Bearer {auth_key}'  # Include the Bearer token in the headers
	}
	url = url.strip("/") +f"/available_months"
	response = requests.get(url , params= {"year":2024} , headers=headers)

	return response

def format_time(time, data_date):
    try:
        if data_date:
            time = data_date.strip() + "-" + time.strip()
        return datetime.strptime(time, "%Y-%m-%d-%H:%M:%S")
    except Exception as e:
        return None

def create_df(df_list, data_date):
    df = pd.DataFrame(df_list)[['time', 'value']]
    df['datetime'] = df['time'].map(lambda x: format_time(time=x, data_date=data_date))
    df['day'] = df['datetime'].map(lambda x: x.day)
    df['hour'] = df['datetime'].map(lambda x: x.hour)
    df['minute'] = df['datetime'].map(lambda x: x.minute)
    df['second'] = df['datetime'].map(lambda x: x.second)

    return df

def generate_heatmap(df):
    pivot_table = df.pivot_table(values='value', index='day', columns='hour', aggfunc='mean')
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap='viridis', annot=True, fmt=".2f")
    plt.title('Heatmap of Average 0-Odd Value by Day and Hour')
    plt.xlabel('Hour')
    plt.ylabel('Day')
    return plt

def generate_scatter_plot(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df['hour'], df['value'], alpha=0.5)
    plt.title('0-Odd Value vs. Hour of Day')
    plt.xlabel('Hour')
    plt.ylabel('0-Odd Value')
    return plt

def generate_histogram(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['value'], bins=30, edgecolor='black')
    plt.title('Distribution of 0-Odd Values')
    plt.xlabel('0-Odd Value')
    plt.ylabel('Frequency')
    return plt

def transform_to_df(response):
    data = response['data']
    
    # Initialize an empty list to store the DataFrames
    dfs = []
    
    # Check the structure of the data
    if isinstance(data, dict):
        for key, value in data.items():
            if isinstance(value, dict):
                # Test case 5: Get weekly data for a month
                for sub_key, sub_value in value.items():
                    df = pd.DataFrame(sub_value)
                    df['date'] = sub_key
                    dfs.append(df)
            elif isinstance(value, list):
                df = pd.DataFrame(value)
                df['date'] = key
                dfs.append(df)
            else:
                for sub_key, sub_value in value.items():
                    for sub_sub_key, sub_sub_value in sub_value.items():
                        
                        df = pd.DataFrame(sub_sub_value)
                        df['date'] = sub_sub_key
                        dfs.append(df)
    
    
    
    df = pd.concat(dfs, ignore_index=True)
    df = df[['value', 'time', 'date']]
    
    df['date'] = df['date'].apply(lambda x: datetime.strptime(x, "%Y-%m-%d").date())
    df['value'] = df['value'].astype(float)
    df['time'] = df['time'].apply(lambda x: datetime.strptime(x, "%H:%M:%S").time())

    df['day'] = df['date'].map(lambda x: x.day)
    df['hour'] = df['time'].map(lambda x: x.hour)
    df['minute'] = df['time'].map(lambda x: x.minute)
    df['second'] = df['time'].map(lambda x: x.second)
    
    return df
