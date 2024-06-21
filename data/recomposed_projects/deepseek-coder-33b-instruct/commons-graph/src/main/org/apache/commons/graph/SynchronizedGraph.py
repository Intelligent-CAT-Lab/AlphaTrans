from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Objects import *


class SynchronizedGraph(Graph):

    _g: Graph[typing.Any, typing.Any] = None
    _lock: typing.Any = None

    __serialVersionUID: int = 4472623111635514693

    def toString(self) -> str:

        return self._g.toString()

    def hashCode(self) -> int:

        prime = 31
        result = 1
        result = prime * result + (0 if self._g is None else hash(self._g))
        result = prime * result + (0 if self._lock is None else hash(self._lock))
        return result

    def equals(self, obj: typing.Any) -> bool:

        if self == obj:
            return True

        if obj is None or type(self) != type(obj):
            return False

        other: SynchronizedGraph[typing.Any, typing.Any] = typing.cast(
            SynchronizedGraph[typing.Any, typing.Any], obj
        )
        return Objects.eq(self._g, other._g)

    def getVertices1(self, e: typing.Any) -> VertexPair[typing.Any]:

        with self._lock:
            return self._g.getVertices1(e)

    def getVertices0(self) -> typing.Iterable[typing.Any]:

        with self._lock:
            return self._g.getVertices0()

    def getSize(self) -> int:

        with self._lock:
            return self._g.getSize()

    def getOrder(self) -> int:

        with self._lock:
            return self._g.getOrder()

    def getEdges(self) -> typing.Iterable[typing.Any]:

        with self._lock:
            return self._g.getEdges()

    def getEdge(self, source: typing.Any, target: typing.Any) -> typing.Any:

        with self._lock:
            return self._g.getEdge(source, target)

    def getDegree(self, v: typing.Any) -> int:

        with self._lock:
            return self._g.getDegree(v)

    def getConnectedVertices(self, v: typing.Any) -> typing.Iterable[typing.Any]:

        with self._lock:
            return self._g.getConnectedVertices(v)

    def containsVertex(self, v: typing.Any) -> bool:

        with self._lock:
            return self._g.containsVertex(v)

    def containsEdge(self, e: typing.Any) -> bool:

        with self._lock:
            return self._g.containsEdge(e)

    def __init__(self, g: Graph[typing.Any, typing.Any]) -> None:

        self._g = g
        self._lock = self
