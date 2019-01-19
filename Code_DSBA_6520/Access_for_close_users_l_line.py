# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 18:20:06 2018

@author: paulb
"""
#Comparing Commute to L vs Ride on L (10 Miles vs 10 Stops)
#Ranges of distances under 10 miles
plt.hist(short_diff_dist, bins = 30, alpha=0.5)
plt.title('Stops on L Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#Short rides (<10 stops)
nx.draw_networkx_nodes(H, pos, node_size = 5, node_color = 'red')
#Short commute (<10 miles)
nx.draw_networkx_nodes(F, pos, node_size = 2, node_color = 'blue')
plt.show()

short_diff

#Start Point
near_start_short_diff = []
node_start_short_diff = []

for i in range(0, len(short_diff)):
    y = []
    z = []
    for j in stations:
        xdist = ((pos[short_diff[i][0]][0] - stations[j][0]) ** 2)
        ydist = ((pos[short_diff[i][0]][1] - stations[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_short_diff.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_short_diff.append(result[0])

near_start_short_diff
node_start_short_diff

#End Point
near_end_short_diff = []
node_end_short_diff = []

for i in range(0, len(short_diff)):
    y = []
    z = []
    for j in stations:
        xdist = ((pos[short_diff[i][1]][0] - stations[j][0]) ** 2)
        ydist = ((pos[short_diff[i][1]][1] - stations[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_short_diff.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_short_diff.append(result[0])

near_end_short_diff
node_end_short_diff

#Short Diff Pairs
path_pairs_sd = list(zip(node_start_short_diff, node_end_short_diff))

path_pairs_sd

path_stn_sd = []

for i in path_pairs_sd:
    path_stn_sd.append(nx.shortest_path_length(STN, i[0], i[1]))

path_stn_sd

plt.hist(path_stn_sd, bins = 30, alpha=0.5)
plt.title('Stops on L Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#Short Rides
len(path_stn_sd)
a = []

for i in path_stn_sd:
    a.append(i < 10 and i > 0)

short_stops_sd = [i for (i, v) in zip(edge_list, a) if v]
len(short_stops_sd)

J = nx.DiGraph()
J.add_weighted_edges_from(short_stops_sd)

#Short rides (<10 stops)
nx.draw(H, pos, node_size = 5, node_color = 'red')
#Both
nx.draw(J, pos, node_size = 2, node_color = 'yellow')
plt.show()

#Short commute (<10 miles)
nx.draw(F, pos, node_size = 2, node_color = 'blue')
#Both
nx.draw(J, pos, node_size = 2, node_color = 'yellow')
plt.show()


#Comparing Both with Stations
nx.draw(J, pos, node_size = 2, node_color = 'yellow')
nx.draw(BLUE, pos_blue, node_color = 'blue', node_size = 10)
nx.draw(RED, pos_red, node_color = 'red', node_size = 10)
nx.draw(PURP, pos_purple, node_color = 'purple', node_size = 10)
nx.draw(BROWN, pos_brown, node_color = 'brown', node_size = 10)
nx.draw(PINK, pos_pink, node_color = 'pink', node_size = 10)
nx.draw(ORANGE, pos_orange, node_color = 'orange', node_size = 10)
nx.draw(GREEN, pos_green, node_color = 'green', node_size = 10)
nx.draw(YELLOW, pos_yellow, node_color = 'yellow', node_size = 10)
plt.show()
