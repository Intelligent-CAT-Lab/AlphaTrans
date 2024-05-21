from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class DefaultSpanningWeightedEdgeMapperBuilder:

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def whereEdgesHaveWeights(
        self, weightedEdges: Mapper[typing.Any, typing.Any]
    ) -> SpanningTreeSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(self, graph: Graph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
