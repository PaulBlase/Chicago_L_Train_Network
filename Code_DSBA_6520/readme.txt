Inventory of scripts and files:

Chicago_nodes_all_trips.mat: All nodes and corresponding GPS locations in dataset
Chicago_nodes_all_links.mat: All edges and weights for dataset
final_project_code.py: Imports data and develops digraph for entire dataset; degree distribution histogram
l_lines.py: Imports data for different lines on L train; creates connections between lines; agglomerates data into one system 'STN'
Access_L_Train.py: Formulates distance from lines for all observations on each line
path_length_for_single_lines.py: Develops path lengths for individual lines unconnected to each other
path_length_for_station.py: Develops path lengths for fully-connected network
Access_for_close_users_l_line.py: Looks at individuals within 10 miles of offline travel and within 10 stops of destination