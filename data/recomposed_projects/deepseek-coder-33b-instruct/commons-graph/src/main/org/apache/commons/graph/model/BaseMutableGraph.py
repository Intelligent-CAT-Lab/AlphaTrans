from __future__ import annotations
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

        if v is None:
            self.checkGraphCondition(
                False, "Impossible to remove a null Vertex from the Graph"
            )
        elif not self.containsVertex(v):
            self.checkGraphCondition(False, f"Vertex '{v}' not present in the Graph")
        else:
            for tail in self.getAdjacencyList().get(v):
                self.getIndexedEdges().remove(VertexPair(v, tail))
            self.getAdjacencyList().remove(v)
            self._decorateRemoveVertex(v)

    def removeEdge(self, e: typing.Any) -> None:

        if e is None:
            self.checkGraphCondition(
                False, "Impossible to remove a null Edge from the Graph"
            )
        elif not self.containsEdge(e):
            self.checkGraphCondition(False, f"Edge '{e}' not present in the Graph")
        else:
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

        if v is None:
            raise ValueError("Impossible to add a null Vertex to the Graph")

        if self.containsVertex(v):
            raise ValueError(f"Vertex '{v}' already present in the Graph")

        self.getAdjacencyList()[v] = set()

        self._decorateAddVertex(v)

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:

        if head is None:
            self.checkGraphCondition(False, "Null head Vertex not admitted")
        if e is None:
            self.checkGraphCondition(
                False, "Impossible to add a null Edge in the Graph"
            )
        if tail is None:
            self.checkGraphCondition(False, "Null tail Vertex not admitted")
        if not self.containsVertex(head):
            self.checkGraphCondition(
                False, f"Head Vertex '{head}' not present in the Graph"
            )
        if not self.containsVertex(tail):
            self.checkGraphCondition(
                False, f"Head Vertex '{tail}' not present in the Graph"
            )
        if self.getEdge(head, tail) is not None:
            self.checkGraphCondition(False, f"Edge {e} is already present in the Graph")

        self.getAllEdges().add(e)

        self._internalAddEdge(head, e, tail)

        self._decorateAddEdge(head, e, tail)

    def _decorateRemoveVertex(self, v: typing.Any) -> None:

        pass

    def _decorateRemoveEdge(self, e: typing.Any) -> None:

        pass

    def _decorateAddVertex(self, v: typing.Any) -> None:

        pass  # LLM could not translate this method

    def _decorateAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:

        pass
