"""
In this module we validate the simple schema of the template. 
This is a very basic test to ensure that the template is in the correct format and in agreement 
with the technical notes.
"""

import json

import pandas as pd
from jsonschema import ValidationError, validate

from icecream import ic

def test_load_schema():
    """
    Test that the schema can be loaded.
    """
    schema_name = "references/project_location_schema.json"
    with open(schema_name, encoding="utf-8") as f:
        schema = json.load(f)

    # create a test dict that could be validated via jsonschema
    test_dict = {
        "kfwProjectNoINPRO": 123456,
        "dataOwner": "Test Data Owner",
        "publishingRestrictions": "yes",
        "locationName": "Test Location Name",
        "plannedOrActualStartDate": "Test Planned or Actual Start Date",
        "plannedOrActualEndDate": "Test Planned or Actual Start Date",
        "activityDescriptionGeneral": "Test Activity Description General",
        "kcThemeSubSector": "Test KC Theme Sub Sector",
        "locationTypeName": "Test Location Type Name",
        "dac5PurposeCode": "Test DAC5 Purpose Classification CRS Code",
        "geographicExactness": "exact",
        "latitude": -5.353234,
        "longitude": 5.4543,
    }

    # now validate the test dict
    validate(instance=test_dict, schema=schema)


def test_validate_json():
    """
    Test that we can use the schema to validate a json file.
    """
    schema_name = "references/project_location_schema.json"
    with open(schema_name, encoding="utf-8") as f:
        schema = json.load(f)

    example_name = "tests/example_project_location.json"
    with open(example_name, encoding="utf-8") as f:
        example_json = json.load(f)
    validate(instance=example_json, schema=schema)


def test_validate_excel():
    """
    Test that the schema can be loaded.
    """
    schema_name = "references/project_location_schema.json"
    with open(schema_name, encoding="utf-8") as f:
        schema = json.load(f)

    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_V02.xlsx"
    worksheet_name = "fill-me"

    excel_df = pd.read_excel(
        excel_file_path,
        sheet_name=worksheet_name,
        dtype={
            "DAC 5 Purpose Classification": str,
            "DAC 3 Code": str,
            "voluntary code": str,
            "Planned or actual start date of activity at the location ": str,
            "Planned or actual end date of activity at the location": str,
            "Date of data collection or latest update": str,
            "Project-specific location identifier": str,
        },
        skiprows=1,
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
            "KC Theme / Sub-Sector": "kcThemeSubSector",
            "KfW Project -No.\n(INPRO)": "kfwProjectNoINPRO",
            "Latitude": "latitude",
            "Location Activity Status": "locationActivityStatus",
            "Location Type Name": "locationTypeName",
            "Location name": "locationName",
            "Longitude": "longitude",
            "Planned or actual end date of activity at the location": "plannedOrActualEndDate",
            "Planned or actual start date of activity at the location ": "plannedOrActualStartDate",
            "Primary Key (as provided in KML file)": "primaryKey",
            "Project-specific location identifier": "projectSpecificLocationIdentifier",
            "Publishing restrictions due to security reasons": "publishingRestrictions",
            "Related Community / Village / Neighborhood": "relatedCommunity",
            "Unique ID": "uniqueID",
        }
    )
    offset = 3
    for index, row in excel_df.iterrows():
        test_dict = row.dropna().to_dict()
        print("Test row: ", index + offset)
        validate(instance=test_dict, schema=schema)


def test_validate_csv():
    """
    Test that we can also import and validate an appropiate csv
    """
    schema_name = "references/project_location_schema.json"
    with open(schema_name, encoding="utf-8") as f:
        schema = json.load(f)

    # now import the sector codes from the template
    csv_file_path = "tests/example_project_location.csv"
    csv_df = pd.read_csv(csv_file_path, dtype={"dac5PurposeCode": str})
    for index, row in csv_df.iterrows():
        test_dict = row.dropna().to_dict()
        print("Test csv row: ", index)
        validate(instance=test_dict, schema=schema)
