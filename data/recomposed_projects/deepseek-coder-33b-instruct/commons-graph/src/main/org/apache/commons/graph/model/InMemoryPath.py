from __future__ import annotations
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Path import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.utils.Objects import *


class InMemoryPath(Path):

    __indexedVertices: Dict[Any, VertexPair[Any]] = {}

    __indexedEdges: Dict[VertexPair[Any], Any] = {}

    __successors: Dict[Any, Any] = {}

    __edges: List[Any] = []

    __vertices: List[Any] = []
    __target: typing.Any = None
    __source: typing.Any = None

    __serialVersionUID: int = -7248626031673230570

    def toString(self) -> str:

        return "InMemoryPath [vertices={}, edges={}]".format(
            self.__vertices, self.__edges
        )

    def hashCode(self) -> int:

        prime = 31
        result = 1
        result = prime * result + hash(self.__edges)
        result = prime * result + hash(self.__vertices)
        result = prime * result + hash(self.__source)
        result = prime * result + hash(self.__target)
        return result

    def equals(self, obj: typing.Any) -> bool:

        if self is obj:
            return True

        if obj is None or self.__class__ != obj.__class__:
            return False

        other = typing.cast(InMemoryPath, obj)
        return (
            eq(self.__source, other.getSource())
            and eq(self.__target, other.getTarget())
            and eq(self.__vertices, other.getVertices0())
            and eq(self.__edges, other.getEdges())
        )

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:

        return self.__indexedVertices.get(e)

    def getVertices0(self) -> typing.Iterable[typing.Any]:

        return tuple(self.__vertices)

    def getTarget(self) -> typing.Any:

        return self.__target

    def getSource(self) -> typing.Any:

        return self.__source

    def getSize(self) -> int:

        return len(self.__edges)

    def getOrder(self) -> int:

        return len(self.__vertices)

    def getEdges(self) -> typing.Iterable[typing.Any]:

        return tuple(self.__edges)

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:

        vertex_pair = VertexPair(source, target)

        if vertex_pair in self.__indexedEdges:
            return self.__indexedEdges[vertex_pair]
        else:
            return None

    def getDegree(self, v: typing.Any) -> int:

        v = checkNotNull(v, "Impossible to get the degree of a null vertex")
        checkArgument(
            v in self.__successors,
            "Impossible to get the degree of input vertex; %s not contained in this path",
            v,
        )

        if self.__source == v or self.__target == v:
            return 1

        return 2

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        v = checkNotNull(v, "Impossible to get the degree of a null vertex")

        if self.__target == v:
            return None

        checkArgument(
            v in self.__successors,
            "Impossible to get the degree of input vertex; %s not contained in this path",
            v,
        )

        connected = list(self.__successors[v])
        return connected

    def containsVertex(self, v: typing.Any) -> bool:

        return v in self.__vertices

    def containsEdge(self, e: typing.Any) -> bool:

        return e in self.__edges

    def addConnectionInTail(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:

        self.__vertices.append(head)
        self.__edges.append(edge)

        if self.__target == tail:
            self.__vertices.append(tail)

        self.__addConnection(head, edge, tail)

    def addConnectionInHead(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:

        if self.__target == tail:
            self.__vertices.insert(0, tail)

        self.__vertices.insert(0, head)
        self.__edges.insert(0, edge)

        self.__addConnection(head, edge, tail)

    def __init__(self, start: typing.Any, target: typing.Any) -> None:

        # Importing the checkNotNull method from Assertions class
        from src.main.org.apache.commons.graph.utils.Assertions import checkNotNull

        self.__source = checkNotNull(start, "Path source cannot be null")
        self.__target = checkNotNull(target, "Path target cannot be null")

    def __addConnection(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> None:

        self.__successors[head] = tail

        vertexPair = VertexPair(head, tail)
        self.__indexedEdges[vertexPair] = edge
        self.__indexedVertices[edge] = vertexPair
