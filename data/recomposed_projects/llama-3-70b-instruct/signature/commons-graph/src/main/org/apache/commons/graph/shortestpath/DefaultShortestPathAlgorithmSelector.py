from __future__ import annotations
import re
import collections
import os
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.collections.FibonacciHeap import *
from src.main.org.apache.commons.graph.shortestpath.DefaultHeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.ShortestDistances import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultShortestPathAlgorithmSelector:

    __target: typing.Any = None

    __source: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def applyingDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        weightOperations = Assertions.checkNotNull(
            weightOperations,
            "Dijkstra algorithm can not be applied using null weight operations",
        )
        shortestDistances = ShortestDistances[typing.Any, typing.Any](weightOperations)
        shortestDistances.setWeight(self.__source, weightOperations.identity())
        unsettledNodes = FibonacciHeap[typing.Any](shortestDistances)
        unsettledNodes.add(self.__source)
        settledNodes = set[typing.Any]()
        predecessors = PredecessorsList[typing.Any, typing.Any, typing.Any](
            self.__graph, weightOperations, self.__weightedEdges
        )
        while not unsettledNodes.isEmpty():
            vertex = unsettledNodes.remove()
            if self.__target.equals(vertex):
                return predecessors.buildPath0(self.__source, self.__target)
            settledNodes.add(vertex)
            for v in self.__graph.getConnectedVertices(vertex):
                if not settledNodes.contains(v):
                    edge = self.__graph.getEdge(vertex, v)
                    if shortestDistances.alreadyVisited(vertex):
                        shortDist = weightOperations.append(
                            shortestDistances.getWeight(vertex),
                            self.__weightedEdges.map(edge),
                        )
                        if (
                            not shortestDistances.alreadyVisited(v)
                            or weightOperations.compare(
                                shortDist, shortestDistances.getWeight(v)
                            )
                            < 0
                        ):
                            shortestDistances.setWeight(v, shortDist)
                            unsettledNodes.add(v)
                            predecessors.addPredecessor(v, vertex)
        raise PathNotFoundException(
            "Path from '%s' to '%s' doesn't exist in Graph '%s'",
            self.__source,
            self.__target,
            self.__graph,
        )

    def applyingBidirectionalDijkstra(
        self, weightOperations: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        weightOperations = Assertions.checkNotNull(
            weightOperations,
            "Bidirectional Dijkstra algorithm can not be applied using null weight operations",
        )
        shortestDistancesForward = ShortestDistances[typing.Any, typing.Any](
            weightOperations
        )
        shortestDistancesForward.setWeight(self.__source, weightOperations.identity())
        shortestDistancesBackwards = ShortestDistances[typing.Any, typing.Any](
            weightOperations
        )
        shortestDistancesBackwards.setWeight(self.__target, weightOperations.identity())
        openForward = FibonacciHeap[typing.Any](shortestDistancesForward)
        openForward.add(self.__source)
        openBackwards = FibonacciHeap[typing.Any](shortestDistancesBackwards)
        openBackwards.add(self.__target)
        closedForward = set[typing.Any]()
        closedBackwards = set[typing.Any]()
        predecessorsForward = PredecessorsList[typing.Any, typing.Any, typing.Any](
            self.__graph, weightOperations, self.__weightedEdges
        )
        predecessorsBackwards = PredecessorsList[typing.Any, typing.Any, typing.Any](
            self.__graph, weightOperations, self.__weightedEdges
        )
        best = None
        touch = None
        while not openForward.isEmpty() and not openBackwards.isEmpty():
            if best is not None:
                tmp = weightOperations.append(
                    shortestDistancesForward.getWeight(openForward.peek()),
                    shortestDistancesBackwards.getWeight(openBackwards.peek()),
                )
                if weightOperations.compare(tmp, best) >= 0:
                    return predecessorsForward.buildPath1(
                        self.__source, touch, self.__target, predecessorsBackwards
                    )
            vertex = openForward.remove()
            closedForward.add(vertex)
            for v in self.__graph.getConnectedVertices(vertex):
                if not closedForward.contains(v):
                    edge = self.__graph.getEdge(vertex, v)
                    if shortestDistancesForward.alreadyVisited(vertex):
                        shortDist = weightOperations.append(
                            shortestDistancesForward.getWeight(vertex),
                            self.__weightedEdges.map(edge),
                        )
                        if (
                            not shortestDistancesForward.alreadyVisited(v)
                            or weightOperations.compare(
                                shortDist, shortestDistancesForward.getWeight(v)
                            )
                            < 0
                        ):
                            shortestDistancesForward.setWeight(v, shortDist)
                            openForward.add(v)
                            predecessorsForward.addPredecessor(v, vertex)
                            if closedBackwards.contains(v):
                                tmpBest = weightOperations.append(
                                    shortDist, shortestDistancesBackwards.getWeight(v)
                                )
                                if (
                                    best is None
                                    or weightOperations.compare(tmpBest, best) < 0
                                ):
                                    best = tmpBest
                                    touch = v
            vertex = openBackwards.remove()
            closedBackwards.add(vertex)
            parentsIterable = (
                self.__graph.getInbound(vertex)
                if isinstance(self.__graph, DirectedGraph)
                else self.__graph.getConnectedVertices(vertex)
            )
            for v in parentsIterable:
                if not closedBackwards.contains(v):
                    edge = self.__graph.getEdge(v, vertex)
                    if shortestDistancesBackwards.alreadyVisited(vertex):
                        shortDist = weightOperations.append(
                            shortestDistancesBackwards.getWeight(vertex),
                            self.__weightedEdges.map(edge),
                        )
                        if (
                            not shortestDistancesBackwards.alreadyVisited(v)
                            or weightOperations.compare(
                                shortDist, shortestDistancesBackwards.getWeight(v)
                            )
                            < 0
                        ):
                            shortestDistancesBackwards.setWeight(v, shortDist)
                            openBackwards.add(v)
                            predecessorsBackwards.addPredecessor(v, vertex)
                            if closedForward.contains(v):
                                tmpBest = weightOperations.append(
                                    shortDist, shortestDistancesForward.getWeight(v)
                                )
                                if (
                                    best is None
                                    or weightOperations.compare(tmpBest, best) < 0
                                ):
                                    best = tmpBest
                                    touch = v
        if touch is None:
            raise PathNotFoundException(
                "Path from '%s' to '%s' doesn't exist in Graph '%s'",
                self.__source,
                self.__target,
                self.__graph,
            )
        return predecessorsForward.buildPath1(
            self.__source, touch, self.__target, predecessorsBackwards
        )

    def applyingAStar(
        self, weightOperations: typing.Any
    ) -> HeuristicBuilder[typing.Any, typing.Any, typing.Any]:
        weightOperations = Assertions.checkNotNull(
            weightOperations,
            "A* algorithm can not be applied using null weight operations",
        )
        return DefaultHeuristicBuilder(
            self.__graph,
            self.__weightedEdges,
            self.__source,
            self.__target,
            weightOperations,
        )

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
        self.__target = target
