from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.ReverseDeleteGraph import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultSpanningTreeSourceSelector:

    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __graph: Graph[typing.Any, typing.Any] = None

    def fromSource(
        self, source: typing.Any
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:

        # checkNotNull
        if source is None:
            raise ValueError(
                "Spanning tree cannot be calculated without expressing the source vertex"
            )

        # checkState
        if not self.__graph.containsVertex(source):
            raise ValueError(f"Vertex {source} does not exist in the Graph")

        return DefaultSpanningTreeAlgorithmSelector(
            self.__graph, self.__weightedEdges, source
        )

    def fromArbitrarySource(
        self,
    ) -> SpanningTreeAlgorithmSelector[typing.Any, typing.Any, typing.Any]:

        from src.main.org.apache.commons.graph.utils.Assertions import checkState

        checkState(
            self.__graph.getOrder() > 0,
            "Spanning tree cannot be calculated on an empty graph",
        )
        return self.fromSource(next(iter(self.__graph.getVertices0())))

    def applyingReverseDeleteAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        checkNotNull(
            weightOperations,
            "The Reverse-Delete algorithm cannot be calulated with null weight operations",
        )

        sortedEdge = PriorityQueue(
            11,
            reverseOrder(
                WeightedEdgesComparator(weightOperations, self.__weightedEdges)
            ),
        )
        visitedEdge = []

        edges = self.__graph.getEdges()
        for we in edges:
            sortedEdge.offer(we)

        tmpGraph = ReverseDeleteGraph(self.__graph, sortedEdge, visitedEdge)

        while not sortedEdge.isEmpty():
            we = sortedEdge.poll()

            vertices = self.__graph.getVertices1(we)

            try:
                findShortestPath(tmpGraph).whereEdgesHaveWeights(
                    self.__weightedEdges
                ).from_(vertices.getHead()).to(vertices.getTail()).applyingDijkstra(
                    weightOperations
                )
            except PathNotFoundException:
                visitedEdge.append(we)

        res = MutableSpanningTree(weightOperations, self.__weightedEdges)
        for v in self.__graph.getVertices0():
            res.addVertex(v)

        for we in edges:
            pair = tmpGraph.getVertices1(we)
            if pair is not None:
                res.addEdge(pair.getHead(), we, pair.getTail())

        return res

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:

        self.__graph = graph
        self.__weightedEdges = weightedEdges
