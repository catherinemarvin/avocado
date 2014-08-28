import numpy
import json

# Load the contents of the nodes and links into memory.
nodes = numpy.genfromtxt("nodes.csv",
    dtype="object",
    delimiter=",",
    skip_header=0,
    usecols=(0,1))

links = numpy.genfromtxt("edges.csv",
    dtype="object",
    delimiter=",",
    skip_header=0,
    usecols=(0,1))

# Replace the ID in the links with their position in the list of nodes for d3.

for n in range(len(nodes)):
  for ls in range(len(links)):
    if nodes[n][0] == links[ls][0]:
      links[ls][0] = n
    if nodes[n][0] == links[ls][1]:
      links[ls][1] = n

data = {}

node_list = []

# Nodes are a list with the names of friends
for node in nodes:
  d = {}
  d["name"] = str(node[1])
  node_list.append(d)
data["nodes"] = node_list

# Links are a list with the source and target

link_list = []

for link in links:
  d = {}
  d["source"] = link[0]
  d["target"] = link[1]
  link_list.append(d)
data["links"] = link_list 

with open("facebook_data.json", "w") as f:
  f.write(json.dumps(data))
