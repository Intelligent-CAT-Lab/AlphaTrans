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
from src.main.org.apache.commons.graph.shortestpath.Heuristic import *
from src.main.org.apache.commons.graph.shortestpath.HeuristicBuilder import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.ShortestDistances import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultHeuristicBuilder(HeuristicBuilder):

    __weightOperations: OrderedMonoid[typing.Any] = None

    __goal: typing.Any = None

    __start: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def withHeuristic(
        self, heuristic: typing.Any
    ) -> WeightedPath[typing.Any, typing.Any, typing.Any]:
        heuristic = Assertions.checkNotNull(
            heuristic, "A* algorithm can not be applied using a null heuristic"
        )
        gScores = ShortestDistances[typing.Any, typing.Any](self.__weightOperations)
        gScores.setWeight(self.__start, self.__weightOperations.identity())
        fScores = ShortestDistances[typing.Any, typing.Any](self.__weightOperations)
        hScore = heuristic.applyHeuristic(self.__start, self.__goal)
        fScores.setWeight(self.__start, hScore)
        closedSet = set()
        openSet = FibonacciHeap[typing.Any](fScores)
        openSet.add(self.__start)
        predecessors = PredecessorsList[typing.Any, typing.Any, typing.Any](
            self.__graph, self.__weightOperations, self.__weightedEdges
        )
        while not openSet.isEmpty():
            current = openSet.remove()
            if self.__goal.equals(current):
                return predecessors.buildPath0(self.__start, self.__goal)
            closedSet.add(current)
            connected = (
                self.__graph.getConnectedVertices(current)
                if isinstance(self.__graph, DirectedGraph)
                else self.__graph.getOutbound(current)
            )
            for v in connected:
                if not closedSet.contains(v):
                    edge = self.__graph.getEdge(current, v)
                    tentativeGScore = self.__weightOperations.append(
                        gScores.getWeight(current), self.__weightedEdges.map(edge)
                    )
                    if (
                        openSet.add(v)
                        or self.__weightOperations.compare(
                            tentativeGScore, gScores.getWeight(v)
                        )
                        < 0
                    ):
                        predecessors.addPredecessor(v, current)
                        gScores.setWeight(v, tentativeGScore)
                        hScore = heuristic.applyHeuristic(v, self.__goal)
                        fScores.setWeight(
                            v,
                            self.__weightOperations.append(
                                gScores.getWeight(v), hScore
                            ),
                        )
        raise PathNotFoundException(
            "Path from '%s' to '%s' doesn't exist in Graph '%s'",
            self.__start,
            self.__goal,
            self.__graph,
        )

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
        weightOperations: OrderedMonoid[typing.Any],
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__start = source
        self.__goal = target
        self.__weightOperations = weightOperations
