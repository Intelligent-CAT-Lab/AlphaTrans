from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.VertexPair import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *


class ShortestEdges:

    __source: typing.Any = None

    __graph: Graph[typing.Any, typing.Any] = None

    __weightedEdges: Mapper[typing.Any, typing.Any] = None

    __weightOperations: OrderedMonoid[typing.Any] = None

    __predecessors: typing.Dict[typing.Any, typing.Any] = {}

    def toString(self) -> str:
        return str(self.__predecessors)

    def isEmpty(self) -> bool:
        return self.__predecessors.isEmpty()

    def hasWeight(self, vertex: typing.Any) -> bool:
        return self.__predecessors.containsKey(vertex)

    def getWeight(self, vertex: typing.Any) -> typing.Any:
        if self.__source == vertex:
            return self.__weightOperations.identity()
        edge = self.__predecessors.get(vertex)
        if edge is None:
            return None
        return self.__weightedEdges.map(edge)

    def createSpanningTree(self) -> SpanningTree[typing.Any, typing.Any, typing.Any]:
        spanningTree: MutableSpanningTree[typing.Any, typing.Any, typing.Any] = (
            MutableSpanningTree[typing.Any, typing.Any, typing.Any](
                self.__weightOperations, self.__weightedEdges
            )
        )

        for edge in self.__predecessors.values():
            vertices: VertexPair[typing.Any] = self.__graph.getVertices1(edge)

            head: typing.Any = vertices.getHead()
            tail: typing.Any = vertices.getTail()

            self.__addEdgeIgnoringExceptions(head, spanningTree)
            self.__addEdgeIgnoringExceptions(tail, spanningTree)

            spanningTree.addEdge(head, self.__graph.getEdge(head, tail), tail)

        return spanningTree

    def compare(self, left: typing.Any, right: typing.Any) -> int:
        if not self.hasWeight(left) and not self.hasWeight(right):
            return 0
        elif not self.hasWeight(left):
            return 1
        elif not self.hasWeight(right):
            return -1
        return self.__weightOperations.compare(
            self.getWeight(left), self.getWeight(right)
        )

    def addPredecessor(self, tail: typing.Any, head: typing.Any) -> None:
        self.__predecessors[tail] = head

    def __init__(
        self,
        graph: Graph[typing.Any, typing.Any],
        source: typing.Any,
        weightOperations: OrderedMonoid[typing.Any],
        weightedEdges: Mapper[typing.Any, typing.Any],
    ) -> None:
        self.__source = source
        self.__graph = graph
        self.__weightOperations = weightOperations
        self.__weightedEdges = weightedEdges

    @staticmethod
    def __addEdgeIgnoringExceptions(
        vertex: typing.Any,
        spanningTree: MutableSpanningTree[typing.Any, typing.Any, typing.Any],
    ) -> None:

        pass  # LLM could not translate this method
