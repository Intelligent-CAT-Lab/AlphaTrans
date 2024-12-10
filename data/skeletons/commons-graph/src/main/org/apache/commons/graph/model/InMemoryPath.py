from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Objects import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.Path import *
import typing
from typing import *
import io
import pathlib

# Imports End


class InMemoryPath(Path):

    # Class Fields Begin
    __serialVersionUID: int = None
    __source: typing.Any = None
    __target: typing.Any = None
    __vertices: typing.List[typing.Any] = None
    __edges: typing.List[typing.Any] = None
    __successors: typing.Dict[typing.Any, typing.Any] = None
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

    def getTarget(self) -> typing.Any:
        pass

    def getSource(self) -> typing.Any:
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

    def addConnectionInTail(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def addConnectionInHead(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:
        pass

    def __init__(self, start: typing.Any, target: typing.Any) -> None:
        pass

    def __addConnection(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:
        pass

    # Class Methods End
