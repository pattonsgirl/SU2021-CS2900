import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# note that here we needed to set the encoding
with open("eq-0616-30days.json", "r", encoding='utf-8') as f:
    contents = json.load(f)

earthquakes = contents["features"]
mags, lats, lons, titles = [], [], [], []
for earthquake in earthquakes:
    mags.append(earthquake["properties"]['mag'])
    lons.append(earthquake["geometry"]["coordinates"][0])
    lats.append(earthquake["geometry"]["coordinates"][1])
    titles.append(earthquake["properties"]["place"])

data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': titles,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {
            'title': 'Magnitude'
        }
    },
}]

figure_layout = Layout(title='Global Earthquakes')

fig = {
    'data': data, 
    'layout': figure_layout
}

offline.plot(fig, filename='global_eqs.html')
