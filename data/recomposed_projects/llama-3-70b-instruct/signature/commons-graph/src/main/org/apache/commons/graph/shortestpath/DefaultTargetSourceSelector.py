from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.AllVertexPairsShortestPath import *
from src.main.org.apache.commons.graph.shortestpath.DefaultShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.NegativeWeightedCycleException import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.shortestpath.ShortestDistances import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultTargetSourceSelector(TargetSourceSelector):

    __source: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __graph: Graph[typing.Any, typing.Any] = None

    def to(
        self, target: typing.Any
    ) -> ShortestPathAlgorithmSelector[typing.Any, typing.Any, typing.Any]:
        target = Assertions.checkNotNull(
            target, "Shortest path can not be calculated to a null target"
        )
        return DefaultShortestPathAlgorithmSelector(
            self.__graph, self.__weightedEdges, self.__source, target
        )

    def applyingBelmannFord(
        self, weightOperations: typing.Any
    ) -> AllVertexPairsShortestPath[typing.Any, typing.Any, typing.Any]:
        weightOperations = Assertions.checkNotNull(
            weightOperations,
            "Belmann-Ford algorithm can not be applied using null weight operations",
        )
        shortestDistances = ShortestDistances[typing.Any, typing.Any](weightOperations)
        shortestDistances.setWeight(self.__source, weightOperations.identity())
        predecessors = PredecessorsList[typing.Any, typing.Any, typing.Any](
            self.__graph, weightOperations, self.__weightedEdges
        )
        for i in range(0, self.__graph.getOrder()):
            for edge in self.__graph.getEdges():
                vertexPair = self.__graph.getVertices1(edge)
                u = vertexPair.getHead()
                v = vertexPair.getTail()
                if shortestDistances.alreadyVisited(u):
                    shortDist = weightOperations.append(
                        shortestDistances.getWeight(u), self.__weightedEdges.map(edge)
                    )
                    if (
                        not shortestDistances.alreadyVisited(v)
                        or weightOperations.compare(
                            shortDist, shortestDistances.getWeight(v)
                        )
                        < 0
                    ):
                        shortestDistances.setWeight(v, shortDist)
                        predecessors.addPredecessor(v, u)
        for edge in self.__graph.getEdges():
            vertexPair = self.__graph.getVertices1(edge)
            u = vertexPair.getHead()
            v = vertexPair.getTail()
            if shortestDistances.alreadyVisited(u):
                shortDist = weightOperations.append(
                    shortestDistances.getWeight(u), self.__weightedEdges.map(edge)
                )
                if (
                    not shortestDistances.alreadyVisited(v)
                    or weightOperations.compare(
                        shortDist, shortestDistances.getWeight(v)
                    )
                    < 0
                ):
                    raise NegativeWeightedCycleException(
                        "Graph contains a negative-weight cycle in vertex %s",
                        None,
                        v,
                        self.__graph,
                    )
        allVertexPairsShortestPath = AllVertexPairsShortestPath[
            typing.Any, typing.Any, typing.Any
        ](weightOperations)
        for target in self.__graph.getVertices0():
            if not self.__source.equals(target):
                try:
                    weightedPath = predecessors.buildPath0(self.__source, target)
                    allVertexPairsShortestPath.addShortestPath(
                        self.__source, target, weightedPath
                    )
                except PathNotFoundException as e:
                    continue
        return allVertexPairsShortestPath

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
    ) -> None:
        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
