from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.DefaultTargetSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultPathSourceSelector(PathSourceSelector):

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def from_(
        self, source: typing.Any
    ) -> TargetSourceSelector[typing.Any, typing.Any, typing.Any]:
        source = Assertions.checkNotNull(
            source, "Shortest path can not be calculated from a null source"
        )
        return DefaultTargetSourceSelector(self.__graph, self.__weightedEdges, source)

    def applyingFloydWarshall(
        self, weightOperations: typing.Any
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:
        weightOperations = Assertions.checkNotNull(
            weightOperations,
            "Floyd-Warshall algorithm can not be applied using null weight operations",
        )
        shortestPaths = AllVertexPairsShortestPath(weightOperations)
        next = {}
        for we in self.__graph.getEdges():
            vertexPair = self.__graph.getVertices1(we)
            shortestPaths.addShortestDistance(
                vertexPair.getHead(), vertexPair.getTail(), self.__weightedEdges.map(we)
            )
            if isinstance(self.__graph, UndirectedGraph):
                shortestPaths.addShortestDistance(
                    vertexPair.getTail(),
                    vertexPair.getHead(),
                    self.__weightedEdges.map(we),
                )
        for k in self.__graph.getVertices0():
            for i in self.__graph.getVertices0():
                for j in self.__graph.getVertices0():
                    if shortestPaths.hasShortestDistance(
                        i, k
                    ) and shortestPaths.hasShortestDistance(k, j):
                        newDistance = weightOperations.append(
                            shortestPaths.getShortestDistance(i, k),
                            shortestPaths.getShortestDistance(k, j),
                        )
                        if (
                            not shortestPaths.hasShortestDistance(i, j)
                            or weightOperations.compare(
                                newDistance, shortestPaths.getShortestDistance(i, j)
                            )
                            < 0
                        ):
                            shortestPaths.addShortestDistance(i, j, newDistance)
                            next[VertexPair(i, j)] = k
        for source in self.__graph.getVertices0():
            for target in self.__graph.getVertices0():
                if source != target:
                    predecessorsList = PredecessorsList(
                        self.__graph, weightOperations, self.__weightedEdges
                    )
                    self.__pathReconstruction(predecessorsList, source, target, next)
                    if not predecessorsList.isEmpty():
                        weightedPath = predecessorsList.buildPath0(source, target)
                        if weightedPath.getOrder() > 0:
                            shortestPaths.addShortestPath(source, target, weightedPath)
        return shortestPaths

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges

    def __pathReconstruction(
        self,
        path: PredecessorsList[typing.Any, typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
        next: typing.Dict[VertexPair[typing.Any], typing.Any],
    ) -> None:
        k = next.get(VertexPair(source, target))
        if k is None:
            edge = self.__graph.getEdge(source, target)
            if edge is not None:
                path.addPredecessor(target, source)
        else:
            self.__pathReconstruction(path, source, k, next)
            self.__pathReconstruction(path, k, target, next)
