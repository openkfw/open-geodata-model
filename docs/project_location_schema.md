# Project Location Model

*This schema defines the structure of the project location model. It is used to validate the project location data provided by the KfW counterpart.*

## Properties

- **`activityDescriptionGeneral`** *(string, required)*: A short description of the main project activity in this location.
- **`additionalActivityDescription`** *(string)*: Free text for additional location–specific information.
- **`alternativeLocationTypeName`** *(string)*: If you selected 'other physical' or 'other immaterial' in the column 'Location Type Name', please propose your own location type name.
- **`budgetShare`** *(number)*: The budget share allocated to this location in €.
- **`dac5PurposeCode`** *(string, required)*: The DAC 5 Purpose Codes for the entire project.
- **`dataOwner`** *(string, required)*: Legal entity that owns the data provided here (= legal authorship).
- **`dateOfDataCollection`** *(string, format: date)*: Date of data collection or latest update.
- **`filenameOfAdditionalGeoData`** *(string)*: Filename of the KML file where the associated geometry information is found.
- **`geographicExactness`** *(string, required)*: Please use 'exact' if you know the geographically exact end destination of a financial flow. Must be one of: `["exact", "approximate"]`.
- **`kcThemeSubSector`** *(string, required)*: Sectoral / cross-sectoral location type preselection field.
- **`kfwProjectNoINPRO`** *(integer, required)*: Every project location in the FC Geodata Model must be assigned to its respective KfW project number, which is provided by KfW.
- **`latitude`** *(number, required)*: Enter the Latitude measured with a GPS device. Minimum: `-90`. Maximum: `90`.
- **`locationActivityStatus`** *(string)*: The location activity status according to the IATI standard. Must be one of: `["NA", "Pipeline/identification", "Implementation", "Finalisation", "Closed", "Cancelled", "Suspended"]`.
- **`locationName`** *(string, required)*: Short name of the project site ideally containing a summary of the main project activity and the location name.
- **`locationTypeName`** *(string, required)*: After selecting the KC Theme/Sub-Sector, please choose the most appropriate location type.
- **`longitude`** *(number, required)*: Enter the Longitude measured with a GPS device. Minimum: `-180`. Maximum: `180`.
- **`plannedOrActualEndDate`** *(string, format: date, required)*: Approximate planned or actual end date of activities on the ground.
- **`plannedOrActualStartDate`** *(string, format: date, required)*: Approximate planned or actual start date of implementation of activities on the ground.
- **`primaryKey`** *(number)*: This is only required if you provide additional geolocation information in another KML file.
- **`projectAcronym`** *(string)*: Please enter the acronym used for the name/title of the project to be visible on your map.
- **`projectSpecificLocationIdentifier`** *(string)*: If the location or activity has a project-specific identifier, it can be entered here.
- **`publishingRestrictions`** *(string, required)*: Indicates if this information is collected in fragile regions and should therefore be omitted from publicly available reports. Must be one of: `["yes", "no"]`.
- **`relatedCommunityVillageNeighborhood`** *(string)*: You may enter a village, hamlet, or neighborhood name that relates to this location.
- **`uniqueId`** *(number)*: For new locations, this column will be empty. For updates, your KfW counterpart will provide you with a list of unique_id numbers in this file to ensure that updated location IDs match with the former ones.
