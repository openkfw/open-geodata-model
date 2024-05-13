---

# Technical Notes on the Project Location Model

!!! note

    You can find the current version of the projection location data collection template [here](https://raw.githubusercontent.com/openkfw/open-geodata-model/main/Project_Location_Data_Template_V02.xlsx).

## Mandatory and Non-Mandatory Fields

The data to be collected are subject to minimum requirements in the form of mandatory fields, and there are non-mandatory fields that can be used for collecting additional site-specific information. Please check if *project location data collection ToRs* exist which specify additionally required fields. If no ToRs exist, please refer to your KfW counterpart which non-mandatory fields to fill.

## What is a project location?

**A project location can consist of one or more features that are part of a financially supported activity where no further geographical discrimination regarding funding is possible.** An example of a single-feature project location is a financially supported hospital in a specific location. An example of a project location with multiple features is a group of adjacent agricultural plots under a financed irrigation plan that benefits all producers in that area. Another example is a set of protected areas jointly financed from a fund if, and only if, further geographical discrimination as to the allocation of funds to specific areas is not possible. If discrimination is possible, data for multiple project locations (such as protected areas) and their financial allocation have to be collected. KfW highly encourages increasing geographical discrimination of financial flows to specific project locations to the maximum possible, as this creates greater aid transparency and financial accountability.

## Exact locations and how to collect them

A project location can be either exact or approximate[^1]. The exact location designates the geographical end point of an international development assistance financial flow. In case you already know your exact location coordinates, you may state them as “exact” locations. This form allows you to collect single location points (e.g., one power plant site) or a larger number of project sites and features (e.g., 300 locations of buildings in different sectors within the framework of a decentralization project). In addition, project sites with larger areas and more complex geometries (e.g., polygons of forest protection areas) or linear location types like roads or railways are supported as well but have to be submitted in KML.  

'Exact[^1] locations' can have three different geometry types:

1.  **Point** geometries (e.g., a well or a hospital)

2.  **Line** geometries (e.g., a road or transmission line)

3.  **Polygon** geometries (e.g., a protected area or agricultural plots)

Independent of the geometry type all project locations should be collected first as a point location the Excel Template. This point may represent the locaction itself or a gateway to the project site, irrespective of the actual feature geometry (i.e., also for lines and polygons). The gateway point may be e.g. the beginning of a road, a village adjacent to agricultural plots or the administration building of a protected area.  If there is a line or polygon geometry and no gateway/entry point can be defined, the geometrical center (centroid) may be used as well. 

[^1]: in the sense of the IATI- Standard

**All coordinates in Excel are to be collected using WGS 84 (EPSG 4326) as the coordinate reference system.**[^3] WGS 84 is the de-facto standard for web mapping applications. Geo-coordinates are to be provided in the decimal place format 00.00000 in the order LONG, LAT (using at least 5 digits after the separator).

[^3]: World Geodetic System 1984 (https://support.virtual-surveyor.com/en/support/solutions/articles/1000261351-what-is-wgs84\)

**For line and polygon geometries:** If you have line or polygon geometries, you need to use both, the Excel template to store all relevant metadata for each location and an additional KML file to store the associated geometries to each location. The Excel file contains two columns that will enable us to to link the geometries with the metadata in Excel. The columns are called "Filename of additional Geo-data submitted as KML" and "Primary Key (As provided in the KML file). The first column should be used to put the filename of the KML which you send to KfW. An example for the filename is "00345_Ouagadougou.kml". The second column should contain a "primary key" that has to be also present in the attribute table of your KML file and links the geometry to the metadata in Excel. You have to name the column "primary key" in KML as well. Use whole numbers (integers) to construct the primary key. In Excel you may also provide a "gateway point" (for details see section "Geometrical characteristics of exact locations"). This point can help us to verify whether the link between the information in KML and Excel is correct. You have to submit all locations for your project in a single KML file. 

It is highly encouraged to check the data before submission in GIS software, such as QGIS or Google Earth Pro. This reduces the need to go back and forth between the responsible KfW counterparts and the project staff.

[^2]: KML (KMZ) is an open XML Standard for Points, Lines and Shapes. Officially named the OpenGIS KML Encoding Standard (OGC KML). It is maintained by the Open Geospatial Consortium, Inc. (OGC). Other Geoformats (e.g., Shapefiles or Geojson) can usually be converted to KML in Standard Geographic Information System (GIS) Software such as ArcGIS or QGIS.

## Approximate locations

The approximate location option [^1]: should be chosen if one or more of the following circumstances apply: 
1. **an exact project location has not (yet) been specified or is not yet known** (e.g. the exact project locations have not yet been determined) -> then choose option: approximate (yet unknown)

2. **an exact project location is not to be collected or communicated due to security reasons** (e.g. in a conflict zone) -> then choose option: approximate (security)

3. **the target location(s) is/are one or more administrative units**, e.g. a district, a province or the entire country or group of countries (e.g. an entire country for a Policy-Based-Lending project or a number of districts in a country for a decentralization project)
   --> then choose option: approximate (admin unit)
   
In case of security risks (e.g., zones of conflict), we strongly recommend only publishing approximate locations!
Approximate locations can be given either using point or polygon data. You may use e.g. administrative areas from existing databases. 

## Figures
<figure markdown>
  ![Figure 1](images/Figure1.png)
  <figcaption>Figure 1: Schematic Representation of Different Location Data for the GeoApp</figcaption>
</figure>

## What is a Location Type?
 
This template follows as closely as possible the International Aid Transparency Initiative IATI standard, but we saw the need to create additional location types, since those already existing in the IATI Standard would not allow us to cover all Financial Cooperation project types. This allows the aggregation of information amongst multiple location types. In case you cannot find a specific location type, please use the most similar location type, e.g., "well" for an "extraction well". You can then add additional information on the location type e.g., "extraction well" under "additional location types", if deemed necessary. 

In our new location type list, you find the IATI location types that are useful for International Development plus additional location types for all sectors that were missing in the existing IATI-list. We therefore created 197 new project location types, including “immaterial” ones like Capacity Development / Training or Voucher Schemes, that cannot be plotted according to any physical feature on a map, but can defined by the area covered by them. We therefore also adapted the definition of “location type” as “project output- or intervention-related type of physical location or immaterial output- or intervention area”.  See also list of Location Types in the Excel Template. Definitions for the original IATI-based location types can be found [here](https://iatistandard.org/en/iati-standard/203/codelists/locationtype/). A comprehensive list of all location types can be found in the Excel Template. 

After preselecting the KC Theme/Sub-Sector, choose the most appropriate location type, see table sheet "Location Types". If there is no fit, please select "other physical" or "other immaterial" and fill out the next column "Alternative Location Type".  In case you need/want to mention two different location types (e.g. school and capacity development) at the same GPS-Coordinate, you may just create two separate two rows for these location types with the different activity descriptions and DAC/CRS-Codes at the same GPS coordinates. 

**Please note that the preselection column "KC Theme/Sub-Sector" only serves to quickly find the correct location type name!** It will not be saved in the system and it does not replace the DAC5 Purpose Classification/CRS-Code assignment below, which effectivley serves to assign the correct subsector to each location!

## DAC 5 Purpose Classification/CRS-Code

The (one to four) five-digit DAC 5 Purpose Codes for the entire project have to be provided by your KfW counterpart (ideally in the project location data collection ToR, see samples here). 

In case there is more than one code for the project, you have to assign the correct code to each location. For example, in a decentralization project, the construction of primary school locations is to be assigned to the respective Basic Education DAC 5-Code, while road rehabilitation sites within the same project are to be assigned to the respective Transport DAC 5-Code. 
In case your project contains locations which contribute not only to one, but two, three or four DAC/CRS-Codes, please create two, three or four separate rows with the same GPS-Coordinates, but different DAC/CRS-Codes, and potentially different location types and activity descriptions.

In case all codes have to be assigned to all locations, then please create a new row for each location, with the only difference being the DAC 5 Purpose Classification. For the complete list of codes, see table sheet "DAC Purpose Codes" of the Excel Template.

## Privacy, confidentiality and publication
 
The Excel Template has to be submitted without containing any personal data or any data that could be linked to individual persons, such as houses of private households. Please note, that KfW does not publish any exact coordinates of its project locations. Location data collection in fragile and conflict contexts should be treated with extra diligence. 

----------------------------------------------------------------------------------------------------------------------

## The Project Location Model

Below, the required project location data is defined for all FC projects. 

### Table 1: The KfW Project Location Model for Financial Cooperation


| **Name** | **Type of data** |  **Mandatory**  | **Asignment** | **Description** | 
| ---------:| ----------------:| ---------------:| --------------:| --------------:|
| A. Unique ID | Number |Filled out by KfW | Per location | For new locations, this column will be empty. For updates, your KfW counterpart will provide you with the list of unique_id numbers in this file to ensure that updated location ids match with the former ones.|
| B. KfW project No. (INPRO) | Number   |Yes| Per location | Every project location in the FC Geodata Model must be assigned to its respective KfW project number that is being provided by KfW in the geodata collection ToR > Annex 3.2 |
| C. Abbreviation of project name (project acronym) | Text     | No | Per location | Please enter here the acronym used for the name/title of the project (e.g. HREII) to be visible on your map. If the project has multiple phases, please add the number of the phase belonging to the before-stated KfW Project-No. |
| D. Data Owner (Institution Name) |Text  |Yes| Per location | Legal Entity who owns the data provided here (= legal authorship) |
| E. Publishing restrictions due to security reasons | Select Text (yes/no)  | Yes  | Per location | Indicates if this information is collected in fragile regions (e.g. areas of severe civil conflict or war) and should therefore be ommited from publicly available reports.
| F. Date of data collection or latest update   | Date YYYY-MM-DD (Date format - English/US)  |No| Per location | Date of data collection or latest update (if date of data collection is unknown). In case only the year is available please choose the 1st of january e.g. 2022-01-01 |
| G. Project-specific location identifier  | Text     |No| Per location | In case the location or activity has a project-specific identifier (e.g., a location code in the MIS of the source Agency, e.g. Project Executing Agency(PEA)) or an identifier in a public database like GADM,  it can be entered here. |
| H. Location name |Text  |Yes| Per location | Short name of the project site ideally containing a summary of the main project activity and the location name (max. 40 characters or digits) |
| I. Location activity status  | Select Text    | No | Per location | The location activity status according to the IATI standard. If you are unaware of the current status please choose "NA". |
| J. Planned or actual start date of activity at the location   | Date  YYYY-MM-DD (Date format - English/US)  | Yes | Per location | Aprox. planned or actual start date of implementation of activities on the ground. This can be e.g. the date when construction work is planned to begin. For no information enter 2100-01-01. Ideally, the start of project implementation is defined in the geodata collection ToR > Annex 3.2 |
| K. Planned or actual end date of activity at the location   | Date  YYYY-MM-DD (Date format - English/US)  | Yes | Per location | Aprox. planned or actual end date of activities on the ground. This can be e.g. the date when the project is planned to cease implementation activities. For no information enter 2100-01-01.  |
| L. Activity-Description (general)  | Text | Yes |Per location | A short description of the main project activity in this location, e.g., hydropower plant construction or construction of small irrigation systems. |
| M. Additional activity description  | Text | No | Per location | Free text (in case you need to add other location–specific information like production volumes, progress values or a tag like “COVID-19”). Please consult your KfW counterpart if additional information is required. |
| N. KC Theme / Sub-Sector | Select Text | Yes | Per location | Sectoral / cross-sectoral location type preselection field, see table sheets "Location Types" & KC Themes. If there is no fit,  select "other physical or other immaterial and fill out the column "Alternative Location Type". |
| O. Location Type Name | Select Text     | Yes | Per location | After selecting the KC Theme/Sub-Sector, choose the most appropriate location type, see table sheet "Location Types". If there is no fit, please select "other physical" or "other immaterial" and fill out the next column "Alternative Location Type".  |
| P. Alternative Location Type Name  | Text    | No | Per location | If you selected "other physical or other immaterial " in the column "Location Type Name", please propose your own location type name. This promotes systemic learning, allows us to identify additionally required location types and will help us to propose a comprehensive IATI standard extension in the future. |
| Q. DAC 5 Purpose Classification /CRS-Code   |Text  | Yes | Per location | The DAC 5 Purpose Codes (one to four) for the entire project have to be provided in the ToR or by your KfW counterpart, see notes above. |
| R. Budget share | Currency number in EUR    | No | Per location | The budget share allocated to this location in €. The sum of all locations in a project should add up to the budget sum in Inpro/PMT including overheads. Data from private partners/PEA must not be entered here! |
| S. Geographic exactness | Select Text | Yes | Per location | Use "exact", if you know the geographically exact end destination of a financial flow & it is not an administrative unit & if you don't face security restrictions to do so. If not, use the resp. type "approximate".   |
| T. Latitude | Decimal Number    | Yes | Per location | Enter the Latitude measured with a GPS device (or centroid for approximate locations). Make sure to use WGS 84 as the Coordinate Reference System (EPSG:4326). Enter Values with at least FIVE digits. Example: 50.12018514689011. |
| U. Longitude | Decimal Number    | Yes | Per location | Enter the Longitude measured with a GPS device (or centroid for approximate locations) here. Make sure to use WGS 84 as the Coordinate Reference System (EPSG:4326). Enter Values with at least FIVE digits. Example: 8.655474047059236  |
| V. Related Community / Village / Neighborhood | Decimal Number    | No | Per location | You may enter a village, hamlet or neighborhood name that relates to this location. This can serve to manually add smaller community resp. administrative unit names not identified in existing global coordinates lists. |
| W. Filename of additional Geo-data submitted as KML (Lines/Polygons) | Text    | Yes, if kmldata is provided | Per location | A string of the KML file where the associated geometry information is found. Note, to link an entry from this excel to the KML file, it is required to correctly fill in the Primary Key column.  |
| X. Primary Key (as provided in KML file) | Decimal Number    | Yes, if kmldata is provided | Per location | Required only in case you provide additonal geolocation information in another KML file. The geometry in the KML file should possess the same primary key as an attribute as it is listed here. |

----------------------------------------------------------------------------------------------------------------------

## Additional notes on selected fields from the model
### A unique ID for each project location

Every project location in the Project Location Model has to receive a unique location identifier number by KfW. For new locations, this column will be empty. For updates, your KfW counterpart will provide you with the list of unique_id numbers in this file to ensure that updated location ids match with the former ones. Please use the IDs provided to you by your KfW focal point from then onwards.

### Publishing restrictions due to security reasons
Indicates if this information is collected in fragile regions (e.g. areas of severe civil conflict or war) and should therefore be ommited from publicly available reports. In fragile contexts, geolocation information must be protected and is not to be published.

### Project-specific location identifier	

If the location or activity has a project-specific identifier, e.g., a location code in the MIS of the PEA, this can be entered here. This enables logically connecting and comparing the location/activity in the KfW–system against the location/activity in the PEA-system. Otherwise the identifier is generated automatically (= Unique ID mentioned above).

### Budget Share

The budget share allocated to this location in €. The sum of all locations in a project should add up to the official budget sum including overheads. Data from private partners/PEA must not be entered here! If the budget shares of all locations are to be provided, the budget sum will be provided by the KfW counterpart in the project location data collection ToR.
