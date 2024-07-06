from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.DefaultTailVertexConnector import *

# from src.test.org.apache.commons.graph.builder.DefaultTailVertexConnector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultTailVertexConnector_ESTest(unittest.TestCase):

    def test4(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        integer0 = Integer(-1471)
        default_tail_vertex_connector0 = DefaultTailVertexConnector(
            undirected_mutable_graph0, integer0, integer0
        )

        try:
            default_tail_vertex_connector0.to(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.BaseGraph", e)

    def test3(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph()
        default_tail_vertex_connector0 = DefaultTailVertexConnector(
            undirected_mutable_graph0, None, None
        )

        # Undeclared exception in Java code, so we use try-except block to catch the exception
        try:
            default_tail_vertex_connector0.to(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Null tail vertex not admitted
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test2(self) -> None:

        integer0 = -1
        defaultTailVertexConnector0 = DefaultTailVertexConnector(
            None, integer0, integer0
        )

        try:
            defaultTailVertexConnector0.to(integer0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.builder.DefaultTailVertexConnector", e
            )

    def test1(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        integer0 = int((-1471))
        undirectedMutableGraph0.addVertex(integer0)
        defaultTailVertexConnector0 = DefaultTailVertexConnector[int, int](
            undirectedMutableGraph0, integer0, integer0
        )
        defaultTailVertexConnector0.to(integer0)

    def test0(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int]()
        integer0 = -1471
        integer1 = 0
        defaultTailVertexConnector0 = DefaultTailVertexConnector[int, int](
            undirectedMutableGraph0, integer1, integer0
        )
