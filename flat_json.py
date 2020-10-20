from collections.abc import MutableMapping
from typing import Dict, Any
from collections import deque
from copy import deepcopy
from tree import JsonTree

class JSONDict(MutableMapping):
    def __init__(self, json_dict):
        """Takes a dictionary with JSON-like data and creates an instance that
        behaves exactly like a dict but with the flattened data"""
        self.json_dict = json_dict

        self.json_tree = JsonTree(self.json_dict)

        self.flat_json = self._flatten_json()

        self.__dict__.update(self.flat_json)

    def _flatten_json(self):
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

    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __getitem__(self, key):
        return self.__dict__[key]
    def __delitem__(self, key):
        del self.__dict__[key]
    def __iter__(self):
        return iter(self.__dict__)
    def __len__(self):
        return len(self.__dict__)
    # The final two methods aren't required, but nice for demo purposes:
    def __str__(self):
        '''returns simple dict representation of the mapping'''
        return str(self.__dict__)
    def __repr__(self):
        '''echoes class, id, & reproducible representation in the REPL'''
        return '{}, D({})'.format(super(JSONDict, self).__repr__(),
                                  self.__dict__)
