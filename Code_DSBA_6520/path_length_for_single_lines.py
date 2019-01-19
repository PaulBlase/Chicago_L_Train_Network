# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 08:51:48 2018

@author: paulb
"""
#BLUE LINE
start_end_blue = list(zip(node_start_blue, node_end_blue))
path_blue = []

for i in start_end_blue:
    path_blue.append(nx.shortest_path_length(BLUE, i[0][0], i[1][0]))

path_blue

plt.hist(path_blue, bins = 20, alpha=0.5)
plt.title('Stops on Blue Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()


#RED LINE
start_end_red = list(zip(node_start_red, node_end_red))
path_red = []

for i in start_end_red:
  path_red.append(nx.shortest_path_length(RED, i[0][0], i[1][0]))

path_red

plt.hist(path_red, bins = 20, alpha=0.5)
plt.title('Stops on Red Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#BROWN LINE
start_end_brown = list(zip(node_start_brown, node_end_brown))
path_brown = []

for i in start_end_brown:
  path_brown.append(nx.shortest_path_length(BROWN, i[0][0], i[1][0]))

path_brown

plt.hist(path_brown, bins = 20, alpha=0.5)
plt.title('Stops on Brown Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#GREEN LINE
start_end_green = list(zip(node_start_green, node_end_green))
path_green = []

for i in start_end_green:
  path_green.append(nx.shortest_path_length(GREEN, i[0][0], i[1][0]))

path_green

plt.hist(path_green, bins = 20, alpha=0.5)
plt.title('Stops on Green Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#PURPLE LINE
start_end_purple = list(zip(node_start_purple, node_end_purple))
path_purple = []

for i in start_end_purple:
  path_purple.append(nx.shortest_path_length(PURP, i[0][0], i[1][0]))

path_purple

plt.hist(path_purple, bins = 20, alpha=0.5)
plt.title('Stops on Purple Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#PINK LINE
start_end_pink = list(zip(node_start_pink, node_end_pink))
path_pink = []

for i in start_end_pink:
  path_pink.append(nx.shortest_path_length(PINK, i[0][0], i[1][0]))

path_pink

plt.hist(path_pink, bins = 10, alpha=0.5)
plt.title('Stops on Pink Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#ORANGE LINE
start_end_orange = list(zip(node_start_orange, node_end_orange))
path_orange = []

for i in start_end_orange:
  path_orange.append(nx.shortest_path_length(ORANGE, i[0][0], i[1][0]))

path_orange

plt.hist(path_orange, bins = 20, alpha=0.5)
plt.title('Stops on Purple Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()

#YELLOW LINE
start_end_yellow = list(zip(node_start_yellow, node_end_yellow))
path_yellow = []

for i in start_end_yellow:
  path_yellow.append(nx.shortest_path_length(YELLOW, i[0][0], i[1][0]))

path_yellow

plt.hist(path_yellow, bins = 5, alpha=0.5)
plt.title('Stops on Yellow Line')
plt.xlabel('Number of Stops')
plt.ylabel('count')
plt.show()
