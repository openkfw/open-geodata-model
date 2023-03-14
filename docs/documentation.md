# ˚Annex 3

> KfW's Project Location Data Collection and Management Approach

## Annex 3.1

> The KfW Geodata Model
>
> In this Section we explain the FC Geodata Model according to which
> project location data should be collected as well as technical
> requirements for the data--collection. The goal is to inform KfW
> staff, PEA, consultants and other external stakeholders responsi- ble
> for data collection as to the types of location data to be collected
> and in what form.
>
> Our FC Geodata Model is based on the IATI standard. The IATI--Standard
> is used by international development organizations and allows
> harmonization of FC project loca- tion data across heterogenous
> projects. The data to be collected are subject to mini- mum
> requirements in the form of mandatory fields, and there are optional
> fields flexibly usable for collecting site-specific information.
>
> Furthermore, projects are able to store single location points (e.g.
> the location of one power plant site) or a larger number of project
> sites and features (e.g. 300 locations of buildings in different
> sectors within the framework of a decentralization project). In
> addition, project sites with larger areas and more complex geometries
> (e.g. polygons of forest protection areas) are supported as well.
>
> Please note that KfW does not publish any exact coordinates of its
> project locations. Location data collection in fragile and conflict
> contexts should be treated with extra dil- igence.

#### 3.1.1 General Notes on Geodata and Location Information

##### What is a project location?

> **A project location can consist of one or more features that are part
> of a finan- cially supported activity where no further geographical
> discrimination regard- ing funding is possible.** An example of a
> single-feature project location is a financially supported hospital in
> a specific location. An example of a project location with multiple
> features is a group of adjacent agricultural plots under a financed
> irrigation plan that benefits all producers in that area. Another
> example is a set of protected areas jointly financed from a fund if
> and only if further geographical discrimination as to the alloca- tion
> of funds to specific areas is not possible. If discrimination is
> possible, data for mul- tiple project locations (such as protected
> areas) and their financial allocation have to be collected. KfW highly
> encourages increasing geographical discrimination of financial flows
> to specific project locations to the maximum possible, as this affords
> greater aid transparency and financial accountability.

##### Difference between exact 34 and approximate locations

> For each project location there will be one exact or approximate
> geolocation data set. The exact geolocation designates the
> geographical end point of an international devel- opment assistance
> financial flow. Approximate locations can be used however when no
> exact geoinformation is (yet) available, or such is not be collected
> for other reasons (details see below).
>
> For exact locations, geographical data are to be collected with GPS
> tools and eventually edited in a Geographical Information System
> (GIS). Approximate locations should be given on administrative scales
> using the GADM database as a global standard.
>
> 34 in the sense of the IATI- Standard

##### When to collect project location information

> KfW strongly encourages the PEA and/or consultant staff to collect
> exact or approxi- mate geo-coordinates as early on as possible in the
> project cycle to increase the usage potential of such data throughout
> the entire project cycle. Ideally, data should be col-
>
> lected already during the project preparation phase, e.g.as part of
> the *Feasibility Study*.
>
> If no exact locations can be determined at this stage, approximate
> location should be used and later be checked during the project
> appraisal and inception stages (including possible transformation from
> approximate to exact location information). During pro- ject
> implementation, data should be updated at least annually in project
> progress reviews, and in order to reflect potential changes in the
> geographical allocation of funds, which are common in Financial
> Cooperation projects.

##### Geometrical characteristics of exact 35 geo location information

> \"Exact locations\" are measured via GPS devices, and geo-coordinates
> are to be col- lected as precisely as possible. For this purpose,
> three different geometry types can be used

1.  Point geometries (e.g. a well or a hospital)

2.  Line geometries (e.g. a road or transmission line)

3.  Polygon geometries/shapes (e.g. a protected area or agricultural
    plots)

