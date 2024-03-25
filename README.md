# KfWs open geodata model
## About
Welcome! This is KfWs repository for storing the geodata model which can be used to collect project location sites and meta-information for KfW financed projects. 
The geodata model comes in form of an excel template which can be used to collect the data. 

**A guideline on how to collect this information is published and continously updated [here](https://openkfw.github.io/open-geodata-model/).**


## Available versions and versioning of the template. 
Please note, that the geodata template and the guidelines are living documents. We keep on advancing the model i.e. by extending the available IATI location codes. 
You might therefore find different versions of the template in this repository over time. We are also working hard to provide the template in different languages. 

## Open Data Kit / KoboToolbox Templates
In addition to the Excel Template named "Project_Location_Data_Template," we provide two other templates named "Project_Location_ODK_Template" for data collection using either [ODK](https://getodk.org/) or [KoboToolbox](https://www.kobotoolbox.org/). Therefore, all three templates adhere to the same configuration, encompassing identical required data points, such as types of locations etc.

## Some general remarks
Most of the technical specifications can be found in the RMMV Guidebook linked above, especifically in the document "Data Model and Data collection Guideline". 
This information is also given as comments in the Excel template if you click on the cells. Most importantly make sure to use WGS 84 as the coordinate reference system
when submitting locations in lat/long format. You might also collect proper geo-data in formats such as kml oder geojson (oder shapefile). If you send this information
together with the template it might help to verify the coordinates in the template. In addition it will be very usefull in cases where a project location is better 
represented by line or polygon geometries (e.g. protected areas or transimission lines). 

## More information on remote management methods
The datamodel is part of KfWs RMMV Initiative. You can find more information [here](https://www.kfw-entwicklungsbank.de/Service/Publications-Videos/Publications-by-topic/Digitalisation/RMMV-Guidebook/). You can also find sample terms of reference there if you require external assistance on collecting the data. 
