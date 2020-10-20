import json
import pprint

from flat_json import JSONDict

with open('test.json', 'r') as injson:
    json_str = injson.read()[3:]
    json_dict = json.loads(json_str)

print("WITHOUT FLATTENING " + "-"*20)
pprint.pprint(json_dict)

print("\n\n\n\n\n\nWITH FLATTENING " + "-"*20)
flat_json = JSONDict(json_dict)
pprint.pprint(flat_json)