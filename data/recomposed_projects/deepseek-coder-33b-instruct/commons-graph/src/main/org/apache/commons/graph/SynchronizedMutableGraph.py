from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.SynchronizedGraph import *


class SynchronizedMutableGraph(MutableGraph, SynchronizedGraph):

    __mutableGraph: MutableGraph[typing.Any, typing.Any] = None

    __serialVersionUID: int = -5985121601939852063

    def removeVertex(self, v: typing.Any) -> None:

        with self.lock:
            self.__mutableGraph.removeVertex(v)

    def removeEdge(self, e: typing.Any) -> None:

        with self.lock:
            self.__mutableGraph.removeEdge(e)

    def addVertex(self, v: typing.Any) -> None:

        with self.lock:
            self.__mutableGraph.addVertex(v)

    def addEdge(self, head: typing.Any, e: typing.Any, tail: typing.Any) -> None:

        with self.lock:
            self.__mutableGraph.addEdge(head, e, tail)

    def __init__(self, g: MutableGraph[typing.Any, typing.Any]) -> None:

        super(SynchronizedMutableGraph, self).__init__(g)
        self.__mutableGraph = g
