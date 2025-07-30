"""
In this module we validate the feature project schema of the template. 
This is a very basic test to ensure that the template is in the correct format and in agreement 
with the technical notes.
"""

import json
from jsonschema import Draft7Validator, ValidationError
from referencing import Registry
import pandas as pd

# Load schemas
with open("references/feature_project_schema.json", "r", encoding="utf-8") as f_p_f:
    feature_project_schema = json.load(f_p_f)

with open("references/dac5_schema.json", "r", encoding="utf-8") as dac5_file:
    dac5_schema = json.load(dac5_file)

with open("references/project_core_schema_en.json", "r", encoding="utf-8") as p_c_f:
    project_core_schema_en = json.load(p_c_f)

with open("references/sector_location_schema_en.json", "r", encoding="utf-8") as s_l_f:
    sector_location_schema_en = json.load(s_l_f)

with open("references/project_core_schema_fr.json", "r", encoding="utf-8") as p_c_f:
    project_core_schema_fr = json.load(p_c_f)

with open("references/sector_location_schema_fr.json", "r", encoding="utf-8") as s_l_f:
    sector_location_schema_fr = json.load(s_l_f)

def test_validate_test_cases():
    """
    Tests to validate json files against feature project schema
    """
    # Create a registry and add schemas
    registry_en = Registry().with_contents(
        [
            ("stack://schemas/dac5.schema", dac5_schema),
            ("stack://schemas/sector_location_type.schema", sector_location_schema_en),
            ("stack://schemas/project_core.schema", project_core_schema_en),
            ("stack://schemas/feature_project.schema", feature_project_schema),
        ],
    )

    validator_en = Draft7Validator(schema=feature_project_schema, registry=registry_en)
    

    test_cases = [
        {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [74.598611, 36.29333]},
            "properties": {
                "kfwProjectNoINPRO": "45157",
                "uniqueId": "2993700005",
                "plannedOrActualEndDate": "2024-12-13",
                "plannedOrActualStartDate": "2019-12-13",
                "dateOfDataCollection": "2020-02-01",
                "sector_location": {
                    "sector": "Energy",
                    "location_type": "hydropower plant / dam",
                },
                "projectAcronym": "HRE II",
                "dataOwner": "Integration Consulting",
                "publishingRestrictions": "no",
                "projectSpecificLocationIdentifier": "WPD_0129",
                "locationName": "Hassanabad I",
                "locationActivityStatus": "Pipeline/identification",
                "activityDescriptionGeneral": "Rehabilitation of MHP Powerhouse",
                "additionalActivityDescription": "1.5 MW",
                "dac5PurposeCode": 23210,
                "budgetShare": 1000000,
                "geographicExactness": "exact",
                "relatedCommunityVillageNeighborhood": "Hassanabad Town & Upper Hunza",
                "schemeVersion": "1.0",
            },
        },
        {
            "type": "Feature",
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    [
                        [-118.2437, 34.0522],
                        [-118.2437, 34.0622],
                        [-118.2537, 34.0622],
                        [-118.2537, 34.0522],
                        [-118.2437, 34.0522],
                    ]
                ],
            },
            "properties": {
                "uniqueId": "9438398640",
                "kfwProjectNoINPRO": "29937",
                "projectAcronym": "HRE II",
                "dataOwner": "Integration Consulting",
                "publishingRestrictions": "no",
                "dateOfDataCollection": "2020-02-01",
                "projectSpecificLocationIdentifier": "WPD_0129",
                "locationName": "Hassanabad I",
                "locationActivityStatus": "Pipeline/identification",
                "plannedOrActualStartDate": "2019-12-13",
                "plannedOrActualEndDate": "2024-12-13",
                "activityDescriptionGeneral": "Rehabilitation of MHP Powerhouse",
                "additionalActivityDescription": "1.5 MW",
                "sector_location": {
                    "sector": "_Generic / Cross_Sectoral",
                    "location_type": "building(s)",
                },
                "location_type2": "",
                "dac5PurposeCode": 23210,
                "budgetShare": 1000000,
                "geographicExactness": "exact",
                "relatedCommunityVillageNeighborhood": "Hassanabad Town & Upper Hunza",
                "filenameOfAdditionalGeoData": "",
                "primaryKey": "10",
            },
        },
    ]

    # Run validation
    for case in test_cases:
        try:
            validator_en.validate(instance=case)
            print("Validation passed.")
        except ValidationError as e:
            print("Validation failed:", e.message)


