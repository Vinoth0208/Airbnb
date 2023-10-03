import pandas as pd
import plotly.express as px
import streamlit
def geovisuals():
    df = pd.read_csv(r'Airbnb.csv')
    location = px.choropleth(data_frame=df,
                             locations='country',
                             color='country',
                             hover_data={'price': True, 'rating': True, 'availability_365': True, 'property_type': True},
                             locationmode='country names')
    streamlit.header(":orange[Geo Visualization of Airbnb Data:]")
    location.update_layout(autosize=False,margin = dict(l=10, r=0, b=20,t=20,pad=9,autoexpand=True),width=1000,)
    streamlit.plotly_chart(location)
