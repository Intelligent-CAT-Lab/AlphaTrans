from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.SynchronizedGraph import *


class SynchronizedDirectedGraph(DirectedGraph, SynchronizedGraph):

    __directedGraph: DirectedGraph[typing.Any, typing.Any] = None

    __serialVersionUID: int = 2275587906693672253

    def getOutDegree(self, v: typing.Any) -> int:
        with self._lock:
            return self.__directedGraph.getOutDegree(v)

    def getOutbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        with self._lock:
            return self.__directedGraph.getOutbound(v)

    def getInDegree(self, v: typing.Any) -> int:
        with self._lock:
            return self.__directedGraph.getInDegree(v)

    def getInbound(self, v: typing.Any) -> typing.Iterable[typing.Any]:
        with self._lock:
            return self.__directedGraph.getInbound(v)

    def __init__(self, g: DirectedGraph[typing.Any, typing.Any]) -> None:
        super().__init__(g)
        self.__directedGraph = g
