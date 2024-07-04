import pandas as pd
import json

# Load the Excel file
excel_file = 'Project_Location_Data_Template_V02.xlsx'
sheet_name = 'Location Types IATI and New'

# Read the Excel sheet into a DataFrame
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Extract the relevant columns
location_types = df[['Code', 'Name', 'Character', 'Geometry']]

# Convert the DataFrame to a list of dictionaries
location_types_list = location_types.to_dict(orient='records')

# Save the list of dictionaries to a JSON file
json_file = 'data/location_types.json'
with open(json_file, 'w') as f:
    json.dump(location_types_list, f, indent=4)

print(f"Location types have been successfully extracted and saved to {json_file}")
