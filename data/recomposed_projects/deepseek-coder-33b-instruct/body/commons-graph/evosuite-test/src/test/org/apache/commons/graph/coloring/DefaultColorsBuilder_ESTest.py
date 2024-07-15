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
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.DefaultColorsBuilder import *

# from src.test.org.apache.commons.graph.coloring.DefaultColorsBuilder_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class DefaultColorsBuilder_ESTest(unittest.TestCase):

    def test1(self) -> None:

        undirected_mutable_graph0 = UndirectedMutableGraph[LinkedHashSet[int], int]()
        default_colors_builder0 = DefaultColorsBuilder[LinkedHashSet[int], int](
            undirected_mutable_graph0
        )

        try:
            default_colors_builder0.with_colors(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test0(self) -> None:

        integer_weight_base_operations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mutable_spanning_tree0 = MutableSpanningTree(
            integer_weight_base_operations0, mapper0
        )
        default_colors_builder0 = DefaultColorsBuilder(mutable_spanning_tree0)
        linked_hash_set0 = set()
        coloring_algorithms_selector0 = default_colors_builder0.with_colors(
            linked_hash_set0
        )
        assert coloring_algorithms_selector0 is not None
