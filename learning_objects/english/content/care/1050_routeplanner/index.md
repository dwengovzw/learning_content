---
available: true
content_location: example-location
content_type: text/markdown
copyright: dwengo
description: How the route planner works
difficulty: 3
educational_goals:
- id: id
  source: Source
- id: id2
  source: Source2
estimated_time: 10
hruid: aiz_routeplanner
keywords:
- ''
language: en
licence: dwengo
return_value:
  callback_schema:
    att: test
    att2: test2
  callback_url: callback-url-example
skos_concepts:
- http://ilearn.ilabt.imec.be/vocab/curr1/s-computers-en-systemen
target_ages:
- 14
- 15
- 16
- 17
- 18
teacher_exclusive: true
title: How the route planner works
version: 3
---
# How a route planner works

**Prior knowledge:** The students know what a graph, nodes and edges are. A new type of graph is introduced here, namely the weighted graph. 

### Assignment for the students
*You know the distances in kilometers between certain municipalities, both along major roads and as the crow flies. The municipalities are Gent, Lokeren, Sint-Niklaas, Dendermonde, Antwerpen, Eeklo, Willebroek and Mechelen.<br>
Determine the shortest route between Gent and Mechelen via these roads. How can a computer help?*

![image](https://user-images.githubusercontent.com/48352335/213933739-10534f75-588b-4817-8463-025524b85009.png)
![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)


### Class brainstorm - Problem: Shortest route from Gent to Mechelen via major roads 
Possible ideas during the brainstorm (→ computational thinking – decomposition):<br>
- How do you find the shortest route? 
	- Look at a map to see the location of the cities. That can help in determining the shortest route.
	- Go through possible routes one by one → a visual representation is needed 
	- Calculate the distance of each possible route
	- The shortest route corresponds to the smallest distance
- Make a sketch of the cities and roads (→ pattern recognition/abstraction network → graph)
	- Indicate distances on the sketch (→ weighted graph)  
- How can a computer help? 
	- That already exists → route planner, e.g., Google Maps
	- How does such a route planner actually work?    
	- How to program it so that a computer calculates the distances of the possible routes? 
		- The computer needs distances between the different municipalities
		- You can only reach a municipality if you come from a municipality that is connected to it
		- The roads are two-way, so there is ‘symmetry with equal distance’ (this is clear from the symmetry in the given table)
		- Note: going through all possible routes is actually a waste of time; some municipalities are not eligible due to their location.

### The teacher summarizes the brainstorm
Example:

![image](https://user-images.githubusercontent.com/48352335/213933875-ae28abd8-eacd-4e3b-b5c0-a629119469a2.png)

View the situation in Google Maps:

![image](https://user-images.githubusercontent.com/48352335/213933904-236a21e1-9be4-4028-b475-b7ec9fec1b33.png)
<center>Source: Google Maps</center>  
 
### Technique to determine the shortest path
#### Table with the given distances in km
![image](https://user-images.githubusercontent.com/48352335/213933739-10534f75-588b-4817-8463-025524b85009.png)	

#### Convert the table into a weighted graph
![M024_Graaf_1](https://user-images.githubusercontent.com/48352335/216783604-7ba61dcf-4e7f-41ba-a05f-017c715fb4d5.png)

#### Students try to find the shortest route themselves (manually)
- Which strategy did the students apply?
- It quickly becomes quite a bit of work
        - Using a computer is useful!
	- It would be handy for the computer to go through all possibilities.

#### Check with Google Maps
![image](https://user-images.githubusercontent.com/48352335/213934118-1120ed5a-8dfd-4c2b-8b5d-2e67a6475172.png)

![image](https://user-images.githubusercontent.com/48352335/213934134-7d235d6a-c110-4fe2-a540-ef187417e885.png)

#### Afterwards: algorithm 
- Did the students devise an algorithm?
- Dijkstra's algorithm
- Optionally implement it on the computer with Python
- Python notebook


### Dijkstra's algorithm

<div class="alert alert-box alert-secondary"><p style=" font-family: 'Courier New', monospace; font-size:12px; ">
Initialize the list ‘visited’   # list contains nodes whose neighbors have all been visited<br>
Initialize the list ‘unvisited’ # list contains nodes whose neighbors have not all been visited yet<br><br>
# fill the ‘unvisited’ list (cost is distance, time … depending on the problem)<br>
# all nodes have no previous node<br>
# all nodes except the start node have infinite cost, the start node has cost 0<br>
For each node in graph:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Add node to the ‘unvisited’ list with cost infinity and previous node none<br>
Set the cost of the start node in the ‘unvisited’ list to 0<br><br>
# examine nodes in the ‘unvisited’ list one by one until that list is empty<br>
# each time start with the node with the smallest cost, call that the current node<br>
# consider all neighbors that are not yet in the ‘visited’ list<br>
# for each neighbor, calculate the cost and compare it with the cost it already had<br>
# if the new cost is smaller, update the neighbor’s data in the ‘unvisited’ list<br>
# after examining all its neighbors, move the current node to the ‘visited’ list<br>
While the ‘unvisited’ list is not empty:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Set current node to the node with the lowest cost from the ‘unvisited’ list<br>
&nbsp;&nbsp;&nbsp;&nbsp;Add the current node with its data (cost and previous node) to the ‘visited’ list<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each neighbor node of the current node:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the neighbor node is not in the ‘visited’ list:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate new cost of neighbor = cost of current node + edge cost<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If this new cost is lower than the neighbor’s previous cost:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update neighbor’s cost to the new cost<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update neighbor’s previous node to the current node<br>
&nbsp;&nbsp;&nbsp;&nbsp;Remove current node from the ‘unvisited’ list<br><br>
Return the ‘visited’ list
</p>
</div>

#### For the program, see notebook ‘Dijkstra’.

#### Applying the algorithm
Using a table and a tree structure you look for the shortest route.

![image](https://user-images.githubusercontent.com/48352335/213934175-be5b3e22-4fc8-49ca-83ad-c73cc8f94298.png)
![M024_Boom_1](https://user-images.githubusercontent.com/48352335/216783699-8bd9beb6-c2d6-4155-909a-a88bdac9524b.png)


#### Practice with the algorithm
**Exercise 1**
Source: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Find the shortest path from A to E.*

![image](https://user-images.githubusercontent.com/48352335/213934203-9e5f3b11-c9fa-4745-9935-c115d214e584.png)
 
**Exercise 2**
Source: https://www.bebras.org/sites/default/files/2015%20Bebras%20Solution%20Guide.pdf

Bebras 2015 – Traveling 

Beaver Martina goes to work by train every day. There is no direct line, so she has to transfer. The map shows the lines she can take with the travel time. Martina’s house is indicated by the letter ‘H’, the place where she works by a ‘W’, and the stations by an ‘S’.

*Which route corresponds to the shortest travel time?*

![image](https://user-images.githubusercontent.com/48352335/213934241-97b3a82e-8fe4-4407-a09f-0caa52c83b4a.png)
 
**Exercise 3** 
Source: https://www.curriculumonline.ie/getmedia/da0c349c-d205-47ff-9b43-6c820a62807c/uk-bebras-2016-answers.pdf <br>
Copyright 2016 UK Bebras – Licence: CC-BY-NC-SA 3.0

Bebras 2016 – Cycle paths 

Cleveria is a cyclist. She explores the one-way cycle paths that run through the villages in her area. Each village has a village stone with a letter on it. All the cycle paths have a cycling direction and a distance. The cycling direction and the distance are indicated by the yellow flags.
 
![image](https://user-images.githubusercontent.com/48352335/213934298-cd8a75f8-ef27-4d77-a20c-140770bf3856.png)

On her explorations, Cleveria leaves blue notes under the village stones, containing a number. That number is the shortest distance from the respective village stone to village A. 

*What number goes under village stone E?*

**Exercise 4**
Source: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all 

*Find the shortest path from S to G.*
 
![image](https://user-images.githubusercontent.com/48352335/213934333-5e062113-f283-490c-bd56-6d4fee4bdee2.png)


### Back to the route problem - critical thinking
- Optimization? Note: going through all possible routes is actually a waste of time; some municipalities are not eligible due to their location.

![image](https://user-images.githubusercontent.com/48352335/213933743-2a57ac0f-b76b-4440-96e4-173f275a649b.png)

#### Technique to apply 
See: https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all

You use a heuristic function to get an idea of which municipalities are more opportune to pass through compared to others, taking into account the municipality where the journey is headed.<br>
As a heuristic function (f-score) you use the straight-line distance (for this application this corresponds to the Euclidean distance).

You augment the weighted graph with the straight-line distance.
  
![M024_Graaf_2](https://user-images.githubusercontent.com/48352335/216783645-5910a805-f876-4643-82f1-d98c15c2a48b.png)

Using a table and a tree structure you look for the shortest route.
![image](https://user-images.githubusercontent.com/48352335/213934386-9fe136a5-ff13-46b2-9ec0-42a8161da0de.png)
![M024_Boom_2](https://user-images.githubusercontent.com/48352335/216783661-d320583e-1ad3-4d09-b8a4-7180c9335c93.png)


### A* algorithm
<div class="alert alert-box alert-secondary"><p style="  font-family: 'Courier New', monospace; font-size:12px;">
Initialize the list ‘visited’   # list contains nodes whose neighbors have all been visited<br>
Initialize the list ‘unvisited’ # list contains nodes whose neighbors have not all been visited yet<br><br>    
# fill the ‘unvisited’ list with nodes, cost, f-score and previous node <br>
# cost is distance, time … depending on the problem<br>
# f-score is cost plus heuristic<br>
# all nodes have no previous node<br>
# all nodes except the start node have infinite cost and infinite f-score<br>
# the start node has cost 0, and as f-score its heuristic<br>
For each node in graph:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Add node to the ‘unvisited’ list with cost and f-score infinity, previous node none<br>
Set the cost of the start node in the ‘unvisited’ list to 0<br>
Set the f-score of the start node in the ‘unvisited’ list to its heuristic (= 0 + heuristic)<br><br>
# examine nodes in the ‘unvisited’ list one by one until the current node is the end node<br>
# each time start with the node with the smallest f-score, call that the current node<br>
# consider all neighbors that are not yet in the ‘visited’ list<br>
# for each neighbor, calculate cost and f-score and compare with the cost it already had<br>
# if the new cost is smaller, update the neighbor’s data in the ‘unvisited’ list<br>
# after examining all its neighbors, move the current node to the ‘visited’ list<br>
While the ‘unvisited’ list is not empty:<br>
&nbsp;&nbsp;&nbsp;&nbsp;Set current node to the node with the lowest f-score from the ‘unvisited’ list<br>
&nbsp;&nbsp;&nbsp;&nbsp;Add the current node with data (cost, f-score and previous node) to the ‘visited’ list<br>
&nbsp;&nbsp;&nbsp;&nbsp;If the current node is equal to the end node:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop the while loop<br>
&nbsp;&nbsp;&nbsp;&nbsp;Otherwise:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For each neighbor node of the current node:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the neighbor node is not in the ‘visited’ list:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate new cost of neighbor = cost of current node + edge cost<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If this new cost is lower than the neighbor’s previous cost:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update neighbor’s cost to the new cost<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update f-score to new cost + heuristic<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update neighbor’s previous node to the current node<br>
&nbsp;&nbsp;&nbsp;&nbsp;Remove current node from the ‘unvisited’ list<br><br>
Return the ‘visited’ list
</p>
</div>

#### Learning objectives
- Apply basic graph concepts to represent a route.
- Students develop an algorithm to find the shortest path between two cities.
- Students are introduced to Dijkstra's algorithm, which is suitable for this.
- Illustrate the usefulness of mathematics.

After this component, students can …
- use basic graph concepts within this context
- find the shortest route
- apply Dijkstra's algorithm
- possibly program Dijkstra's algorithm 
- have improved their critical and logical thinking

#### Attainment targets
Graphs, computational thinking, interplay between society and STEM, media literacy, privacy.