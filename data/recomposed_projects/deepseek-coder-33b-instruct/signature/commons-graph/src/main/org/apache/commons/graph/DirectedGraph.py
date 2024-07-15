from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *


class DirectedGraph(ABC):

    def getOutDegree(self, v: typing.Any) -> int:

        # Assuming that the graph is represented as a dictionary where the keys are the vertices and the values are lists of the vertices that are connected to the key vertex.
        # The out-degree of a vertex is the number of edges going out from it.

        if v in self.graph:
            return len(self.graph[v])
        else:
            return 0

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        # Your implementation here
        pass

    def getInDegree(self, v: typing.Any) -> int:

        # Assuming that the graph is represented as a dictionary where the keys are the vertices and the values are lists of vertices that are connected to the key vertex.
        # The in-degree of a vertex is the number of edges pointing to it.

        in_degree = 0
        for vertex in self.graph:
            if v in self.graph[vertex]:
                in_degree += 1
        return in_degree

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        # The actual implementation of this method depends on the specific implementation of the DirectedGraph class.
        # Here is a placeholder implementation that returns an empty list.

        return []
