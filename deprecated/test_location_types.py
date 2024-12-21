"""
In this module we test that the location codes used within the template are valid and the ones from 
the reference. For the moment this is mostly superficial but should serve as a basis as we move 
forward to translations and a comparison with the iati standard.
"""

import pandas as pd


def test_location_types():
    """
    Test that the location types used within the template are valid and the ones
    from the reference.
    """

    # first load the external reference provided by IATI
    file_path = "open-geodata-model-package/references/kfw_location_types.xlsx"

    reference = pd.read_excel(file_path)

    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_V02.xlsx"
    worksheet_name = "Location Types IATI and New"

    col_list = [
        "KC-Theme / Sub-Sector",
        "physical or immaterial location type",
        "(IATI) Location Type Code",
        "(IATI) Location Type Name (EN) =  project output- or intervention-related type"
        " of physical location or immaterial output- or intervention area",
        "Geodata Type",
        "IATI Category",
        "(IATI) Location Type Description (EN)",
    ]

    excel_df = pd.read_excel(
        excel_file_path, sheet_name=worksheet_name, usecols=col_list
    )
    excel_df = excel_df.rename(
        columns={
            "KC-Theme / Sub-Sector": "subsector",
            "physical or immaterial location type": "character",
            "(IATI) Location Type Code": "code",
            "(IATI) Location Type Name (EN) =  project output- or "
            "intervention-related type of physical location or "
            "immaterial output- or intervention area": "name",
            "Geodata Type": "geometry",
            "IATI Category": "category",
            "(IATI) Location Type Description (EN)": "description",
        }
    )

    # now test if all the codes in the template are in the reference
    assert reference["code"].equals(excel_df["code"])
    assert reference["name"].equals(excel_df["name"])


def test_fr_location_types():
    """
    Test that the location types used within the french template are valid and the ones
    from the reference.
    """

    # first load the external reference provided by IATI
    file_path = "references/kfw_location_types.xlsx"

    reference = pd.read_excel(file_path)

    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_V021_FR.xlsx"
    worksheet_name = "Location Types IATI and New"

    col_list = [
        "Thème /Sous-secteur",
        "type de site physique ou immatériel",
        "(IITA) Nom du type de site (FR) = type de site physique ou de zone de "
        "production ou d’intervention immatérielle lié à la production ou "
        "à l’intervention du projet",
        "Type de données géographiques",
        "(IATI) Location Type Code",
    ]

    excel_df = pd.read_excel(
        excel_file_path, sheet_name=worksheet_name, usecols=col_list
    )
    excel_df = excel_df.rename(
        columns={
            "(IATI) Location Type Code": "code",
            "(IITA) Nom du type de site (FR) = type de site physique ou de zone de "
            "production ou d’intervention immatérielle lié à la production ou "
            "à l’intervention du projet": "name_fr",
        }
    )

    # now test if all the codes in the template are in the reference
    assert reference["code"].equals(excel_df["code"])
    assert reference["name_fr"].equals(excel_df["name_fr"])


def test_fr_location_types_excel_ref():
    """
    Test that the location types used within the french template are valid and the ones
    from the reference.
    """

    # first load the external reference provided by IATI
    file_path = "references/kfw_location_types.xlsx"

    reference = pd.read_excel(file_path)

    # now import the sector codes from the template
    excel_file_path = "Project_Location_Data_Template_V021_FR.xlsx"
    worksheet_name = "Location Types IATI and New"

    col_list = [
        "Thème /Sous-secteur",
        "type de site physique ou immatériel",
        "(IITA) Nom du type de site (FR) = type de site physique ou de zone de "
        "production ou d’intervention immatérielle lié à la production ou "
        "à l’intervention du projet",
        "Type de données géographiques",
        "(IATI) Location Type Code",
    ]

    excel_df = pd.read_excel(
        excel_file_path, sheet_name=worksheet_name, usecols=col_list
    )
    excel_df = excel_df.rename(
        columns={
            "(IATI) Location Type Code": "code",
        }
    )

    # now test if all the codes in the template are in the reference
    assert reference["code"].equals(excel_df["code"])
