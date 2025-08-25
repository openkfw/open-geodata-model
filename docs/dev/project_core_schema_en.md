# Project Location Model

- [1. Property `Project Location Model > schemeVersion`](#schemeVersion)
- [2. Property `Project Location Model > activityDescriptionGeneral`](#activityDescriptionGeneral)
- [3. Property `Project Location Model > additionalActivityDescription`](#additionalActivityDescription)
- [4. Property `Project Location Model > alternativeLocationTypeName`](#alternativeLocationTypeName)
- [5. Property `Project Location Model > budgetShare`](#budgetShare)
- [6. Property `Project Location Model > dac5PurposeCode`](#dac5PurposeCode)
- [7. Property `Project Location Model > dataOwner`](#dataOwner)
- [8. Property `Project Location Model > dateOfDataCollection`](#dateOfDataCollection)
- [9. Property `Project Location Model > filenameOfAdditionalGeoData`](#filenameOfAdditionalGeoData)
- [10. Property `Project Location Model > geographicExactness`](#geographicExactness)
- [11. Property `Project Location Model > sector_location`](#sector_location)
- [12. Property `Project Location Model > kfwProjectNoINPRO`](#kfwProjectNoINPRO)
- [13. Property `Project Location Model > locationActivityStatus`](#locationActivityStatus)
- [14. Property `Project Location Model > locationName`](#locationName)
- [15. Property `Project Location Model > plannedOrActualEndDate`](#plannedOrActualEndDate)
- [16. Property `Project Location Model > plannedOrActualStartDate`](#plannedOrActualStartDate)
- [17. Property `Project Location Model > primaryKey`](#primaryKey)
- [18. Property `Project Location Model > projectAcronym`](#projectAcronym)
- [19. Property `Project Location Model > projectSpecificLocationIdentifier`](#projectSpecificLocationIdentifier)
- [20. Property `Project Location Model > publishingRestrictions`](#publishingRestrictions)
- [21. Property `Project Location Model > relatedCommunityVillageNeighborhood`](#relatedCommunityVillageNeighborhood)
- [22. Property `Project Location Model > uniqueId`](#uniqueId)

**Title:** Project Location Model

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** This schema defines the structure of the project location model. It is used to validate the project location data provided by the KfW counterpart.

| Property                                                                       | Pattern | Type              | Deprecated | Definition                        | Title/Description                                                                                                                                                                                              |
| ------------------------------------------------------------------------------ | ------- | ----------------- | ---------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [schemeVersion](#schemeVersion )                                             | No      | const             | No         | -                                 | -                                                                                                                                                                                                              |
| + [activityDescriptionGeneral](#activityDescriptionGeneral )                   | No      | string            | No         | -                                 | A short description of the main project activity in this location.                                                                                                                                             |
| - [additionalActivityDescription](#additionalActivityDescription )             | No      | string            | No         | -                                 | Free text for additional location–specific information.                                                                                                                                                        |
| - [alternativeLocationTypeName](#alternativeLocationTypeName )                 | No      | string            | No         | -                                 | If you selected 'other physical' or 'other immaterial' in the column 'Location Type Name', please propose your own location type name.                                                                         |
| - [budgetShare](#budgetShare )                                                 | No      | number            | No         | -                                 | The budget share allocated to this location in €.                                                                                                                                                              |
| + [dac5PurposeCode](#dac5PurposeCode )                                         | No      | enum (of integer) | No         | In dac5_schema.json               | DAC 5 Purpose Code                                                                                                                                                                                             |
| + [dataOwner](#dataOwner )                                                     | No      | string            | No         | -                                 | Legal entity that owns the data provided here (= legal authorship).                                                                                                                                            |
| - [dateOfDataCollection](#dateOfDataCollection )                               | No      | string            | No         | -                                 | Date of data collection or latest update.                                                                                                                                                                      |
| - [filenameOfAdditionalGeoData](#filenameOfAdditionalGeoData )                 | No      | string            | No         | -                                 | Filename of the KML file where the associated geometry information is found.                                                                                                                                   |
| + [geographicExactness](#geographicExactness )                                 | No      | enum (of string)  | No         | -                                 | Please use 'exact' if you know the geographically exact end destination of a financial flow.                                                                                                                   |
| + [sector_location](#sector_location )                                         | No      | enum (of null)    | No         | In sector_location_schema_en.json | Sectoral / cross-sectoral location type preselection field. / most appropriate location type                                                                                                                   |
| + [kfwProjectNoINPRO](#kfwProjectNoINPRO )                                     | No      | string            | No         | -                                 | Every project location in the FC Geodata Model must be assigned to its respective KfW project number, which is provided by KfW.                                                                                |
| - [locationActivityStatus](#locationActivityStatus )                           | No      | enum (of string)  | No         | -                                 | The location activity status according to the IATI standard.                                                                                                                                                   |
| + [locationName](#locationName )                                               | No      | string            | No         | -                                 | Short name of the project site ideally containing a summary of the main project activity and the location name.                                                                                                |
| + [plannedOrActualEndDate](#plannedOrActualEndDate )                           | No      | string            | No         | -                                 | Approximate planned or actual end date of activities on the ground.                                                                                                                                            |
| + [plannedOrActualStartDate](#plannedOrActualStartDate )                       | No      | string            | No         | -                                 | Approximate planned or actual start date of implementation of activities on the ground.                                                                                                                        |
| - [primaryKey](#primaryKey )                                                   | No      | string            | No         | -                                 | This is only required if you provide additional geolocation information in another KML file.                                                                                                                   |
| - [projectAcronym](#projectAcronym )                                           | No      | string            | No         | -                                 | Please enter the acronym used for the name/title of the project to be visible on your map.                                                                                                                     |
| - [projectSpecificLocationIdentifier](#projectSpecificLocationIdentifier )     | No      | object            | No         | -                                 | If the location or activity has a project-specific identifier, it can be entered here.                                                                                                                         |
| + [publishingRestrictions](#publishingRestrictions )                           | No      | enum (of string)  | No         | -                                 | Indicates if this information is collected in fragile regions and should therefore be omitted from publicly available reports.                                                                                 |
| - [relatedCommunityVillageNeighborhood](#relatedCommunityVillageNeighborhood ) | No      | string            | No         | -                                 | You may enter a village, hamlet, or neighborhood name that relates to this location.                                                                                                                           |
| - [uniqueId](#uniqueId )                                                       | No      | string            | No         | -                                 | For new locations, this column will be empty. For updates, your KfW counterpart will provide you with a list of unique_id numbers in this file to ensure that updated location IDs match with the former ones. |

## <a name="schemeVersion"></a>1. Property `Project Location Model > schemeVersion`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"1.0"`

## <a name="activityDescriptionGeneral"></a>2. Property `Project Location Model > activityDescriptionGeneral`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** A short description of the main project activity in this location.

## <a name="additionalActivityDescription"></a>3. Property `Project Location Model > additionalActivityDescription`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Free text for additional location–specific information.

## <a name="alternativeLocationTypeName"></a>4. Property `Project Location Model > alternativeLocationTypeName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** If you selected 'other physical' or 'other immaterial' in the column 'Location Type Name', please propose your own location type name.

## <a name="budgetShare"></a>5. Property `Project Location Model > budgetShare`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** The budget share allocated to this location in €.

## <a name="dac5PurposeCode"></a>6. Property `Project Location Model > dac5PurposeCode`

**Title:** DAC 5 Purpose Code

|                |                     |
| -------------- | ------------------- |
| **Type**       | `enum (of integer)` |
| **Required**   | Yes                 |
| **Defined in** | dac5_schema.json    |

**Description:** The DAC 5 Purpose Codes for the entire project.

Must be one of:
* 11110
* 11120
* 11130
* 11182
* 11220
* 11230
* 11231
* 11232
* 11240
* 11250
* 11260
* 11320
* 11330
* 11420
* 11430
* 12110
* 12181
* 12182
* 12191
* 12220
* 12230
* 12240
* 12250
* 12261
* 12262
* 12263
* 12264
* 12281
* 12310
* 12320
* 12330
* 12340
* 12350
* 12382
* 13010
* 13020
* 13030
* 13040
* 13081
* 14010
* 14015
* 14020
* 14021
* 14022
* 14030
* 14031
* 14032
* 14040
* 14050
* 14081
* 15110
* 15111
* 15112
* 15113
* 15114
* 15125
* 15130
* 15142
* 15150
* 15151
* 15152
* 15153
* 15160
* 15170
* 15180
* 15190
* 15210
* 15220
* 15230
* 15240
* 15250
* 15261
* 16010
* 16020
* 16030
* 16040
* 16050
* 16061
* 16062
* 16063
* 16064
* 16070
* 16080
* 21010
* 21020
* 21030
* 21040
* 21050
* 21061
* 21081
* 22010
* 22020
* 22030
* 22040
* 23110
* 23181
* 23182
* 23183
* 23210
* 23220
* 23230
* 23231
* 23232
* 23240
* 23250
* 23260
* 23270
* 23310
* 23320
* 23330
* 23340
* 23350
* 23360
* 23410
* 23510
* 23610
* 23620
* 23630
* 23631
* 23640
* 23641
* 23642
* 24010
* 24020
* 24030
* 24040
* 24050
* 24081
* 25010
* 25020
* 25030
* 25040
* 31110
* 31120
* 31130
* 31140
* 31150
* 31161
* 31162
* 31163
* 31164
* 31165
* 31166
* 31181
* 31182
* 31191
* 31192
* 31193
* 31194
* 31195
* 31210
* 31220
* 31261
* 31281
* 31282
* 31291
* 31310
* 31320
* 31381
* 31382
* 31391
* 32110
* 32120
* 32130
* 32140
* 32161
* 32162
* 32163
* 32164
* 32165
* 32166
* 32167
* 32168
* 32169
* 32170
* 32171
* 32172
* 32173
* 32174
* 32182
* 32210
* 32220
* 32261
* 32262
* 32263
* 32264
* 32265
* 32266
* 32267
* 32268
* 32310
* 33110
* 33120
* 33130
* 33140
* 33150
* 33181
* 33210
* 41010
* 41020
* 41030
* 41040
* 41081
* 41082
* 43010
* 43030
* 43040
* 43050
* 43060
* 43071
* 43072
* 43073
* 43081
* 43082
* 51010
* 52010
* 53030
* 53040
* 60010
* 60020
* 60030
* 60040
* 60061
* 60062
* 60063
* 72010
* 72040
* 72050
* 73010
* 74020
* 91010
* 93010
* 99810
* 99820

## <a name="dataOwner"></a>7. Property `Project Location Model > dataOwner`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Legal entity that owns the data provided here (= legal authorship).

## <a name="dateOfDataCollection"></a>8. Property `Project Location Model > dateOfDataCollection`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

**Description:** Date of data collection or latest update.

## <a name="filenameOfAdditionalGeoData"></a>9. Property `Project Location Model > filenameOfAdditionalGeoData`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Filename of the KML file where the associated geometry information is found.

## <a name="geographicExactness"></a>10. Property `Project Location Model > geographicExactness`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Please use 'exact' if you know the geographically exact end destination of a financial flow.

Must be one of:
* "exact"
* "approximate (yet unknown)"
* "approximate (security)"
* "approximate (admin unit)"

## <a name="sector_location"></a>11. Property `Project Location Model > sector_location`

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `enum (of null)`               |
| **Required**   | Yes                            |
| **Defined in** | sector_location_schema_en.json |

**Description:** Sectoral / cross-sectoral location type preselection field. / most appropriate location type

Must be one of:
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null
* null

## <a name="kfwProjectNoINPRO"></a>12. Property `Project Location Model > kfwProjectNoINPRO`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Every project location in the FC Geodata Model must be assigned to its respective KfW project number, which is provided by KfW.

## <a name="locationActivityStatus"></a>13. Property `Project Location Model > locationActivityStatus`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** The location activity status according to the IATI standard.

Must be one of:
* "NA"
* "Pipeline/identification"
* "Implementation"
* "Finalisation"
* "Closed"
* "Cancelled"
* "Suspended"
* "Other"

## <a name="locationName"></a>14. Property `Project Location Model > locationName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Short name of the project site ideally containing a summary of the main project activity and the location name.

## <a name="plannedOrActualEndDate"></a>15. Property `Project Location Model > plannedOrActualEndDate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `date`   |

**Description:** Approximate planned or actual end date of activities on the ground.

## <a name="plannedOrActualStartDate"></a>16. Property `Project Location Model > plannedOrActualStartDate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `date`   |

**Description:** Approximate planned or actual start date of implementation of activities on the ground.

## <a name="primaryKey"></a>17. Property `Project Location Model > primaryKey`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** This is only required if you provide additional geolocation information in another KML file.

## <a name="projectAcronym"></a>18. Property `Project Location Model > projectAcronym`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Please enter the acronym used for the name/title of the project to be visible on your map.

## <a name="projectSpecificLocationIdentifier"></a>19. Property `Project Location Model > projectSpecificLocationIdentifier`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** If the location or activity has a project-specific identifier, it can be entered here.

## <a name="publishingRestrictions"></a>20. Property `Project Location Model > publishingRestrictions`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Indicates if this information is collected in fragile regions and should therefore be omitted from publicly available reports.

Must be one of:
* "yes "
* "no"

## <a name="relatedCommunityVillageNeighborhood"></a>21. Property `Project Location Model > relatedCommunityVillageNeighborhood`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** You may enter a village, hamlet, or neighborhood name that relates to this location.

## <a name="uniqueId"></a>22. Property `Project Location Model > uniqueId`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** For new locations, this column will be empty. For updates, your KfW counterpart will provide you with a list of unique_id numbers in this file to ensure that updated location IDs match with the former ones.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-08-25 at 14:24:33 +0200
