from typing import Tuple, List, Dict, Any


class Edge:
    def __init__(self, _from: str, _to: str, cost: int):
        self._from = _from
        self._to = _to
        self._cost = cost


class Graph:
    def __init__(self):
        self._graph: Dict[str, List[Edge]] = dict()

    def add_node(self, node: str) -> None:
        if node not in self._graph:
            self._graph[node] = []

    def add_nodes(self, nodes: List[str]) -> None:
        for node in nodes:
            self.add_node(node)

    def add_edges(self, connections: Any) -> None:
        if not isinstance(connections, list):
            exit('bad usage: add_edges (expected list)')
        if isinstance(connections[0], tuple):
            for connection in connections:
                _from, _to, cost = connection
                self._graph[_from].append(Edge(_from, _to, cost))
        elif isinstance(connections[0], Edge):
            for connection in connections:
                self._graph[connection._from].append(connection)

    def remove_node(self, node: str) -> None:
        if node not in self._graph:
            return

        for node, edges in self._graph.items():
            self._graph[node] = [e for e in edges if e._from is not node and e._to is not node]
        del self._graph[node]


if __name__ == '__main__':
    G = Graph()
    G.add_nodes(['s', 't'])
    G.add_edges([('s', 't', 3)])

    G.add_node('a')
    connections = [Edge('s', 'a', 1), Edge('a', 't', 1)]
    G.add_edges(connections)
