from __future__ import annotations

from collections import deque
from typing import List, Dict, Any, Union
from copy import deepcopy
from tree import JsonTree

JSONDict = Dict[str, Any]


class JsonFlattener:
    """Flatten an input JSON dictionary to keys based on leaf node key names"""

    def __init__(self, json_dict: JSONDict):
        self.json_dict = json_dict

        self.json_tree = JsonTree(self.json_dict)

        self.flat_json = self.flatten_json()

    def flatten_json(self):
        flattened_dict = {}
        for leaf_node in self.json_tree.leaf_nodes:
            key_arr = deque([])
            for key in leaf_node.json_data.keys():
                key_arr.appendleft(str(key))  # ensure key is str
                new_key = '_'.join(key_arr)
                if new_key in flattened_dict:
                    for prior_key in leaf_node.prior_keys[-2::-1]:
                        key_arr.appendleft(str(prior_key))
                        new_key = '_'.join(key_arr)
                        if new_key not in flattened_dict:
                            break
                flattened_dict[new_key] = list(leaf_node.json_data.values())[0]
        return flattened_dict