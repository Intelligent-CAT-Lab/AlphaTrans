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
            v != None, "Impossible to remove a null Vertex from the Graph", []
        )
        self._checkGraphCondition(
            self.containsVertex(v), "Vertex '%s' not present in the Graph", [v]
        )

        for tail in self.getAdjacencyList().get(v):
            self.getIndexedEdges().remove(VertexPair(v, tail))
        self.getAdjacencyList().remove(v)

        self._decorateRemoveVertex(v)

    def removeEdge(self, e: typing.Any) -> None:
        checkGraphCondition(
            e != None, "Impossible to remove a null Edge from the Graph"
        )
        checkGraphCondition(containsEdge(e), "Edge '%s' not present in the Graph", e)
        vertexPair = getVertices1(e)
        decorateRemoveEdge(e)
        internalRemoveEdge(vertexPair.getHead(), e, vertexPair.getTail())
        getAllEdges().remove(e)

    def _internalRemoveEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        vertexPair = VertexPair(head, tail)
        self.__indexedVertices.pop(e)
        self.__indexedEdges.pop(vertexPair)
        self.__adjacencyList.get(vertexPair.getHead()).remove(vertexPair.getTail())

    def _internalAddEdge(
        self, head: typing.Any, e: typing.Any, tail: typing.Any
    ) -> None:
        self.__adjacencyList.get(head).add(tail)

        vertexPair = VertexPair(head, tail)
        self.__indexedEdges.put(vertexPair, e)

        if not self.__indexedVertices.containsKey(e):
            self.__indexedVertices.put(e, vertexPair)

    def addVertex(self, v: typing.Any) -> None:
        self._checkGraphCondition(
            v != None, "Impossible to add a null Vertex to the Graph", []
        )
        self._checkGraphCondition(
            not self.containsVertex(v), "Vertex '%s' already present in the Graph", [v]
        )

        self._getAdjacencyList().put(v, LinkedHashSet())

        self._decorateAddVertex(v)

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:
        self._checkGraphCondition(head != None, "Null head Vertex not admitted", [])
        self._checkGraphCondition(
            e != None, "Impossible to add a null Edge in the Graph", []
        )
        self._checkGraphCondition(tail != None, "Null tail Vertex not admitted", [])
        self._checkGraphCondition(
            self.containsVertex(head),
            "Head Vertex '%s' not present in the Graph",
            [head],
        )
        self._checkGraphCondition(
            self.containsVertex(tail),
            "Head Vertex '%s' not present in the Graph",
            [tail],
        )
        self._checkGraphCondition(
            self.getEdge(head, tail) == None,
            "Edge %s is already present in the Graph",
            [e],
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
        self.decorateAddEdge(head, e, tail)
