from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
import typing
from typing import *
import io
import pathlib

# Imports End


class FlowNetworkHandler:

    # Class Fields Begin
    __flowNetwork: DirectedGraph[typing.Any, typing.Any] = None
    __source: typing.Any = None
    __target: typing.Any = None
    __weightOperations: OrderedMonoid[typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __maxFlow: typing.Any = None
    __residualEdgeCapacities: typing.Dict[typing.Any, typing.Any] = None
    __predecessors: PredecessorsList[typing.Any, typing, Any, typing.Any] = None
    __foundAugmentingPath: bool = None
    # Class Fields End

    # Class Methods Begin
    def onCompleted(self) -> typing.Any:
        pass

    def discoverGraph(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:
        pass

    def finishVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def discoverVertex(self, vertex: typing.Any) -> VisitState:
        pass

    def updateResidualNetworkWithCurrentAugmentingPath(self) -> None:
        pass

    def hasAugmentingPath(self) -> bool:
        pass

    def __init__(
        self,
        flowNetwork: DirectedGraph[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
        weightOperations: OrderedMonoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
