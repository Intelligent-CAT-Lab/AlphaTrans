from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.flow.FlowNetworkHandler import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import typing
from typing import *
import io

# Imports End


class EdgeWrapper:

    # Class Fields Begin
    __wrapped: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def getWrapped(self) -> typing.Any:
        pass

    @staticmethod
    def EdgeWrapper1() -> EdgeWrapper[typing.Any]:
        pass

    def __init__(self, wrapped: typing.Any) -> None:
        pass

    # Class Methods End


class MapperWrapper(Mapper):

    # Class Fields Begin
    __weightOperations: typing.Any = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def map_(self, input_: EdgeWrapper[typing.Any]) -> typing.Any:
        pass

    def __init__(
        self,
        weightOperations: typing.Any,
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End


class DefaultMaxFlowAlgorithmSelector(MaxFlowAlgorithmSelector):

    # Class Fields Begin
    __graph: DirectedGraph[typing.Any, typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __source: typing.Any = None
    __target: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def applyingFordFulkerson(self, weightOperations: typing.Any) -> typing.Any:
        pass

    def applyingEdmondsKarp(self, weightOperations: typing.Any) -> typing.Any:
        pass

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
    ) -> None:
        pass

    def __newFlowNetwok(
        self, graph: DirectedGraph[typing.Any, typing.Any], weightOperations: typing.Any
    ) -> DirectedGraph[typing.Any, EdgeWrapper[typing.Any]]:
        pass

    # Class Methods End
