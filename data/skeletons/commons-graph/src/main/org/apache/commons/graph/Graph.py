from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.VertexPair import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class Graph(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:
        pass

    def getVertices0(self) -> typing.Iterable[typing.Any]:
        pass

    def getSize(self) -> int:
        pass

    def getOrder(self) -> int:
        pass

    def getEdges(self) -> typing.Iterable[typing.Any]:
        pass

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:
        pass

    def getDegree(self, v: typing.Any) -> int:
        pass

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        pass

    def containsVertex(self, v: typing.Any) -> bool:
        pass

    def containsEdge(self, e: typing.Any) -> bool:
        pass

    # Class Methods End
