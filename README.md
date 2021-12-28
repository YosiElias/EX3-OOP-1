# Oop_Ex3
![This is an image](https://github.com/roee-tal/EX3-OOP/blob/main/data%20for%20git/welcome.jpeg)
This project is the fourth task in the course. The task implements a data structure of weighted and directional gragh but this time in **PYTHON**. The project implements a number of algorithms on the graph including calculate a short path between two vertices in the graph, the ability to implement graphical interface presenting the graph, and load json files to be a graph and more. 


## Table of contents
* [Main classes planning](#Main-classes-planning)
* [Graph Class](#Graph-Class)
* [GraphAlgo class](#GraphAlgo-class)
* [Implementations and principles](#Implementations-and-principles)
* [GUI-Explanation and how to run](#GUI-Explanation-and-how-to-run)
* [Performances](#Performances)
* [Visualization](#Visualization)
* [External info](#External-info)



###  Main classes planning
> The project has 2 abstract classes to implement. We used few classes for implementation:
* Node class
* Edge class
* Graph class
* Graph algorithm class

### Graph Class
> This class implements Graph Interface. The class contains inner classes - **Node**- and **Edge**-. Few words on those classes:

#### Node class
Every made every node to have:
* id
* position(tuple)
* info(saves the total weight of the edge goes into him - used for short path and more)
* tag(saves the node id which he came from - used for short path and more)
* visit(used for short path and more)
* maxDist(used for center)

#### Edge class
Every edge has his own weight, source, and dest.


> NOTE: The main idea was to use the unique id that every node have and to access him with complexity if o(1) with dictionary.
The graph will save all the relevant data about each node and edge in the graph, so we can check some algorithm with a better complexity.

#### Back to Graph Class
 This class represents a Directional Weighted Graph. It supports a large number of nodes.
 This implementation dictionaries. Each graph has few fields:
 * Nodes = dict of all nodes in the graph
 * Edges = dict of all edges in the graph
 * Edges from = dict of dicts which every node has dict of all the edges that goes **out** of him
 * Edges from = dict of dicts which every node has dict of all the edges that goes **into** him
 * MC : Mode Count, a variable that stored the amount of changes(add node, remove node, add edge, remove edge)made in this graph.
 
> NOTE: because the graph is directed - the 2 dict of dicts are probably different, so we decided to keep them both as fiels - this will help us in the algorithms as we see next.

### Methods
*addNode* - adds a new node to the graph with the given node_data.

*addEdge* - adds a new edge to the graph with the given node_data.

*remove edge* - Deletes the edge from the graph.

*remove node* - Deletes the node from the graph.

*sizes* - of the nodes and the edges dicts.

*get all_in\out_edges_of_node* - return all edges goes out\into every node.


## GraphAlgo class
This class implements GraphAlgo interface. The only field in the class is a weighted graph on which we want to perform the methods.

#### methods
- *load from json* - loads the graph to the structure from the json.
- *ShortestPathDist* - returns the weight of the shortest path between src to dest, and the list of nodes we've go through in the way. This method uses dijkstra algorithm that will be detailed below. 
- *center* - finds the NodeData which minimizes the max distance to all the other nodes. 
- *Tsp* - computes a list of consecutive nodes which go over all the nodes in cities. the sum of the weights of all the consecutive (pairs) of nodes (directed) is the "cost" of the solution - the lower the better.
- *save* - saves this weighted (directed) graph to the given file name - in JSON format

## Implementations and principles
* As said before, we used dicts to store the graph. 

* **functions**   
   - *ShortestPath* - 
       -In this function, we implemented based on Dijkstra algorithm, in the implementation we use Priority Queue of python - to improve the complexity.
          
       -first, we put the source node in the Priority Queue, with weight 0. Then - move all his neighbours(edges goes out of him) and update(if neccesary - accordind to dijkstra) their weight and tag. 
       
       -Then - only if those neighbours haven't been in the queue - put them in the queue with the updated weight.
       
       -Next - take out the next node (with lower weight) and repeat the process. Do this while the queue is not empty.
       
       -Each node will be only one time in the queue.
       
       -Note: Every node has **'info'** field - that there we update the weight, and **'tag'** field - which saves the recent node that he came from. This is make the imlementation easier, because the access to the information and its update is much comfortable.
       
       -Instead of search the minimum node weight (that takes O(n)) the 'get' of the Priority Queue takes(O(logn)).
       
       -As we said, when the queue is empty, the loop is over, and then we move to the second thing - return list of the path of the node id.
       we start from the dest node, check his tag, returns the node with the matching id to the tag, and so on, until we get the source node.
       
       -We also used shortest path to calculate center and tsp.  


     

   - *Center* - based on shortest path.To efficient run time - 'Shortest path' also calculate the distance from source node to all other nodes, so first we check for each node the distances to all other nodes, and update the 'maxDist' field to every node(the furthest node by weight). Then return the node with the **lower** maxDist 
(Note: we dont need to check fron every node to every node).

* **Junit** - In order to check the implementations we also used the given json files and we also create a graph from a small json file so we can follow more intensive                for the methods and how they works step by step using debug.
     * Because the task contains a lot of classes and code, we used junit at every step to check everything works well - the aspect of the correctness and also the aspect of          the performances.
     * We follow to order on main.py(we check every 'check'(check0...) step by step
     * We create 2 classes of test - one for the Graph class, and second for the GraphAlgo class.
     * If the check for some method has failed - most of the time we make intensive examination on the small graph we created because it is easier to follow, and then changed the implementation until the method passed for all jsons.


## GUI-Explanation and how to run
In order to run the algorithms on a particular graph with our GUI:
   1.	Run the function ' plot_graph' from 'GraphAlgo'.
          * The graph will now be displayed in a new window where you can perform all the steps below.
   2.	You can now execute all the algorithms by click 'esc' and then selecting the menu 'Function'   ->  'algorithm function name' (e.g.  'center'). 
          * Now for each function that requires input, a new input window will be displayed depending on the selected function.
          * When you have finished entering the input (according to the instructions in the window), press 'Play' and the input window will close automatically
          * **Note**: A valid input must be entered (for example, do not enter an id Node that does not exist in the graph on 'shortPath' function).
   If you do so, a corresponding error message will be received in a new window.
          *	**Note**: In the 'TSP' and 'shortPath'  functions the data must be entered with a 'space' (as explained in the window itself).
   3.	You can edit the graph you loaded by click 'esc' and then selecting the menu 'Edit'  ->  'Edit funftion' (e.g.  'Add Node').
   	      * **Note**: A valid input must be entered (for example, do not enter an id Node that does not exist in the graph on 'Remove Node' function).
                      If you do so, a corresponding error message will be received in a new window.
   4.	In addition, you can perform general operations on the graph, such as loading a new graph, saving the graph in a JSON file, and exiting the program (by click 'esc' and           then selecting the menu 'File').
         *	**Note**: If you load a new graph, the current graph will be automatically deleted from the board and the new graph will be displayed in its place.
         * **Note**: Because we made a GUI, when function 'plot_graph' is enabled the program will continue to run the GUI but will not continue to run the file from which it                      was called.
         * We were instructed to leave it that way, but write a note so that the assignment checker knows it.
         * In addition, we created a simpler plot in order to appropriate the assignment in the best way, which can be run by the 'plot_graph_small' function. 


## Visualization
json1 with tsp function of some nodes:
![This is an image](https://github.com/YosiElias/Ex2-OOP/blob/master/Ex2/src/resources/TSPgraph.jpeg)

json2 with shortest path between 2 nodes
![This is an image](https://github.com/YosiElias/Ex2-OOP/blob/master/Ex2/src/resources/GraphShort.jpeg)

json2 after removing 3 nodes
![This is an image](https://github.com/YosiElias/Ex2-OOP/blob/master/Ex2/src/resources/Graph2.jpeg)



### External info

* More about directed weighted graph:  [http://math.oxford.emory.edu/site/cs171/directedAndEdgeWeightedGraphs/](http://math.oxford.emory.edu/site/cs171/directedAndEdgeWeightedGraphs/)

* More about Dijkstra's algorithm:
 [https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)



