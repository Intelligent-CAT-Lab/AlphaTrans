from __future__ import annotations
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.collections.DisjointSet import *
from src.main.org.apache.commons.graph.collections.FibonacciHeap import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.spanning.ShortestEdges import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SuperVertex import *
from src.main.org.apache.commons.graph.spanning.WeightedEdgesComparator import *
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class DefaultSpanningTreeAlgorithmSelector:

    __source: typing.Any = None
    __weightedEdges: Mapper[typing.Any, typing.Any] = None
    __graph: Graph[typing.Any, typing.Any] = None

    def applyingPrimAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        checkNotNull(
            weightOperations,
            "The Prim algorithm cannot be calculated with null weight operations",
        )

        shortestEdges = ShortestEdges(
            self.__graph, self.__source, weightOperations, self.__weightedEdges
        )

        unsettledNodes = FibonacciHeap(shortestEdges)
        unsettledNodes.add(self.__source)

        settledEdges = set()

        while not unsettledNodes.isEmpty():
            vertex = unsettledNodes.remove()

            for v in self.__graph.getConnectedVertices(vertex):
                edge = self.__graph.getEdge(vertex, v)
                weightLessThanCurrent = (not shortestEdges.hasWeight(v)) or (
                    weightOperations.compare(
                        self.__weightedEdges.map(edge), shortestEdges.getWeight(v)
                    )
                    < 0
                )
                if edge not in settledEdges and weightLessThanCurrent:
                    if not unsettledNodes.contains(v):
                        unsettledNodes.add(v)

                    shortestEdges.addPredecessor(v, edge)

        return shortestEdges.createSpanningTree()

    def applyingKruskalAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        checkNotNull(
            weightOperations,
            "The Kruskal algorithm cannot be calculated with null weight operations",
        )

        settledNodes = set()

        orderedEdges = FibonacciHeap(
            WeightedEdgesComparator(weightOperations, self.__weightedEdges)
        )

        for edge in self.__graph.getEdges():
            orderedEdges.add(edge)

        disjointSet = DisjointSet()

        spanningTree = MutableSpanningTree(weightOperations, self.__weightedEdges)

        for v in self.__graph.getVertices0():
            spanningTree.addVertex(v)

        while (
            not orderedEdges.isEmpty() and len(settledNodes) < self.__graph.getOrder()
        ):
            edge = orderedEdges.remove()

            vertices = self.__graph.getVertices1(edge)
            head = vertices.getHead()
            tail = vertices.getTail()
            settledNodes.add(head)
            settledNodes.add(tail)

            if disjointSet.find1(head) != disjointSet.find1(tail):
                disjointSet.union(head, tail)
                spanningTree.addEdge(head, edge, tail)

        return spanningTree

    def applyingBoruvkaAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        checkNotNull(
            weightOperations,
            "The Boruvka algorithm cannot be calculated with null weight operations",
        )

        spanningTree = MutableSpanningTree(weightOperations, self.__weightedEdges)

        components = set()

        mapping = dict()

        for v in self.__graph.getVertices0():
            sv = SuperVertex(
                v,
                self.__graph,
                WeightedEdgesComparator(weightOperations, self.__weightedEdges),
            )

            components.add(sv)

            mapping[v] = sv

            spanningTree.addVertex(v)

        while len(components) > 1:
            edges = []
            for sv in components:
                edge = sv.getMinimumWeightEdge()
                if edge is not None:
                    edges.append(edge)

            checkState(len(edges) > 0 or len(components) == 1, "unconnected graph")

            for edge in edges:
                pair = self.__graph.getVertices1(edge)
                head = pair.getHead()
                tail = pair.getTail()

                headSv = mapping[head]
                tailSv = mapping[tail]

                if headSv != tailSv:
                    headSv.merge(tailSv)

                    for v in tailSv:
                        mapping[v] = headSv

                    components.remove(tailSv)

                    if spanningTree.getVertices1(edge) is None:
                        spanningTree.addEdge(head, edge, tail)

        return spanningTree

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
        source: typing.Any,
    ) -> None:

        self.__graph = graph
        self.__weightedEdges = weightedEdges
        self.__source = source
