from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Objects import *


class BaseGraph(Graph, ABC):

    __indexedVertices: Dict[Any, VertexPair[Any]] = {}

    __indexedEdges: typing.Dict[VertexPair[typing.Any], typing.Any] = {}

    __allEdges: Set[Any] = set()

    __adjacencyList: typing.Dict[typing.Any, typing.Set[typing.Any]] = {}

    __serialVersionUID: int = -8066786787634472712

    def toString(self) -> str:

        return str(self.__adjacencyList)

    def hashCode(self) -> int:

        prime = 31
        return (
            hash(1)
            * hash(prime)
            * hash(self.__adjacencyList)
            * hash(self.__allEdges)
            * hash(self.__indexedEdges)
            * hash(self.__indexedVertices)
        )

    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True

        if obj is None or type(self) != type(obj):
            return False

        other = typing.cast(BaseGraph, obj)
        return Objects.eq(self.__adjacencyList, other.getAdjacencyList())

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:

        return self.__indexedVertices.get(e)

    def getVertices0(self) -> typing.Iterable[typing.Any]:

        return typing.cast(
            typing.Iterable[typing.Any], typing.frozenset(self.__adjacencyList.keys())
        )

    def getSize(self) -> int:

        return len(self.__allEdges)

    def getOrder(self) -> int:

        return len(self.__adjacencyList)

    def _getIndexedVertices(self) -> typing.Dict[typing.Any, VertexPair[typing.Any]]:

        return self.__indexedVertices

    def _getIndexedEdges(self) -> typing.Dict[VertexPair[typing.Any], typing.Any]:

        return self.__indexedEdges

    def getEdges(self) -> typing.Iterable[typing.Any]:

        return tuple(self.__allEdges)

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:

        self._checkGraphCondition(
            self.containsVertex(source),
            "Vertex %s does not exist in the Graph",
            [source],
        )
        self._checkGraphCondition(
            self.containsVertex(target),
            "Vertex %s does not exist in the Graph",
            [target],
        )

        return self.__indexedEdges.get(VertexPair(source, target))

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        self._checkGraphCondition(
            self.containsVertex(v), "Vertex %s does not exist in the Graph", [v]
        )
        adj = self.__adjacencyList.get(v)
        return typing.cast(typing.Iterable[typing.Any], tuple(adj))

    def _getAllEdges(self) -> typing.Set[typing.Any]:

        return self.__allEdges

    def _getAdjacencyList(self) -> typing.Dict[typing.Any, typing.Set[typing.Any]]:

        return self.__adjacencyList

    def containsVertex(self, v: typing.Any) -> bool:

        return v in self.__adjacencyList.keys()

    def containsEdge(self, e: typing.Any) -> bool:

        return e in self.__indexedVertices

    @staticmethod
    def _checkGraphCondition(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:

        if not expression:
            error_message = errorMessageTemplate.format(*errorMessageArgs)
            raise GraphException(error_message, None, None)
