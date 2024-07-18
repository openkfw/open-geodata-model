"""
In this module we validate the simple schema of the template. 
This is a very basic test to ensure that the template is in the correct format and in agreement with the 
technical notes.
"""

import json
from jsonschema import validate

def test_load_schema():
    """
    Test that the schema can be loaded.
    """
    schema_name = "references/project_location_schema.json"
    with open(schema_name) as f:
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
        "dac5PurposeClassificationCRSCode":"Test DAC5 Purpose Classification CRS Code",
        "geographicExactness": "exact",
        "latitude": -5.353234,
        "longitude": 5.4543,
    }

    # now validate the test dict
    validate(instance=test_dict, schema=schema)
