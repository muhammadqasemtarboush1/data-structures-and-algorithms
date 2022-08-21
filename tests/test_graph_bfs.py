import pytest
from graph.graph import *


def test_breadth_first(graph_da):
    assert graph_da[0].breadth_first(graph_da[1]) == ['A', 'B', 'D', 'C', 'E', 'K']

def test_breadth_first_2(graph_da):
    assert graph_da[0].breadth_first(graph_da[2]) == ['C', 'D', 'K', 'B', 'E', 'A']



@pytest.fixture
def graph_da():
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    k = g.add_node('K')
    g.add_edge(a, b)
    g.add_edge(b, d)
    g.add_edge(c, d)
    g.add_edge(e, d)
    g.add_edge(c, k)
    return [g,a,c]
