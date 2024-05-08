---
comments: true
---

# Technical Notes on the project location model

!!! note

    You can find the current version of the projection location data collection template [here](https://raw.githubusercontent.com/openkfw/open-geodata-model/main/Project_Location_Data_Template_V02.xlsx).

## What is a project location?

**A project location can consist of one or more features that are part of a financially supported activity where no further geographical discrimination regarding funding is possible.** An example of a single-feature project location is a financially supported hospital in a specific location. An example of a project location with multiple features is a group of adjacent agricultural plots under a financed irrigation plan that benefits all producers in that area. Another example is a set of protected areas jointly financed from a fund if, and only if, further geographical discrimination as to the allocation of funds to specific areas is not possible. If discrimination is possible, data for multiple project locations (such as protected areas) and their financial allocation have to be collected. KfW highly encourages increasing geographical discrimination of financial flows to specific project locations to the maximum possible, as this affords greater aid transparency and financial accountability.

## Difference between exact and approximate locations

A project location can be either exact[^1] or approximate. The exact location designates the geographical end point of an international development assistance financial flow. Approximate locations should be used, however, if either of the following applies: 
1. no exact geoinformation is (yet) available,
2. project location data is not collected due to security reasons
3. The target area of a project is an administrative unit.

Approximate locations can be given either using point, lines or polygon data. You may use e.g. administrative areas from existing databases. 


[^1]: in the sense of the IATI- Standard

## Exact locations and how to collect them

'Exact[^1] locations' can have three different geometry types:

1.  Point geometries (e.g., a well or a hospital)

2.  Line geometries (e.g., a road or transmission line)

3.  Polygon geometries (e.g., a protected area or agricultural plots)

Independent of the geometry type all project locations should be collected first as a point location the Excel Template. This point may represent the locaction itself or a gateway to the project site, irrespective of the actual feature geometry (i.e., also for lines and polygons). The gateway point may be e.g. the beginning of a road, a village adjacent to agricultural plots or the administration building of a protected area.  If there is a line or polygon geometry and no gateway/entry point can be defined, the geometrical center (centroid) may be used as well. 

**All coordinates in Excel are to be collected using WGS 84 (EPSG 4326) as the coordinate reference system.**[^3] WGS 84 is the de-facto standard for web mapping applications. Geo-coordinates are to be provided in the decimal place format 00.00000 in the order LONG, LAT (using at least 5 digits after the separator).

[^3]: World Geodetic System 1984 (https://support.virtual-surveyor.com/en/support/solutions/articles/1000261351-what-is-wgs84\)

**For line and polygon geometries:** If you have line or polygon geometries, you need to use both, the Excel template to store all relevant metadata for each location and an additional KML file to store the associated geometries to each location. The Excel file contains two columns that will enable us to to link the geometries with the metadata in Excel. The columns are called "Filename of additional Geo-data submitted as KML" and "Primary Key (As provided in the KML file). The first column should be used to put the filename of the KML which you send to KfW. An example for the filename is "00345_Ouagadougou.kml". The second column should contain a "primary key" that has to be also present in the attribute table of your KML file and links the geometry to the metadata in Excel. You should name the column "primary key" in KML as well. Use whole numbers (integers) to construct the primary key. In Excel you may also provide a "gateway point" (for details see section "Geometrical characteristics of exact locations"). This point can help us to verify whether the link between the information in KML and Excel is correct. You should submit all locations for your project in a single KML file. 

It is highly encouraged to check the data before submission in GIS software, such as QGIS or Google Earth Pro. This reduces the need to go back and forth between the responsible KfW counterparts and the project staff.

[^2]: KML (KMZ) is an open XML Standard for Points, Lines and Shapes. Officially named the OpenGIS KML Encoding Standard (OGC KML). It is maintained by the Open Geospatial Consortium, Inc. (OGC). Other Geoformats (e.g., Shapefiles or Geojson) can usually be converted to KML in Standard Geographic Information System (GIS) Software such as ArcGIS or QGIS.

## When to use approximate locations

Approximate[^1] locations should be used when no exact geoinformation is available (yet), or when exact location information should not be collected or communicated, or when the target area is an administrative unit. The approximate location option should be chosen if one or more of the following circumstances apply:

-   an exact project location has not (yet) been specified or is not yet known -> then choose option: *approximate (yet unknown)*

-   an exact project location is not to be collected or communicated due to security reasons -> then choose option: *approximate (security)*   

-   the target location(s) is/are one or more administrative units, e.g. a district, a province or the entire country -> then choose option: *approximate (admin unit)*   

## Figures
<figure markdown>
  ![Figure 1](images/Figure1.png)
  <figcaption>Figure 1: Schematic Representation of Different Location Data for the GeoApp</figcaption>
</figure>

<figure markdown>
  ![Figure 2](images/Figure2.png)
  <figcaption>Figure 2: How to Collect Project Location Data</figcaption>
</figure>


<figure markdown>
  ![Figure 3](images/Figure3.png)
  <figcaption>Figure 3: How to Upload Which Type of Location Data?</figcaption>
</figure>

## The project location model

Below, the required project location data is defined for all FC projects. Project-related data is usually provided from both internal and external sources. The external data (see column "Source" with field entry "Input") has to be provided by the PEA or consultant staff using the template(s) provided by KfW and be validated by the responsible KfW PM/analyst before uploading.

#### Table 2: The KfW Project Location Geodata Model for Financial Cooperation

| **Name** | **Type of data** | **Source**      |  **Mandatory**  | **Asignment** | **Description** | 
| ---------|:----------------:| ---------------:| ---------------:| --------------:| --------------:|
| 1. Unique ID | Number | Input  | Given | Per location | Every project location in the FC Geodata Model has to receive a unique location identifier number. This is the unique location identifier that is already provided in the Excel template in the Sub-Annex of the geodata collection ToR >Annex 3.2|
| 2. KfW project No. (INPRO) | Number | Input  |Yes| Per location | Every project location in the FC Geodata Model must be assigned to its respective KfW project number that is being provided by KfW in the geodata collection ToR > Annex 3.2 |
| 3. Project-specific location identifier  | Text    | Selection |No| Per location | If the location or activity has a project-specific identifier, e.g., a location code in the MIS of the PEA, this can be entered here. This enables logically connecting and comparing the  location/activity in the KfW–system against the location/activity in the PEA-system. Otherwise the identifier is generated automatically (= No. 1 Unique ID in this table)|
| 4. Location name |Text | Input |Yes| Per location | Short summary of the main project activity (max. 12 characters or digits)
| 5. Author of the data (=the legal owner) |Text | Input|Yes| Per location | Person and/or Legal Entity who collected the data (= legal authorship)
| 6. Publishing restrictions due to security reasons | Select Text (yes/no) | Input | Yes  | Per location | In fragile contexts, geolocation information must be protected and may not be published, for example in online maps, public ESIA or evaluation reports for security reasons (e.g., risk of conflict, repression/discrimination or terrorist attack) in the target area(s) |
| 7. Date of data collection or latest update   | Date | Input |No| Per location | Date of data collection or latest update (if date of data collection is unknown) Form: DD.MM.YYYY (numbers only) |
| 8. Location activity status  | Select Text  | Input  |Yes| Per location | As per IATI–Standard, see List of Activity Status options in the Excel–Template. Updates are only mandatory annually at the time of annual reporting for the respective funding client, as too many updates could otherwise be required depending on the project type. We recommend more frequent regular updating however for your own project monitoring |
| 9. Planned or actual start date of activity at the location   | Date   | Input | Yes | Per location | Ideally, the start of the activity / implementation at the respective location is defined in the geodata collection ToR > Annex 3.2
| 10. Activity description (general)  | Text |    Input | Yes |Per location | A short description of the main project activity in this location, e.g., hydropower plant construction or construction of small irrigation systems
| 11. Additional activity description  | Text |   Input | No | Per location | Free text (in case you need to add other location–specific information like production volumes, progress values or a tag like “COVID-19”)
| 12. Location type code IATI | Select Text   | Selection  | Yes | Per location | See List of Location Types in the Excel Template. This allows aggregating across location type and assignment of icons for publication on the map. Please use the most similar type, e.g., "well.". You can add the exact location type e.g., "extraction well" under "additional location types" if necessary. Definitions for all IATI-based location types can be found [here](https://iatistandard.org/en/iati-standard/203/codelists/locationtype/)
| 13. Alternative location type   | Text  | Input  | No | Per location | Free text for additional location types (in case you don’t find a suitable Location Type Name in the drop-down menu). This promotes systemic learning and allows us to identify additionally required location types
| 14. Budget share | Currency number in EUR  | Input  | No | Per location | The budget share allocated to this location in €. The sum of all locations in a project should add up to the budget sum in INPRO/PMT, including overheads. The budget sum is provided in the geodata collection ToR > Annex 3.2
| 15. DAC 5 purpose classification   |Text | Input | Yes | Per location | Assignment to the relevant DAC 5 Digit Codes from the respective 1 to 3 Codes defined for the project. For example, in a decentralization project, the construction of primary school locations is to be assigned to the respective Basic Education DAC 5-Code, while road rehabilitation sites within the same project are to be assigned to the respective Transport DAC 5-Code
| 16. Geographic exactness according to IATI  |Select Text (exact or approximate) |   Input | Yes | Per location | The “exact” specification is to be used when the coder is confident of coding the exact geographically end destination of a financial flow. Flows that can only be traced to a general area or an approximate location are to be coded as “approximate.” In case of security risks (e.g., zones of conflict), we strongly recommend only publishing approximate locations|

**If exact locations are known, use Geo-Coordinates:**

| **Name** | **Type of data** | **Source**      |  **Mandatory**  | **Asignment** | **Description** | 
| ---------|:----------------:| ---------------:| ---------------:| --------------:| --------------:|
| 17. Geo-coordinates of the respective location gateway (Latitude/LAT) | Decimal | Input | Yes | Per location | Point: 1 coordinate (LAT). At least 5 digits after the dot for each coordinate. Only use if exact locations are known. Example: 50.12018514689011. Usage of WGS84 as Coordinate Reference System mandatory |
| 18. Geo-coordinates of the respective location gateway (Longitude/LONG) | Decimal | Input | Yes | Per location | Point: 1 coordinates (LONG). At least 5 digits after the dot for each coordinate. Only use if exact locations are known. Example: 8.655474047059236. Usage of WGS84 as Coordinate Reference System mandatory |
| 19. Related community/neighborhood/village | Text | Input | No | Per location | This is for manually adding smaller locations or administrative unit names not identified in global geo-coordinates lists such as GADM  |
| 20. Additional geodata submitted as KML (Lines/Polygons) | Select Text (yes/no) | Input | Yes | Per location |Are you providing additional geodata with the geometry shapes for line and polygon data? It his recommended to supply this kind of information as it helps KfW to better identify the project areas. Data has to be submitted as separate KML files per location (one file per location entry in the table)|

### Table 2: The KfW Project Location Data Collection Model for Financial Cooperation


| **Name** | **Type of data** | **Source**      |  **Mandatory**  | **Asignment** | **Description** | 
| ---------|:----------------:| ---------------:| ---------------:| --------------:| --------------:|
| A. Unique ID | Number | Input  | Given | Per location | For new locations, this column will be empty. For updates, your KfW counterpart will provide you with the list of unique_id numbers in this file to ensure that updated location ids match with the former ones.|
| B. KfW project No. (INPRO) | Number | Input  |Yes| Per location | Every project location in the FC Geodata Model must be assigned to its respective KfW project number that is being provided by KfW in the geodata collection ToR > Annex 3.2 |
| C. Abbreviation of project name (project acronym) | Text    | Input | No | Per location | Please enter here the acronym used for the name/title of the project (e.g. HREII) to be visible on your map. If the project has multiple phases, please add the number of the phase belonging to the before-stated KfW Project-No. |
| D. Data Owner (Institution Name) |Text | Input |Yes| Per location | Legal Entity who owns the data provided here (= legal authorship) |
| E. Publishing restrictions due to security reasons | Select Text (yes/no) | Input | Yes  | Per location | Indicates if this information is collected in fragile regions (e.g. areas of severe civil conflict or war) and should therefore be ommited from publicly available reports.In fragile contexts, geolocation information must be protected and may not be published, for example in online maps, public ESIA or evaluation reports for security reasons (e.g., risk of conflict, repression/discrimination or terrorist attack) in the target area(s) |
| F. Date of data collection or latest update   | Date YYYY-MM-DD (Date format - English/US) | Input |No| Per location | Date of data collection or latest update (if date of data collection is unknown). In case only the year is available please choose the 1st of january e.g. 2022-01-01 |
| G. Project-specific location identifier  | Text    | Selection |No| Per location | In case the location or activity has a project-specific identifier (e.g., a location code in the MIS of the source Agency, e.g. Project Executing Agency(PEA)) or an identifier in a public database like GADM,  it can be entered here. This enables logically connecting and comparing the location/activity in the KfW–system against the location/activity in the Agency/PEA-system. In case your location is an administrative unit (=approximate (admin unit) in Column S "Geographic Exactness"), which is available in GADM, you may state its GADM GID (e.g. VNM.1.1.1_1 in Vietnam) the GID level (e.g. level 4) and GADM Version (e.g. 4.0.4) = VNM.1.1.1_L4_1_4.0.4 as "Project-specific location identifier" in Column G. Otherwise the identifier is the Unique ID in Column A of this table. If a Geographic Information System (GIS), (Remote) Management Information System (R/MIS) or Maintenance Management System (MMS) or a public database such as GADM is used in the project, then the existing location IDs can also be entered in the Excel template as Project-Specific Location Identifiers (No. G in the table below), as defined in the Excel/Kobo template. This makes it easier to check location data across project partner systems and verify the use of funds.|
| H. Location name |Text | Input |Yes| Per location | Short name of the project site ideally containing a summary of the main project activity and the location name (max. 40 characters or digits) |
| I. Location activity status  | Select Text  | Input  | No | Per location | The location activity status according to the IATI standard. If you are unaware of the current status please choose "NA". Updates are only mandatory annually at the time of annual reporting for the respective funding client, as too many updates could otherwise be required depending on the project type. We recommend more frequent regular updating however for your own project monitoring |
| J. Planned or actual start date of activity at the location   | Date  YYYY-MM-DD (Date format - English/US) | Input | Yes | Per location | Aprox. planned or actual start date of implementation of activities on the ground. This can be e.g. the date when construction work is planned to begin. For no information enter 2100-01-01. Ideally, the start of project implementation is defined in the geodata collection ToR > Annex 3.2 |
| K. Planned or actual end date of activity at the location   | Date  YYYY-MM-DD (Date format - English/US) | Input | Yes | Per location | Aprox. planned or actual end date of activities on the ground. This can be e.g. the date when the project is planned to cease implementation activities. For no information enter 2100-01-01.  |
| L. Activity-Description (general)  | Text |    Input | Yes |Per location | A short description of the main project activity in this location, e.g., hydropower plant construction or construction of small irrigation systems. |
| M. Additional activity description  | Text |   Input | No | Per location | Free text (in case you need to add other location–specific information like production volumes, progress values or a tag like “COVID-19”). Please consult your KfW counterpart if additional information is required. |
| N. KC Theme / Sub-Sector | Select Text |  Selection | Yes | Per location | Sectoral / cross-sectoral location type preselection field, see table sheets "Location Types" & KC Themes. If there is no fit,  select "other physical or other immaterial and fill out the column "Alternative Location Type". Please note, that this field only serves to help you find the correct location type name, not for assigning the correct subsector (the latter is done thourgh selecting the correct DAC/CRS-Code in column Q. |
| O. Location Type Name | Select Text   | Selection  | Yes | Per location | After selecting the KC Theme/Sub-Sector, choose the most appropriate location type, see table sheet "Location Types". If there is no fit, please select "other physical" or "other immaterial" and fill out the next column "Alternative Location Type". In case you need/want to mention two different location types (e.g. school and capacity development) at the same GPS-Coordinate, you may just create two separate two rows for these locations types with the respectively different activity descriptions, DAC/CRS-Codes at the same GPS coordinates.  |
| P. Alternative Location Type Name  | Text  | Input  | No | Per location | If you selected "other physical or other immaterial " in the column "Location Type Name", please propose your own location type name. This promotes systemic learning, allows us to identify additionally required location types and will help us to propose a comprehensive IATI standard extension in the future. |
| Q. DAC 5 Purpose Classification /CRS-Code   |Text | Input | Yes | Per location | The DAC 5 Purpose Codes (one to four) for the entire project have to be provided by your KfW counterpart (ideally in the ToR, see Annex 3.2). In case your project contains locations contributing not only to one, but two, three or four DAC/CRS-Codes, please create two, three or four separate rows with the same GPS-Coordinates, but different DAC/CRS-Codes, and potentially different location types and activity descriptions. In case all codes have to be assigned to all locations, then please create a new row for each location, with the only difference being the DAC 5 Purpose Classification. 
| R. Budget share | Currency number in EUR  | Input  | No | Per location | The budget share allocated to this location in €. The sum of all locations in a project should add up to the budget sum in Inpro/PMT including overheads. Data from private partners/PEA must not be entered here! If the budget shares of all locations are to be provided, the budget sum will be provided by the KfW counterpart in the geodata collection ToR > Annex 3.2 |
| S. Geographic exactness | Select Text |   Input | Yes | Per location | The “exact” specification is to be used when the coder is confident of coding the exact geographically end destination of a financial flow. In case you already know your exact location coordinates, you may state them as “exact” locations. Flows that can only be traced to a general area or an approximate location are to be coded as “approximate. In case you don’t know (yet) your exact locations (=approximate (yet unknown)), or you only need to define administrative units (e.g. one entire country for a Policy-Based-Lending project, or a number of districts in a country for a decentralization project) (=approximate (admin unit)) or if you cannot communicate exact coordinates due to security restrictions in a conflict zone (=approximate (security)), you may state them respectively as “approximate”.  In case of security risks (e.g., zones of conflict), we strongly recommend only publishing approximate locations! |
| T. Latitude | Decimal Number  | Input  | Yes | Per location | Enter the Latitude measured with a GPS device (or centroid for approximate locations). Make sure to use WGS 84 as the Coordinate Reference System (EPSG:4326). Enter Values with at least FIVE digits. Example: 50.12018514689011. |
| U. Longitude | Decimal Number  | Input  | Yes | Per location | Enter the Longitude measured with a GPS device (or centroid for approximate locations) here. Make sure to use WGS 84 as the Coordinate Reference System (EPSG:4326). Enter Values with at least FIVE digits. Example: 8.655474047059236  |
| V. Related Community / Village / Neighborhood | Decimal Number  | Input  | No | Per location | You may enter a village, hamlet or neighborhood name that relates to this location. This can serve to manually add smaller community resp. administrative unit names not identified in global coordinates lists such as GADM. |
| W. Filename of additional Geo-data submitted as KML (Lines/Polygons) | Text  | Input  | Yes, if kmldata is provided | Per location | A string of the KML file where the associated geometry information is found. If your location does not represent a single point location, please provide additional geoinformation in the KML format (e.g. in the case your location covers a forest area or an administrative unit like a district as a whole). In the section ‘Location data’, under ‘Latitude’ and ‘Longitude’, fill in the coordinates of the locations centroid. Provide the information of the additional columns in this section. For each row entry with additional geolocation, indicate the filename of the KML file in which the associated geometry is stored. Note, to link an entry from this excel to the KML file, it is required to correctly fill in the Primary Key column X.  |
| X. Primary Key (as provided in KML file) | Decimal Number  | Input  | Yes, if kmldata is provided | Per location | Required only in case you provide additonal geolocation information in another KML file. The geometry in the KML file should possess the same primary key as an attribute as it is listed here.|

