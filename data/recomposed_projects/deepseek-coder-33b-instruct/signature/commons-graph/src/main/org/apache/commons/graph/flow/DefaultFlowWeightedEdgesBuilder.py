from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.flow.DefaultFromHeadBuilder import *
from src.main.org.apache.commons.graph.flow.FlowWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultFlowWeightedEdgesBuilder:

    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def whereEdgesHaveWeights(
        self, weightedEdges: typing.Any
    ) -> FromHeadBuilder[typing.Any, typing.Any, typing.Any]:

        weightedEdges = Assertions.checkNotNull(
            weightedEdges, "Function to calculate edges weight can not be null."
        )
        return DefaultFromHeadBuilder(self.__graph, weightedEdges)

    def __init__(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph
