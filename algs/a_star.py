#!/usr/bin/python3

## python modules
import collections

class Node(object):
    def __init__(self, info, weight=1, heuristic=0, sort_fn=None):
        self.info = info
        self.weight = weight
        self.heuristic = heuristic
        self.visited = False
        if sort_fn is None:
            sort_fn = lambda x: x.weight
        self.sort_fn = sort_fn
        self.distance = 0
        self.path = []
        self.neighbors = set()

    #######################################################
    def addNeighbors(self, neighbors):
        if not isinstance(neighbors, collections.Iterable):
            neighbors = list(neighbors)
        if not isinstance(next(iter(neighbors)), Node):
            neighbors = set(Node(node) for node in neighbors)
        self.neighbors.update(neighbors)
        return

    def getUnvisitedNeighbors(self):
        ngbrs = [node for node in self.neighbors if not node.visiter]
        return sorted(ngbrs, key=self.sort_fn)




###############################################################################
class Graph(object):
    def __init__(self, nodes=set(), start=None, stop=None):
        if nodes is not None:   ## wait,t his doesnt do what i want yet....
            if not isinstance(next(iter(nodes)), Node):
                nodes = set(Node(node) for node in nodes)
        self.nodes = nodes
        self.start = start
        self.stop = stop
