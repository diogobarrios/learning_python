import json
from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/mapping_global_data_sets/data/eq_data_30_day_m1.json'
with open(filename) as json_file:
    all_eq_data = json.load(json_file)


# Seeing what is needed from json file.
# readable_file = 'data/mapping_global_data_sets/data/readable_eq_data.json'
# with open(readable_file, 'w') as readable_json:
#    json.dump(all_eq_data, readable_json, indent=4)


# Making a List of all earthquakes.
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

# Extracting title of json_file
title = all_eq_data['metadata']['title']

# Extracting Magnitudes and Location Data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

# print(mags[:10])
# print(lons[:10])
# print(lats[:10])

# Building a World Map
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'}
    }
}]

my_layout = Layout(title=title)

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
