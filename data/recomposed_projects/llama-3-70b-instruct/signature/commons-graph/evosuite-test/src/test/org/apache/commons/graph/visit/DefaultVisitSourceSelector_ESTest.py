from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.Mapper import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *
from src.main.org.apache.commons.graph.visit.DefaultVisitSourceSelector import *

# from src.test.org.apache.commons.graph.visit.DefaultVisitSourceSelector_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.visit.VisitAlgorithmsSelector import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DefaultVisitSourceSelector_ESTest(unittest.TestCase):

    def test2(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        defaultVisitSourceSelector0 = DefaultVisitSourceSelector(directedMutableGraph0)

        try:
            defaultVisitSourceSelector0.from_(directedMutableGraph0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Vertex {} does not exist in the Graph
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test1(self) -> None:

        defaultVisitSourceSelector0 = DefaultVisitSourceSelector(None)
        object0 = object()

        try:
            defaultVisitSourceSelector0.from_(object0)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.visit.DefaultVisitSourceSelector", e
            )

    def test0(self) -> None:

        integer_weight_base_operations0 = IntegerWeightBaseOperations()
        mutable_spanning_tree0 = MutableSpanningTree(
            integer_weight_base_operations0, None
        )
        integer0 = Integer(0)
        mutable_spanning_tree0.addVertex(integer0)
        default_visit_source_selector0 = DefaultVisitSourceSelector(
            mutable_spanning_tree0
        )
        visit_algorithms_selector0 = default_visit_source_selector0.from_(integer0)
        assert visit_algorithms_selector0 is not None
