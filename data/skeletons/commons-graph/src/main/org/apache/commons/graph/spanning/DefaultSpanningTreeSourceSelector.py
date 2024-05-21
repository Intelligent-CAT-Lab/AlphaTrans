from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.ReverseDeleteGraph import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultSpanningTreeSourceSelector:

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def fromSource(
        self, source: typing.Any
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def fromArbitrarySource(
        self,
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingReverseDeleteAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
