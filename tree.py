from node import Node

class Tree:
    """Flatten a nested dictionary of JSON-data as much as possible"""
    def __init__(self, json_dict):
        self.json_dict = json_dict 
        self.map_tree(self.json_dict)

    def map_tree(self, json_dict):
        self.root_node = Node(json_data=json_dict)


