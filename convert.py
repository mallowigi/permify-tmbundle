import plistlib
import json

def convert_tmlanguage_to_json(plist_path, json_path):
    with open(plist_path, 'rb') as plist_file:
        plist_content = plistlib.load(plist_file)
    with open(json_path, 'w') as json_file:
        json.dump(plist_content, json_file, indent=2)

# Example usage
convert_tmlanguage_to_json('untitled.tmLanguage', 'permify.tmlanguage.json')