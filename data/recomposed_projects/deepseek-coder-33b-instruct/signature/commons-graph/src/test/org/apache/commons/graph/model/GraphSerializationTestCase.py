from __future__ import annotations
import re
import pickle
import unittest
import pytest
import pathlib
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.builder.LinkedConnectionBuilder import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.InMemoryWeightedPath import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class GraphSerializationTestCase(unittest.TestCase):

    __FILE_NAME: str = "target/serialiazedGraph.dat"

    def testSerializeUndirectedWeightdGraph(self) -> None:

        g = CommonsGraph.newUndirectedMutableGraph(
            self.__buildWeightedGraphConnections()
        )

        self.__checkSerialization(g)

    def testSerializeUndirectedGraph(self) -> None:

        g = CommonsGraph.newUndirectedMutableGraph(self.__buildGraphConnections())

        self.__checkSerialization(g)

    def testSerializeSyncronyzedDirectedWeightdGraph(self) -> None:

        g = CommonsGraph.synchronize2(
            CommonsGraph.newDirectedMutableGraph(self.__buildWeightedGraphConnections())
        )

        self.__checkSerialization(g)

    def testSerializeSpanningTree(self) -> None:

        spanningTree = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](DoubleWeightBaseOperations(), BaseWeightedEdge[float]())

        CommonsGraph.populate(spanningTree).withConnections(
            self.__buildWeightedGraphConnections()
        )

        self.__checkSerialization(spanningTree)

    def testSerializePath(self) -> None:

        start = BaseLabeledVertex("start")
        goal = BaseLabeledVertex("goal")
        a = BaseLabeledVertex("a")
        b = BaseLabeledVertex("b")
        c = BaseLabeledVertex("c")

        g = InMemoryWeightedPath(
            start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge()
        )

        g.addConnectionInTail(start, BaseLabeledWeightedEdge("start <-> a", 1.5), a)
        g.addConnectionInTail(a, BaseLabeledWeightedEdge("a <-> b", 2), b)
        g.addConnectionInTail(b, BaseLabeledWeightedEdge("b <-> c", 3), c)
        g.addConnectionInTail(c, BaseLabeledWeightedEdge("c <-> goal", 3), goal)

        self.__checkSerialization(g)

    def testSerializeDirectedWeightdGraph(self) -> None:

        g = CommonsGraph.newDirectedMutableGraph(self.__buildWeightedGraphConnections())

        self.__checkSerialization(g)

    def testSerializeDirectedGraph(self) -> None:

        g = CommonsGraph.newDirectedMutableGraph(self.__buildGraphConnections())

        self.__checkSerialization(g)

    def cleanUp(self) -> None:

        f = pathlib.Path(self.__FILE_NAME)
        if f.exists():
            f.unlink()

    @staticmethod
    def __checkSerialization(g: Graph[BaseLabeledVertex, typing.Any]) -> None:

        with open(__FILE_NAME, "wb") as fout:
            pickle.dump(g, fout)

        with open(__FILE_NAME, "rb") as fin:
            cloned = pickle.load(fin)

        assert g == cloned

    @staticmethod
    def __buildWeightedGraphConnections() -> (
        GraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
    ):

        class GraphConnectionImpl(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
        ):
            def connect0(self):
                a = self.addVertex(BaseLabeledVertex("a"))
                b = self.addVertex(BaseLabeledVertex("b"))
                c = self.addVertex(BaseLabeledVertex("c"))
                d = self.addVertex(BaseLabeledVertex("d"))

                self.addEdge(BaseLabeledWeightedEdge[float]("a -> c", 1.0)).from_(a).to(
                    c
                )
                self.addEdge(BaseLabeledWeightedEdge[float]("c -> d", 1.0)).from_(c).to(
                    d
                )
                self.addEdge(BaseLabeledWeightedEdge[float]("d -> b", 1.0)).from_(d).to(
                    b
                )

        return GraphConnectionImpl()

    @staticmethod
    def __buildGraphConnections() -> (
        GraphConnection[BaseLabeledVertex, BaseLabeledEdge]
    ):

        class GraphConnections(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]
        ):
            def connect0(self):
                a = self.addVertex(BaseLabeledVertex("a"))
                b = self.addVertex(BaseLabeledVertex("b"))
                c = self.addVertex(BaseLabeledVertex("c"))
                d = self.addVertex(BaseLabeledVertex("d"))

                self.addEdge(BaseLabeledEdge("a -> c")).from_(a).to(c)
                self.addEdge(BaseLabeledEdge("c -> d")).from_(c).to(d)
                self.addEdge(BaseLabeledEdge("d -> b")).from_(d).to(b)

        return GraphConnections()
