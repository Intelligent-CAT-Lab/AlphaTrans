from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io

# Imports End


class ShortestEdges:

    # Class Fields Begin
    __predecessors: typing.Dict[typing.Any, typing.Any] = None
    __weightOperations: OrderedMonoid[typing.Any] = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __graph: Graph[typing.Any, typing.Any] = None
    __source: typing.Any = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def isEmpty(self) -> bool:
        pass

    def hasWeight(self, vertex: typing.Any) -> bool:
        pass

    def getWeight(self, vertex: typing.Any) -> typing.Any:
        pass

    def createSpanningTree(self) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        pass

    def compare(self, left: typing.Any, right: typing.Any) -> int:
        pass

    def addPredecessor(self, tail: typing.Any, head: typing.Any) -> None:
        pass

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        source: typing.Any,
        weightOperations: OrderedMonoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        pass

    @staticmethod
    def __addEdgeIgnoringExceptions(
        vertex: typing.Any,
        spanningTree: MutableSpanningTree[typing.Any, typing.Any, typing.Any],
    ) -> None:
        pass

    # Class Methods End
