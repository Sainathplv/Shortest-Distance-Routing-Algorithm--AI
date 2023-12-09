# Shortest-Distance-Routing-Algorithm--AI

TASK-1
———————————————  ALGORITHM USED —————————— 
1.UNINFORMED SEARCH	:	UNIFORM COST SEARCH ALGORITHM IS USED FOR THIS 

2.INFORMED SEARCH	:	A* SEARCH ALGORITHM  IS USED FOR THIS 



———————————————	PROGRAMMING LANGUAGE   	————————	
	PROGRAMMING LANGUAGE	:		PYTHON 3
	IDE  : Pycharm


———————————————	PROGRAMMING LANGUAGE   	————————
1)Intially
 we need find a search algorithm for a given text file
 if the text file has source,destination,and distance
 so firstly we need to get the data from the lines and seperate them as source,destination,and distance
 and then plot a graph to that
created a plotgraph(function)

2)if it is heuristic file
created a heuristic read function

3)then created informed search function
A* SEARCH ALGORITHM  IS USED


4)created a uninformed search function
UNIFORM COST SEARCH ALGORITHM IS USED

5) main function






—————————	RUNNING THE CODE ————————————	
NOTE		:	ALL THE INPUT FILE MUST BE IN THE SAME FOLDER	
			THE SOURCE AND DESTINATION ARE CASE-SENSITIVE

RUN :

You can use either pycharm or OPEN TERMINAL

if it is in pycharm open Terminal in pycharm and do the sam process as in open terminal(written below)

OPEN TERMINAL AND DIRECT YOURSELF TO WHERE THE FILE IS SAVED USING CD COMMAND to TASK-1.

SINCE THIS IS A PYTHON 3 FILE . YOUR COMMAND MUST INCLUDE python3 

Next the file name . As this is a python file will have the extension .py : find_route.py

  —command for UCS implementation ——

COMMAND	:	python3 find_route.py input1.txt source destination

EXAMPLE	:	python3 find_route.py input1.txt Bremen Kassel
	
	Output :
	========
Uninformed Search Algorithm -- Uniform Cost Search
Generated: 19
Expanded: 12
Maximum nodes: 11
Distance:  297
Path:
Bremen to Hannover: 132 kms
Hannover to Kassel: 165 kms




  —— A* implementation ——— 
COMMAND	:	python3 find_route.py input1.txt source destination h_kassel.txt

EXAMPLE	:	python3 find_route.py input1.txt Bremen Kassel h_kassel.txt

	Output :
	========
Generated: 9
Expanded: 4
Maximum nodes: 7
Distance:  297
Path:
Bremen to Hannover: 132 kms
Hannover to Kassel: 165 kms

  —— References ———

  # ref : https://www.geeksforgeeks.org/python-create-graph-from-text-file/
  # ref : https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all
  # ref : https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs/
  # ref : https://towardsdatascience.com/search-algorithm-dijkstras-algorithm-uniform-cost-search-with-python-ccbee250ba9
  
