from __future__ import annotations

from typing import Dict, Any
from collections import deque
from copy import deepcopy
from tree import JsonTree

JSONDict = Dict[str, Any]

class JsonFlattener:
    """Flatten an input JSON dictionary to keys based on leaf node key names"""

    def __init__(self, json_dict: JSONDict):
        self.json_dict = json_dict

        self.json_tree = JsonTree(self.json_dict)

        self.flat_json = self._flatten_json()

    def _flatten_json(self):
        """
        Primary algorithm that creates the flattened dictionary from a mapped
        tree of JSON data
        """
        flattened_dict = {}
        for leaf_node in self.json_tree.leaf_nodes:
            key_arr = deque([])
            for key in leaf_node.prior_keys[::-1]:
                new_key = self._new_key(key, key_arr)
                if new_key not in flattened_dict:
                    break
            flattened_dict[new_key] = list(leaf_node.json_data.values())[0]
        return flattened_dict

    def _new_key(self, key: str, key_arr: deque) -> str:
        key_arr.appendleft(str(key))
        return '_'.join(key_arr)
