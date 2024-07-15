from __future__ import annotations
import re
import random
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
        source: BaseLabeledVertex = self.__sourceListUni.pop(0)
        target: BaseLabeledVertex = self.__targetListUni.pop(0)

        try:
            path: WeightedPath[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
            ] = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(source)
                .to(target)
                .applyingDijkstra(self.__weightOperations)
            )

            assert path.getSize() > 0
            assert path.getWeight() > 0.0
        except Exception as e:
            e.printStackTrace()

    def testPerformBidirectionalDijkstra(self) -> None:
        source: BaseLabeledVertex = self.__sourceListBi.removeFirst()
        target: BaseLabeledVertex = self.__targetListBi.removeFirst()

        try:
            path: WeightedPath[
                BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
            ] = (
                CommonsGraph.findShortestPath(self.__graph)
                .whereEdgesHaveWeights(BaseWeightedEdge[float]())
                .from_(source)
                .to_(target)
                .applyingBidirectionalDijkstra(self.__weightOperations)
            )

            assertTrue(path.getSize() > 0)
            assertTrue(path.getWeight() > 0.0)
        except Exception as e:
            e.printStackTrace()

    @staticmethod
    def setUp() -> None:
        UniVsBiDijkstraBenchmarkTestCase.__weightOperations = (
            DoubleWeightBaseOperations()
        )

        UniVsBiDijkstraBenchmarkTestCase.__weightedEdges = Mapper[
            BaseLabeledWeightedEdge[float], float
        ]()

        UniVsBiDijkstraBenchmarkTestCase.__graph = CommonsGraph.newDirectedMutableGraph(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledWeightedEdge[float]]()
        )

        UniVsBiDijkstraBenchmarkTestCase.__vertices = []

        for i in range(UniVsBiDijkstraBenchmarkTestCase.__NODES):
            v = BaseLabeledVertex(str(i))
            UniVsBiDijkstraBenchmarkTestCase.__graph.addVertex(v)
            UniVsBiDijkstraBenchmarkTestCase.__vertices.append(v)

        for i in range(UniVsBiDijkstraBenchmarkTestCase.__NODES - 1):
            UniVsBiDijkstraBenchmarkTestCase.__graph.addEdge(
                BaseLabeledWeightedEdge[float](
                    f"{UniVsBiDijkstraBenchmarkTestCase.__vertices[i]} -> {UniVsBiDijkstraBenchmarkTestCase.__vertices[i + 1]}",
                    10.0 * random.random() + 1.0,
                )
            ).from_(UniVsBiDijkstraBenchmarkTestCase.__vertices[i]).to(
                UniVsBiDijkstraBenchmarkTestCase.__vertices[i + 1]
            )

        UniVsBiDijkstraBenchmarkTestCase.__graph.addEdge(
            BaseLabeledWeightedEdge[float](
                f"{UniVsBiDijkstraBenchmarkTestCase.__vertices[UniVsBiDijkstraBenchmarkTestCase.__NODES - 1]} -> {UniVsBiDijkstraBenchmarkTestCase.__vertices[0]}",
                10.0 * random.random() + 1.0,
            )
        ).from_(
            UniVsBiDijkstraBenchmarkTestCase.__vertices[
                UniVsBiDijkstraBenchmarkTestCase.__NODES - 1
            ]
        ).to(
            UniVsBiDijkstraBenchmarkTestCase.__vertices[0]
        )

        maxEdges = max(
            0,
            UniVsBiDijkstraBenchmarkTestCase.__EDGES
            - UniVsBiDijkstraBenchmarkTestCase.__NODES,
        )
        for i in range(maxEdges):
            while (
                not UniVsBiDijkstraBenchmarkTestCase.__graph.addEdge(
                    BaseLabeledWeightedEdge[float](
                        f"{UniVsBiDijkstraBenchmarkTestCase.__vertices[random.randint(0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1)]} -> {UniVsBiDijkstraBenchmarkTestCase.__vertices[random.randint(0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1)]}",
                        10.0 * random.random() + 1.0,
                    )
                )
                .from_(
                    UniVsBiDijkstraBenchmarkTestCase.__vertices[
                        random.randint(0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1)
                    ]
                )
                .to(
                    UniVsBiDijkstraBenchmarkTestCase.__vertices[
                        random.randint(0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1)
                    ]
                )
            ):
                pass

        UniVsBiDijkstraBenchmarkTestCase.__sourceListUni = []
        UniVsBiDijkstraBenchmarkTestCase.__targetListUni = []

        UniVsBiDijkstraBenchmarkTestCase.__sourceListBi = []
        UniVsBiDijkstraBenchmarkTestCase.__targetListBi = []

        random = Random()

        for i in range(15):
            s = UniVsBiDijkstraBenchmarkTestCase.__vertices[
                random.randint(0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1)
            ]
            UniVsBiDijkstraBenchmarkTestCase.__sourceListUni.append(s)
            UniVsBiDijkstraBenchmarkTestCase.__sourceListBi.append(s)

            t = UniVsBiDijkstraBenchmarkTestCase.__vertices[
                random.randint(0, UniVsBiDijkstraBenchmarkTestCase.__NODES - 1)
            ]
            UniVsBiDijkstraBenchmarkTestCase.__targetListUni.append(t)
            UniVsBiDijkstraBenchmarkTestCase.__targetListBi.append(t)
