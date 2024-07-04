from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.DefaultHeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultGrapher(GraphConnector):

    __graph: MutableGraph[typing.Any, typing.Any] = None

    def addVertex(self, node: typing.Any) -> typing.Any:
        node = Assertions.checkNotNull(node, "Null vertex not admitted")
        self.__graph.addVertex(node)
        return node

    def addEdge(self, arc: typing.Any) -> HeadVertexConnector[typing.Any, typing.Any]:

        arc = Assertions.checkNotNull(arc, "Null edge not admitted")
        return DefaultHeadVertexConnector(self.__graph, arc)

    def __init__(self, graph: MutableGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph
