import folium

def create():
    return folium.GeoJson(data = open("world_population.json"),\
        name = "World Population",\
        style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] <= 10000000 else 'orange' if 10000000 < x['properties']['POP2005'] < 20000000 else 'red'})
