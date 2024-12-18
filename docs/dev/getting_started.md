# Getting Started

This section will have all Information you need to create your own custom schema based on this.

## How does our Software work (currently)?

There are two schemas:

* [the Excel-Schema](../../open-geodata-model-package/references): describes the excel-schema
* [the customized Geojson-Schema / ODK](../../open-geodata-model-package/schemas/1.0): is standard which should be made
  the excel-schema
  deprecated.

Our [Validator](TODO:Links) has the following functionality:

* can validate an excel-schema,
* transform an excel-schema to our customized geojson-schema
* can validate our customized geojson-schema

TODO: pic

## Understanding the Schemas

This area is mandatory if you want to edit the Schemas and will give an Introduction how the schemas work.

### Technology-Stack

Currently the schema is based on the following components:

* [json-schema](https://json-schema.org/)-project: A good documentation on the keywords you'll
  find [here](https://json-schema.org/understanding-json-schema/reference)
* [ajv](https://ajv.js.org/): this is the validator which is used
* the documentation of the schemas are created by [jsonschema2md ](https://pypi.org/project/jsonschema2md/)

!!! danger

Please be aware that AJV doesn't have to support all **keywords** from json-schema.org.
For compatibility reasons to our Software we recommand to use *
*[only keywords](https://ajv.js.org/json-schema.html#draft-07)** from the *
*[draft-07](https://ajv.js.org/json-schema.html#draft-07)**
which are supported by [AJV](https://ajv.js.org/json-schema.html#draft-07).

### Schema-Structure

Here will be explained the structure of our two schemas.

* [the Excel-Schema](../../open-geodata-model-package/references): describes the excel-schema
    *
    entry-point: [project_location_schema.json](../../open-geodata-model-package/references/project_location_schema.json)
    * example-excel-file: [kfw_location_types.xlsx](../../open-geodata-model-package/references/kfw_location_types.xlsx)
    * part of the entry-point:
        * [iati_location_type_v2_0_3.json](../../open-geodata-model-package/references/iati_location_type_v2_0_3.json)
        * [iati_sector_codes_v2_0_3.json](../../open-geodata-model-package/references/iati_sector_codes_v2_0_3.json)
* [the customized Geojson-Schema / ODK](../../open-geodata-model-package/schemas/1.0): is standard which should be made
  the excel-schema
  deprecated.
    * entry-points:
        *
        geojson: [feature_project_schema.json](../../open-geodata-model-package/schemas/1.0/feature_project_schema.json)
        * [master_project_schema.json](../../open-geodata-model-package/schemas/1.0/master_project_schema.json):
          basically this is just a
          decision-tree between wdpa-schema (=world database of protected areas) and core-schema. If another schema is
          needed this is the place to be.
        * [project_core_schema.json](../../open-geodata-model-package/schemas/1.0/project_core_schema.json)
        * [wdpa_schema.json](../../open-geodata-model-package/schemas/1.0/wdpa_schema.json)

