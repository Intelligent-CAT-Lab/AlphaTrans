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
from src.main.org.apache.commons.graph.flow.DefaultToTailBuilder import *

# from src.test.org.apache.commons.graph.flow.DefaultToTailBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.flow.MaxFlowAlgorithmSelector import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultToTailBuilder_ESTest(unittest.TestCase):

    def test1(self) -> None:

        defaultToTailBuilder0 = DefaultToTailBuilder[int, int, int](None, None, None)

        try:
            defaultToTailBuilder0.to(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        mapper0 = mock(Mapper[int, int], ViolatedAssumptionAnswer())
        integer0 = Integer(0)
        defaultToTailBuilder0 = DefaultToTailBuilder[int, int, int](
            revertedGraph0, mapper0, integer0
        )
        maxFlowAlgorithmSelector0 = defaultToTailBuilder0.to(integer0)
        assert maxFlowAlgorithmSelector0 is not None
