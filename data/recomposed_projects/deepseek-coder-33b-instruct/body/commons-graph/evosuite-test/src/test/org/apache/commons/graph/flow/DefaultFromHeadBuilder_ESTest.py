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
from src.main.org.apache.commons.graph.flow.DefaultFromHeadBuilder import *

# from src.test.org.apache.commons.graph.flow.DefaultFromHeadBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.flow.ToTailBuilder import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultFromHeadBuilder_ESTest(unittest.TestCase):

    def test1(self) -> None:

        directed_mutable_graph0 = DirectedMutableGraph()
        default_from_head_builder0 = DefaultFromHeadBuilder(
            directed_mutable_graph0, None
        )

        try:
            default_from_head_builder0.from_(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # head vertex has to be specifies when looking for the max flow
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[int, int]()
        revertedGraph0 = RevertedGraph[int, int](directedMutableGraph0)
        mapper0 = mock(Mapper[int, int], ViolatedAssumptionAnswer())
        defaultFromHeadBuilder0 = DefaultFromHeadBuilder[int, int, int](
            revertedGraph0, mapper0
        )
        integer0 = Integer(974)
        toTailBuilder0 = defaultFromHeadBuilder0.from_(integer0)
        assert toTailBuilder0 is not None
