# Modèle de Localisation des Projets

- [1. Property `Modèle de Localisation des Projets > schemeVersion`](#schemeVersion)
- [2. Property `Modèle de Localisation des Projets > activityDescriptionGeneral`](#activityDescriptionGeneral)
- [3. Property `Modèle de Localisation des Projets > additionalActivityDescription`](#additionalActivityDescription)
- [4. Property `Modèle de Localisation des Projets > alternativeLocationTypeName`](#alternativeLocationTypeName)
- [5. Property `Modèle de Localisation des Projets > budgetShare`](#budgetShare)
- [6. Property `Modèle de Localisation des Projets > dac5PurposeCode`](#dac5PurposeCode)
- [7. Property `Modèle de Localisation des Projets > dataOwner`](#dataOwner)
- [8. Property `Modèle de Localisation des Projets > dateOfDataCollection`](#dateOfDataCollection)
- [9. Property `Modèle de Localisation des Projets > filenameOfAdditionalGeoData`](#filenameOfAdditionalGeoData)
- [10. Property `Modèle de Localisation des Projets > geographicExactness`](#geographicExactness)
- [11. Property `Modèle de Localisation des Projets > sector_location`](#sector_location)
- [12. Property `Modèle de Localisation des Projets > kfwProjectNoINPRO`](#kfwProjectNoINPRO)
- [13. Property `Modèle de Localisation des Projets > locationActivityStatus`](#locationActivityStatus)
- [14. Property `Modèle de Localisation des Projets > locationName`](#locationName)
- [15. Property `Modèle de Localisation des Projets > plannedOrActualEndDate`](#plannedOrActualEndDate)
- [16. Property `Modèle de Localisation des Projets > plannedOrActualStartDate`](#plannedOrActualStartDate)
- [17. Property `Modèle de Localisation des Projets > primaryKey`](#primaryKey)
- [18. Property `Modèle de Localisation des Projets > projectAcronym`](#projectAcronym)
- [19. Property `Modèle de Localisation des Projets > projectSpecificLocationIdentifier`](#projectSpecificLocationIdentifier)
- [20. Property `Modèle de Localisation des Projets > publishingRestrictions`](#publishingRestrictions)
- [21. Property `Modèle de Localisation des Projets > relatedCommunityVillageNeighborhood`](#relatedCommunityVillageNeighborhood)
- [22. Property `Modèle de Localisation des Projets > uniqueId`](#uniqueId)

**Title:** Modèle de Localisation des Projets

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Ce schéma définit la structure du modèle de sites des projet. Il sert à valider les données de sites du projet fournies par le partenaire KfW.

| Property                                                                       | Pattern | Type              | Deprecated | Definition                        | Title/Description                                                                                                                                                                                         |
| ------------------------------------------------------------------------------ | ------- | ----------------- | ---------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| + [schemeVersion](#schemeVersion )                                             | No      | const             | No         | -                                 | -                                                                                                                                                                                                         |
| + [activityDescriptionGeneral](#activityDescriptionGeneral )                   | No      | string            | No         | -                                 | Une brève description de l'activité principale du projet sur ce site.                                                                                                                                     |
| - [additionalActivityDescription](#additionalActivityDescription )             | No      | string            | No         | -                                 | Texte libre pour des informations supplémentaires spécifiques au site.                                                                                                                                    |
| - [alternativeLocationTypeName](#alternativeLocationTypeName )                 | No      | string            | No         | -                                 | Si vous avez sélectionné 'autre physique' ou 'autre immatériel' dans la colonne 'Nom du type de site', veuillez proposer votre propre nom de type de site.                                                |
| - [budgetShare](#budgetShare )                                                 | No      | number            | No         | -                                 | La part du budget allouée à ce site en €.                                                                                                                                                                 |
| + [dac5PurposeCode](#dac5PurposeCode )                                         | No      | enum (of integer) | No         | In dac5_schema.json               | DAC 5 Purpose Code                                                                                                                                                                                        |
| + [dataOwner](#dataOwner )                                                     | No      | string            | No         | -                                 | Entité juridique qui possède les données fournies ici (= droit d'auteur légal).                                                                                                                           |
| - [dateOfDataCollection](#dateOfDataCollection )                               | No      | string            | No         | -                                 | Date de collecte des données ou de la dernière mise à jour.                                                                                                                                               |
| - [filenameOfAdditionalGeoData](#filenameOfAdditionalGeoData )                 | No      | string            | No         | -                                 | Nom du fichier KML contenant les informations géométriques associées.                                                                                                                                     |
| + [geographicExactness](#geographicExactness )                                 | No      | enum (of string)  | No         | -                                 | Veuillez utiliser 'exacte' si vous connaissez la destination finale géographique exacte d'un flux financier.                                                                                              |
| + [sector_location](#sector_location )                                         | No      | enum (of null)    | No         | In sector_location_schema_fr.json | Champ de présélection du type de localisation Secteurs / Sous-secteurs. / type de localisation le plus approprié.                                                                                         |
| + [kfwProjectNoINPRO](#kfwProjectNoINPRO )                                     | No      | string            | No         | -                                 | Chaque site du projet dans le modèle de géodonnées FC doit être attribué à son numéro de projet KfW respectif, qui est fourni par la KfW.                                                                 |
| - [locationActivityStatus](#locationActivityStatus )                           | No      | enum (of string)  | No         | -                                 | La phase de réalisation de l’activité selon la norme IATI.                                                                                                                                                |
| + [locationName](#locationName )                                               | No      | string            | No         | -                                 | Nom court du site, incluant idéalement un résumé de l’activité principale et le nom du lieu.                                                                                                              |
| + [plannedOrActualEndDate](#plannedOrActualEndDate )                           | No      | string            | No         | -                                 | Date de fin approximative prévue ou réelle des activités sur le site.                                                                                                                                     |
| + [plannedOrActualStartDate](#plannedOrActualStartDate )                       | No      | string            | No         | -                                 | Date de début approximative prévue ou réelle de la mise en œuvre des activités sur le site.                                                                                                               |
| - [primaryKey](#primaryKey )                                                   | No      | string            | No         | -                                 | Ceci n'est requis que si vous fournissez des informations de géolocalisation supplémentaires dans un autre fichier KML.                                                                                   |
| - [projectAcronym](#projectAcronym )                                           | No      | string            | No         | -                                 | Veuillez entrer l'acronyme utilisé pour le nom/titre du projet afin qu'il soit visible sur votre carte.                                                                                                   |
| - [projectSpecificLocationIdentifier](#projectSpecificLocationIdentifier )     | No      | object            | No         | -                                 | Si le site ou l'activité a un identifiant spécifique au projet, il peut être saisi ici.                                                                                                                   |
| + [publishingRestrictions](#publishingRestrictions )                           | No      | enum (of string)  | No         | -                                 | Indique si ces informations sont collectées dans des régions fragiles et doivent donc être omises des rapports accessibles au public.                                                                     |
| - [relatedCommunityVillageNeighborhood](#relatedCommunityVillageNeighborhood ) | No      | string            | No         | -                                 | Vous pouvez saisir le nom d’un village, d’un hameau ou d’un quartier lié à ce site.                                                                                                                       |
| - [uniqueId](#uniqueId )                                                       | No      | string            | No         | -                                 | Pour les nouveaux sites, cette colonne reste vide. Pour les mises à jour, votre partenaire KfW fournira une liste de numéros unique_id afin d’assurer la correspondance avec les identifiants précédents. |

## <a name="schemeVersion"></a>1. Property `Modèle de Localisation des Projets > schemeVersion`

|              |         |
| ------------ | ------- |
| **Type**     | `const` |
| **Required** | Yes     |

Specific value: `"1.0"`

## <a name="activityDescriptionGeneral"></a>2. Property `Modèle de Localisation des Projets > activityDescriptionGeneral`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Une brève description de l'activité principale du projet sur ce site.

## <a name="additionalActivityDescription"></a>3. Property `Modèle de Localisation des Projets > additionalActivityDescription`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Texte libre pour des informations supplémentaires spécifiques au site.

## <a name="alternativeLocationTypeName"></a>4. Property `Modèle de Localisation des Projets > alternativeLocationTypeName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Si vous avez sélectionné 'autre physique' ou 'autre immatériel' dans la colonne 'Nom du type de site', veuillez proposer votre propre nom de type de site.

## <a name="budgetShare"></a>5. Property `Modèle de Localisation des Projets > budgetShare`

|              |          |
| ------------ | -------- |
| **Type**     | `number` |
| **Required** | No       |

**Description:** La part du budget allouée à ce site en €.

## <a name="dac5PurposeCode"></a>6. Property `Modèle de Localisation des Projets > dac5PurposeCode`

**Title:** DAC 5 Purpose Code

|                |                     |
| -------------- | ------------------- |
| **Type**       | `enum (of integer)` |
| **Required**   | Yes                 |
| **Defined in** | dac5_schema.json    |

**Description:** Les codes CAD 5 assignés à l’ensemble du projet.

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

## <a name="dataOwner"></a>7. Property `Modèle de Localisation des Projets > dataOwner`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Entité juridique qui possède les données fournies ici (= droit d'auteur légal).

## <a name="dateOfDataCollection"></a>8. Property `Modèle de Localisation des Projets > dateOfDataCollection`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |
| **Format**   | `date`   |

**Description:** Date de collecte des données ou de la dernière mise à jour.

## <a name="filenameOfAdditionalGeoData"></a>9. Property `Modèle de Localisation des Projets > filenameOfAdditionalGeoData`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Nom du fichier KML contenant les informations géométriques associées.

## <a name="geographicExactness"></a>10. Property `Modèle de Localisation des Projets > geographicExactness`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Veuillez utiliser 'exacte' si vous connaissez la destination finale géographique exacte d'un flux financier.

Must be one of:
* "exacte"
* "approximative (encore inconnue)"
* "approximative (sécurité)"
* "approximative (unité d’administration)"

## <a name="sector_location"></a>11. Property `Modèle de Localisation des Projets > sector_location`

|                |                                |
| -------------- | ------------------------------ |
| **Type**       | `enum (of null)`               |
| **Required**   | Yes                            |
| **Defined in** | sector_location_schema_fr.json |

**Description:** Champ de présélection du type de localisation Secteurs / Sous-secteurs. / type de localisation le plus approprié.

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

## <a name="kfwProjectNoINPRO"></a>12. Property `Modèle de Localisation des Projets > kfwProjectNoINPRO`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Chaque site du projet dans le modèle de géodonnées FC doit être attribué à son numéro de projet KfW respectif, qui est fourni par la KfW.

## <a name="locationActivityStatus"></a>13. Property `Modèle de Localisation des Projets > locationActivityStatus`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | No                 |

**Description:** La phase de réalisation de l’activité selon la norme IATI.

Must be one of:
* "Ne s’applique pas (NA)"
* "Identification"
* "Exécution"
* "Finalisation"
* "Terminé"
* "Annulé"
* "Suspendu"
* "Divers"

## <a name="locationName"></a>14. Property `Modèle de Localisation des Projets > locationName`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |

**Description:** Nom court du site, incluant idéalement un résumé de l’activité principale et le nom du lieu.

## <a name="plannedOrActualEndDate"></a>15. Property `Modèle de Localisation des Projets > plannedOrActualEndDate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `date`   |

**Description:** Date de fin approximative prévue ou réelle des activités sur le site.

## <a name="plannedOrActualStartDate"></a>16. Property `Modèle de Localisation des Projets > plannedOrActualStartDate`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | Yes      |
| **Format**   | `date`   |

**Description:** Date de début approximative prévue ou réelle de la mise en œuvre des activités sur le site.

## <a name="primaryKey"></a>17. Property `Modèle de Localisation des Projets > primaryKey`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Ceci n'est requis que si vous fournissez des informations de géolocalisation supplémentaires dans un autre fichier KML.

## <a name="projectAcronym"></a>18. Property `Modèle de Localisation des Projets > projectAcronym`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Veuillez entrer l'acronyme utilisé pour le nom/titre du projet afin qu'il soit visible sur votre carte.

## <a name="projectSpecificLocationIdentifier"></a>19. Property `Modèle de Localisation des Projets > projectSpecificLocationIdentifier`

|                           |                  |
| ------------------------- | ---------------- |
| **Type**                  | `object`         |
| **Required**              | No               |
| **Additional properties** | Any type allowed |

**Description:** Si le site ou l'activité a un identifiant spécifique au projet, il peut être saisi ici.

## <a name="publishingRestrictions"></a>20. Property `Modèle de Localisation des Projets > publishingRestrictions`

|              |                    |
| ------------ | ------------------ |
| **Type**     | `enum (of string)` |
| **Required** | Yes                |

**Description:** Indique si ces informations sont collectées dans des régions fragiles et doivent donc être omises des rapports accessibles au public.

Must be one of:
* "oui "
* "non"

## <a name="relatedCommunityVillageNeighborhood"></a>21. Property `Modèle de Localisation des Projets > relatedCommunityVillageNeighborhood`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Vous pouvez saisir le nom d’un village, d’un hameau ou d’un quartier lié à ce site.

## <a name="uniqueId"></a>22. Property `Modèle de Localisation des Projets > uniqueId`

|              |          |
| ------------ | -------- |
| **Type**     | `string` |
| **Required** | No       |

**Description:** Pour les nouveaux sites, cette colonne reste vide. Pour les mises à jour, votre partenaire KfW fournira une liste de numéros unique_id afin d’assurer la correspondance avec les identifiants précédents.

----------------------------------------------------------------------------------------------------------------------------
Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-08-25 at 14:24:35 +0200
