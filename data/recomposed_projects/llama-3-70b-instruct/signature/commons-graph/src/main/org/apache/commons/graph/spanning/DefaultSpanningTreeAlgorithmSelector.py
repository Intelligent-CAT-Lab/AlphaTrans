from __future__ import annotations
import re
import collections
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

        pass  # LLM could not translate this method

    def applyingKruskalAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:

        pass  # LLM could not translate this method

    def applyingBoruvkaAlgorithm(
        self, weightOperations: typing.Any
    ) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        # <pre>
        # procedure Boruvka MST(G(V; E)):
        #     T <= V
        #     while |T| < n do
        #         for all connected component C in T do
        #             e <= the smallest-weight edge from C to another component in T
        #             if e not exists in T then
        #                 T <= T u {e}
        #             end if
        #         end for
        #     end while
        # <pre>

        Assertions.checkNotNull(
            weightOperations,
            "The Boruvka algorithm cannot be calculated with null weight operations",
        )

        spanningTree = MutableSpanningTree[typing.Any, typing.Any, typing.Any](
            weightOperations, self.__weightedEdges
        )

        components = set[SuperVertex[typing.Any, typing.Any, typing.Any]]()

        mapping = dict[typing.Any, SuperVertex[typing.Any, typing.Any, typing.Any]]()

        for v in self.__graph.getVertices0():
            sv = SuperVertex[typing.Any, typing.Any, typing.Any](
                v,
                self.__graph,
                WeightedEdgesComparator[typing.Any, typing.Any](
                    weightOperations, self.__weightedEdges
                ),
            )

            components.add(sv)

            mapping[v] = sv

            spanningTree.addVertex(v)

        while len(components) > 1:
            edges = list[typing.Any]()

            for sv in components:
                edge = sv.getMinimumWeightEdge()
                if edge is not None:
                    edges.append(edge)

            Assertions.checkState(
                len(edges) > 0 or len(components) == 1, "unconnected graph"
            )

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
