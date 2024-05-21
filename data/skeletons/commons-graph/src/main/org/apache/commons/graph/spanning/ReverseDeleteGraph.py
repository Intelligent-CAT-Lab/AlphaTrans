from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class ReverseDeleteGraph(Graph):

    # Class Fields Begin
    __serialVersionUID: int = None
    __graph: Graph[typing.Any, typing.Any] = None
    __sortedEdge: typing.Collection[typing.Any] = None
    __visitedEdge: typing.Collection[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:
        pass

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        pass

    def getSize(self) -> int:
        pass

    def getOrder(self) -> int:
        pass

    def getEdges(self) -> typing.Iterable[typing.Any]:
        pass

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:
        pass

    def getDegree(self, v: typing.Any) -> int:
        pass

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def containsVertex(self, v: typing.Any) -> bool:
        pass

    def containsEdge(self, e: typing.Any) -> bool:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        sortedEdge: typing.Collection[typing.Any],
        visitedEdge: typing.Collection[typing.Any],
    ) -> None:
        pass

    # Class Methods End
