import sys

from matplotlib import pyplot as plt

from Explore import explore
from Geovisualization import geovisuals
from PlottingandCharts import plotsandcharts

sys.path.insert(1, r'C:\Users\Vinoth\PycharmProjects\Airbnb\venv\Lib\site-packages')
import streamlit_option_menu
import streamlit as st
st.set_page_config(layout="wide",page_title="Airbnb Analysis")


selected = streamlit_option_menu.option_menu("Menu", ["About", "Exploration","Plots and Charts", "GeoVisualization", 'Contact'],
                                                 icons=["exclamation-circle","search","bar-chart","globe",'telephone-forward' ],
                                                 menu_icon= "menu-button-wide",
                                                 default_index=0,
                                                 orientation="horizontal",
                                                 styles={"nav-link": {"font-size": "15px", "text-align": "centre",  "--hover-color": "#d1798e"},
                        "nav-link-selected": {"background-color": "#b30e35"}})
if selected=='About':
    st.title(':violet[Project Title: Airbnb Analysis]')
    st.header(':red[Technologies used:]')
    st.subheader(':white[Python scripting, Data Preprocessing, Visualization, EDA, Streamlit, MongoDb, PowerBI or Tableau ]')
    st.header(':orange[Domain:]')
    st.subheader('Travel Industry, Property Management and Tourism')
    st.title(":green[About Application]")
    st.markdown('''As an Airbnb host or potential host, you may have wondered about the factors that affect rental prices and occupancy rates on the platform. By analyzing Airbnb data, we can gain insights into these trends and make data-driven decisions to maximize your earning potential.
One key aspect to consider is the location of your property. By examining data from different neighborhoods or cities, we can determine which areas have higher demand and corresponding higher prices. For example, properties near popular tourist attractions, city centers, or major transportation hubs tend to have higher occupancy rates and rental prices.

Another factor that influences rental prices is the type of property you offer. By analyzing data on different accommodation types, such as entire homes, private rooms, or shared spaces, you can identify which options are in higher demand and can potentially fetch higher prices. Understanding the preferences of Airbnb users can guide your decision-making and help you optimize your listing.

Additionally, analyzing historical booking data can provide insights into seasonal demand patterns. By examining trends across different months or even specific events or holidays, you can determine the optimal time to list your property and adjust prices accordingly. This can help maximize your rental income and achieve higher occupancy rates throughout the year.

Moreover, guest reviews play a crucial role in attracting potential guests. Analyzing review data can provide insights into the factors that contribute to positive guest experiences, such as cleanliness, responsiveness, and amenities. Understanding these preferences can help you improve your listing and enhance guest satisfaction, leading to positive reviews and increased bookings.

Lastly, analyzing data on similar listings in your area can help you set competitive prices. By examining the rental prices and occupancy rates of comparable properties, you can ensure that your listing is competitive and attractive to potential guests.

In conclusion, analyzing Airbnb data can provide valuable insights into various factors that affect rental prices and occupancy rates. By leveraging this data, hosts can make informed decisions to optimize their listings, maximize earning potential, and provide exceptional guest experiences.''')

    st.title(":green[Sample image of power bi dashboard]")
    st.image('Powerbi Dashboard.JPG')

if selected=='Exploration':
    explore()
if selected=='Plots and Charts':
    plotsandcharts()
if selected=='GeoVisualization':
    geovisuals()
if selected=='Contact':
    col1, col2=st.columns([0.5,1.5], gap='small')
    with col2:
        st.subheader("Name: :green[Vinoth Palanivel]")
        st.write("Degree: :green[Bachelor of Engineering in Electrical and Electronics Engineering]")
        st.write("E-mail: :green[vinothchennai97@gmail.com]")
        st.write("Mobile: :green[7904197698 or 9677112815]")
        st.write("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
        st.write("Github: :orange[https://github.com/Vinoth0208/]")
        st.write("Project links:")
        st.write("1. https://github.com/Vinoth0208/Youtube_Project_For_DataScience")
        st.write("2. https://github.com/Vinoth0208/PhonepePulse")
        st.write("3. https://github.com/Vinoth0208/Bizcard")
