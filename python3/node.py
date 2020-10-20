from __future__ import annotations
from typing import List, Dict, Any, Union
from collections import deque

JSONDict = Dict[str, Any]

class Node:
    """
    Representation of one step into a JSON Tree
    """

    def __init__(self, json_data: Any, tree: 'JsonTree', linked_list: deque = deque([]), prior_keys: List[Union[str, int]] = []) -> None:
        self.json_data = json_data
        self.tree = tree
        self.linked_list = linked_list
        self.prior_keys = prior_keys

        self.dtype = type(self.json_data)

        self.nodes = []

        #If the node is a leaf then it has no edges
        if self.is_leaf:
            self.json_data = {prior_keys[-1]: self.json_data}
            self.tree.leaf_nodes.append(self)

        else:
            self.get_edges()

    @property
    def is_leaf(self):
        """
        If the dtype of self.json_data is not a dict or a list then it must be
        a leaf node
        """
        return self.dtype is not list and self.dtype is not dict

    def get_edges(self):
        """
        Get all edges connected to current Node
        """
        iter_arr = zip(range(len(self.json_data)),
                       self.json_data) if self.dtype is list else self.json_data.items()

        for key, value in iter_arr:
            next_linked_list = self.linked_list + deque([self])
            next_key = self.prior_keys + [key]
            node = Node(value, self.tree, next_linked_list, next_key)
            self.nodes.append(node)

    def __repr__(self):
        return str(self.json_data)
