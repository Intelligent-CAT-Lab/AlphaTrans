from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Objects import *


class BaseGraph(Graph, ABC):

    __indexedVertices: typing.Dict[typing.Any, VertexPair[typing.Any]] = {}

    __indexedEdges: typing.Dict[VertexPair[typing.Any], typing.Any] = {}

    __allEdges: typing.Set[typing.Any] = set()
    __adjacencyList: typing.Dict[typing.Any, typing.Set[typing.Any]] = {}

    __serialVersionUID: int = -8066786787634472712

    def toString(self) -> str:
        return str(self.__adjacencyList)

    def hashCode(self) -> int:
        return Objects.hash(
            1,
            31,
            [
                self.__adjacencyList,
                self.__allEdges,
                self.__indexedEdges,
                self.__indexedVertices,
            ],
        )

    def equals(self, obj: typing.Any) -> bool:
        if self == obj:
            return True

        if obj is None or type(self) != type(obj):
            return False

        other: BaseGraph = obj
        return Objects.eq(self.__adjacencyList, other.getAdjacencyList())

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:
        return self.__indexedVertices.get(e)

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        return unmodifiableSet(self.__adjacencyList.keys())

    def getSize(self) -> int:
        return len(self.__allEdges)

    def getOrder(self) -> int:
        return len(self.__adjacencyList)

    def _getIndexedVertices(self) -> typing.Dict[typing.Any, VertexPair[typing.Any]]:
        return self.__indexedVertices

    def _getIndexedEdges(self) -> typing.Dict[VertexPair[typing.Any], typing.Any]:
        return self.__indexedEdges

    def getEdges(self) -> typing.Iterable[typing.Any]:
        return unmodifiableCollection(self.__allEdges)

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:

        pass  # LLM could not translate this method

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        self._checkGraphCondition(
            self.containsVertex(v), "Vertex %s does not exist in the Graph", v
        )
        adj = self.__adjacencyList.get(v)
        return unmodifiableSet(adj)

    def _getAllEdges(self) -> typing.Set[typing.Any]:
        return self.__allEdges

    def _getAdjacencyList(self) -> typing.Dict[typing.Any, typing.Set[typing.Any]]:
        return self.__adjacencyList

    def containsVertex(self, v: typing.Any) -> bool:
        return v in self.__adjacencyList

    def containsEdge(self, e: typing.Any) -> bool:
        return e in self.__indexedVertices

    @staticmethod
    def _checkGraphCondition(
        expression: bool,
        errorMessageTemplate: str,
        errorMessageArgs: typing.List[typing.Any],
    ) -> None:
        if not expression:
            raise GraphException(errorMessageTemplate, None, errorMessageArgs)
