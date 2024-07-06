from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.VertexPair import *


class ReverseDeleteGraph(Graph):

    __visitedEdge: typing.Collection[typing.Any] = None

    __sortedEdge: typing.Collection[typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    __serialVersionUID: int = -543197749473412325

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:

        pass  # LLM could not translate this method

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        return self.__graph.getVertices0()

    def getSize(self) -> int:
        return len(self.__sortedEdge) + len(self.__visitedEdge)

    def getOrder(self) -> int:
        return self.__graph.getOrder()

    def getEdges(self) -> typing.Iterable[typing.Any]:
        e: List[WE] = []
        e.extend(self.__sortedEdge)
        e.extend(self.__visitedEdge)
        return e

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:
        edge = self.__graph.getEdge(source, target)
        if edge in self.__sortedEdge:
            return edge
        if edge in self.__visitedEdge:
            return edge
        return None

    def getDegree(self, v: typing.Any) -> int:
        raise GraphException("Unused Method", None, None)

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        tmp: List[typing.Any] = []
        for originalVertex in self.__graph.getConnectedVertices(v):
            if self.getEdge(v, originalVertex) is not None:
                tmp.append(originalVertex)
        return tmp

    def containsVertex(self, v: typing.Any) -> bool:
        return self.__graph.containsVertex(v)

    def containsEdge(self, e: typing.Any) -> bool:
        return self.__graph.containsEdge(e)

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        sortedEdge: typing.Collection[typing.Any],
        visitedEdge: typing.Collection[typing.Any],
    ) -> None:
        self.__graph = graph
        self.__sortedEdge = sortedEdge
        self.__visitedEdge = visitedEdge
