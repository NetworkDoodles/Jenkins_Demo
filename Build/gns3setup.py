import requests

# Replace with your GNS3 server and project ID
gns3_server = 'http://10.10.2.30'
project_id = 'b2122160-73a4-4a6d-b725-e0f3a887b360'

# Open the project
open_project_url = f'{gns3_server}/v2/projects/{project_id}/open'
requests.post(open_project_url)

# Get the list of nodes
nodes_url = f'{gns3_server}/v2/projects/{project_id}/nodes'
response = requests.get(nodes_url)
nodes = response.json()

# Start all nodes
for node in nodes:
    node_id = node['node_id']
    start_url = f'{gns3_server}/v2/projects/{project_id}/nodes/{node_id}/start'
    requests.post(start_url)

print('Project opened and all nodes have been started.')
