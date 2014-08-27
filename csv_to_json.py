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

for node in nodes:
  d = {}
