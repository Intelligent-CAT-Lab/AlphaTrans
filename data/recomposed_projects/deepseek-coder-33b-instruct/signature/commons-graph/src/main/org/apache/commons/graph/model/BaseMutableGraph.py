from __future__ import annotations
import re
import os
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.BaseGraph import *


class BaseMutableGraph(MutableGraph, BaseGraph, ABC):

    __serialVersionUID: int = 1549113549446254183

    def removeVertex(self, v: typing.Any) -> None:

        self._checkGraphCondition(
            v is not None, "Impossible to remove a null Vertex from the Graph"
        )
        self._checkGraphCondition(
            self.containsVertex(v), f"Vertex '{v}' not present in the Graph"
        )

        for tail in self.getAdjacencyList().get(v):
            self.getIndexedEdges().pop(VertexPair(v, tail), None)

        self.getAdjacencyList().pop(v, None)

        self._decorateRemoveVertex(v)

    def removeEdge(self, e: typing.Any) -> None:

        self._checkGraphCondition(
            e is not None, "Impossible to remove a null Edge from the Graph"
        )
        self._checkGraphCondition(
            self.containsEdge(e), f"Edge '{e}' not present in the Graph"
        )

        vertexPair = self.getVertices1(e)
        self._decorateRemoveEdge(e)
        self._internalRemoveEdge(vertexPair.getHead(), e, vertexPair.getTail())

        self.getAllEdges().remove(e)

    def _internalRemoveEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        vertexPair = VertexPair(head, tail)
        self._indexedVertices.pop(e, None)
        self._indexedEdges.pop(vertexPair, None)
        self._adjacencyList[vertexPair.getHead()].discard(vertexPair.getTail())

    def _internalAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        if head not in self._adjacencyList:
            self._adjacencyList[head] = set()
        self._adjacencyList[head].add(tail)

        vertexPair = VertexPair(head, tail)
        self._indexedEdges[vertexPair] = e

        if e not in self._indexedVertices:
            self._indexedVertices[e] = vertexPair

    def addVertex(self, v: typing.Any) -> None:

        self._checkGraphCondition(
            v is not None, "Impossible to add a null Vertex to the Graph"
        )
        self._checkGraphCondition(
            not self.containsVertex(v), f"Vertex '{v}' already present in the Graph"
        )

        self.__adjacencyList[v] = set()

        self._decorateAddVertex(v)

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:

        self._checkGraphCondition(head is not None, "Null head Vertex not admitted")
        self._checkGraphCondition(
            e is not None, "Impossible to add a null Edge in the Graph"
        )
        self._checkGraphCondition(tail is not None, "Null tail Vertex not admitted")
        self._checkGraphCondition(
            self.containsVertex(head), f"Head Vertex '{head}' not present in the Graph"
        )
        self._checkGraphCondition(
            self.containsVertex(tail), f"Tail Vertex '{tail}' not present in the Graph"
        )
        self._checkGraphCondition(
            self.getEdge(head, tail) is None,
            f"Edge {e} is already present in the Graph",
        )

        self.getAllEdges().add(e)

        self._internalAddEdge(head, e, tail)

        self._decorateAddEdge(head, e, tail)

    def _decorateRemoveVertex(self, v: typing.Any) -> None:

        # Your code here
        pass

    def _decorateRemoveEdge(self, e: typing.Any) -> None:

        # Your implementation here
        pass

    def _decorateAddVertex(self, v: typing.Any) -> None:

        # Your implementation here
        pass

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        # Your implementation here
        pass
