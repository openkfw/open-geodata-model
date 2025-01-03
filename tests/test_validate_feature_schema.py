"""
In this module we validate the feature project schema of the template. 
This is a very basic test to ensure that the template is in the correct format and in agreement 
with the technical notes.
"""

import json
from jsonschema import Draft7Validator, ValidationError
from referencing import Registry

# Load schemas
with open("references/feature_project_schema.json", "r", encoding="utf-8") as f_p_f:
    feature_project_schema = json.load(f_p_f)

with open("references/dac5_schema.json", "r", encoding="utf-8") as dac5_file:
    dac5_schema = json.load(dac5_file)

with open("references/project_core_schema.json", "r", encoding="utf-8") as p_c_f:
    project_core_schema = json.load(p_c_f)

with open("references/sector_location_schema.json", "r", encoding="utf-8") as s_l_f:
    sector_location_schema = json.load(s_l_f)


def test_validate_test_cases():
    """
    Tests to validate json files against feature project schema
    """
    # Create a registry and add schemas
    registry = Registry().with_contents(
        [
            ("stack://schemas/dac5.schema", dac5_schema),
            ("stack://schemas/sector_location_type.schema", sector_location_schema),
            ("stack://schemas/project_core.schema", project_core_schema),
            ("stack://schemas/feature_project.schema", feature_project_schema),
        ],
    )

    validator = Draft7Validator(schema=feature_project_schema, registry=registry)

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
            validator.validate(instance=case)
            print("Validation passed.")
        except ValidationError as e:
            print("Validation failed:", e.message)
