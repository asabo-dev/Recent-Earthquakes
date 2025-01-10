from pathlib import Path
import json

import plotly.express as px

# Read data as a string and convert to a Python object.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/recent_eq/eq_data_7_day_m1.geojson')
path.exists()
contents = path.read_text(encoding='utf-8')
eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('/Users/quanefiom/desktop/developer/python_work/chapters/chp16_Downloading_Data/recent_eq/readable_eq_data.geojson')
readable_contents = json.dumps(eq_data, indent=4)
path.write_text(readable_contents)

# Examine all earthquakes in the dataset.
eq_dicts = eq_data['features']

# Extract the magnitude and location data of each earthquake.
mags, lons, lats = [], [], []
for eq_dict in eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Extract the title of the dataset.
title = eq_data['metadata']['title']

# Map the earthquakes.
fig = px.scatter_geo(lon=lons, lat=lats, size=mags, title=title, color=mags, color_continuous_scale='Viridis', labels={'color': 'Magnitude'}, projection='natural earth',)
fig.show()

# The code above reads the data from a file containing the most recent earthquake data, and then creates a map of the earthquakes.