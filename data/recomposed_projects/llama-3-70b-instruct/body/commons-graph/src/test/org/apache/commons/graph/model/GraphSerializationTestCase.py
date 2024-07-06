from __future__ import annotations
import re
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
        g: MutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
            CommonsGraph.newUndirectedMutableGraph(
                self.__buildWeightedGraphConnections()
            )
        )

        self.__checkSerialization(g)

    def testSerializeUndirectedGraph(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            CommonsGraph.newUndirectedMutableGraph(self.__buildGraphConnections())
        )
        self.__checkSerialization(g)

    def testSerializeSyncronyzedDirectedWeightdGraph(self) -> None:
        g: Graph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
            CommonsGraph.synchronize2(
                CommonsGraph.newDirectedMutableGraph(
                    GraphSerializationTestCase.__buildWeightedGraphConnections()
                )
            )
        )

        GraphSerializationTestCase.__checkSerialization(g)

    def testSerializeSpanningTree(self) -> None:
        spanningTree: MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ] = MutableSpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ](
            DoubleWeightBaseOperations(), BaseWeightedEdge[float]()
        )
        CommonsGraph.populate(spanningTree).withConnections(
            self.__buildWeightedGraphConnections()
        )
        self.__checkSerialization(spanningTree)

    def testSerializePath(self) -> None:
        start: BaseLabeledVertex = BaseLabeledVertex("start")
        goal: BaseLabeledVertex = BaseLabeledVertex("goal")
        a: BaseLabeledVertex = BaseLabeledVertex("a")
        b: BaseLabeledVertex = BaseLabeledVertex("b")
        c: BaseLabeledVertex = BaseLabeledVertex("c")

        g: InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[double], double
        ] = InMemoryWeightedPath[
            BaseLabeledVertex, BaseLabeledWeightedEdge[double], double
        ](
            start, goal, DoubleWeightBaseOperations(), BaseWeightedEdge[double]()
        )

        g.addConnectionInTail(
            start, BaseLabeledWeightedEdge[double]("start <-> a", 1.5), a
        )
        g.addConnectionInTail(a, BaseLabeledWeightedEdge[double]("a <-> b", 2.0), b)
        g.addConnectionInTail(b, BaseLabeledWeightedEdge[double]("b <-> c", 3.0), c)
        g.addConnectionInTail(
            c, BaseLabeledWeightedEdge[double]("c <-> goal", 3.0), goal
        )

        self.__checkSerialization(g)

    def testSerializeDirectedWeightdGraph(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
            CommonsGraph.newDirectedMutableGraph(self.__buildWeightedGraphConnections())
        )
        self.__checkSerialization(g)

    def testSerializeDirectedGraph(self) -> None:
        g: MutableGraph[BaseLabeledVertex, BaseLabeledEdge] = (
            CommonsGraph.newDirectedMutableGraph(self.__buildGraphConnections())
        )
        self.__checkSerialization(g)

    def cleanUp(self) -> None:
        f = pathlib.Path(self.__FILE_NAME)
        if f.exists():
            f.unlink()

    @staticmethod
    def __checkSerialization(g: Graph[BaseLabeledVertex, typing.Any]) -> None:

        pass  # LLM could not translate this method

    @staticmethod
    def __buildWeightedGraphConnections() -> (
        GraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]
    ):

        pass  # LLM could not translate this method

    @staticmethod
    def __buildGraphConnections() -> (
        GraphConnection[BaseLabeledVertex, BaseLabeledEdge]
    ):
        return AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]().connect0()
