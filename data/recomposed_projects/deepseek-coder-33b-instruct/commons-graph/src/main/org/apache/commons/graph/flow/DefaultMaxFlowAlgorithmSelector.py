from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.flow.FlowNetworkHandler import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitSourceSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class EdgeWrapper:

    __wrapped: typing.Any = None

    def getWrapped(self) -> typing.Any:

        return self.__wrapped

    @staticmethod
    def EdgeWrapper1() -> EdgeWrapper[typing.Any]:

        return EdgeWrapper(None)

    def __init__(self, wrapped: typing.Any) -> None:

        self.__wrapped = wrapped


class MapperWrapper(Mapper):

    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __weightOperations: typing.Any = None

    def map(self, input: EdgeWrapper[typing.Any]) -> typing.Any:

        if input.getWrapped() is None:
            return self.__weightOperations.identity()
        return self.__weightedEdges.map(input.getWrapped())

    def __init__(
        self,
        weightOperations: typing.Any,
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:

        self.__weightOperations = weightOperations
        self.__weightedEdges = weightedEdges


class DefaultMaxFlowAlgorithmSelector:

    __target: typing.Any = None
    __source: typing.Any = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __graph: DirectedGraph[typing.Any, typing.Any] = None

    def applyingFordFulkerson(self, weightOperations: typing.Any) -> typing.Any:

        checkedWeightOperations = Assertions.checkNotNull(
            weightOperations,
            "Weight operations can not be null to find the max flow in the graph",
        )

        flowNetwork = self.__newFlowNetwok(self.__graph, checkedWeightOperations)

        flowNetworkHandler = FlowNetworkHandler(
            flowNetwork,
            self.__source,
            self.__target,
            checkedWeightOperations,
            MapperWrapper(checkedWeightOperations, self.__weightedEdges),
        )

        CommonsGraph.visit(flowNetwork).from_(self.__source).applyingDepthFirstSearch1(
            flowNetworkHandler
        )

        while flowNetworkHandler.hasAugmentingPath():
            flowNetworkHandler.updateResidualNetworkWithCurrentAugmentingPath()
            CommonsGraph.visit(flowNetwork).from_(
                self.__source
            ).applyingDepthFirstSearch1(flowNetworkHandler)

        return flowNetworkHandler.onCompleted()

    def applyingEdmondsKarp(self, weightOperations: typing.Any) -> typing.Any:

        checkedWeightOperations = checkNotNull(
            weightOperations,
            "Weight operations can not be null to find the max flow in the graph",
        )

        flowNetwork = self.__newFlowNetwok(self.__graph, checkedWeightOperations)

        flowNetworkHandler = FlowNetworkHandler(
            flowNetwork,
            self.__source,
            self.__target,
            checkedWeightOperations,
            MapperWrapper(checkedWeightOperations, self.__weightedEdges),
        )

        visit(flowNetwork).from_(self.__source).applyingBreadthFirstSearch1(
            flowNetworkHandler
        )

        while flowNetworkHandler.hasAugmentingPath():
            flowNetworkHandler.updateResidualNetworkWithCurrentAugmentingPath()
            visit(flowNetwork).from_(self.__source).applyingBreadthFirstSearch1(
                flowNetworkHandler
            )

        return flowNetworkHandler.onCompleted()

    def __init__(
        self,
        graph: DirectedGraph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
        target: typing.Any,
    ) -> None:

        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
        self.__target = target

    def __newFlowNetwok(
        self, graph: DirectedGraph[typing.Any, typing.Any], weightOperations: typing.Any
    ) -> DirectedGraph[typing.Any, EdgeWrapper[typing.Any]]:

        class NewFlowNetwork(
            AbstractGraphConnection[typing.Any, EdgeWrapper[typing.Any]]
        ):
            def connect0(self):
                for vertex in graph.getVertices0():
                    self.addVertex(vertex)
                for edge in graph.getEdges():
                    edgeVertices = graph.getVertices1(edge)
                    head = edgeVertices.getHead()
                    tail = edgeVertices.getTail()

                    self.addEdge(EdgeWrapper(edge)).from_(head).to(tail)

                    if graph.getEdge(tail, head) is None:
                        self.addEdge(EdgeWrapper.EdgeWrapper1()).from_(tail).to(head)

        return CommonsGraph.newDirectedMutableGraph(NewFlowNetwork())
