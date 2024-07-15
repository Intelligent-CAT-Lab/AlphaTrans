from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.MutableGraph import *
from src.main.org.apache.commons.graph.builder.DefaultGrapher import *

# from src.test.org.apache.commons.graph.builder.DefaultGrapher_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.builder.HeadVertexConnector import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultGrapher_ESTest(unittest.TestCase):

    def test4(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        defaultGrapher0 = DefaultGrapher(undirectedMutableGraph0)

        with pytest.raises(RuntimeError):
            defaultGrapher0.addEdge(None)
            verifyException("org.apache.commons.graph.utils.Assertions", RuntimeError)

    def test2(self) -> None:

        undirectedMutableGraph0 = UndirectedMutableGraph()
        defaultGrapher0 = DefaultGrapher(undirectedMutableGraph0)

        with pytest.raises(RuntimeError):
            defaultGrapher0.addVertex(None)
            pytest.fail("Expecting exception: RuntimeError")

    def test1(self) -> None:

        defaultGrapher0 = DefaultGrapher[int, int](None)
        integer0 = int(0)

        with self.assertRaises(RuntimeError):
            defaultGrapher0.addVertex(integer0)

    def test0(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, new_callable=ViolatedAssumptionAnswer)
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        defaultGrapher0 = DefaultGrapher(mutableSpanningTree0)
        integer0 = Integer(2512)
        headVertexConnector0 = defaultGrapher0.addEdge(integer0)
        assert headVertexConnector0 is not None
