from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.weight.Monoid import *


class PredecessorsList:

    __predecessors: typing.Dict[typing.Any, typing.Any] = {}

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightOperations: Monoid[typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def isEmpty(self) -> bool:
        return self.__predecessors.isEmpty()

    def buildPath1(
        self,
        source: typing.Any,
        touch: typing.Any,
        target: typing.Any,
        backwardsList: PredecessorsList,
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        path: InMemoryWeightedPath[typing.Any, typing.Any, typing.Any] = (
            InMemoryWeightedPath[typing.Any, typing.Any, typing.Any](
                source, target, self.__weightOperations, self.__weightedEdges
            )
        )
        vertex: typing.Any = touch
        while not source == vertex:
            predecessor: typing.Any = self.__predecessors.get(vertex)
            if predecessor == None:
                raise PathNotFoundException(
                    "Path from '%s' to '%s' doesn't exist", source, target
                )
            edge: typing.Any = self.__graph.getEdge(predecessor, vertex)
            path.addConnectionInHead(predecessor, edge, vertex)
            vertex = predecessor
        vertex = touch
        while not target == vertex:
            predecessor: typing.Any = backwardsList.__predecessors.get(vertex)
            if predecessor == None:
                raise PathNotFoundException(
                    "Path from '%s' to '%s' doesn't exist", source, target
                )
            edge: typing.Any = self.__graph.getEdge(vertex, predecessor)
            path.addConnectionInTail(vertex, edge, predecessor)
            vertex = predecessor
        return path

    def buildPath0(
        self, source: typing.Any, target: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        path: InMemoryWeightedPath[typing.Any, typing.Any, typing.Any] = (
            InMemoryWeightedPath[typing.Any, typing.Any, typing.Any](
                source, target, self.__weightOperations, self.__weightedEdges
            )
        )
        vertex: typing.Any = target
        while not source.__eq__(vertex):
            predecessor: typing.Any = self.__predecessors.get(vertex)
            if predecessor is None:
                raise PathNotFoundException(
                    "Path from '%s' to '%s' doesn't exist", source, target
                )
            edge: typing.Any = self.__graph.getEdge(predecessor, vertex)
            path.addConnectionInHead(predecessor, edge, vertex)
            vertex = predecessor
        return path

    def addPredecessor(self, tail: typing.Any, head: typing.Any) -> None:
        self.__predecessors[tail] = head

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightOperations: Monoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__weightedEdges = weightedEdges
        self.__weightOperations = weightOperations
        self.__graph = graph
