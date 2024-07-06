from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityBuilder import *
from src.main.org.apache.commons.graph.connectivity.DefaultConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultConnectivityBuilder(ConnectivityBuilder):

    __graph: Graph[typing.Any, typing.Any] = None

    def includingVertices(
        self, vertices: typing.List[typing.Any]
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        vertices = Assertions.checkNotNull(
            vertices,
            "Graph connectivity cannote be applied on null vertices array, use no-args if you intend specify no vertices",
        )
        return DefaultConnectivityAlgorithmsSelector(self.__graph, vertices)

    def includingAllVertices(
        self,
    ) -> ConnectivityAlgorithmsSelector[typing.Any, typing.Any]:
        return DefaultConnectivityAlgorithmsSelector(
            self.__graph, self.__graph.getVertices0()
        )

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:
        self.__graph = graph
