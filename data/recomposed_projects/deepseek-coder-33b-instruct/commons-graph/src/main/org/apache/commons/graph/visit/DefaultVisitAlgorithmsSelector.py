from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.visit.GraphVisitHandler import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.visit.VisitGraphBuilder import *
from src.main.org.apache.commons.graph.visit.VisitState import *


class DefaultVisitAlgorithmsSelector(VisitAlgorithmsSelector):

    __source: typing.Any = None
    __graph: typing.Any = None

    def applyingDepthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:

        return self.__applyingSearch(handler, False)

    def applyingDepthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:

        return self.applyingDepthFirstSearch1(VisitGraphBuilder())

    def applyingBreadthFirstSearch1(
        self, handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any]
    ) -> typing.Any:

        return self.__applyingSearch(handler, True)

    def applyingBreadthFirstSearch0(self) -> Graph[typing.Any, typing.Any]:

        return self.applyingBreadthFirstSearch1(VisitGraphBuilder())

    def __init__(self, graph: typing.Any, source: typing.Any) -> None:

        self.__graph = graph
        self.__source = source

    def __applyingSearch(
        self,
        handler: GraphVisitHandler[typing.Any, typing.Any, typing.Any, typing.Any],
        enqueue: bool,
    ) -> typing.Any:

        handler = checkNotNull(handler, "Graph visitor handler can not be null.")

        handler.discoverGraph(self.__graph)

        vertexList = LinkedList[VertexPair[typing.Any]]()

        vertexList.addLast(VertexPair[typing.Any](self.__source, self.__source))

        visitedVertices = set[typing.Any]()
        visitedVertices.add(self.__source)

        visitingGraph = True

        while visitingGraph and not vertexList.isEmpty():
            pair = vertexList.removeFirst() if enqueue else vertexList.removeLast()
            v = pair.getHead()
            prevHead = pair.getTail()
            e = None if prevHead == v else self.__graph.getEdge(prevHead, v)

            skipVertex = False

            if e is not None:
                if v in visitedVertices:
                    skipVertex = True
                else:
                    stateAfterEdgeDiscovery = handler.discoverEdge(prevHead, e, v)
                    if stateAfterEdgeDiscovery != VisitState.CONTINUE:
                        skipVertex = True
                        if stateAfterEdgeDiscovery == VisitState.ABORT:
                            visitingGraph = False

                    if handler.finishEdge(prevHead, e, v) == VisitState.ABORT:
                        skipVertex = True
                        visitingGraph = False

            vertexWasDiscovered = False
            if not skipVertex:
                visitedVertices.add(v)
                stateAfterVertexDiscovery = handler.discoverVertex(v)
                vertexWasDiscovered = True
                if stateAfterVertexDiscovery != VisitState.CONTINUE:
                    skipVertex = True
                    if stateAfterVertexDiscovery == VisitState.ABORT:
                        visitingGraph = False

            if not skipVertex:
                connected = (
                    self.__graph.getOutbound(v).iterator()
                    if isinstance(self.__graph, DirectedGraph)
                    else self.__graph.getConnectedVertices(v).iterator()
                )

                while connected.hasNext():
                    w = connected.next()
                    if w not in visitedVertices:
                        vertexList.addLast(VertexPair[typing.Any](w, v))

            if vertexWasDiscovered and handler.finishVertex(v) == VisitState.ABORT:
                visitingGraph = False

        handler.finishGraph(self.__graph)

        return handler.onCompleted()
