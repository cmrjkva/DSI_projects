import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
from scipy.stats import linregress
import sqlite3
from urllib.request import urlopen
import json
import plotly.express as px
import plotly.graph_objects as go
from mpl_toolkits.basemap import Basemap
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
# %config InlineBackend.figure_format = 'retina'

# Imports
#------------------------------------------------
# Page configuration
st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

st.title('Fires in the Western United States')

st.write('Use the sidebar to select a page to view.')

page = st.sidebar.selectbox(
    'Page',
    ('Home', 'Map')
)

#------------------------------------------------------------
#Bringing in the data and the function for the plot

@st.cache(persist = True)
def load_data():
        #reading in fire data with coordinates
    fire_position_input = pd.read_csv('./data/fire_lat_lon.csv', index_col=False)
        #mapping classes to numeric values
    fire_position_input['fire_size_class'] = fire_position_input['fire_size_class'].map({
                                                                'A': int(1),'B': int(2),
                                                                "C": int(3),"D": int(4),
                                                                "E": int(5),"F": int(6),
                                                                "G": int(7)})
    return fire_position_input

# Function for the map!
# Creating a function to take in month and year and create a plot of all the fires of that month,
# color cordinated by their size.
def fires_month_year(month, year):
    fire_position = fire_position_input[fire_position_input['year'] == year]
    fire_position = fire_position[fire_position['month'] == month]
    fire_position.reset_index(inplace=True)

    # Grabbing the lats and longs data
    lats = []
    lons = []
    fire_class_list = []
    for i in fire_position.index:
        lats.append(fire_position['latitude'][i])
        lons.append(fire_position['longitude'][i])
        fire_class_list.append(float(fire_position['fire_size_class'][i]))

    # found this out on
    # https://makersportal.com/blog/2018/7/20/geographic-mapping-from-a-csv-file-using-python-and-basemap

    # setting parameters for title and axes
    font = {'family' : 'tahoma',
            'size'   : 12}
    plt.rc('font', **font)

    # How much to zoom from coordinates (in degrees)
    zoom_scale = 3

    # Setup the bounding box for the zoom and bounds of the map
    bbox = [np.min(lats)-zoom_scale,np.max(lats)+zoom_scale,\
            np.min(lons)-zoom_scale,np.max(lons)+zoom_scale]

    fig, ax = plt.subplots(figsize=(16,7))

    # Define the projection, scale, the corners of the map, and the resolution.
    m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
                llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i')

    # Draw coastlines and fill continents and water with color
    m.drawcoastlines()
    m.fillcontinents(color='#CCCCCC',lake_color='lightblue')

    # draw parallels, meridians, and color boundaries
    m.drawparallels(np.arange(bbox[0],bbox[1],(bbox[1]-bbox[0])/5),labels=[1,0,0,0])
    m.drawmeridians(np.arange(bbox[2],bbox[3],(bbox[3]-bbox[2])/5),labels=[0,0,0,1],rotation=0)
    m.drawmapboundary(fill_color='lightblue')

    # format colors for fire size by class
    cmap = plt.get_cmap('hot_r')
    normalize = matplotlib.colors.Normalize(vmin=1, vmax=7) # 1 corresponds to small fires (class A), 7 - large ones (G)


    for ii in range(0, len(fire_class_list)):
        x,y = m(lons[ii],lats[ii])
        color_interp = np.interp(fire_class_list[ii],[1, 7],[10,300])
        plt.plot(x,y,marker='o',markersize=2,color=cmap(int(color_interp)))

    # formating the color bar
    cax, _ = matplotlib.colorbar.make_axes(ax)
    cbar = matplotlib.colorbar.ColorbarBase(cax, cmap=cmap,norm=normalize,label='Fire Size')

    # save the figure and show it
    plt.title("Fires in Western US states")

    st.write(f'Number of fires started during {month}/{year} : {len(fire_position)}.')
    st.write(f'large fires : {len(fire_position[fire_position["fire_size_class"] >4])} ')
    st.write(f'medium fire : {len(fire_position[(fire_position["fire_size_class"] > 2) & (fire_position["fire_size_class"]< 5)])}')
    st.write(f'small fires : {len(fire_position[fire_position["fire_size_class"] < 3])}')
    return fig


#-------------------------------------------------------
# More Page configuration

if page == 'Home':
    st.subheader('Home Page')
    st.write('Hello, welcome our fire dataset visualization!')

if page == 'Map':
    # header
    st.subheader('Fire by month')
    st.write('''Input the month and year and you'll see how many fires
    started in the western United States.''')

    # get user input
    month = st.slider("Select the Month", 1, 12)
    st.text('Selected: {}'.format(month))
    year = st.slider("Select the Year", 1992, 2015)
    st.text('Selected: {}'.format(year))

    # run the plotting function.
    fire_position_input = load_data()
    st.pyplot(fires_month_year(month, year))
