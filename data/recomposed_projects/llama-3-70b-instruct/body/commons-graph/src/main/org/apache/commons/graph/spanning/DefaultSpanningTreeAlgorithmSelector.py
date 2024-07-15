from __future__ import annotations
import re
import collections
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.collections.DisjointSet import *
from src.main.org.apache.commons.graph.collections.FibonacciHeap import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.spanning.ShortestEdges import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SuperVertex import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultSpanningTreeAlgorithmSelector:

    __source: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def applyingPrimAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        pass  # LLM could not translate this method

    def applyingKruskalAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        pass  # LLM could not translate this method

    def applyingBoruvkaAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        pass  # LLM could not translate this method

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
