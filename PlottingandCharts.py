import sys

import pandas as pd
import streamlit
from matplotlib import pyplot as plt
import seaborn as sns
sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Airbnb\venv\Lib\site-packages')

def plotsandcharts():
    df=pd.read_csv(r'Airbnb.csv')
    col1, col2 = streamlit.columns([1, 1], gap='large')
    col3, col4 = streamlit.columns([1, 1], gap='large')
    col5, col6 = streamlit.columns([1, 1], gap='large')
    col7, col8 = streamlit.columns([1, 1], gap='large')
    col9, col10 = streamlit.columns([1, 1], gap='large')
    with col1:
        plt.figure(figsize=(20,10))
        x=sns.barplot(data=df, y=df.property_type.values, x=df.price.values)
        x.set_title("Property Types vs Prices")
        streamlit.pyplot(x.get_figure(),use_container_width=True)
    with col2:
        plt.figure(figsize=(10, 5))
        x = sns.violinplot(x=df.price.head(100))
        x.set_title('Top 100 Property price')
        streamlit.pyplot(x.get_figure(), use_container_width=True)

    with col3:
        plt.figure(figsize=(10, 5))
        x = sns.boxplot(data=df, y=df.property_type.head(100), x=df.rating.head(100))
        x.set_title('Top 100 Property vs rating')
        streamlit.pyplot(x.get_figure(), use_container_width=True)

    with col4:
        plt.figure(figsize=(10,5))
        x=sns.countplot(data=df, y=df.room_type)
        x.set_title("Total room types")
        streamlit.pyplot(x.get_figure(), use_container_width=True)
    with col5:
        plt.figure(figsize=(10,8))
        x = sns.countplot(data=df,x=df.bed_type,order=df.bed_type.value_counts().index[1:10])
        x.set_title("Bed_types available and their counts")
        streamlit.pyplot(x.get_figure())
    with col6:
        plt.figure(figsize=(10,5))
        x=sns.barplot(data=df, y=df.property_type[df.rating.values<85], x=df.rating[df.rating.values<85])
        x.set_title("Property type with rating below 85")
        streamlit.pyplot(x.get_figure())
    with col7:
        country_df = df.groupby(df.country, as_index=False)['price'].mean()
        plt.figure(figsize=(10, 5))
        x = sns.scatterplot(data=country_df, y=country_df.price, x=country_df.country)
        x.set_title("Average Listing Price in  Countries")
        streamlit.pyplot(x.get_figure())
    with col8:
        plt.figure(figsize=(10, 5))
        x=sns.barplot(data=df, x=df.rating, y=df.price)
        x.set_title('Price vs rating')
        streamlit.pyplot(x.get_figure())
    with col9:
        plt.figure(figsize=(10, 5))
        x = sns.barplot(data=df, y=df.property_type.values, x=df.availability_365.values)
        x.set_title("No of days Property Available for a year")
        streamlit.pyplot(x.get_figure())

    with col10:
        plt.figure(figsize=(10, 5))
        x = sns.countplot(data=df, y=df.property_type, order=df.property_type.value_counts().iloc[:10].index)
        x.set_title("Top 10 Property types")
        streamlit.pyplot(x.get_figure())
