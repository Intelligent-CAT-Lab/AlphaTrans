from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultSpanningWeightedEdgeMapperBuilder:

    __graph: Graph[typing.Any, typing.Any] = None

    def whereEdgesHaveWeights(
        self, weightedEdges: Mapper[typing.Any, typing.Any]
    ) -> SpanningTreeSourceSelector[typing.Any, typing.Any, typing.Any]:

        weightedEdges = Assertions.checkNotNull(
            weightedEdges, "Function to calculate edges weight can not be null."
        )
        return DefaultSpanningTreeSourceSelector(self.__graph, weightedEdges)

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:
        self.__graph = graph
