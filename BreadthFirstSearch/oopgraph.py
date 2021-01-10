from __future__ import annotations
from typing import Union


class SearchMangoSellerResult:

    def __init__(self, graph: Graph):
        self.graph = Graph

    def knows_seller(self) -> bool:
        if self.graph       # eh

class Graph:

    def __init__(self,  name: str, sells_mango: bool = False):
        self.name = name
        self.sells_mango = sells_mango

    def find_mango_seller(self, *args):
        raise NotImplementedError


class Leaf(Graph):

    def find_mango_seller(self):
        return 0, self.name, self if self.sells_mango else None


class Node(Graph):

    def __init__(self, name: str, sells_mango: bool = False, leaves: Union[Leaf, Node] = None):
        super().__init__(name, sells_mango)
        if not leaves:
            leaves = []
        self.leaves = leaves

    def find_mango_seller(self, up: Node):
        if self.sells_mango:
            return self
        else:
            for leaf in self.leaves:
                if seller := leaf.find_mango_seller():
                    depth = seller[0] + 1
                    return depth, path, seller = 0, 1, 2
            else:
                return None


