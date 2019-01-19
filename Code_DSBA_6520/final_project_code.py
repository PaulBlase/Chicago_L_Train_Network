# -*- coding: utf-8 -*-
"""
Spyder Editor
SOURCES:
    https://stackoverflow.com/questions/19915266/drawing-a-graph-with-networkx-on-a-basemap
    https://networkx.github.io/documentation/stable/auto_examples/drawing/plot_degree_histogram.html

This is a temporary script file.
"""
import networkx as nx
from scipy.io import loadmat
import matplotlib.pyplot as plt
import collections

#Nodes
x = loadmat('C:/Users/paulb/Documents/DSBA6520/Final_Project/Chicago_nodes_all_trips.mat')
a = x.get('Nodes', None)
len(a)
a

pos={}

for i in a:
    pos[i[0]] = (i[1], i[2])

#Edges
y = loadmat('C:/Users/paulb/Documents/DSBA6520/Final_Project/Chicago_links_all_trips.mat')
z = y.get('Links', None)
len(z)
b = list(z)

edge_list = []
start_loc = [] 
end_loc = []

for i in b:
    #Weighted Edge
    edge_list.append((i[0], i[1], i[2]))
    start_loc.append(i[0])
    end_loc.append(i[1])

G = nx.DiGraph()
    
G.add_weighted_edges_from(edge_list)
G.edges.data('weight')

G.edges

nx.draw(G, pos, node_size = 5, node_color = 'blue')
plt.show()

G.degree()

#Degree Distribution
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

fig, ax = plt.subplots()
plt.bar(deg, cnt, width=0.80, color='b')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d + 0.4 for d in deg])
ax.set_xticklabels(deg)
plt.show()

