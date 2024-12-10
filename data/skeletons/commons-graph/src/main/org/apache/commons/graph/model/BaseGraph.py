from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Graph import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class BaseGraph(Graph, ABC):

    # Class Fields Begin
    __serialVersionUID: int = None
    __adjacencyList: typing.Dict[typing.Any, typing.Set[typing.Any]] = None
    __allEdges: typing.Set[typing.Any] = None
    __indexedEdges: typing.Dict[VertexPair[typing.Any], typing.Any] = None
    __indexedVertices: typing.Dict[typing.Any, VertexPair[typing.Any]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, obj: typing.Any) -> bool:
        pass

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:
        pass

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        pass

    def getSize(self) -> int:
        pass

    def getOrder(self) -> int:
        pass

    def _getIndexedVertices(self) -> typing.Dict[typing.Any, VertexPair[typing.Any]]:
        pass

    def _getIndexedEdges(self) -> typing.Dict[VertexPair[typing.Any], typing.Any]:
        pass

    def getEdges(self) -> typing.Iterable[typing.Any]:
        pass

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:
        pass

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def _getAllEdges(self) -> typing.Set[typing.Any]:
        pass

    def _getAdjacencyList(self) -> typing.Dict[typing.Any, typing.Set[typing.Any]]:
        pass

    def containsVertex(self, v: typing.Any) -> bool:
        pass

    def containsEdge(self, e: typing.Any) -> bool:
        pass

    @staticmethod
    def _checkGraphCondition(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        pass

    # Class Methods End
