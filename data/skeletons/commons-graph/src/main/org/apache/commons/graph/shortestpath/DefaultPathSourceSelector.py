from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
import pathlib

# Imports End


class DefaultPathSourceSelector(PathSourceSelector):

    # Class Fields Begin
    __graph: Graph[typing.Any, typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def from_(
        self, source: typing.Any
    ) -> TargetSourceSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def applyingFloydWarshall(
        self, weightOperations: typing.Any
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    def __pathReconstruction(
        self,
        path: PredecessorsList[typing.Any, typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
        next_: typing.Dict[VertexPair[typing.Any], typing.Any],
    ) -> None:
        pass

    # Class Methods End
