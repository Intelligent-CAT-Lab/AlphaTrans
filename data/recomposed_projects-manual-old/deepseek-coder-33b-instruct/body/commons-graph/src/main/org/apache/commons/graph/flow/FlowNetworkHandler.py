from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.shortestpath.PredecessorsList import *
from src.main.org.apache.commons.graph.visit.BaseGraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitState import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class FlowNetworkHandler:

    __foundAugmentingPath: bool = False

    __predecessors: PredecessorsList[typing.Any, typing, Any, typing.Any] = None

    __residualEdgeCapacities: Dict[typing.Any, typing.Any] = {}
    __maxFlow: typing.Any = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightOperations: OrderedMonoid[typing.Any] = None

    __target: typing.Any = None

    __source: typing.Any = None

    __flowNetwork: DirectedGraph[typing.Any, typing.Any] = None

    def onCompleted(self) -> typing.Any:
        return self.__maxFlow

    def discoverGraph(self, graph: DirectedGraph[typing.Any, typing.Any]) -> None:

        self.__predecessors = PredecessorsList[typing.Any, typing.Any, typing.Any](
            graph, self.__weightOperations, self.__weightedEdges
        )
        self.__foundAugmentingPath = False

    def discoverEdge(
        self, head: typing.Any, edge: typing.Any, tail: typing.Any
    ) -> VisitState:

        residualEdgeCapacity = self.__residualEdgeCapacities.get(edge)
        if (
            self.__weightOperations.compare(
                residualEdgeCapacity, self.__weightOperations.identity()
            )
            <= 0
        ):
            return VisitState.SKIP
        self.__predecessors.addPredecessor(tail, head)
        return VisitState.CONTINUE

    def finishVertex(self, vertex: typing.Any) -> VisitState:

        if vertex == self.__target:
            self.__foundAugmentingPath = True
            return VisitState.ABORT

        return VisitState.CONTINUE

    def discoverVertex(self, vertex: typing.Any) -> VisitState:

        return self.finishVertex(vertex)

    def updateResidualNetworkWithCurrentAugmentingPath(self) -> None:

        augmentingPath = self.__predecessors.buildPath0(self.__source, self.__target)

        flowIncrement = None
        for edge in augmentingPath.getEdges():
            edgeCapacity = self.__residualEdgeCapacities.get(edge)
            if (
                flowIncrement is None
                or self.__weightOperations.compare(edgeCapacity, flowIncrement) < 0
            ):
                flowIncrement = edgeCapacity

        self.__maxFlow = self.__weightOperations.append(self.__maxFlow, flowIncrement)
        for edge in augmentingPath.getEdges():
            directCapacity = self.__residualEdgeCapacities.get(edge)
            self.__residualEdgeCapacities[edge] = self.__weightOperations.append(
                directCapacity, self.__weightOperations.inverse(flowIncrement)
            )

            vertexPair = self.__flowNetwork.getVertices1(edge)
            inverseEdge = self.__flowNetwork.getEdge(
                vertexPair.getTail(), vertexPair.getHead()
            )
            inverseCapacity = self.__residualEdgeCapacities.get(inverseEdge)
            self.__residualEdgeCapacities[inverseEdge] = self.__weightOperations.append(
                inverseCapacity, flowIncrement
            )

    def hasAugmentingPath(self) -> bool:
        return self.__foundAugmentingPath

    def __init__(
        self,
        flowNetwork: DirectedGraph[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
        weightOperations: OrderedMonoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:

        self.__flowNetwork = flowNetwork
        self.__source = source
        self.__target = target
        self.__weightOperations = weightOperations
        self.__weightedEdges = weightedEdges

        self.__maxFlow = self.__weightOperations.identity()

        for edge in self.__flowNetwork.getEdges():
            self.__residualEdgeCapacities[edge] = self.__weightedEdges.map(edge)

        self.__predecessors = None
