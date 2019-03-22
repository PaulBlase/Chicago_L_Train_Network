# Chicago L Train System

![Chicago L system](https://www.transitchicago.com/assets/1/6/ctamap_Lsystem.png)
> Source: https://www.transitchicago.com/assets/1/6/ctamap_Lsystem.png

The L system is used by over 750,000 people on the average weekday. Transporting workers (and casual city dwellers) from as far North as Evanston, all the way down to 95th street on the Southside. It is a staple for residents of the city and has an essential function in the city. Extensions have been done to expand the line and increase ridership, such as via the Evanston stops mentioned earlier. This leads us to a question: who does the rail system benefit the most? Do changes to the line lean the benefits of using the L train toward higher income citizens?

Data was collected from CMAP travel inventories to assess the proximity, route time, and number of stops taken by individuals sampled from the city of Chicago as well as the collar counties. Using coordinate data, we intend to assess the above to evaluate where residents benefit the most from the current routes and stops, attempting to understand the decisions behind the routing of the line. Evaluating by ward and demographic data, we will assess whether the data suggests these decisions are biased by race and income.

### Data Manipulation
In order to assess the points, first data was extracted from CMAP. Points provided an initial set of coordinates as well as an endpoint connected to an individual surveyed. A location with a higher prevalence leads to a higher degree, indicating a hub individuals travel from or, more likely, travel to. Degree distribution is displayed in the histogram below.

![degree_distrib](https://user-images.githubusercontent.com/40553610/54729268-fa4bfd00-4b58-11e9-9a33-abe9fa464cdc.png "Degree Distribution")

What can we then say about the distance most people need to travel? We find that the majority of individuals live within ten miles of their desired destination.

![dist_edges](https://user-images.githubusercontent.com/40553610/54829100-0be1f180-4c8c-11e9-81b0-9288afb8b2cd.png)

Baesd on the layout of the city, this likely includes many residents of the city who would be able to access the system. This creates a prime candidate pool, but we need to understand proximity to these stations. If riders are unable to get to their local stops, what would be the point in riding the train?

![dist_ll_all_nodes](https://user-images.githubusercontent.com/40553610/54832356-61210180-4c92-11e9-976d-d0cea454c193.png) ![dist_ll_init_node](https://user-images.githubusercontent.com/40553610/54832400-76962b80-4c92-11e9-9ef3-a6b86e1c383a.png) ![dist_ll_end_node](https://user-images.githubusercontent.com/40553610/54832441-8ada2880-4c92-11e9-9d91-df4bb1da5e65.png)

Again, we find a clear pool of candidates for the system. While there is a stratified separation of individuals from their closest point to begin riding, most endpoints of travel end up in the city. This would indicate that, though the L system will likely not be the sole method of travel for commuters in Chicago, even for those who are not close to a stop, it can still provide a useful stop gap. Several aspects, such as issues with parking, should lead to this and coordinated stops with the Metra system, which reaches out to the suburbs, should compound on the value provided.

With what we know about the L system, how do individual lines provide for these individuals? Are specific lines serving riders better than others? Our initial tests should be looking to find the residual distance commuters need to cover.

![blue_line_prox](https://user-images.githubusercontent.com/40553610/54833069-be698280-4c93-11e9-9d34-38e1d7d31d1e.png) ![brown_line_prox](https://user-images.githubusercontent.com/40553610/54833089-c9bcae00-4c93-11e9-8b9f-a2c812f703d2.png) ![green_line_prox](https://user-images.githubusercontent.com/40553610/54833115-d80aca00-4c93-11e9-8383-09b22c435792.png) ![orange_line_prox](https://user-images.githubusercontent.com/40553610/54833132-e2c55f00-4c93-11e9-9044-0b678566c9bf.png) ![pink_line_prox](https://user-images.githubusercontent.com/40553610/54833143-eb1d9a00-4c93-11e9-84ef-a058d5bc804d.png) ![purple_line_prox](https://user-images.githubusercontent.com/40553610/54833162-f375d500-4c93-11e9-8dd5-f02882f4acdd.png) ![red_line_prox](https://user-images.githubusercontent.com/40553610/54833181-fb357980-4c93-11e9-8cc3-f5e6abc3402a.png) ![yellow_line_prox](https://user-images.githubusercontent.com/40553610/54833211-05577800-4c94-11e9-93a6-fb2665ba42c3.png)

From the map above, we can follow some context on the proximity to the train lines. Clearly, the system operates with the red line as the main line serving the Southside, while the blue and brown serve the Northside and Near Northwest and West suburbs, while the purple connects the system to the Northern suburbs. With this layout, the emphasis is on the North side of the city, where we generally see higher income households.
