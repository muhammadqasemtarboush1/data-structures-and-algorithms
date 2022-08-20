import pytest
from graph.graph import *


# Node can be successfully added to the graph
def test_happy_path_add(gr_data):
    assert gr_data[0].size() == 5


# An edge can be successfully added to the graph
def test_edge_add():
    gg = Graph()
    aa = gg.add_node('A')
    ba = gg.add_node('B')
    gg.add_edge(aa, ba)
    gg.add_edge(ba, aa)
    assert gg.get_neighbors(ba) == [{0, 'A'}]


# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes(gr_data):
    assert len(gr_data[0].get_nodes()) == 5


# Neighbors are returned with the weight between nodes included
def test_get_neighbors(gr_data):
    assert gr_data[0].get_neighbors(gr_data[1]) == [{0, 'B'}, {0, 'E'}, {0, 'C'}]


# The proper size is returned, representing the number of nodes in the graph
def test_size(gr_data):
    assert gr_data[0].size() == 5


@pytest.fixture
def gr_data():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(b, a)
    g.add_edge(a, e)
    g.add_edge(e, a)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)
    return (g, a)
