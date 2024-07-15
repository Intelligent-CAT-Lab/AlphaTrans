from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.DefaultGrapher import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.GraphConnector import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultLinkedConnectionBuilder(LinkedConnectionBuilder):

    __graph: typing.Any = None

    def withConnections(
        self, graphConnection: GraphConnection[typing.Any, typing.Any]
    ) -> typing.Any:

        graphConnection = Assertions.checkNotNull(
            graphConnection, "Input graph cannot be configured with null connections"
        )

        grapher = DefaultGrapher(self.__graph)
        graphConnection.connect(grapher)

        return self.__graph

    def __init__(self, graph: typing.Any) -> None:
        self.__graph = graph
