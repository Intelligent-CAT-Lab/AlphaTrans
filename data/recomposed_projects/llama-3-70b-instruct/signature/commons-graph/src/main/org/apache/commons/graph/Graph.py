from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.VertexPair import *


class Graph(ABC):

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:
        return VertexPair(self.getVertex1(e), self.getVertex2(e))

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        return self.getVertices()

    def getSize(self) -> int:
        return self.vertexSet.size()

    def getOrder(self) -> int:
        return self.order

    def getEdges(self) -> typing.Iterable[typing.Any]:
        return self.edges

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:
        return self.getEdge(source, target)

    def getDegree(self, v: typing.Any) -> int:
        return self.getEdges(v).size()

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        pass  # LLM could not translate this method

    def containsVertex(self, v: typing.Any) -> bool:
        return v in self.vertices

    def containsEdge(self, e: typing.Any) -> bool:
        return self.getEdges().contains(e)
