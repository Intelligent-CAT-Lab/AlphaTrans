from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.DefaultTailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultHeadVertexConnector(HeadVertexConnector):

    __edge: typing.Any = None

    __graph: MutableGraph[typing.Any, typing.Any] = None

    def from_(self, head: typing.Any) -> TailVertexConnector[typing.Any, typing.Any]:
        head = Assertions.checkNotNull(head, "Null head vertex not admitted")
        return DefaultTailVertexConnector(self.__graph, self.__edge, head)

    def __init__(
        self, graph: MutableGraph[typing.Any, typing.Any], edge: typing.Any
    ) -> None:
        self.__edge = edge
        self.__graph = graph
