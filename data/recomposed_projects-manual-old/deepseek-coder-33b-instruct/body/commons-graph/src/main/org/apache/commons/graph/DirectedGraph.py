from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *


class DirectedGraph(ABC):

    def getOutDegree(self, v: typing.Any) -> int:

        # This is a placeholder method. The actual implementation will depend on the specifics of your graph data structure.
        # Here, we assume that the graph is represented as a dictionary where the keys are the vertices and the values are lists of outgoing edges.

        # Replace the following line with the actual implementation of your graph data structure.
        return len(self.graph[v])

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def getInDegree(self, v: typing.Any) -> int:

        # This method is not implemented in the provided partial Python translation.
        # The actual implementation would depend on the specifics of the DirectedGraph class and its data structure.
        # Here is a placeholder implementation:

        raise NotImplementedError("This method is not implemented yet.")

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass
