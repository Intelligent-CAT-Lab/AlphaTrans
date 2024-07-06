from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.model.BaseMutableGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class VisitGraphBuilder(BaseGraphVisitHandler):

    __visitGraph: BaseMutableGraph[typing.Any, typing.Any] = None

    def onCompleted(self) -> Graph[typing.Any, typing.Any]:
        return self.__visitGraph

    def discoverGraph(self, graph: typing.Any) -> None:
        if isinstance(graph, DirectedGraph):
            self.__visitGraph = DirectedMutableGraph()
        else:
            self.__visitGraph = UndirectedMutableGraph()

        for vertex in graph.getVertices0():
            self.__visitGraph.addVertex(vertex)

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        self.__visitGraph.addEdge(head, edge, tail)
        return VisitState.CONTINUE
