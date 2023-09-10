# WMS Map Image Retrieval and GeoJSON Conversion

This repository contains Python scripts for retrieving map images from a Web Map Service (WMS) and converting the geographical data to GeoJSON format. It is particularly useful for accessing map data from web services and working with geospatial data in your projects.

## Data Source

The scripts in this repository are designed to work with specific data sources. Here is information about the data source used in the provided scripts:

**WMS Map Image Retrieval**

The first script, `wms_map_image.py`, demonstrates how to retrieve a map image from a Web Map Service. In this example, we use the following data source:

- WMS Service URL: [https://public-mapservice.lf.goteborg.se/geoserver/LF_Externwebb/wms](https://public-mapservice.lf.goteborg.se/geoserver/LF_Externwebb/wms)
- Layer Name: 'Alla_Skisser_LF'
- Coordinate Reference System (CRS): EPSG:3857
- Bounding Box (Bbox): (1333596.8324914703,7915283.590014855,1333673.2695197554,7915360.027043146)
- Output Image Size: 256x256 pixels
- Output Image Format: image/png

## WMS Map Image Retrieval

The first script, `wms_map_image.py`, demonstrates how to retrieve a map image from a Web Map Service. In this example, we use the following data source:

![map](https://github.com/dpakprajul/store_from_wms/assets/38970123/5364e8d3-6bb2-4d9d-8e8f-ffe54d4b9d99)

- WMS Service URL: [https://public-mapservice.lf.goteborg.se/geoserver/LF_Externwebb/wms](https://public-mapservice.lf.goteborg.se/geoserver/LF_Externwebb/wms)
- Layer Name: 'Alla_Skisser_LF'
- Coordinate Reference System (CRS): EPSG:3857
- Bounding Box (Bbox): (1333596.8324914703,7915283.590014855,1333673.2695197554,7915360.027043146)
- Output Image Size: 256x256 pixels
- Output Image Format: image/png


**GeoJSON Conversion from Web Service**

The second script, `geojson_conversion.py`, sends a GET request to a specific URL to retrieve geographical data in JSON format. The data source used in this script is as follows:

- URL: [https://ip-api.mobidata-bw.de/v1/NVBW/geoserver/ows?service=wfs&version=2.0.0&request=GetFeature&typeName=bikesharingStations&outputFormat=application/json](https://ip-api.mobidata-bw.de/v1/NVBW/geoserver/ows?service=wfs&version=2.0.0&request=GetFeature&typeName=bikesharingStations&outputFormat=application/json)

## WMS Map Image Retrieval

The `wms_map_image.py` script demonstrates how to retrieve a map image from a WMS service using the `owslib` library. It includes the following key steps:

1. Define the WMS service URL.
2. Connect to the WMS service.
3. Specify the layer to retrieve.
4. Define the coordinate reference system and bounding box.
5. Specify the output image size and format.
6. Build the request to retrieve the map image.
7. Save the map image to a file.
8. Display the map image using Matplotlib.

## GeoJSON Conversion from Web Service

The `geojson_conversion.py` script showcases how to send a GET request to a URL, retrieve geographical data in JSON format, and convert it to GeoJSON format using the `requests`, `json`, and `geopandas` libraries. The main steps include:

1. Send a GET request to the specified URL.
2. Convert the JSON response to GeoJSON format.
3. Print the GeoJSON output.
4. Convert the GeoJSON data to a GeoDataFrame using Geopandas.
5. Save the GeoDataFrame to both GeoJSON and shapefile formats.

Feel free to use and modify these scripts for your own projects involving WMS services and geospatial data conversion.

**Note:** Make sure to install the required libraries (`owslib`, `matplotlib`, `requests`, `json`, `geopandas`) before running the scripts. You can typically install these libraries using `pip`.
