"""
In this module we test that the sector codes used within the template are valid and the ones from 
the IATI standard.
"""

import json

import pandas as pd


def test_sector_codes():
    """
    Test that the sector codes used within the template are valid and the ones
    from the IATI standard.
    """

    # first load the external reference provided by IATI
    file_path = "open-geodata-model-package/references/iati_sector_codes_v2_0_3.json"

    with open(file_path, encoding="utf-8") as f:
        full_data = json.load(f)

    sector_codes = full_data["data"]

    # create a list of all the codes in the sector_codes
    iati_codes = []
    for sector in sector_codes:
        # only choose active sectors
        if sector["status"] == "active":
            iati_codes.append(sector["code"])

    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_V02.xlsx"
    worksheet_name = "DAC Purpose Codes"

    df = pd.read_excel(
        excel_file_path,
        sheet_name=worksheet_name,
        dtype={"DAC 5 Code (CRS Code)": str, "DAC 3 Code": str, "voluntary code": str},
    )

    # create a list of all the codes in the template
    template_codes = []
    for code in df["DAC 5 Code (CRS Code)"]:
        if pd.notnull(code):
            template_codes.append(code)

    voluntary_codes = []
    for code in df["voluntary code"]:
        if pd.notnull(code):
            voluntary_codes.append(code)

    # test that no codes are missing
    missing_codes = 0
    for code in iati_codes:
        if code not in template_codes and not code in voluntary_codes:
            print(f"the code {code} is not present in the template")
            missing_codes += 1
    assert missing_codes == 0

    # test that we have the same length of iati codes and template codes
    assert len(iati_codes) == len(template_codes) + len(voluntary_codes)
