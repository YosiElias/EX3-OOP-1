from random import seed, randrange, random
from unittest import TestCase
import unittest


from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

class TestGraph(TestCase):

    def test_load(self):
        g_algo = GraphAlgo()
        file1 = '../data/A5.json'
        file2 = '../data/A1.json'
        file3 = '../data/A3.json'
        g_algo.load_from_json(file1)
        self.assertEqual(g_algo._graph.v_size(),48)
        g_algo.load_from_json(file2)
        self.assertEqual(g_algo._graph.v_size(),17)
        g_algo.load_from_json(file3)
        self.assertEqual(g_algo._graph.v_size(), 49)


    def test_center_new(self):
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g_algo = GraphAlgo(g)
        i,d = g_algo.centerPoint()
        # inf because the graph is not connected
        self.assertEqual(None, i)
        g.add_edge(3, 0, 1.9)
        i,d = g_algo.centerPoint()
        # now the graph is connected
        self.assertEqual(1, i)


    def test_center_A1(self):
        graph = GraphAlgo()
        f1 = "../data/A1.json"
        graph.load_from_json(f1)
        i, d = GraphAlgo.centerPoint(graph)
        self.assertEqual(8,i)


    def test_center_algo_A5(self):
        graph = GraphAlgo()
        file = "../data/A5.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.centerPoint(graph)
        self.assertEqual(40, j)

    def test_center_1000(self):
        graph = GraphAlgo()
        file = r"C:\Users\97254\PycharmProjects\Ex3\data\1000Nodes.json"
        graph.load_from_json(file)
        i,d = GraphAlgo.centerPoint(graph)
        self.assertEqual(362, i)

    # test on the json file we created
    def test_center_algo(self):
        graph = GraphAlgo()
        file = "../data/algo.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.centerPoint(graph)
        # there is no center - the graph in not connected
        self.assertEqual(None, j)


    # SHORTEST PATH TESTS

    def test_short_path_algo(self):
        graph = GraphAlgo()
        file = "../data/algo.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.shortest_path(graph, 0,1)
        self.assertEqual([0,2,3,1], e)

        i,d = GraphAlgo.shortest_path(graph, 1,0)
        self.assertEqual(float('inf'),i)
        self.assertEqual([],d)

    def test_short_path_A1(self):
        graph = GraphAlgo()
        file = "../data/A3.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.shortest_path(graph, 3,11)
        self.assertEqual([3, 31, 30, 20, 11], e)


    def test_short_path_1000(self):
        graph = GraphAlgo()
        file = r"C:\Users\97254\PycharmProjects\Ex3\data\1000Nodes.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.shortest_path(graph, 260,13)
        self.assertEqual([260, 826, 927, 889, 566, 13], e)
        self.assertEqual(561.4059279239871,j)

    def test_short_path_10k(self):
        graph = GraphAlgo()
        file = "../data/10000Nodes.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.shortest_path(graph,987,8324)
        self.assertEqual([987, 8119, 8704, 8122, 5607, 195, 4555, 7055, 9178, 8324], e)

    def test_short_path_100k(self):
        graph = GraphAlgo()
        file = r"C:\Users\97254\PycharmProjects\Ex3\data\100000.json"
        graph.load_from_json(file)
        j,e = GraphAlgo.shortest_path(graph, 1,22090)
        self.assertEqual(814.3408619971573,j)

    def test_short_path_10(self):
        graph = GraphAlgo()
        # file = "../data/10000Nodes.json"
        # graph.load_from_json(file)
        graph._graph = graph_creator(num_of_nodes=2, num_of_ed=1)
        graph.plot_graph()
        # j,e = GraphAlgo.shortest_path(graph,987,8324)
        # self.assertEqual([987, 8119, 8704, 8122, 5607, 195, 4555, 7055, 9178, 8324], e)

    def test_tsp(self):
        graph = GraphAlgo()
        file = r"C:\Users\97254\PycharmProjects\Ex3\data\100000.json"
        graph.load_from_json(file)
        ans = graph.TSP([1, 3, 5, 7, 9, 0])
        # self.assertEqual(ans[1],1.8884659521433524)
        self.assertEqual(ans[1], [1, 0])


def graph_creator(num_of_nodes: int, num_of_ed: int):
    seed(1)
    graph = DiGraph()
    i = 0
    while i < num_of_nodes:
        graph.add_node(i)
        i = i + 1
    for n in graph.getN().values():
        while len(graph.all_out_edges_of_node(n.get_id())) < 20:
            # rnd = randrange(0, num_of_nodes)
            rnd2 = randrange(0, num_of_nodes)
            rnd3 = random()
            if n.get_id() != rnd2:
                graph.add_edge(n.get_id(), rnd2, rnd3 * 100)
    # while graph.e_size() < num_of_ed:
    #     rnd = randrange(0, num_of_nodes)
    #     rnd2 = randrange(0, num_of_nodes)
    #     rnd3 = random()
    #     if rnd != rnd2:
    #         graph.add_edge(rnd, rnd2, rnd3 * 100)
    return graph