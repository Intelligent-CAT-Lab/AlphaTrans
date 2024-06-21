from __future__ import annotations
import io
import os
from src.main.org.apache.commons.graph.CommonsGraph import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *


class SCCAlgorithmBenchmarkTestCase:

    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None

    __EDGES: int = 5000

    __NODES: int = 5000

    def testPerformTarjan(self) -> None:

        actual = CommonsGraph.findStronglyConnectedComponent(
            self.__graph
        ).applyingTarjan()
        assert len(actual) > 0

    def testPerformKosaraju(self) -> None:

        actual = CommonsGraph.findStronglyConnectedComponent(
            self.__graph
        ).applyingKosarajuSharir0()
        assert len(actual) > 0

    def testPerformCheriyanMehlhornGabow(self) -> None:

        actual = CommonsGraph.findStronglyConnectedComponent(
            self.__graph
        ).applyingCheriyanMehlhornGabow()
        assert len(actual) > 0

    @staticmethod
    def setUp() -> None:

        class GraphConnection(
            AbstractGraphConnection[BaseLabeledVertex, BaseLabeledEdge]
        ):
            def connect0(self) -> None:
                vertices = []
                for i in range(SCCAlgorithmBenchmarkTestCase.__NODES):
                    v = BaseLabeledVertex(str(i))
                    self.addVertex(v)
                    vertices.append(v)

                r = random.Random()
                for i in range(SCCAlgorithmBenchmarkTestCase.__EDGES):
                    v1 = r.randint(0, SCCAlgorithmBenchmarkTestCase.__NODES - 1)
                    v2 = r.randint(0, SCCAlgorithmBenchmarkTestCase.__NODES - 1)

                    try:
                        self.addEdge(BaseLabeledEdge(f"{v1} -> {v2}")).from_(
                            vertices[v1]
                        ).to(vertices[v2])
                    except GraphException:
                        pass

        SCCAlgorithmBenchmarkTestCase.__graph = CommonsGraph.newDirectedMutableGraph(
            GraphConnection()
        )
