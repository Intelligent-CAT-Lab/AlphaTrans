from __future__ import annotations
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

        actual = (
            CommonsGraph.minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingPrimAlgorithm(DoubleWeightBaseOperations())
        )

        assert actual.getSize() > 0

    def testPerformKruskal(self) -> None:

        actual = (
            CommonsGraph.minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingKruskalAlgorithm(DoubleWeightBaseOperations())
        )

        assert actual.getSize() > 0

    def testPerformBoruvka(self) -> None:

        actual = (
            CommonsGraph.minimumSpanningTree(self.__graph)
            .whereEdgesHaveWeights(self.__weightedEdges)
            .fromArbitrarySource()
            .applyingBoruvkaAlgorithm(DoubleWeightBaseOperations())
        )

        assert actual.getSize() > 0

    @staticmethod
    def setUp() -> None:

        MinimumSpanningTreeBenchmarkTestCase.__weightedEdges = Mapper(
            lambda input: input.getWeight()
        )

        MinimumSpanningTreeBenchmarkTestCase.__graph = CommonsGraph.newUndirectedMutableGraph(
            AbstractGraphConnection(
                lambda: (
                    vertices := [
                        BaseLabeledVertex(str(i))
                        for i in range(MinimumSpanningTreeBenchmarkTestCase.__NODES)
                    ],
                    [
                        MinimumSpanningTreeBenchmarkTestCase.__graph.addVertex(v)
                        for v in vertices
                    ],
                    [
                        MinimumSpanningTreeBenchmarkTestCase.__graph.addEdge(
                            BaseLabeledWeightedEdge(
                                f"{vertices[i]} -> {vertices[i + 1]}",
                                float(random.randint(0, 10)),
                            )
                        )
                        .from_(vertices[i])
                        .to(vertices[i + 1])
                        for i in range(MinimumSpanningTreeBenchmarkTestCase.__NODES - 1)
                    ],
                    MinimumSpanningTreeBenchmarkTestCase.__graph.addEdge(
                        BaseLabeledWeightedEdge(
                            f"{vertices[MinimumSpanningTreeBenchmarkTestCase.__NODES - 1]} -> {vertices[0]}",
                            float(random.randint(0, 10)),
                        )
                    )
                    .from_(vertices[MinimumSpanningTreeBenchmarkTestCase.__NODES - 1])
                    .to(vertices[0]),
                    maxEdges := max(
                        0,
                        MinimumSpanningTreeBenchmarkTestCase.__EDGES
                        - MinimumSpanningTreeBenchmarkTestCase.__NODES,
                    ),
                    [
                        MinimumSpanningTreeBenchmarkTestCase.__graph.addEdge(
                            BaseLabeledWeightedEdge(
                                f"{vertices[random.randint(0, MinimumSpanningTreeBenchmarkTestCase.__NODES - 1)]} -> {vertices[random.randint(0, MinimumSpanningTreeBenchmarkTestCase.__NODES - 1)]}",
                                float(random.randint(0, 10)),
                            )
                        )
                        .from_(
                            vertices[
                                random.randint(
                                    0, MinimumSpanningTreeBenchmarkTestCase.__NODES - 1
                                )
                            ]
                        )
                        .to(
                            vertices[
                                random.randint(
                                    0, MinimumSpanningTreeBenchmarkTestCase.__NODES - 1
                                )
                            ]
                        )
                        for _ in range(maxEdges)
                    ],
                )
            )
        )
