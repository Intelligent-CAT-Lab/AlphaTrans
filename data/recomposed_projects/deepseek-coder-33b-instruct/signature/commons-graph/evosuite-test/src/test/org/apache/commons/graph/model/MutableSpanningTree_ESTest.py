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
from src.main.org.apache.commons.graph.model.MutableSpanningTree import *

# from src.test.org.apache.commons.graph.model.MutableSpanningTree_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.Monoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Stubber import *


class MutableSpanningTree_ESTest(unittest.TestCase):

    def test6(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(return_value=None)
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        integer0 = Integer(0)

        with pytest.raises(RuntimeError):
            mutableSpanningTree0.decorateRemoveEdge(integer0)
            verifyException(
                "org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations",
                RuntimeError,
            )

    def test5(self) -> None:

        mutableSpanningTree0 = None
        try:
            mutableSpanningTree0 = MutableSpanningTree(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.model.MutableSpanningTree", e)

    def test4(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        doReturn(None).when(mapper0).map(any_int())
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        integer0 = Integer(0)
        mutableSpanningTree0.addVertex(integer0)
        mutableSpanningTree0.decorateAddEdge(integer0, integer0, integer0)
        integer1 = mutableSpanningTree0.getWeight()
        self.assertIsNone(integer1)

    def test3(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(side_effect=lambda x: integer0)
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        mutableSpanningTree0.decorateRemoveEdge(integer0)
        self.assertEqual(0, mutableSpanningTree0.getSize())

    def test2(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(0)
        mapper0 = mock(Mapper, new=ViolatedAssumptionAnswer())
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        integer1 = integerWeightBaseOperations0.append(integer0, integer0)

        with pytest.raises(RuntimeError):
            mutableSpanningTree0.decorateAddEdge(integer1, integer0, integer0)
            verifyException(
                "org.apache.commons.graph.model.BaseMutableGraph", RuntimeError
            )

    def test1(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(0)
        integer1 = Integer(0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        when(mapper0.map(any_int())).then_return(integer0)
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        mutableSpanningTree0.add_vertex(integer1)
        mutableSpanningTree0.decorate_add_edge(integer1, integer0, integer0)
        self.assertTrue(integer0 == integer1)

    def test0(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(0)
        integer1 = Integer(0)
        mapper0 = mock(Mapper, ViolatedAssumptionAnswer())
        mapper0.map = Mock(side_effect=lambda x: integer0)
        mutableSpanningTree0 = MutableSpanningTree(
            integerWeightBaseOperations0, mapper0
        )
        mutableSpanningTree0.addVertex(integer0)
        mutableSpanningTree0.decorateAddEdge(integer0, integer0, integer1)
        self.assertEqual(1, mutableSpanningTree0.getOrder())
