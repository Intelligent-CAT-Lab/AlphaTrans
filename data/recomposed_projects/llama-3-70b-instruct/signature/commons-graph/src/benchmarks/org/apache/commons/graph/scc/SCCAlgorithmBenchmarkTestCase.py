from __future__ import annotations
import re
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
        actual: Set[Set[BaseLabeledVertex]] = (
            CommonsGraph.findStronglyConnectedComponent(self.__graph).applyingTarjan()
        )
        self.assertTrue(actual.size() > 0)

    def testPerformKosaraju(self) -> None:
        actual = CommonsGraph.findStronglyConnectedComponent(
            self.__graph
        ).applyingKosarajuSharir0()
        self.assertTrue(actual.size() > 0)

    def testPerformCheriyanMehlhornGabow(self) -> None:
        actual = CommonsGraph.findStronglyConnectedComponent(
            self.__graph
        ).applyingCheriyanMehlhornGabow()
        self.assertTrue(len(actual) > 0)

    @staticmethod
    def setUp() -> None:

        pass  # LLM could not translate this method
