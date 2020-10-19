from __future__ import annotations

from node import Node

class JsonTree:
    """Tree of linked lists that map out the JSON data"""

    def __init__(self, json_dict: 'JSONDict'):
        self.json_dict = json_dict
        self.map_tree(self.json_dict)

    def map_tree(self, json_dict):
        """Map the entire JSON tree and get access to leaf nodes"""
        self.leaf_nodes = []
        self.root_node = Node(json_data=json_dict, tree=self)
