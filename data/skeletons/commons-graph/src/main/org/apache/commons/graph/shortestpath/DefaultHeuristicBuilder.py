from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.shortestpath.ShortestDistances import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.collections.FibonacciHeap import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io
import pathlib

# Imports End


class DefaultHeuristicBuilder(HeuristicBuilder):

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __start: typing.Any = None
    __goal: typing.Any = None
    __weightOperations: OrderedMonoid[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def withHeuristic(
        self, heuristic: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
        weightOperations: OrderedMonoid[typing.Any],
    ) -> None:
        pass

    # Class Methods End
