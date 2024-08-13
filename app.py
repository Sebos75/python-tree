import json
from anytree import Node, RenderTree

with open('data.json') as f: 
    json_data = json.load(f)

nodes = {item['id']: Node(item['name']) for item in json_data}

for item in json_data:
    parent_id = item['parentId']
    if parent_id:
        nodes[item['id']].parent = nodes[parent_id]

root_nodes = [node for node in nodes.values() if node.is_root]

for root in root_nodes:
    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")
        