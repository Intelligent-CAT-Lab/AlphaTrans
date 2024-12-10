from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io

# Imports End


class RevertedGraph(DirectedGraph):

    # Class Fields Begin
    __serialVersionUID: int = None
    __directedGraph: DirectedGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:
        pass

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        pass

    def getSize(self) -> int:
        pass

    def getOutDegree(self, v: typing.Any) -> int:
        pass

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def getOrder(self) -> int:
        pass

    def getInDegree(self, v: typing.Any) -> int:
        pass

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
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

    def __init__(self, directedGraph: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
