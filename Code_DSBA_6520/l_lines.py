# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:35:06 2018
SOURCES:
    https://stackoverflow.com/questions/24809757/how-to-make-a-histogram-from-a-list-of-data
@author: paulb
"""
import networkx as nx
import matplotlib.pyplot as plt
import csv

#BLUELINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/blue_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    blue = list(reader)
blue

pos_blue={}
node_blue= []

for i in blue:
    pos_blue[i[0]] = (float(i[1]), float(i[2]))
    node_blue.append(i[0])

node_blue
pos_blue
BLUE = nx.Graph()
BLUE.add_path(node_blue)

#REDLINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/red_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    red = list(reader)
red

pos_red={}
node_red= []

for i in red:
    pos_red[i[0]] = (float(i[1]), float(i[2]))
    node_red.append(i[0])
    
pos_red
RED = nx.Graph()
RED.add_path(node_red)

#BROWNLINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/brown_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    brown = list(reader)
brown

pos_brown={}
node_brown= []

for i in brown:
    pos_brown[i[0]] = (float(i[1]), float(i[2]))
    node_brown.append(i[0])
    
node_brown
pos_brown
BROWN = nx.Graph()
BROWN.add_path(node_brown)
BROWN.add_edges_from([('Lake_BROWN', 'Merchandise Mart_BROWN')])

#ORANGELINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/orange_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    orange= list(reader)
orange

pos_orange={}
node_orange= []

for i in orange:
    pos_orange[i[0]] = (float(i[1]), float(i[2]))
    node_orange.append(i[0])

node_orange
pos_orange
ORANGE = nx.Graph()
ORANGE.add_path(node_orange)
ORANGE.add_edges_from([('Adams/Wabash_ORANGE', 'Roosevelt_ORANGE')])

#PURPLELINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/purple_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    purple = list(reader)
purple

pos_purple={}
node_purple= []

for i in purple:
    pos_purple[i[0]] = (float(i[1]), float(i[2]))
    node_purple.append(i[0])
    
node_purple
pos_purple
PURP = nx.Graph()
PURP.add_path(node_purple)
PURP.add_edges_from([('Washington_PURP','Merchandise Mart_PURP')])

#GREENLINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/green_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    green = list(reader)
green

with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/green_line_branch.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    greenb = list(reader)
greenb

pos_green={}
node_green= []

for i in green:
    pos_green[i[0]] = (float(i[1]), float(i[2]))
    node_green.append(i[0])
    
pos_green
GREEN = nx.Graph()
GREEN.add_path(node_green)

pos_greenb={}
node_greenb= []

for i in greenb:
    pos_greenb[i[0]] = (float(i[1]), float(i[2]))
    pos_green[i[0]] = (float(i[1]), float(i[2]))
    node_greenb.append(i[0])

GREEN.add_path(node_greenb)
GREEN.add_edges_from([('Garfield_GREEN', 'King Drive_GREEN')])

#PINKLINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/pink_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    pink = list(reader)
pink

pos_pink={}
node_pink= []

for i in pink:
    pos_pink[i[0]] = (float(i[1]), float(i[2]))
    node_pink.append(i[0])
    
node_pink
pos_pink
PINK = nx.Graph()
PINK.add_path(node_pink)
PINK.add_edges_from([('Washington/Wells_PINK', 'Clinton_PINK')])

#YELLOWLINE
with open('C:/Users/paulb/Documents/DSBA6520/Final_Project/yellow_line.txt') as f:
    reader = csv.reader(f, delimiter="\t")
    yellow = list(reader)
yellow

pos_yellow={}
node_yellow= []

for i in yellow:
    pos_yellow[i[0]] = (float(i[1]), float(i[2]))
    node_yellow.append(i[0])
    
YELLOW = nx.Graph()
YELLOW.add_path(node_yellow)

#VISUALIZATION
nx.draw(G, pos, node_size = 5, node_color = 'blue')
nx.draw(BLUE, pos_blue, node_color = 'blue', node_size = 10)
nx.draw(RED, pos_red, node_color = 'red', node_size = 10)
nx.draw(PURP, pos_purple, node_color = 'purple', node_size = 10)
nx.draw(BROWN, pos_brown, node_color = 'brown', node_size = 10)
nx.draw(PINK, pos_pink, node_color = 'pink', node_size = 10)
nx.draw(ORANGE, pos_orange, node_color = 'orange', node_size = 10)
nx.draw(GREEN, pos_green, node_color = 'green', node_size = 10)
nx.draw(YELLOW, pos_yellow, node_color = 'yellow', node_size = 10)
plt.show()

#Single L System Graph
stations = {**pos_blue, **pos_red, **pos_yellow, **pos_green, **pos_purple, 
            **pos_brown, **pos_pink, **pos_orange}
stations
STN = nx.Graph()
STN.add_path(node_blue)
STN.add_path(node_red)
STN.add_path(node_green)
STN.add_path(node_greenb)
STN.add_path(node_brown)
STN.add_path(node_purple)
STN.add_path(node_pink)
STN.add_path(node_yellow)
STN.add_path(node_orange)

#In Line
STN.add_edges_from([('Lake_BROWN', 'Merchandise Mart_BROWN')])
STN.add_edges_from([('Adams/Wabash_ORANGE', 'Roosevelt_ORANGE')])
STN.add_edges_from([('Washington_PURP','Merchandise Mart_PURP')])
STN.add_edges_from([('Garfield_GREEN', 'King Drive_GREEN')])
STN.add_edges_from([('Washington/Wells_PINK', 'Clinton_PINK')])

#Between Lines
STN.add_edges_from([('Howard_RED', 'Howard_YELLOW'), ('Howard_RED', 'Howard_PURP'), ('Howard_PURP', 'Howard_YELLOW')])
STN.add_edges_from([('Wilson_RED', 'Wilson_PURP')])
STN.add_edges_from([('Belmont_RED', 'Belmont_PURP'), ('Belmont_BROWN', 'Belmont_PURP'), ('Belmont_RED', 'Belmont_BROWN')])
STN.add_edges_from([('Fullerton_RED', 'Fullerton_PURP'), ('Fullerton_BROWN', 'Fullerton_PURP'), ('Fullerton_RED', 'Fullerton_BROWN')])
STN.add_edges_from([('Lake_BLUE', 'Lake_RED'), ('Lake_BLUE', 'Lake_PURP'), ('Lake_BLUE', 'Lake_GREEN'),
                    ('Lake_BLUE', 'Lake_PINK'), ('Lake_BLUE', 'Lake_ORANGE'), ('Lake_BLUE', 'Lake_BROWN'),
                    ('Lake_BROWN', 'Lake_RED'), ('Lake_BROWN', 'Lake_PURP'), ('Lake_BROWN', 'Lake_GREEN'),
                    ('Lake_BROWN', 'Lake_PINK'), ('Lake_BROWN', 'Lake_ORANGE'), ('Lake_ORANGE', 'Lake_RED'), 
                    ('Lake_ORANGE', 'Lake_PURP'), ('Lake_ORANGE', 'Lake_GREEN'), ('Lake_ORANGE', 'Lake_PINK'),                    
                    ('Lake_PINK', 'Lake_PURP'), ('Lake_PINK', 'Lake_GREEN'), ('Lake_PINK', 'Lake_RED'),
                    ('Lake_GREEN', 'Lake_PURP'), ('Lake_RED', 'Lake_GREEN'), ('Lake_PURP', 'Lake_RED')])
STN.add_edges_from([('Jackson_RED', 'Jackson_BLUE')])
STN.add_edges_from([('Roosevelt_RED', 'Roosevelt_GREEN'), ('Roosevelt_RED', 'Roosevelt_ORANGE'), ('Roosevelt_ORANGE', 'Roosevelt_GREEN')])
STN.add_edges_from([('Washington_RED', 'Washington_BLUE')])
STN.add_edges_from([('Ashland_PINK', 'Ashland_GREEN')])
STN.add_edges_from([('Clinton_PINK', 'Clinton_GREEN')])
STN.add_edges_from([('State/Lake_PINK', 'State/Lake_GREEN'), ('State/Lake_PINK', 'State/Lake_ORANGE'), ('State/Lake_PINK', 'State/Lake_PURP'),
                    ('State/Lake_PINK', 'State/Lake_BROWN'), ('State/Lake_BROWN', 'State/Lake_GREEN'), ('State/Lake_BROWN', 'State/Lake_ORANGE'), 
                    ('State/Lake_BROWN', 'State/Lake_PURP'), ('State/Lake_PURP', 'State/Lake_GREEN'), ('State/Lake_PURP', 'State/Lake_ORANGE'), 
                    ('State/Lake_ORANGE', 'State/Lake_GREEN')])

STN.edges

nx.draw(STN, stations, node_size = 50)
nx.draw(BLUE, pos_blue, node_color = 'blue', node_size = 50)
nx.draw(RED, pos_red, node_color = 'red', node_size = 50)
nx.draw(PURP, pos_purple, node_color = 'purple', node_size = 50)
nx.draw(BROWN, pos_brown, node_color = 'brown', node_size = 50)
nx.draw(PINK, pos_pink, node_color = 'pink', node_size = 50)
nx.draw(ORANGE, pos_orange, node_color = 'orange', node_size = 50)
nx.draw(GREEN, pos_green, node_color = 'green', node_size = 50)
nx.draw(YELLOW, pos_yellow, node_color = 'yellow', node_size = 50)
plt.show()