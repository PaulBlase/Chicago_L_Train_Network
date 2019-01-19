# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 17:51:02 2018
SOURCES:
    https://stackoverflow.com/questions/18713321/element-wise-addition-of-2-lists
    
@author: paulb
"""
import numpy as np

pos
distance = []

#Distance to Union Station (41.8795583, -87.6419634)
for i in pos:
    xdist = ((pos[i][0] + 87.6419634) ** 2)
    ydist = ((pos[i][1] - 41.8795583) ** 2)
    distance.append(((xdist + ydist) ** .5) * 69)
    
distance

distancenp = np.array(distance)
plt.hist(distancenp, bins = 50, alpha=0.5)
plt.title('Distance to West Loop of all Nodes')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop
near = []

for i in pos:
    z = []
    for j in stations:
        xdist = ((pos[i][0] - stations[j][0]) ** 2)
        ydist = ((pos[i][1] - stations[j][1]) ** 2)
        z.append(((xdist + ydist) ** .5) * 69)
    near.append(min(z))

near

nearnp = np.array(near)
plt.hist(nearnp , bins = 50, alpha=0.5)
plt.title('Distance to Nearest L Station of all Nodes')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance of edges
edge_distance = []

for i in start_loc:
    xdist = ((pos[start_loc[i]][0] - pos[end_loc[i]][0]) ** 2)
    ydist = ((pos[start_loc[i]][1] - pos[end_loc[i]][1]) ** 2)
    edge_distance.append(((xdist + ydist) ** .5) * 69)

edge_distance

edge_distancenp = np.array(edge_distance)
plt.hist(edge_distancenp, bins = 50, alpha=0.5)
plt.title('Distance of Edge')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance from start location
#Distance to Union Station (41.8795583, -87.6419634)
distance_start = []

for i in start_loc:
    xdist = ((pos[start_loc[i]][0] + 87.6419634) ** 2)
    ydist = ((pos[start_loc[i]][1] - 41.8795583) ** 2)
    distance_start.append(((xdist + ydist) ** .5) * 69)
    
distance_start

distance_startnp = np.array(distance_start)
plt.hist(distance_startnp, bins = 50, alpha=0.5)
plt.title('Distance to West Loop from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop
near_start = []

for i in start_loc:
    z = []
    for j in stations:
        xdist = ((pos[start_loc[i]][0] - stations[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - stations[j][1]) ** 2)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start.append(min(z))

near_start

near_startnp = np.array(near_start)
plt.hist(near_startnp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest L Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance from end location
#Distance to Union Station (41.8795583, -87.6419634)
distance_end = []

for i in end_loc:
    xdist = ((pos[end_loc[i]][0] + 87.6419634) ** 2)
    ydist = ((pos[end_loc[i]][1] - 41.8795583) ** 2)
    distance_end.append(((xdist + ydist) ** .5) * 69)
    
distance_end

distance_endnp = np.array(distance_end)
plt.hist(distance_endnp, bins = 50, alpha=0.5)
plt.title('Distance to West Loop from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop
near_end = []

for i in end_loc:
    z = []
    for j in stations:
        xdist = ((pos[end_loc[i]][0] - stations[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - stations[j][1]) ** 2)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end.append(min(z))

near_end

near_endnp = np.array(near_end)
plt.hist(near_endnp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest L Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by L train
diff = [sum(x) for x in zip(near_start, near_end)]

diff

diffnp = np.array(diff)
plt.hist(diffnp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off L Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Short Edges
len(diff)
a = []

for i in diff:
    a.append(i < 10)

short_diff = [i for (i, v) in zip(edge_list, a) if v]
short_diff_dist = [i for (i, v) in zip(diff, a) if v]
len(short_diff)

F = nx.DiGraph()
F.add_weighted_edges_from(short_diff)

nx.draw(F, pos, node_size = 5, node_color = 'blue')
nx.draw(BLUE, pos_blue, node_color = 'blue', node_size = 10)
nx.draw(RED, pos_red, node_color = 'red', node_size = 10)
nx.draw(PURP, pos_purple, node_color = 'purple', node_size = 10)
nx.draw(BROWN, pos_brown, node_color = 'brown', node_size = 10)
nx.draw(PINK, pos_pink, node_color = 'pink', node_size = 10)
nx.draw(ORANGE, pos_orange, node_color = 'orange', node_size = 10)
nx.draw(GREEN, pos_green, node_color = 'green', node_size = 10)
nx.draw(YELLOW, pos_yellow, node_color = 'yellow', node_size = 10)
plt.show()
