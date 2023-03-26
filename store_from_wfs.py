


import requests
import json

# Send GET request to the URL
url = "https://ip-api.mobidata-bw.de/v1/NVBW/geoserver/ows?service=wfs&version=2.0.0&request=GetFeature&typeName=bikesharingStations&outputFormat=application/json"
response = requests.get(url)

# Convert the JSON response to GeoJSON format
data = json.loads(response.content)
geojson = {
    "type": "FeatureCollection",
    "features": []
}
for feature in data["features"]:
    geojson["features"].append({
        "type": "Feature",
        "geometry": feature["geometry"],
        "properties": feature["properties"]
    })

# Print the GeoJSON output
print(json.dumps(geojson))

import geopandas as gpd

# Convert the JSON response to a GeoDataFrame
gdf = gpd.GeoDataFrame.from_features(data)
gdf.to_file("bikesharingStationsgeojson.geojson", driver="GeoJSON")
# Save the GeoDataFrame to a shapefile
gdf.to_file("bikesharingStations.shp")
