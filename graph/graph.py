from collections import deque


class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)


class Vertex:
    def __init__(self, value):
        """
        Node/vertex constructor
        :param value
        """
        self.value = value

    def __str__(self):
        return self.value


class Edge:
    def __init__(self, vertex, weight=0):
        """
        Edge constructor
         :param vertex , and weight with default weight = 0
         """
        self.weight = weight
        self.vertex = vertex


class Graph:
    def __init__(self):
        """
        Graph constructor
        """
        self.__adj_list = {}

    def add_node(self, value):
        """ Add the node to adj_list as key and value it will be an empty list"""
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        add edge to the key in the adj_list in both keys
        :param start_vertex:
        :param end_vertex:
        :param weight:
        """
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex, weight)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)

    def get_nodes(self):
        """
        will return all the nodes in the graph (keys of the obj)
        :return: Array of keys
        """
        return self.__adj_list.keys()

    def size(self):
        """
        will return the length of the graph
        :return: integer
        """
        return len(self.__adj_list)

    def get_neighbors(self, vertex):
        """
        will return all the neighbors of each vertex that selected
        :param vertex:
        :return: array of neighbors related to selected vertex and the weight of them
        """
        keys = self.__adj_list.get(vertex, [])
        # print(keys)
        arr = []
        for i in keys:
            arr.append((i.vertex.value, i.weight))
        return arr

    def breadth_first(self, start_vertex):
        """
        will return a collection of visited nodes in the order where they visited were visited
        :param start_vertex (Node):
        :return: A array of nodes
        """
        result = []
        visted = set()
        q = Queue()
        q.enqueue(start_vertex)
        visted.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()
            # if current_vertex != start_vertex:
            result.append(current_vertex.value)
            neighbors = self.__adj_list.get(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)
        return result


if __name__ == "__main__":
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


    print(g.breadth_first(a))
