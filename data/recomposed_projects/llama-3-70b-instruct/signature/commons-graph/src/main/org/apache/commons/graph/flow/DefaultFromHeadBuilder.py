from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.flow.DefaultToTailBuilder import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultFromHeadBuilder(FromHeadBuilder):

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def from_(
        self, head: typing.Any
    ) -> ToTailBuilder[typing.Any, typing.Any, typing.Any]:
        head = Assertions.checkNotNull(
            head, "head vertex has to be specifies when looking for the max flow"
        )
        return DefaultToTailBuilder(self.__graph, self.__weightedEdges, head)

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
