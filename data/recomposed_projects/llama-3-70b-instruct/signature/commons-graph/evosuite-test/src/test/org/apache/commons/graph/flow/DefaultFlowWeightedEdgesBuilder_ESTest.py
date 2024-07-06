from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder import *

# from src.test.org.apache.commons.graph.flow.DefaultFlowWeightedEdgesBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.flow.FromHeadBuilder import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultFlowWeightedEdgesBuilder_ESTest(unittest.TestCase):

    def test1(self) -> None:

        defaultFlowWeightedEdgesBuilder0 = DefaultFlowWeightedEdgesBuilder(None)

        with self.assertRaises(RuntimeError):
            defaultFlowWeightedEdgesBuilder0.whereEdgesHaveWeights(None)
            self.fail("Expecting exception: RuntimeError")

        verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        defaultFlowWeightedEdgesBuilder0 = DefaultFlowWeightedEdgesBuilder[int, int](
            directedMutableGraph0
        )
        mapper0 = Mock(Mapper[int, int])
        fromHeadBuilder0 = defaultFlowWeightedEdgesBuilder0.whereEdgesHaveWeights(
            mapper0
        )
        self.assertIsNotNone(fromHeadBuilder0)
