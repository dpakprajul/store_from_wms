from owslib.wms import WebMapService
import matplotlib.pyplot as plt

# Define the WMS service URL
wms_url = 'https://public-mapservice.lf.goteborg.se/geoserver/LF_Externwebb/wms'

# Connect to the WMS service
wms = WebMapService(wms_url)

# Define the layer to retrieve
layer_name = 'Alla_Skisser_LF'

# Define the coordinate reference system and bounding box
crs = 'EPSG:3857'
bbox = (1333596.8324914703,7915283.590014855,1333673.2695197554,7915360.027043146)

# Define the output image size
width = 256
height = 256

# Define the output image format
image_format = 'image/png'

# Build the request to retrieve the map image
map_request = wms.getmap(
    layers=[layer_name],
    srs=crs,
    bbox=bbox,
    size=(width, height),
    format=image_format
)

gml_request = wms.getfeature(
    typename=[layer_name],
    srsname=crs,
    bbox=bbox,
    outputformat=image_format
)

# Print the GML response
print(gml_request.read())
# Save the map image to a file
with open('D:\RID-master\RID-master\map.png', 'wb') as f:
    f.write(map_request.read())

# Display the map image using matplotlib
image = plt.imread('D:\RID-master\RID-master\map.png')
plt.imshow(image)
plt.axis('off')
plt.show()

