from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.connectivity.ConnectivityAlgorithmsSelector import *
from src.main.org.apache.commons.graph.connectivity.DefaultConnectivityBuilder import *

# from src.test.org.apache.commons.graph.connectivity.DefaultConnectivityBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultConnectivityBuilder_ESTest(unittest.TestCase):

    def test3(self) -> None:

        defaultConnectivityBuilder0 = DefaultConnectivityBuilder(None)

        try:
            defaultConnectivityBuilder0.includingAllVertices()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.connectivity.DefaultConnectivityBuilder", e
            )

    def test2(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        defaultConnectivityBuilder0 = DefaultConnectivityBuilder[int, int](
            undirectedMutableGraph0
        )
        integerArray0 = [0] * 6
        connectivityAlgorithmsSelector0 = defaultConnectivityBuilder0.includingVertices(
            integerArray0
        )
        assert connectivityAlgorithmsSelector0 is not None

    def test1(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        defaultConnectivityBuilder0 = DefaultConnectivityBuilder(
            undirectedMutableGraph0
        )

        with pytest.raises(RuntimeError):
            defaultConnectivityBuilder0.includingVertices(None)
            pytest.fail("Expecting exception: RuntimeError")

    def test0(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph[int, int]()
        defaultConnectivityBuilder0 = DefaultConnectivityBuilder[int, int](
            undirectedMutableGraph0
        )
        connectivityAlgorithmsSelector0 = (
            defaultConnectivityBuilder0.includingAllVertices()
        )
        assert connectivityAlgorithmsSelector0 is not None
