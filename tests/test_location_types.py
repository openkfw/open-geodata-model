"""
In this module we test that the location codes used within the template are valid and the ones from 
the reference. For the moment this is mostly superficial but should serve as a basis as we move forward
to translations and a comparison with the iati standard.
"""

import pandas as pd

def test_location_types():
    """
    Test that the location types used within the template are valid and the ones
    from the reference.
    """

    # first load the external reference provided by IATI
    file_path = "references/kfw_location_types.json"

    reference = pd.read_json(file_path)

    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_V02.xlsx"
    worksheet_name = "Location Types IATI and New"

    col_list = [
        "KC-Theme / Sub-Sector",
        "physical or immaterial location type",
        "(IATI) Location Type Code",
        "(IATI) Location Type Name (EN) =  project output- or intervention-related type of physical location or immaterial output- or intervention area",
        "Geodata Type",
        "IATI Category",
        "(IATI) Location Type Description (EN)",
    ]

    excel_df = pd.read_excel(excel_file_path, sheet_name=worksheet_name, usecols=col_list)
    excel_df = excel_df.rename(
        columns={
        "KC-Theme / Sub-Sector": "subsector",
        "physical or immaterial location type": "character",
        "(IATI) Location Type Code": "code",
        "(IATI) Location Type Name (EN) =  project output- or intervention-related type of physical location or immaterial output- or intervention area": "name",
        "Geodata Type": "geometry",
        "IATI Category": "category",
        "(IATI) Location Type Description (EN)": "description",
    }
    )

    # now test if all the codes in the template are in the reference
    assert reference["code"].equals(excel_df["code"])