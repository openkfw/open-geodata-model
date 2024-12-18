import glob
import json
import os

import jsonschema2md


class ConvertPaths:
    def __init__(self, input_root, output_root):
        self.input_root = input_root
        self.output_root = output_root


def make_md(files, paths: ConvertPaths):
    parser = jsonschema2md.Parser(
        examples_as_yaml=False,
        show_examples="all",
    )
    for load_file in files:
        # print(f)
        with open(load_file, "r") as json_file:
            md_lines = parser.parse_schema(json.load(json_file))
            md_file = load_file.replace(".json", ".md").replace(paths.input_root, paths.output_root)
            try:
                create_folder = os.path.dirname(md_file)
                os.makedirs(create_folder)
            except:
                print(f"folder: {create_folder} already exists lets continue")
            save_md_file = open(md_file, "w")
            save_md_file.write(''.join(md_lines))
            save_md_file.close()


def main():
    converter_paths = ConvertPaths(
        "../open-geodata-model-package",
        "dev/schema_documentation"
    )

    excel_ref = glob.glob(f"{converter_paths.input_root}/references/*.json")
    schema = glob.glob(f"{converter_paths.input_root}/schemas/1.0/*.json")

    make_md(excel_ref, converter_paths)
    make_md(schema, converter_paths)


if __name__ == "__main__":
    main()
