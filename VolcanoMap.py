import folium
import pandas
import markerfactory
import populationlayer

volcano_df = pandas.read_csv("volcanoes-USA.txt")
map_center = [volcano_df["LAT"].mean(), volcano_df["LON"].mean()]

map = folium.Map(location = map_center, zoom_start = 6, tiles = "Stamen Terrain")

minimum = int(min(volcano_df['ELEV']))
step = int((max(volcano_df['ELEV']) - minimum)/3)

fg = folium.FeatureGroup(name="Volcano Locations")
for lat, lng, name, elevation in zip(volcano_df["LAT"], volcano_df["LON"], volcano_df["NAME"], volcano_df["ELEV"]):

    marker = markerfactory.make(lat, lng, name, elevation, minimum, step)
    marker.add_to(fg)

fg.add_to(map)

population_layer = populationlayer.create()
population_layer.add_to(map)

folium.LayerControl().add_to(map)

map.save(outfile = "generated_volcano_map.html")
