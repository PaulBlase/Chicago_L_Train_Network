# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:25:30 2018

@author: paulb
"""
#Start Node
starts = []

for i in range(0, len(node_start_blue)):
    starts.append([node_start_blue[i], node_start_red[i], node_start_brown[i], node_start_green[i], 
                      node_start_purple[i], node_start_pink[i], node_start_orange[i], node_start_yellow[i]])

starts

starts_dist = []

for i in range(0, len(near_start_blue)):
    starts_dist.append([near_start_blue[i], near_start_red[i], near_start_brown[i], near_start_green[i], 
                                  near_start_purple[i], near_start_pink[i], near_start_orange[i], near_start_yellow[i]])

starts_dist

start_list = []

for i in range(0, len(starts)):
    y = starts[i]
    z = starts_dist[i]
    result = [x for x, y in zip(y, z) if y == min(z)]
    start_list.append(result[0][0])

start_list

#End Node    
ends = []

for i in range(0, len(node_end_blue)):
    ends.append([node_end_blue[i], node_end_red[i], node_end_brown[i], node_end_green[i], 
                      node_end_purple[i], node_end_pink[i], node_end_orange[i], node_end_yellow[i]])

ends

ends_dist = []

for i in range(0, len(near_end_blue)):
    ends_dist.append([near_end_blue[i], near_end_red[i], near_end_brown[i], near_end_green[i], 
                      near_end_purple[i], near_end_pink[i], near_end_orange[i], near_end_yellow[i]])

ends_dist

end_list = []

for i in range(0, len(ends)):
  y = ends[i]
  z = ends_dist[i]
  result = [x for x, y in zip(y, z) if y == min(z)]
  end_list.append(result[0][0])
  
end_list

#Finding Path Length
path_pairs = list(zip(start_list, end_list))

path_stn = []

for i in path_pairs:
    path_stn.append(nx.shortest_path_length(STN, i[0], i[1]))

path_stn

path_stnnp = np.array(path_stn)
plt.hist(path_stnnp, bins = 20, alpha=0.5)
plt.title('Stops on L Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#Short Rides
len(path_stn)
a = []

for i in path_stn:
    a.append(i < 10 and i > 0)

short_stops = [i for (i, v) in zip(edge_list, a) if v]
len(short_stops)

H = nx.DiGraph()
H.add_weighted_edges_from(short_stops)

nx.draw(H, pos, node_size = 5, node_color = 'blue')
nx.draw(BLUE, pos_blue, node_color = 'blue', node_size = 10)
nx.draw(RED, pos_red, node_color = 'red', node_size = 10)
nx.draw(PURP, pos_purple, node_color = 'purple', node_size = 10)
nx.draw(BROWN, pos_brown, node_color = 'brown', node_size = 10)
nx.draw(PINK, pos_pink, node_color = 'pink', node_size = 10)
nx.draw(ORANGE, pos_orange, node_color = 'orange', node_size = 10)
nx.draw(GREEN, pos_green, node_color = 'green', node_size = 10)
nx.draw(YELLOW, pos_yellow, node_color = 'yellow', node_size = 10)
plt.show()

