from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class RevertedGraph(DirectedGraph):

    __directedGraph: DirectedGraph[typing.Any, typing.Any] = None

    __serialVersionUID: int = 5867643705350331891

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:

        directedVertexPair = self.__directedGraph.getVertices1(e)
        return VertexPair(directedVertexPair.getTail(), directedVertexPair.getHead())

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        return self.__directedGraph.getVertices0()

    def getSize(self) -> int:
        return self.__directedGraph.getSize()

    def getOutDegree(self, v: typing.Any) -> int:
        return self.__directedGraph.getOutDegree(v)

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return self.__directedGraph.getInbound(v)

    def getOrder(self) -> int:
        return self.__directedGraph.getOrder()

    def getInDegree(self, v: typing.Any) -> int:
        return self.__directedGraph.getOutDegree(v)

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return self.__directedGraph.getOutbound(v)

    def getEdges(self) -> typing.Iterable[typing.Any]:
        return self.__directedGraph.getEdges()

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:
        return self.__directedGraph.getEdge(target, source)

    def getDegree(self, v: typing.Any) -> int:
        return self.__directedGraph.getDegree(v)

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        return self.__directedGraph.getConnectedVertices(v)

    def containsVertex(self, v: typing.Any) -> bool:
        return self.__directedGraph.containsVertex(v)

    def containsEdge(self, e: typing.Any) -> bool:
        return self.__directedGraph.containsEdge(e)

    def __init__(self, directedGraph: DirectedGraph[typing.Any, typing.Any]) -> None:

        self.__directedGraph = Assertions.checkNotNull(
            directedGraph, "Adapted DirectedGraph must be not null"
        )
