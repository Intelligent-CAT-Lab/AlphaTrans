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
            self._containsVertex(v), "Vertex '%s' not present in the Graph", v
        )

        for tail in self._getAdjacencyList().get(v):
            self._getIndexedEdges().pop(VertexPair(v, tail))

        self._getAdjacencyList().pop(v)

        self._decorateRemoveVertex(v)

    def removeEdge(self, e: typing.Any) -> None:

        self._checkGraphCondition(
            e is not None, "Impossible to remove a null Edge from the Graph"
        )
        self._checkGraphCondition(
            self.containsEdge(e), "Edge '%s' not present in the Graph" % e
        )
        vertexPair = self.getVertices1(e)
        self._decorateRemoveEdge(e)
        self._internalRemoveEdge(vertexPair.getHead(), e, vertexPair.getTail())
        self.getAllEdges().remove(e)

    def _internalRemoveEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        vertexPair = VertexPair(head, tail)
        self.getIndexedVertices().remove(e)
        self.getIndexedEdges().remove(vertexPair)
        self.getAdjacencyList().get(vertexPair.getHead()).remove(vertexPair.getTail())

    def _internalAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        self.getAdjacencyList()[head].add(tail)

        vertexPair = VertexPair(head, tail)
        self.getIndexedEdges()[vertexPair] = e

        if e not in self.getIndexedVertices():
            self.getIndexedVertices()[e] = vertexPair

    def addVertex(self, v: typing.Any) -> None:

        self._checkGraphCondition(
            v is not None, "Impossible to add a null Vertex to the Graph"
        )
        self._checkGraphCondition(
            not self.containsVertex(v), "Vertex '%s' already present in the Graph" % v
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
            self.containsVertex(head),
            "Head Vertex '%s' not present in the Graph" % head,
        )
        self._checkGraphCondition(
            self.containsVertex(tail),
            "Head Vertex '%s' not present in the Graph" % tail,
        )
        self._checkGraphCondition(
            self.getEdge(head, tail) is None,
            "Edge %s is already present in the Graph" % e,
        )

        self.getAllEdges().add(e)

        self._internalAddEdge(head, e, tail)

        self._decorateAddEdge(head, e, tail)

    def _decorateRemoveVertex(self, v: typing.Any) -> None:
        pass

    def _decorateRemoveEdge(self, e: typing.Any) -> None:
        pass

    def _decorateAddVertex(self, v: typing.Any) -> None:
        pass

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        pass
