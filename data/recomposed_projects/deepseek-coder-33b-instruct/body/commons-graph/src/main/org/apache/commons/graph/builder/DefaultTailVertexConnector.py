from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultTailVertexConnector(TailVertexConnector):

    __head: typing.Any = None

    __edge: typing.Any = None

    __graph: MutableGraph[typing.Any, typing.Any] = None

    def to(self, tail: typing.Any) -> None:

        tail = checkNotNull(tail, "Null tail vertex not admitted")
        self.__graph.addEdge(self.__head, self.__edge, tail)

    def __init__(
        self,
        graph: MutableGraph[typing.Any, typing.Any],
        edge: typing.Any,
        head: typing.Any,
    ) -> None:

        self.__graph = graph
        self.__edge = edge
        self.__head = head

    def to(self, tail: T) -> None:
        pass
