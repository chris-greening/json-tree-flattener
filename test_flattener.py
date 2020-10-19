import json
import pprint

from json_flattener import JsonFlattener

with open('test.json', 'r') as injson:
    json_str = injson.read()[3:]
    json_dict = json.loads(json_str)

print("WITHOUT FLATTENING " + "-"*20)
pprint.pprint(json_dict)

print("\n\n\n\n\n\nWITH FLATTENING " + "-"*20)
flat_json = JsonFlattener(json_dict)
pprint.pprint(flat_json.flat_json)