def test_validate_excel():
    """
    Tests Excel Template against the schema.
    """
    # Create a registry and add schemas
    registry = Registry().with_contents(
        [
            ("stack://schemas/dac5.schema", dac5_schema),
            ("stack://schemas/sector_location_type.schema", sector_location_schema_en),
            ("stack://schemas/project_core.schema", project_core_schema_en),
            ("stack://schemas/feature_project.schema", feature_project_schema),
        ],
    )

    registry_fr = Registry().with_contents(
        [
            ("stack://schemas/dac5.schema", dac5_schema),
            ("stack://schemas/sector_location_type.schema", sector_location_schema_fr),
            ("stack://schemas/project_core.schema", project_core_schema_fr),
            ("stack://schemas/feature_project.schema", feature_project_schema),
        ],
    )

    validator = Draft7Validator(schema=feature_project_schema, registry=registry)

    validator_fr = Draft7Validator(schema=feature_project_schema, registry=registry_fr)
    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_EN_V03.xlsx"
    worksheet_name = "fill-me"

    excel_df = pd.read_excel(
        excel_file_path,
        sheet_name=worksheet_name,
        dtype={
            "dac5PurposeCode": float,
            "budgetShare": float,
            "primaryKey": str,
            "plannedOrActualStartDate": str,
            "plannedOrActualEndDate": str,
            "dateOfDataCollection": str,
            "projectSpecificLocationIdentifier": str,
            "kfwProjectNoINPRO": str,
            "uniqueId": str
        },
        skiprows=2,
    )
    excel_df = excel_df.rename(
        columns={
            "Abbreviation of project name (project acronym)": "projectAcronym",
            "Activity-Description (general)": "activityDescriptionGeneral",
            "Additional Activity-Description ": "additionalActivityDescription",
            "Alternative Location Type Name": "alternativeLocationTypeName",
            "Budget share": "budgetShare",
            "DAC 5 Purpose Classification": "dac5PurposeCode",
            "Data Owner (Institution Name)\n": "dataOwner",
            "Date of data collection or latest update": "dateOfDataCollection",
            "Filename of additional Geo-data submitted as"
            " KML (Lines/Polygons)": "filenameOfAdditionalGeoData",
            "Geographic Exactness": "geographicExactness",
            "KC Theme / Sub-Sector": "sector",
            "KfW Project -No.\n(INPRO)": "kfwProjectNoINPRO",
            "Latitude": "latitude",
            "Location Activity Status": "locationActivityStatus",
            "Location Type Name": "location_type",
            "Location name": "locationName",
            "Longitude": "longitude",
            "Planned or actual start date of activity at the location ": "plannedOrActualStartDate",
            "Planned or actual end date of activity at the location": "plannedOrActualEndDate",
            "Primary Key (as provided in KML file)": "primaryKey",
            "Project-specific location identifier": "projectSpecificLocationIdentifier",
            "Publishing restrictions due to security reasons": "publishingRestrictions",
            "Related Community / Village / Neighborhood": "relatedCommunity",
            "Unique ID": "uniqueID",
        }
    )
    offset = 0
    for index, row in excel_df.iterrows():
        p_d = row.dropna().to_dict()
        t_d = {"type": "Feature"}
        t_d["geometry"] = {
            "type": "Point",
            "coordinates": [p_d["longitude"], p_d["latitude"]],
        }
        t_d["properties"] = {
            "sector_location": {
                "sector": p_d["sector"],
                "location_type": p_d["location_type"],
            }
        }
        p_d.pop("longitude")
        p_d.pop("latitude")
        p_d.pop("location_type")
        p_d.pop("sector")
        for x in p_d:
            t_d["properties"][x] = p_d[x]
        if "schemeVersion" not in t_d:
            t_d["properties"]["schemeVersion"] = "1.0"
        print("Test row: ", index + offset)
        validator.validate(instance=t_d)

    # now import the sector codes from the template
    excel_file_path_fr = "Project_Location_Data_Template_FR_V03.xlsx"
    worksheet_name = "fill-me Remplissez-moi"

    excel_df = pd.read_excel(
        excel_file_path_fr,
        sheet_name=worksheet_name,
        dtype={
            "dac5PurposeCode": float,
            "budgetShare": float,
            "primaryKey": str,
            "plannedOrActualStartDate": str,
            "plannedOrActualEndDate": str,
            "dateOfDataCollection": str,
            "projectSpecificLocationIdentifier": str,
            "kfwProjectNoINPRO": str,
            "uniqueId": str
        },
        skiprows=2,
    )

    offset = 0
    for index, row in excel_df.iterrows():
        p_d = row.dropna().to_dict()
        t_d = {"type": "Feature"}
        t_d["geometry"] = {
            "type": "Point",
            "coordinates": [p_d["longitude"], p_d["latitude"]],
        }
        t_d["properties"] = {
            "sector_location": {
                "sector": p_d["sector"],
                "location_type": p_d["location_type"],
            }
        }
        p_d.pop("longitude")
        p_d.pop("latitude")
        p_d.pop("location_type")
        p_d.pop("sector")
        for x in p_d:
            t_d["properties"][x] = p_d[x]
        if "schemeVersion" not in t_d:
            t_d["properties"]["schemeVersion"] = "1.0"
        print("Test row: ", index + offset)
        validator_fr.validate(instance=t_d)