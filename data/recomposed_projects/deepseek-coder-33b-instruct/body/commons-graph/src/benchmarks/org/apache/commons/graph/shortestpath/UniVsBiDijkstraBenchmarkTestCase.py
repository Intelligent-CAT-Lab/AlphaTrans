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
            print(e)

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
            print(e)

    @staticmethod
    def setUp() -> None:

        pass  # LLM could not translate this method