> All exact project locations have to be collected at first as a point
> geometry that repre- sents a gateway to the project location,
> irrespective of the actual feature geometry (i.e., also for lines and
> polygons). This may be for example the center of a road, a village
> adjacent to agricultural plots or the administration building of a
> protected forest. If there is a line or polygon geometry and no
> gateway can be defined, the geometrical center (centroid) is to be
> used. This information is to be collected in an Excel--template (xlsx)
> or a future open-source based geodata collection tool providing the
> geographical coordinates of the gateway point (more information to be
> provided at \>
> [https://www.](https://www.kfw-entwicklungsbank.de/Service/Publikationen-Videos/Publikationen-thematisch/Digitalisierung/RMMV-Guidebook/)
> [kfw-entwicklungsbank.de/Service/Publikationen-Videos/Publikationen-thematisch/Digi-](https://www.kfw-entwicklungsbank.de/Service/Publikationen-Videos/Publikationen-thematisch/Digitalisierung/RMMV-Guidebook/)
> [talisierung/RMMV-Guidebook/.](https://www.kfw-entwicklungsbank.de/Service/Publikationen-Videos/Publikationen-thematisch/Digitalisierung/RMMV-Guidebook/)
> In addition, line and polygon geometries have to be col- lected in
> KML36 format independently for each project site (details are given
> below in data formats and templates).

#### ![](media/image1.png)Figure A3.1: Schematic Representation of Different Location Data for the GeoApp

> **Legend**
>
> Exact Locations
>
> ![](media/image4.png){width="0.23527887139107612in"
> height="8.76104549431321e-2in"}![](media/image5.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Point Line
>
> ![](media/image6.png){width="0.23847878390201224in"
> height="0.14506889763779526in"} Polygon
>
> Gateway Points
>
> ![](media/image7.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Line Gateway
> ![](media/image8.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Polygon Gateway
>
> Centroid Points
>
> ![](media/image9.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Polygon Centroid
> ![](media/image10.png){width="0.13386045494313212in"
> height="0.13386045494313212in"} Line Centroid
>
> Approximate Locations
>
> Administrational Boundaries (GADM
>
> ![](media/image11.png){width="0.31234142607174104in"
> height="9.055555555555556e-2in"}Municipality/Distrikt Center

![](media/image12.png)

![](media/image5.png){width="0.13272200349956256in"
height="0.13270778652668416in"}![](media/image13.png){width="0.1562357830271216in"
height="0.15625in"}

![](media/image14.png){width="0.1562357830271216in"
height="0.15625in"}![](media/image15.png)

> 35 in the sense of the IATI- Standard
>
> 36 KML (KMZ) is an open XML Standard for Points, Lines and Shapes

##### When to use approximate 37 geo location information

> Approximate locations can be used when no exact geoinformation is
> available (yet), or when exact location information should not be
> collected and stored. The approximate location option should be chosen
> if one or more of the following circumstances apply:

-   an exact project location has not (yet) been specified

-   an exact project location is not (yet) known or defined

-   the target location(s) is/are one or more administrative units.

> In such cases, approximate location must be defined based on
> administrative units applying the GADM standard \>
> <https://gadm.org/>. GADM is used as a common standard for
> administrative units to afford harmonized and consistent collection of
> approximate locations.

#### A3.1.2 Project Geodata Standard Formats and Templates

##### Exact locations using Excel Template (and potentially KML files)

> As outlined above, all project locations should be collected using the
> Excel template (or a future open-source-based geodata collection tool)
> provided by KfW, which utilizes pre- defined categories under the IATI
> standard and built-in selection methods facilitating clean data entry.
> The geolocation is to be submitted in Excel with the geo-coordinates
>
> that can be obtained with a GPS tool. **All coordinates are to be
> collected using**
>
> **WGS 84** 38 **as the coordinate reference system.** WGS 84 is the
> de--facto standard for web mapping applications. Geo-coordinates are
> to be provided in the decimal place format 00.00000 in the order LONG,
> LAT (using at least 5 digits after the separator).

-   **For point locations** like buildings, filling out the exact GPS
    point location in the

> Excel template is sufficient. We estimate that about 90% of all
> project locations are point locations.

-   **For line and polygon geometries,** the gateway GPS point location
    is stored in

> Excel. In suh this case, geometry data should be supplied additionally
> in KML39 for- mat separately for each project location. For multiple
> line or polygon locations, multi- ple KML files have to be submitted.
> A single KML file can however contain a single geometry (e.g. a road)
> or multiple geometries (e.g. multiple agricultural plots) that are
> linked to the gateway location collected in Excel. Multiple KML files
> should be submitted to KfW as.zip or .tar container. The data
> collector must ensure that the KfW staff responsible for uploading the
> data into the GeoApp are able to connect single KML files with project
> locations to the gateway points in Excel. To do so, the data
> collectors need to use the unique identifier given in the Excel
> template (column "Unique ID") together with the respective location
> name, separated by an underscore character "\_" as filename for the
> KML data. An example of such a KML filename is
> "00345_Ouagadougou.kml". We follow this two-step approach for line and
> polygon geodata to ensure that all relevant metadata is collected in a
> clean way in Excel while still being able to submit relevant geometry
> information in a common geo-- standard. It is strongly encouraged to
> submit additional geometry information in KML for locations larger
> than 1000 m (line) or 500 m2 (shapes) wherever possible to enable KfW
> to see the spatial delimitation of our projects (e.g. a transmission
> line or
>
> the boundaries of a protected area). **KML files are also to be
> submitted using**
>
> **WGS 84 as the coordinate reference system.** The WG S84 datum is
> also used by OpenStreetMaps and Google Maps
> [(http://www.opengis.net/def/crs/EPSG/0/4326](http://www.opengis.net/def/crs/EPSG/0/4326)
> KML Template file). The complete specification for OGC KML can be
> found at [http://](http://www.opengeospatial.org/standards/kml/)
> [www.opengeospatial.org/standards/kml/](http://www.opengeospatial.org/standards/kml/)
> or <https://www.ogc.org/standards/kml>.
>
> It is strongly encouraged to check the data before submission in GIS
> software, such as QGIS or Google Earth Pro. This reduces the need to
> go back and forth between the responsible project managers and the
> projects.
>
> 37 in the sense of the IATI- Standard
>
> 38 World Geodetic System 1984,
> <https://support.virtual-surveyor.com/en/support/solutions/articles/1000261351-what-is-wgs84->
>
> 39 KML is an open standard officially named the OpenGIS KML Encoding
> Standard (OGC KML). It is maintained by the Open Geospatial
> Consortium, Inc. (OGC). Other Geoformats (e.g., Shapefiles or GeoJson)
> can usually be converted to KML in Standard GIS Software such as
> ArcGIS or QGIS.
>
> 148 \| **RMMV Guidebook**

##### Approximate locations using Excel Template and GADM standard

> Approximate project locations should be collected by referencing the
> respective adminis- trative unit on the lowest administrative scale
> available in the GADM standard. GADM differentiates up to seven
> different levels, although for many developing countries, only three
> or four levels have yet been defined. Here are the most commonly
> available admin- istrative unit levels:

-   level 0 (shape of the national boundary)

-   level 1 (region, province, governorate, etc.)

-   level 2 (district, zone, department, municipality etc.)

-   level 3 (community, tehsil, etc.)

> If the respective administrative unit level has not been defined in
> GADM, you may instead indicate the GPS coordinates of the respective
> administrative unit center (munic- ipality, district center or similar
> as a point location). In such case, you must specify the location as
> "approximate" in column No. 21. of the Excel template "Geographic
> Exactness according to IATI standard". This ensures that this location
> is not confused with the actual location of the site.
>
> Mixing the administrative unit levels is not allowed because this
> would render the Geo- data Model inconsistent.
>
> The GIS database of GADM can be downloaded at \>
> <https://gadm.org/data.html> and ana- lyzed in a common Geographic
> Information System such as QGIS, ArcGIS, or Google Earth Pro. Data
> collectors have to enter the GADM-defined polygon Geographic ID (GID),
> the GID level and the utilized GADM database version. See [\> Figure
> A3.2
> below](#approximate-locations-using-excel-template-and-gadm-standard)
> for more information:

#### Figure A3.2: How to Collect Project Location Data

> **Legend**
>
> ![](media/image17.jpeg)Exact Locations
>
> ![](media/image18.png)![](media/image19.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Point

![](media/image20.png){width="0.23527887139107612in"
height="8.76104549431321e-2in"}Line and (for excel data choose Gateway
Point or Centroid)

![](media/image21.png){width="0.23847878390201224in"
height="0.14506889763779526in"} Polygon and (for excel data choose
Gateway Point or Centroid)

> ![](media/image22.png)Gateway Points
>
> ![](media/image17.jpeg)![](media/image24.png)![](media/image26.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Line Gateway
> ![](media/image27.png){width="0.13386045494313212in"
> height="0.13384623797025372in"} Polygon Gateway
>
> ![](media/image17.jpeg)Centroid Points
>
> ![](media/image28.png){width="0.11344378827646544in"
> height="0.11344378827646544in"}![](media/image29.png){width="0.13347112860892388in"
> height="0.13348534558180228in"}![](media/image30.png){width="0.13386045494313212in"
> height="0.13384951881014873in"} Polygon Centroid
> ![](media/image31.png){width="0.13386045494313212in"
> height="0.13386045494313212in"} Line Centroid
>
> Approximate Locations
>
> ![](media/image17.jpeg)![](media/image32.png){width="0.12057305336832896in"
> height="0.16535542432195977in"}Administrational Boundaries (GADM) or
>
> ![](media/image33.png)![](media/image11.png){width="0.31233923884514436in"
> height="9.055555555555556e-2in"}![](media/image35.png){width="0.13347112860892388in"
> height="0.13348534558180228in"}Municipality/Distrikt Center

#### Table A3.1: How to Collect Which Type of Location Data?

+---------------+--------------+-------------------+-----------------+
| > **Type of   | >            | > **How to        | > **Comment**   |
| > location    |  **Example** | > collect**       |                 |
| > data**      |              |                   |                 |
+===============+==============+===================+=================+
| > Exact       |              |                   |                 |
+---------------+--------------+-------------------+-----------------+
| > Point       | > Hospital   | > Excel           |                 |
|               |              | > (LAT/LONG)      |                 |
+---------------+--------------+-------------------+-----------------+
| > Line        | > Road       | > Excel           | > Choose        |
|               |              | > (LAT/LONG) +    | > gateway point |
|               |              | > KML             | > or            |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > centroid for  |
|               |              |                   | > Excel         |
+---------------+--------------+-------------------+-----------------+
| > Polygon     | > Protected  | > Excel           | > Choose        |
|               | > Area       | > (LAT/LONG) +    | > gateway point |
|               |              | > KML             | > or            |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > centroid for  |
|               |              |                   | > Excel         |
+---------------+--------------+-------------------+-----------------+
| > Point --    | > Start of a | > Excel           | > Complement    |
| > Gateway     | > Road       | > (LAT/LONG)      | > with KML      |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > data if       |
|               |              |                   | > possible      |
+---------------+--------------+-------------------+-----------------+
| > Point --    | > Center of  | > Excel           | > Complement    |
| > Polygon     | > a          | > (LAT/LONG)      | > with KML      |
+---------------+--------------+-------------------+-----------------+
|               | > protected  |                   | > data if       |
|               | > area       |                   | > possible      |
+---------------+--------------+-------------------+-----------------+
| > Approximate |              |                   |                 |
+---------------+--------------+-------------------+-----------------+
| > Adm         |              | > Excel (GADM) or | > If no GADM    |
| inistrational |              | > Excel           | > boundaries    |
+---------------+--------------+-------------------+-----------------+
| > Boundaries  |              | > (LAT/LONG) +    | > are available |
|               |              | > KML             | > you can also  |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > upload the    |
|               |              |                   | > boundaries of |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > the           |
|               |              |                   | > a             |
|               |              |                   | dministrational |
|               |              |                   | > area          |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > as a Polygon  |
|               |              |                   | > in KML. Sup-  |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > plement this  |
|               |              |                   | > information   |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > with Excel    |
|               |              |                   | > where you can |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > give e.g.,    |
|               |              |                   | > the centroid  |
|               |              |                   | > of            |
+---------------+--------------+-------------------+-----------------+
|               |              |                   | > the polygon   |
+---------------+--------------+-------------------+-----------------+
| > Municipa    |              | > Excel           |                 |
| lity/district |              | > (LAT/LONG)      |                 |
+---------------+--------------+-------------------+-----------------+
| > Center      |              |                   |                 |
+---------------+--------------+-------------------+-----------------+

> Figure A3.3: How to Upload Which Type of Location Data?

##### ![](media/image36.png)Geometry Types Upload MapView

> ![Figure A3.3 illustrates that exact point locations need to be
> collected through only using the KfW excel template, while line and
> polygon locations additionally require submitting a kml-file
> containing the GPS-coordinates of the lines and polygons of each
> location in the excel
> file.](media/image39.jpeg){width="0.4402515310586177in"
> height="0.40562445319335083in"} ![Figure A3.3 illustrates that exact
> point locations need to be collected through only using the KfW excel
> template, while line and polygon locations additionally require
> submitting a kml-file containing the GPS-coordinates of the lines and
> polygons of each location in the excel
> file.](media/image40.png){width="0.2775984251968504in"
> height="0.38499890638670164in"}
>
> ![](media/image41.png){width="0.110249343832021in"
> height="0.13638779527559056in"}![](media/image42.png){width="0.110249343832021in"
> height="0.136499343832021in"}![](media/image43.png){width="0.110249343832021in"
> height="0.13638779527559056in"}Meta-Data + \"Gateway Point\" or
> \"Centroid\" or \"Municipality Capital\"

![](media/image44.png){width="0.2397998687664042in"
height="0.1735411198600175in"}

![](media/image45.png){width="0.23749671916010498in"
height="0.17187445319335082in"}

![](media/image45.png){width="0.23749671916010498in"
height="0.17187445319335082in"}

> Pure Geometries

![](media/image45.png){width="0.23749671916010498in"
height="0.17187445319335082in"}![](media/image46.png)

![](media/image45.png){width="0.23749671916010498in"
height="0.17187445319335082in"}

> GeoApp Sprint Review

##### ![](media/image47.png)How to compare project location data from existing systems (R/MIS, GIS)?

> If a Geographic Information System (GIS), (Remote) Management
> Information System (R/MIS) or Maintenance Management System (MMS) is
> used in the project, then the existing location IDs can also be
> entered in the Excel template as Project-Specific Loca- tion
> Identifiers (No. 7 in the table below), as defined in the Excel
> template. This makes it easier to check location data across project
> partner systems and verify use of funds.

#### A3.1.3 The KfW Project Location Geodata Model for Financial Cooperation

> Below, the required project location data is defined for all FC
> projects. Project-related data is usually provided from both internal
> and external sources. The external data (see column "Source" with
> field entry "Input") has to be provided by the PEA or consultant staff
> using the template(s) provided by KfW and be validated by the
> responsible KfW PM/analyst before uploading.

#### Table A3.2: The KfW Project Location Geodata Model for Financial Cooperation

+-----------+-------+-----+--------+-------+--------------------------+
| >         | > *   | > * | > *    | >     | > **Description**        |
|  **Name** | *Type | *So | *Manda |  **As |                          |
|           | > of  | urc | tory** | signm |                          |
|           | > d   | e** |        | ent** |                          |
|           | ata** |     |        |       |                          |
+===========+=======+=====+========+=======+==========================+
| > 1\.     | > N   | >   | >      | > Per | > Every project location |
| > Unique  | umber |  In |  Given | > loc | > in the FC Geodata      |
| > ID      |       | put |        | ation | > Model                  |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > has to receive a       |
|           |       |     |        |       | > unique location        |
|           |       |     |        |       | > identifier num-        |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > ber This is the unique |
|           |       |     |        |       | > location identifier    |
|           |       |     |        |       | > that is                |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > already provided in    |
|           |       |     |        |       | > the Excel template in  |
|           |       |     |        |       | > the                    |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > Sub-Annex of the       |
|           |       |     |        |       | > geodata collection ToR |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | -   [Annex               |
|           |       |     |        |       |     3.2](#_bookmark154)  |
+-----------+-------+-----+--------+-------+--------------------------+
| > 2\. KfW | > N   | >   | > Yes  | > Per | > Every project location |
| > Project | umber |  In |        | > pr  | > in the FC Geodata      |
| > -No.    |       | put |        | oject | > Model                  |
+-----------+-------+-----+--------+-------+--------------------------+
| > (INPRO) |       |     |        |       | > must be assigned to    |
|           |       |     |        |       | > its respective KfW     |
|           |       |     |        |       | > project                |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > number that is being   |
|           |       |     |        |       | > provided by KfW in the |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > geodata collection ToR |
|           |       |     |        |       | > [\> Annex              |
|           |       |     |        |       | > 3.2.](#_bookmark154)   |
+-----------+-------+-----+--------+-------+--------------------------+
| > 3\.     | >     | >   | > No   | > Per | > If the location or     |
| > Project |  Text |  In |        | > loc | > activity has a         |
| -specific |       | put |        | ation | > project-specific       |
+-----------+-------+-----+--------+-------+--------------------------+
| >         |       |     |        |       | > identifier, e.g. a     |
|  location |       |     |        |       | > location code in the   |
| > i       |       |     |        |       | > Manage-                |
| dentifier |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > ment Information       |
|           |       |     |        |       | > System of the Project  |
|           |       |     |        |       | > Execut-                |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > ing Agency, this can   |
|           |       |     |        |       | > be entered here. This  |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > enables logically      |
|           |       |     |        |       | > connecting and         |
|           |       |     |        |       | > comparing the          |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > location/activity in   |
|           |       |     |        |       | > the KfW--system        |
|           |       |     |        |       | > against the            |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > location/activity in   |
|           |       |     |        |       | > the PEA-system.        |
|           |       |     |        |       | > Otherwise              |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > the identifier is      |
|           |       |     |        |       | > generated              |
|           |       |     |        |       | > automatically (= No.   |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > 1 Unique ID in this    |
|           |       |     |        |       | > table).                |
+-----------+-------+-----+--------+-------+--------------------------+
| > 4\.     | >     | >   | > Yes  | > Per | > Short summary of the   |
| >         |  Text |  In |        | > loc | > main project activity  |
|  Location |       | put |        | ation |                          |
| > Name    |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > (max. 12 characters or |
|           |       |     |        |       | > digits)                |
+-----------+-------+-----+--------+-------+--------------------------+
| > 5\.     | >     | >   | > Yes  | > Per | > Person and/or Legal    |
| > Author  |  Text |  In |        | > pr  | > Entity who collected   |
| > of the  |       | put |        | oject | > the                    |
| > Data    |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > (=the   |       |     |        |       | > data (= legal          |
| > legal   |       |     |        |       | > authorship)            |
| > owner)  |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > 6\.     | > S   | >   | > Yes  | > Per | > In fragile contexts,   |
| > P       | elect |  In |        | > loc | > geolocation            |
| ublishing | >     | put |        | ation | > information            |
|           |  Text |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > res     | > (ye |     |        |       | > must be protected and  |
| trictions | s/no) |     |        |       | > may not be published,  |
| > due to  |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| >         |       |     |        |       | > for example in online  |
|  security |       |     |        |       | > maps, public ESIA or   |
| > reasons |       |     |        |       | > eval-                  |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > uation reports, for    |
|           |       |     |        |       | > security reasons (e.g. |
|           |       |     |        |       | > risk of                |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > conflict,              |
|           |       |     |        |       | > r                      |
|           |       |     |        |       | epression/discrimination |
|           |       |     |        |       | > or terrorist           |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > attack) in the target  |
|           |       |     |        |       | > area(s).               |
+-----------+-------+-----+--------+-------+--------------------------+
| > 7\.     | >     | >   | > No   | > Per | > Date of data           |
| > Date of |  Date |  In |        | > loc | > collection or latest   |
| > data    |       | put |        | ation | > update (if date        |
+-----------+-------+-----+--------+-------+--------------------------+
| > c       |       |     |        |       | > of data collection is  |
| ollection |       |     |        |       | > unknown)               |
| > or      |       |     |        |       |                          |
| > latest  |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > update  |       |     |        |       | > Form: DD.MM.YYYY       |
|           |       |     |        |       | > (numbers only)         |
+-----------+-------+-----+--------+-------+--------------------------+
| > 8\.     | > S   | >   | > Yes  | > Per | > As per IATI--Standard  |
| >         | elect |  In |        | > loc | > see List of Activity   |
|  Location | >     | put |        | ation | > Status                 |
| >         |  Text |     |        |       |                          |
|  Activity |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > Status  |       |     |        |       | > options in the         |
|           |       |     |        |       | > Excel--Template.       |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > Updates are only       |
|           |       |     |        |       | > mandatory annually at  |
|           |       |     |        |       | > the                    |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > time of annual         |
|           |       |     |        |       | > reporting for the      |
|           |       |     |        |       | > respective             |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > funding client, as too |
|           |       |     |        |       | > many updates could     |
|           |       |     |        |       | > other-                 |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > wise be required       |
|           |       |     |        |       | > depending on project   |
|           |       |     |        |       | > type. We               |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > recommend more         |
|           |       |     |        |       | > frequent regular       |
|           |       |     |        |       | > updating               |
+-----------+-------+-----+--------+-------+--------------------------+
|           |       |     |        |       | > however for your own   |
|           |       |     |        |       | > project monitoring.    |
+-----------+-------+-----+--------+-------+--------------------------+
| > 9\.     | >     | >   | > Yes  | > Per | > Ideally, the start of  |
| > Planned |  Date |  In |        | > loc | > the activity /         |
| > or      |       | put |        | ation | > implementation         |
| > actual  |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > start   |       |     |        |       | > at the respective      |
| > date of |       |     |        |       | > location is defined in |
| >         |       |     |        |       | > the geo-               |
|  activity |       |     |        |       |                          |
+-----------+-------+-----+--------+-------+--------------------------+
| > at the  |       |     |        |       | > data collection ToR    |
| >         |       |     |        |       | > [\> Annex              |
|  location |       |     |        |       | > 3.2.](#_bookmark154)   |
+-----------+-------+-----+--------+-------+--------------------------+

+-----------+-------+-----+-------+-------+--------------------------+
| >         | > *   | > * | > **M | >     | > **Description**        |
|  **Name** | *Type | *So | andat |  **As |                          |
|           | > of  | urc | ory** | signm |                          |
|           | > d   | e** |       | ent** |                          |
|           | ata** |     |       |       |                          |
+===========+=======+=====+=======+=======+==========================+
| > 10\.    | >     | >   | > Yes | > Per | > A short description of |
| >         |  Text |  In |       | > loc | > the main project       |
| Activity- |       | put |       | ation | > activity               |
| -Descrip- |       |     |       |       |                          |
+-----------+-------+-----+-------+-------+--------------------------+
| > tion    |       |     |       |       | > in this location,      |
| >         |       |     |       |       | > e.g., hydropower plant |
| (general) |       |     |       |       | > construc-              |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > tion or construction   |
|           |       |     |       |       | > of small irrigation    |
|           |       |     |       |       | > systems.               |
+-----------+-------+-----+-------+-------+--------------------------+
| > 11\.    | >     | >   | > No  | > Per | > Free text (in case you |
| > A       |  Text |  In |       | > loc | > need to add other      |
| dditional |       | put |       | ation | > loca-                  |
+-----------+-------+-----+-------+-------+--------------------------+
| > Act     |       |     |       |       | > tion--specific         |
| ivity--De |       |     |       |       | > information like       |
| scription |       |     |       |       | > production vol-        |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > umes, progress values  |
|           |       |     |       |       | > or a tag like          |
|           |       |     |       |       | > "COVID-19").           |
+-----------+-------+-----+-------+-------+--------------------------+
| > 12\.    | > S   | >   | > Yes | > Per | > See List of Location   |
| >         | elect | Sel |       | > loc | > Types in the Excel     |
|  Location | >     | ect |       | ation | > Tem-                   |
| > Type    |  Text | ion |       |       |                          |
+-----------+-------+-----+-------+-------+--------------------------+
| > Code    |       |     |       |       | > plate                  |
| > IATI    |       |     |       |       |                          |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > This allows            |
|           |       |     |       |       | > aggregating across     |
|           |       |     |       |       | > location type          |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > and assignment of      |
|           |       |     |       |       | > icons for publication  |
|           |       |     |       |       | > on the                 |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > map. Please use the    |
|           |       |     |       |       | > most similar type,     |
|           |       |     |       |       | > e.g.,                  |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > \"well.\". You can add |
|           |       |     |       |       | > the exact location     |
|           |       |     |       |       | > type e.g.,             |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > \"extraction well\"    |
|           |       |     |       |       | > under \"additional     |
|           |       |     |       |       | > location               |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > types\" if necessary.  |
|           |       |     |       |       | > Definitions for all    |
|           |       |     |       |       | > IATI-based             |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > location types can be  |
|           |       |     |       |       | > found here: \>         |
|           |       |     |       |       | > [https://iati-         |
|           |       |     |       |       | ](https://iatistandard.o |
|           |       |     |       |       | rg/en/iati-standard/203/ |
|           |       |     |       |       | codelists/locationtype/) |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > [standard.org/en/iati  |
|           |       |     |       |       | -standard/203/codelists/ |
|           |       |     |       |       | ](https://iatistandard.o |
|           |       |     |       |       | rg/en/iati-standard/203/ |
|           |       |     |       |       | codelists/locationtype/) |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > [locationtype/         |
|           |       |     |       |       | ](https://iatistandard.o |
|           |       |     |       |       | rg/en/iati-standard/203/ |
|           |       |     |       |       | codelists/locationtype/) |
+-----------+-------+-----+-------+-------+--------------------------+
| > 13\.    | >     | >   | > No  | > Per | > Free text for          |
| > Al      |  Text |  In |       | > loc | > additional location    |
| ternative |       | put |       | ation | > types (in case         |
| > Loca-   |       |     |       |       |                          |
+-----------+-------+-----+-------+-------+--------------------------+
| > tion    |       |     |       |       | > you don't find a       |
| > Type    |       |     |       |       | > suitable Location Type |
|           |       |     |       |       | > Name in                |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > the drop-down menu).   |
|           |       |     |       |       | > This promotes systemic |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > learning and allows us |
|           |       |     |       |       | > to identify            |
|           |       |     |       |       | > additionally           |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > required location      |
|           |       |     |       |       | > types.                 |
+-----------+-------+-----+-------+-------+--------------------------+
| > 14\.    | > Cur | >   | > No  | > Per | > The budget share       |
| > Budget  | rency |  In |       | > loc | > allocated to this      |
| > share   |       | put |       | ation | > location in €.         |
+-----------+-------+-----+-------+-------+--------------------------+
|           | > n   |     |       |       | > The sum of all         |
|           | umber |     |       |       | > locations in a project |
|           | > in  |     |       |       | > should add             |
+-----------+-------+-----+-------+-------+--------------------------+
|           | > EUR |     |       |       | > up to the budget sum   |
|           |       |     |       |       | > in INPRO/PMT,          |
|           |       |     |       |       | > including              |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > overheads. The budget  |
|           |       |     |       |       | > sum is provided in the |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > geodata collection ToR |
|           |       |     |       |       | > [\> Annex              |
|           |       |     |       |       | > 3.2](#_bookmark154).   |
+-----------+-------+-----+-------+-------+--------------------------+
| > 15\.    | >     | >   | > Yes | > Per | > Assignment to the      |
| > DAC 5   |  Text |  In |       | > loc | > relevant DAC 5 Digit   |
| > Purpose |       | put |       | ation | > Codes                  |
+-----------+-------+-----+-------+-------+--------------------------+
| > Class   |       |     |       |       | > from the respective 1  |
| ification |       |     |       |       | > to 3 Codes defined for |
|           |       |     |       |       | > the                    |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > project. For example,  |
|           |       |     |       |       | > in a decentralization  |
|           |       |     |       |       | > proj-                  |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > ect, the construction  |
|           |       |     |       |       | > of primary school      |
|           |       |     |       |       | > locations              |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > is to be assigned to   |
|           |       |     |       |       | > the respective Basic   |
|           |       |     |       |       | > Educa-                 |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > tion DAC 5-Code, while |
|           |       |     |       |       | > road rehabilitation    |
|           |       |     |       |       | > sites                  |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > within the same        |
|           |       |     |       |       | > project are to be      |
|           |       |     |       |       | > assigned to            |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > the respective         |
|           |       |     |       |       | > Transport DAC 5-Code.  |
+-----------+-------+-----+-------+-------+--------------------------+
| > 16\.    | > S   | >   | > Yes | > Per | > The "exact"            |
| > G       | elect |  In |       | > loc | > specification is to be |
| eographic | >     | put |       | ation | > used when the          |
|           |  Text |     |       |       |                          |
+-----------+-------+-----+-------+-------+--------------------------+
| >         | > (   |     |       |       | > coder is confident of  |
| Exactness | exact |     |       |       | > coding the             |
| >         | > or  |     |       |       | > geographically         |
| according |       |     |       |       |                          |
+-----------+-------+-----+-------+-------+--------------------------+
| > to IATI | > ap  |     |       |       | > exact end destination  |
|           | proxi |     |       |       | > of a financial flow.   |
|           | mate) |     |       |       | > Flows                  |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > that can only be       |
|           |       |     |       |       | > traced to a general    |
|           |       |     |       |       | > area or an             |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > approximate location   |
|           |       |     |       |       | > are to be coded as     |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > "approximate." In case |
|           |       |     |       |       | > of security risks      |
|           |       |     |       |       | > (e.g.                  |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > zones of conflict), we |
|           |       |     |       |       | > strongly recommend     |
|           |       |     |       |       | > only                   |
+-----------+-------+-----+-------+-------+--------------------------+
|           |       |     |       |       | > publishing approximate |
|           |       |     |       |       | > locations.             |
+-----------+-------+-----+-------+-------+--------------------------+

##### Name Type of data Source Mandatory Assignment Description

+-----------+------+-----+------+---------+--------------------------+
| > **If    |      |     |      |         |                          |
| > exact   |      |     |      |         |                          |
| >         |      |     |      |         |                          |
| locations |      |     |      |         |                          |
| > are     |      |     |      |         |                          |
| > known,  |      |     |      |         |                          |
| > use     |      |     |      |         |                          |
| >         |      |     |      |         |                          |
| Geo-Coord |      |     |      |         |                          |
| inates:** |      |     |      |         |                          |
+===========+======+=====+======+=========+==========================+
| > 17\.    | >    | >   | >    | Per     | > Point: 1 coordinate    |
| > Geo-Co  |  Dec |  In |  Yes | l       | > (LAT)                  |
| ordinates | imal | put |      | ocation |                          |
+-----------+------+-----+------+---------+--------------------------+
| > of the  |      |     |      |         | > At least 5 digits      |
| > r       |      |     |      |         | > after the dot for each |
| espective |      |     |      |         | > coordi-                |
+-----------+------+-----+------+---------+--------------------------+
| >         |      |     |      |         | > nate                   |
|  location |      |     |      |         |                          |
| > gateway |      |     |      |         |                          |
+-----------+------+-----+------+---------+--------------------------+
| > (Lati   |      |     |      |         | > Only use if exact      |
| tude/LAT) |      |     |      |         | > locations are known.   |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > Example:               |
|           |      |     |      |         | > 50.12018514689011      |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > Usage of WGS84 as      |
|           |      |     |      |         | > Coordinate Reference   |
|           |      |     |      |         | > Sys-                   |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > tem mandatory          |
+-----------+------+-----+------+---------+--------------------------+
| > 18\.    | >    | >   | >    | Per     | > Point: 1 coordinates   |
| > Geo-Co  |  Dec |  In |  Yes | l       | > (LONG)                 |
| ordinates | imal | put |      | ocation |                          |
+-----------+------+-----+------+---------+--------------------------+
| > of the  |      |     |      |         | > At least 5 digits      |
| > r       |      |     |      |         | > after the dot for each |
| espective |      |     |      |         | > coordi-                |
+-----------+------+-----+------+---------+--------------------------+
| >         |      |     |      |         | > nate                   |
|  location |      |     |      |         |                          |
| > gateway |      |     |      |         |                          |
+-----------+------+-----+------+---------+--------------------------+
| > (L      |      |     |      |         | > Only use if exact      |
| ongitude/ |      |     |      |         | > locations are known.   |
| > LONG)   |      |     |      |         |                          |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > Example:               |
|           |      |     |      |         | > 8.655474047059236      |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > Usage of WGS84 as      |
|           |      |     |      |         | > Coordinate Reference   |
|           |      |     |      |         | > Sys-                   |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > tem mandatory          |
+-----------+------+-----+------+---------+--------------------------+
| > 1       | >    | >   | > No | Per     | > This is for manually   |
| 9.Related | Text |  In |      | l       | > adding smaller         |
| > Commu-  |      | put |      | ocation | > locations or           |
+-----------+------+-----+------+---------+--------------------------+
| >         |      |     |      |         | > administrative unit    |
| nity/Neig |      |     |      |         | > names not identified   |
| hborhood/ |      |     |      |         | > in                     |
+-----------+------+-----+------+---------+--------------------------+
| > Village |      |     |      |         | > global geo-coordinates |
|           |      |     |      |         | > lists such as GADM.    |
+-----------+------+-----+------+---------+--------------------------+
| > 20\.    | > Se | >   | >    | Per     | > Are you providing      |
| > A       | lect |  In |  Yes | l       | > additional geodata     |
| dditional | >    | put |      | ocation | > with the               |
| > Geo-    | Text |     |      |         |                          |
+-----------+------+-----+------+---------+--------------------------+
| > data    | >    |     |      |         | > geometry shapes for    |
| >         | (yes |     |      |         | > line and polygon data? |
| submitted | /no) |     |      |         |                          |
| > as      |      |     |      |         |                          |
+-----------+------+-----+------+---------+--------------------------+
| > KML     |      |     |      |         | > It his recommended to  |
| > (Lines/ |      |     |      |         | > supply this kind of    |
| Polygons) |      |     |      |         | > infor-                 |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > mation as it helps KfW |
|           |      |     |      |         | > to better identify the |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > project areas. Data    |
|           |      |     |      |         | > has to be submitted as |
|           |      |     |      |         | > sep-                   |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > arate KML files per    |
|           |      |     |      |         | > location (one file per |
|           |      |     |      |         | > loca-                  |
+-----------+------+-----+------+---------+--------------------------+
|           |      |     |      |         | > tion entry in the      |
|           |      |     |      |         | > table).                |
+-----------+------+-----+------+---------+--------------------------+
| > **Use   |      |     |      |         |                          |
| > ap      |      |     |      |         |                          |
| proximate |      |     |      |         |                          |
| >         |      |     |      |         |                          |
| locations |      |     |      |         |                          |
| >         |      |     |      |         |                          |
| according |      |     |      |         |                          |
| > to the  |      |     |      |         |                          |
| > GADM    |      |     |      |         |                          |
| >         |      |     |      |         |                          |
|  standard |      |     |      |         |                          |
| > only if |      |     |      |         |                          |
| > exact   |      |     |      |         |                          |
| >         |      |     |      |         |                          |
| locations |      |     |      |         |                          |
| > are not |      |     |      |         |                          |
| > (yet)   |      |     |      |         |                          |
| > known   |      |     |      |         |                          |
| > or are  |      |     |      |         |                          |
| > not to  |      |     |      |         |                          |
| > be      |      |     |      |         |                          |
| > c       |      |     |      |         |                          |
| ollected, |      |     |      |         |                          |
| >         |      |     |      |         |                          |
| processed |      |     |      |         |                          |
| > or      |      |     |      |         |                          |
| > trans   |      |     |      |         |                          |
| mitted:** |      |     |      |         |                          |
+-----------+------+-----+------+---------+--------------------------+

21. GADM GID Text Input Yes Per approxi- The Geographic ID (GID) of the
    administrative

> mate location level that receives the financial flow. Try to use the
> lowest administrational level possible. For multiple approximate
> locations (administra- tional areas) use multiple data entries.
>
> Example value: VNM.1.1.1_1 for a specific area in Vietnam
>
> Only use if exact locations are unknown.

22. GID Level Text Input Yes Per approxi- Administrative level within
    the GADM database

> mate location (0-7). This should be the name of the column the GID was
> extracted from
>
> Example value: GID_3 for level three Only use if exact locations are
> unknown.

23. GADM version Text Input Yes Per approxi- The version of the utilized
    GADM database

> mate location available at:
>
> Example value: 4.0.4.
>
> Only use if exact locations are unknown.
