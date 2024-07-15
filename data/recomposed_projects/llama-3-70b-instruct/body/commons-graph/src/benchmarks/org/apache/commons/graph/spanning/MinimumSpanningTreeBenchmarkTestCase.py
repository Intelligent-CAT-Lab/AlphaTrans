from __future__ import annotations
import re
import io
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.SpanningTree import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledWeightedEdge import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeAlgorithmSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *
from src.main.org.apache.commons.graph.spanning.SpanningWeightedEdgeMapperBuilder import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class MinimumSpanningTreeBenchmarkTestCase:

    __weightedEdges: Mapper[BaseLabeledWeightedEdge[float], float] = None

    __graph: UndirectedMutableGraph[
        BaseLabeledVertex, BaseLabeledWeightedEdge[float]
    ] = None

    __EDGES: int = 6000
    __NODES: int = 1000

    def testPerformPrim(self) -> None:
        actual: SpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ] = (
            minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingPrimAlgorithm(DoubleWeightBaseOperations())
        )
        assertTrue(actual.getSize() > 0)

    def testPerformKruskal(self) -> None:
        actual: SpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ] = (
            minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        assertTrue(actual.getSize() > 0)

    def testPerformBoruvka(self) -> None:
        actual: SpanningTree[
            BaseLabeledVertex, BaseLabeledWeightedEdge[float], float
        ] = (
            minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
        )

        assertTrue(actual.getSize() > 0)

    @staticmethod
    def setUp() -> None:

        pass  # LLM could not translate this method
