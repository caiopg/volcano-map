import folium

def make(lat, lng, popup, elevation, minimum, step):
    icon = createIcon(elevation, minimum, step)
    location = [lat, lng]

    marker = folium.Marker(location = location, popup = popup, icon = icon)

    return marker


def createIcon(elevation, minimum, step):
    if elevation in range(minimum, minimum+step):
        icon = folium.Icon(color = "green")
    elif elevation in range (minimum+step, minimum+2*step):
        icon = folium.Icon(color = "orange")
    else:
        icon = folium.Icon(color = "red")

    return icon
