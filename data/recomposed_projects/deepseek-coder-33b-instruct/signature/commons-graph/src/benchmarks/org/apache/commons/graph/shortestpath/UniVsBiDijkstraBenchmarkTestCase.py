from __future__ import annotations
import re
import pathlib
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.WeightedPath import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.test.org.apache.commons.graph.model.BaseWeightedEdge import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.shortestpath.PathSourceSelector import *
from src.main.org.apache.commons.graph.shortestpath.PathWeightedEdgesBuilder import *
from src.main.org.apache.commons.graph.shortestpath.ShortestPathAlgorithmSelector import *
from src.main.org.apache.commons.graph.shortestpath.TargetSourceSelector import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class UniVsBiDijkstraBenchmarkTestCase:

    __weightOperations: OrderedMonoid[float] = None

    __vertices: typing.List[BaseLabeledVertex] = None

    __targetListBi: typing.List[BaseLabeledVertex] = None

    __targetListUni: typing.List[BaseLabeledVertex] = None

    __sourceListBi: typing.List[BaseLabeledVertex] = None

    __sourceListUni: typing.List[BaseLabeledVertex] = None

    __weightedEdges: Mapper[BaseLabeledWeightedEdge[float], float] = None

    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledWeightedEdge[float]] = (
        None
    )

    __EDGES: int = 100000
    __NODES: int = 5000

    def testPerformUnidirectionalDijkstra(self) -> None:

        source = self.__sourceListUni.pop(0)
        target = self.__targetListUni.pop(0)

        try:
            path = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge())
                .from_(source)
                .to(target)
                .applyingDijkstra(self.__weightOperations)
            )

            assert path.getSize() > 0
            assert path.getWeight() > 0.0
        except Exception as e:
            e.printStackTrace()

    def testPerformBidirectionalDijkstra(self) -> None:

        source = self.__sourceListBi.pop(0)
        target = self.__targetListBi.pop(0)

        try:
            path = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge())
                .from_(source)
                .to(target)
                .applyingBidirectionalDijkstra(self.__weightOperations)
            )

            assert path.getSize() > 0
            assert path.getWeight() > 0.0
        except Exception as e:
            e.printStackTrace()

    @staticmethod
    def setUp() -> None:

        UniVsBiDijkstraBenchmarkTestCase.__weightOperations = (
            DoubleWeightBaseOperations()
        )

        UniVsBiDijkstraBenchmarkTestCase.__weightedEdges = Mapper(
            lambda input: input.getWeight()
        )

        UniVsBiDijkstraBenchmarkTestCase.__graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection(
                r=Random(),
                addEdge=lambda src, dst: UniVsBiDijkstraBenchmarkTestCase.__addEdge(
                    src, dst
                ),
                connect0=UniVsBiDijkstraBenchmarkTestCase.__connect0,
            )
        )

        UniVsBiDijkstraBenchmarkTestCase.__sourceListUni = LinkedList()
        UniVsBiDijkstraBenchmarkTestCase.__targetListUni = LinkedList()

        UniVsBiDijkstraBenchmarkTestCase.__sourceListBi = LinkedList()
        UniVsBiDijkstraBenchmarkTestCase.__targetListBi = LinkedList()

        r = Random()

        for i in range(15):
            s = UniVsBiDijkstraBenchmarkTestCase.__vertices[
                r.nextInt(len(UniVsBiDijkstraBenchmarkTestCase.__vertices))
            ]
            UniVsBiDijkstraBenchmarkTestCase.__sourceListUni.add(s)
            UniVsBiDijkstraBenchmarkTestCase.__sourceListBi.add(s)

            t = UniVsBiDijkstraBenchmarkTestCase.__vertices[
                r.nextInt(len(UniVsBiDijkstraBenchmarkTestCase.__vertices))
            ]
            UniVsBiDijkstraBenchmarkTestCase.__targetListUni.add(t)
            UniVsBiDijkstraBenchmarkTestCase.__targetListBi.add(t)

    @staticmethod
    def __addEdge(src: BaseLabeledVertex, dst: BaseLabeledVertex) -> bool:
        try:
            UniVsBiDijkstraBenchmarkTestCase.__graph.addEdge(
                BaseLabeledWeightedEdge(
                    f"{src} -> {dst}",
                    10.0 * UniVsBiDijkstraBenchmarkTestCase.__r.nextDouble() + 1.0,
                )
            ).fromVertex(src).to(dst)
            return True
        except GraphException:
            return False

    @staticmethod
    def __connect0() -> None:
        UniVsBiDijkstraBenchmarkTestCase.__vertices = ArrayList()
        for i in range(UniVsBiDijkstraBenchmarkTestCase.__NODES):
            v = BaseLabeledVertex(str(i))
            UniVsBiDijkstraBenchmarkTestCase.__graph.addVertex(v)
            UniVsBiDijkstraBenchmarkTestCase.__vertices.add(v)

        for i in range(UniVsBiDijkstraBenchmarkTestCase.__NODES - 1):
            UniVsBiDijkstraBenchmarkTestCase.__addEdge(
                UniVsBiDijkstraBenchmarkTestCase.__vertices.get(i),
                UniVsBiDijkstraBenchmarkTestCase.__vertices.get(i + 1),
            )

        UniVsBiDijkstraBenchmarkTestCase.__addEdge(
            UniVsBiDijkstraBenchmarkTestCase.__vertices.get(
                UniVsBiDijkstraBenchmarkTestCase.__NODES - 1
            ),
            UniVsBiDijkstraBenchmarkTestCase.__vertices.get(0),
        )

        maxEdges = max(
            0,
            UniVsBiDijkstraBenchmarkTestCase.__EDGES
            - UniVsBiDijkstraBenchmarkTestCase.__NODES,
        )
        for i in range(maxEdges):
            while not UniVsBiDijkstraBenchmarkTestCase.__addEdge(
                UniVsBiDijkstraBenchmarkTestCase.__vertices.get(
                    UniVsBiDijkstraBenchmarkTestCase.__r.nextInt(
                        UniVsBiDijkstraBenchmarkTestCase.__NODES
                    )
                ),
                UniVsBiDijkstraBenchmarkTestCase.__vertices.get(
                    UniVsBiDijkstraBenchmarkTestCase.__r.nextInt(
                        UniVsBiDijkstraBenchmarkTestCase.__NODES
                    )
                ),
            ):
                pass
