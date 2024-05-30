from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.builder.TailVertexConnector import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.builder.AbstractGraphConnection import *
from src.main.org.apache.commons.graph.GraphException import *
from src.main.org.apache.commons.graph.scc.SccAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.test.org.apache.commons.graph.model.BaseLabeledVertex import *
from src.test.org.apache.commons.graph.model.BaseLabeledEdge import *
from src.main.org.apache.commons.graph.builder.GraphConnection import *
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.CommonsGraph import *
import os
import io

# Imports End


class SCCAlgorithmBenchmarkTestCase:

    # Class Fields Begin
    __NODES: int = None
    __EDGES: int = None
    __graph: DirectedMutableGraph[BaseLabeledVertex, BaseLabeledEdge] = None
    # Class Fields End

    # Class Methods Begin
    def testPerformTarjan(self) -> None:
        pass

    def testPerformKosaraju(self) -> None:
        pass

    def testPerformCheriyanMehlhornGabow(self) -> None:
        pass

    @staticmethod
    def setUp() -> None:
        pass

    # Class Methods End
