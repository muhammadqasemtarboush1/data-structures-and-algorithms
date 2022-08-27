import pytest
from graph.graph import *
from graph_business_trip.graph_business_trip import *


def test_1(grf):
    # actual = business_trip(grf, [arendelle, manstropolis])
    # expected = (True, '$82')
    assert actual != expected


@pytest.fixture

def grf():
    graph = Graph()
    c1 = graph.add_node('pandora')
    c2 = graph.add_node('arendelle')
    c3 = graph.add_node('metroville')
    c4 = graph.add_node('narina')
    c5 = graph.add_node('naboo')
    c6 = graph.add_node('manstropolis')
    graph.add_edge(c1,c2,82)
    return graph