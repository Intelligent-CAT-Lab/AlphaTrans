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
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.spanning.DefaultSpanningWeightedEdgeMapperBuilder import *

# from src.test.org.apache.commons.graph.spanning.DefaultSpanningWeightedEdgeMapperBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.spanning.SpanningTreeSourceSelector import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultSpanningWeightedEdgeMapperBuilder_ESTest(unittest.TestCase):

    def test1(self) -> None:

        defaultSpanningWeightedEdgeMapperBuilder0 = (
            DefaultSpanningWeightedEdgeMapperBuilder[int, int](None)
        )

        try:
            defaultSpanningWeightedEdgeMapperBuilder0.whereEdgesHaveWeights(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        defaultSpanningWeightedEdgeMapperBuilder0 = (
            DefaultSpanningWeightedEdgeMapperBuilder[int, int](revertedGraph0)
        )
        mapper0 = Mock(Mapper[int, int])
        spanningTreeSourceSelector0 = (
            defaultSpanningWeightedEdgeMapperBuilder0.whereEdgesHaveWeights(mapper0)
        )
        self.assertIsNotNone(spanningTreeSourceSelector0)
