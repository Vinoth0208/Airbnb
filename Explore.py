import sys
import pandas as pd
import streamlit as st
sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Airbnb\venv\Lib\site-packages')
import streamlit_option_menu
from Dataextraction import extract
import plotly.express as px


def explore():
    tab1, tab2 = st.tabs(["$\huge 📝 Raw Data$", "$\huge📊📉📈 Insights $"])
    df = pd.read_csv(r'Airbnb.csv')
    with tab1:
        st.header(":green[Click the below button to get the data]")
        bt=st.button('Get Data')
        if bt:
            data=extract()
            st.title(":blue[Raw Data from MongoDB]")
            st.write(data)
            csv =pd.read_csv(r'Airbnb.csv')
            data=csv.to_csv()
            st.download_button(
            label="Download data as CSV",
            data=data,
            file_name='Airbnb.csv',
            mime='text/csv',)

    with tab2:
        col1, col2 = st.columns([1, 1], gap='large')
        with col1:
            country = st.multiselect('Select a Country', sorted(df.country.unique()),sorted(df.country.unique()))
            prop = st.multiselect('Select Property_type', sorted(df.property_type.unique()),
                                          sorted(df.property_type.unique()))
        with col2:
            room = st.multiselect('Select Room_type', sorted(df.room_type.unique()),
                                          sorted(df.room_type.unique()))
            price = st.slider('Select Price', df.price.min(), df.price.max(), (df.price.min(), df.price.max()))

        query = f'country in {country} & room_type in {room} & property_type in {prop} & price >= {price[0]} & price <= {price[1]}'
        col1, col2 = st.columns(2, gap='medium')
        with col1:
            df1 = df.query(query).groupby(["property_type"]).size().reset_index(name="Listings").sort_values(
                by='Listings', ascending=False)[:10]
            image = px.bar(df1,
                         title='Top 10 Propety types',
                         x='Listings',
                         y='property_type',
                         orientation='h',
                         color='property_type',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(image, use_container_width=True)

            df2 = df.query(query).groupby(["host_location"]).size().reset_index(name="location").sort_values(by='location',ascending=False)[:10]
            image = px.bar(df2,
                         title='Top 10 Hosts Location with Highest number of Listings',
                         x='location',
                         y='host_location',
                         orientation='h',
                         color='host_location',
                         color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(image, use_container_width=True)

            df3 = df.query(query).groupby(["room_type"]).size().reset_index(name="counts")
            image = px.pie(df3,
                         title='Total Listings in each Room_types',
                         names='room_type',
                         values='counts',
                         color_discrete_sequence=px.colors.sequential.Agsunset
                         )
            image.update_traces(textposition='outside', textinfo='value+label')
            st.plotly_chart(image, use_container_width=True)

        with col2:
            country_df = df.query(query).groupby('country', as_index=False)['price'].mean()
            image = px.scatter_geo(data_frame=country_df,
                                 locations='country',
                                 color='price',
                                 hover_data=['price'],
                                 locationmode='country names',
                                 size='price',
                                 title='Avg Price in each Country',
                                 )
            st.plotly_chart(image, use_container_width=True)

            country_df1 = df.query(query).groupby('country', as_index=False)['rating'].mean()
            image = px.scatter_geo(data_frame=country_df1,
                                   locations='country',
                                   color='rating',
                                   hover_data=['rating'],
                                   locationmode='country names',
                                   size='rating',
                                   title='Avg rating in each Country',
                                   color_continuous_scale='agsunset'
                                   )
            st.plotly_chart(image, use_container_width=True)

