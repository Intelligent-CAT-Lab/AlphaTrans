from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.flow.DefaultMaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultToTailBuilder(ToTailBuilder):

    __head: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def to(
        self, tail: typing.Any
    ) -> MaxFlowAlgorithmSelector[typing.Any, typing.Any, typing.Any]:

        tail = Assertions.checkNotNull(
            tail, "tail vertex has to be specifies when looking for the max flow", []
        )
        return DefaultMaxFlowAlgorithmSelector(
            self.__graph, self.__weightedEdges, self.__head, tail
        )

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        head: typing.Any,
    ) -> None:

        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__head = head
