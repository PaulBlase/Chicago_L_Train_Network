# Chicago L Train System
The L system is used by over 750,000 people on the average weekday. Transporting workers (and casual city dwellers) from as far North as Evanston, all the way down to 95th street on the Southside. It is a staple for residents of the city and has an essential function in the city. Extensions have been done to expand the line and increase ridership, such as via the Evanston stops mentioned earlier. This leads us to a question: who does the rail system benefit the most? Do changes to the line lean the benefits of using the L train toward higher income citizens?

Data was collected from CMAP travel inventories to assess the proximity, route time, and number of stops taken by individuals sampled from the city of Chicago as well as the collar counties. Using coordinate data, we intend to assess the above to evaluate where residents benefit the most from the current routes and stops, attempting to understand the decisions behind the routing of the line. Evaluating by ward and demographic data, we will assess whether the data suggests these decisions are biased by race and income.

### Data Manipulation
In order to assess the points, first data was extracted from CMAP. Points provided an initial set of coordinates as well as an endpoint connected to an individual surveyed. A location with a higher prevalence leads to a higher degree, indicating a hub individuals travel from or, more likely, travel to. Degree distribution is displayed in the histogram below.

![degree_distrib](https://user-images.githubusercontent.com/40553610/54729268-fa4bfd00-4b58-11e9-9a33-abe9fa464cdc.png)
