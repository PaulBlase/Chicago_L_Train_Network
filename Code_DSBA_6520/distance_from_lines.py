# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 20:22:16 2018

@author: paulb
"""
#BLUE LINE
#Distance to closest L stop from Start
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

near_start_blue = []
node_start_blue = []

for i in start_loc:
    y = []
    z = []
    for j in node_blue:
        xdist = ((pos[start_loc[i]][0] - pos_blue[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_blue[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_blue.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_blue.append(result)

near_start_blue
node_start_blue


near_start_bluenp = np.array(near_start_blue)
plt.hist(near_start_bluenp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Blue Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_blue = []
node_end_blue = []

for i in end_loc:
    y = []
    z = []
    for j in node_blue:
        xdist = ((pos[end_loc[i]][0] - pos_blue[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_blue[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_blue.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_blue.append(result)

near_end_blue
node_end_blue

near_end_bluenp = np.array(near_end_blue)
plt.hist(near_end_bluenp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Blue Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_blue = [sum(x) for x in zip(near_start_blue, near_end_blue)]

diff_blue

diff_bluenp = np.array(diff_blue)
plt.hist(diff_bluenp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Blue Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#RED LINE
#Distance to closest L stop from Start
near_start_red = []
node_start_red = []

for i in start_loc:
    y = []
    z = []
    for j in node_red:
        xdist = ((pos[start_loc[i]][0] - pos_red[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_red[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_red.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_red.append(result)

near_start_red
node_start_red

near_start_rednp = np.array(near_start_red)
plt.hist(near_start_rednp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Red Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_red = []
node_end_red = []

for i in end_loc:
    y = []
    z = []
    for j in node_red:
        xdist = ((pos[end_loc[i]][0] - pos_red[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_red[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_red.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_red.append(result)

near_end_red
node_end_red

near_end_rednp = np.array(near_end_red)
plt.hist(near_end_rednp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Red Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_red = [sum(x) for x in zip(near_start_red, near_end_red)]

diff_red

diff_rednp = np.array(diff_red)
plt.hist(diff_rednp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Red Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#GREEN LINE
#Distance to closest L stop from Start
near_start_green = []
node_start_green = []

for i in start_loc:
    y = []
    z = []
    for j in node_green:
        xdist = ((pos[start_loc[i]][0] - pos_green[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_green[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_green.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_green.append(result)

near_start_green
node_start_green

near_start_greennp = np.array(near_start_green)
plt.hist(near_start_greennp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Green Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_green = []
node_end_green = []

for i in end_loc:
    y = []
    z = []
    for j in node_green:
        xdist = ((pos[end_loc[i]][0] - pos_green[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_green[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_green.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_green.append(result)

near_end_green
node_end_green

near_end_greennp = np.array(near_end_green)
plt.hist(near_end_greennp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Green Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_green = [sum(x) for x in zip(near_start_green, near_end_green)]

diff_green

diff_greennp = np.array(diff_green)
plt.hist(diff_greennp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Green Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#BROWN LINE
#Distance to closest L stop from Start
near_start_brown = []
node_start_brown = []

for i in start_loc:
    y = []
    z = []
    for j in node_brown:
        xdist = ((pos[start_loc[i]][0] - pos_brown[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_brown[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_brown.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_brown.append(result)

near_start_brown
node_start_brown

near_start_brownnp = np.array(near_start_brown)
plt.hist(near_start_brownnp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Brown Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_brown = []
node_end_brown = []

for i in end_loc:
    y = []
    z = []
    for j in node_brown:
        xdist = ((pos[end_loc[i]][0] - pos_brown[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_brown[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_brown.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_brown.append(result)

near_end_brown
node_end_brown


near_end_brownnp = np.array(near_end_brown)
plt.hist(near_end_brownnp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Brown Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_brown = [sum(x) for x in zip(near_start_brown, near_end_brown)]

diff_brown

diff_brownnp = np.array(diff_brown)
plt.hist(diff_brownnp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Brown Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#ORANGE LINE
#Distance to closest L stop from Start
near_start_orange = []
node_start_orange = []

for i in start_loc:
    y = []
    z = []
    for j in node_orange:
        xdist = ((pos[start_loc[i]][0] - pos_orange[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_orange[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_orange.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_orange.append(result)

near_start_orange
node_start_orange

near_start_orangenp = np.array(near_start_orange)
plt.hist(near_start_orangenp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Orange Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_orange = []
node_end_orange = []

for i in end_loc:
    y = []
    z = []
    for j in node_orange:
        xdist = ((pos[end_loc[i]][0] - pos_orange[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_orange[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_orange.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_orange.append(result)

near_end_orange
node_end_orange

near_end_orangenp = np.array(near_end_orange)
plt.hist(near_end_orangenp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Orange Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_orange = [sum(x) for x in zip(near_start_orange, near_end_orange)]

diff_orange

diff_orangenp = np.array(diff_orange)
plt.hist(diff_orangenp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Orange Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#PURPLE LINE
#Distance to closest L stop from Start
near_start_purple = []
node_start_purple = []

for i in start_loc:
    y = []
    z = []
    for j in node_purple:
        xdist = ((pos[start_loc[i]][0] - pos_purple[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_purple[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_purple.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_purple.append(result)

near_start_purple
node_start_purple

near_start_purplenp = np.array(near_start_purple)
plt.hist(near_start_purplenp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Purple Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_purple = []
node_end_purple = []

for i in end_loc:
    y = []
    z = []
    for j in node_purple:
        xdist = ((pos[end_loc[i]][0] - pos_purple[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_purple[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_purple.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_purple.append(result)

near_end_purple
node_end_purple
near_end_purplenp = np.array(near_end_purple)
plt.hist(near_end_purplenp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Purple Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_purple = [sum(x) for x in zip(near_start_purple, near_end_purple)]

diff_purple

diff_purplenp = np.array(diff_purple)
plt.hist(diff_purplenp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Purple Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#PINK LINE
#Distance to closest L stop from Start
near_start_pink = []
node_start_pink = []

for i in start_loc:
    y = []
    z = []
    for j in node_pink:
        xdist = ((pos[start_loc[i]][0] - pos_pink[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_pink[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_pink.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_pink.append(result)

near_start_pink
node_start_pink

near_start_pinknp = np.array(near_start_pink)
plt.hist(near_start_pinknp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Pink Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_pink = []
node_end_pink = []

for i in end_loc:
    y = []
    z = []
    for j in node_pink:
        xdist = ((pos[end_loc[i]][0] - pos_pink[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_pink[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_pink.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_pink.append(result)

near_end_pink
node_end_pink
near_end_pinknp = np.array(near_end_pink)
plt.hist(near_end_pinknp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Pink Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_pink = [sum(x) for x in zip(near_start_pink, near_end_pink)]

diff_pink

diff_pinknp = np.array(diff_pink)
plt.hist(diff_pinknp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Pink Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#YELLOW LINE
#Distance to closest L stop from Start
near_start_yellow = []
node_start_yellow = []

for i in start_loc:
    y = []
    z = []
    for j in node_yellow:
        xdist = ((pos[start_loc[i]][0] - pos_yellow[j][0]) ** 2)
        ydist = ((pos[start_loc[i]][1] - pos_yellow[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_start_yellow.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_start_yellow.append(result)

near_start_yellow
node_start_yellow

near_start_yellownp = np.array(near_start_yellow)
plt.hist(near_start_yellownp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Yellow Line Station from Initial Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance to closest L stop from End
near_end_yellow = []
node_end_yellow = []

for i in end_loc:
    y = []
    z = []
    for j in node_yellow:
        xdist = ((pos[end_loc[i]][0] - pos_yellow[j][0]) ** 2)
        ydist = ((pos[end_loc[i]][1] - pos_yellow[j][1]) ** 2)
        y.append(j)
        z.append(((xdist + ydist) ** .5) * 69)
    near_end_yellow.append(min(z))
    result = [x for x, y in zip(y, z) if y == min(z)]
    node_end_yellow.append(result)

near_end_yellow
node_end_yellow

near_end_yellownp = np.array(near_end_yellow)
plt.hist(near_end_yellownp, bins = 50, alpha=0.5)
plt.title('Distance to Nearest Yellow Line Station from End Node')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()

#Distance not covered by line
diff_yellow = [sum(x) for x in zip(near_start_yellow, near_end_yellow)]

diff_yellow

diff_yellownp = np.array(diff_yellow)
plt.hist(diff_yellownp, bins = 50, alpha=0.5)
plt.title('Minimum Distance off Yellow Line')
plt.xlabel('Distance (in miles)')
plt.ylabel('count')
plt.show()
