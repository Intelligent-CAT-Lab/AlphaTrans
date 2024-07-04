from __future__ import annotations
import time
import re
import mock
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.coloring.UncoloredOrderedVertices import *

# from src.test.org.apache.commons.graph.coloring.UncoloredOrderedVertices_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *
# from src.main.org.evosuite.runtime.ViolatedAssumptionAnswer import *
# from src.main.org.evosuite.shaded.org.mockito.Mockito import *
# from src.main.org.evosuite.shaded.org.mockito.stubbing.Answer import *


class UncoloredOrderedVertices_ESTest(unittest.TestCase):

    def test10(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices[LinkedHashSet[object]]()
        int0 = uncoloredOrderedVertices0.size()
        self.assertEqual(0, int0)

    def test09(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices()
        object0 = Object()
        integer0 = Integer(-855)
        uncoloredOrderedVertices0.addVertexDegree(object0, integer0)
        uncoloredOrderedVertices0.addVertexDegree(object0, integer0)
        self.assertEqual(1, uncoloredOrderedVertices0.size())

    def test08(self) -> None:

        integer0 = -759
        uncoloredOrderedVertices0 = UncoloredOrderedVertices()
        object0 = object()
        uncoloredOrderedVertices0.addVertexDegree(object0, integer0)
        consumer0 = mock(Consumer, new_callable=ViolatedAssumptionAnswer)
        uncoloredOrderedVertices0.forEach(consumer0)
        self.assertEqual(1, uncoloredOrderedVertices0.size())

    def test06(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices()

        try:
            uncoloredOrderedVertices0.compare(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.coloring.UncoloredOrderedVertices", e
            )

    def test05(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices()
        object0 = object()

        # Undeclared exception in Java code, so we use try-except block to catch the exception
        try:
            uncoloredOrderedVertices0.addVertexDegree(object0, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.graph.coloring.UncoloredOrderedVertices", e
            )

    def test04(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices()
        integer0 = -93
        integer1 = -653
        int0 = uncoloredOrderedVertices0.compare(integer0, integer1)
        self.assertEqual(-1, int0)

    def test03(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices()
        integer0 = int(Integer.getInteger("H", -2222))
        integer1 = Integer(0)
        int0 = uncoloredOrderedVertices0.compare(integer0, integer1)
        self.assertEqual(1, int0)

    def test02(self) -> None:

        integer0 = Integer(0)
        uncoloredOrderedVertices0 = (
            UncoloredOrderedVertices < LinkedHashSet < Object >> ()
        )
        int0 = uncoloredOrderedVertices0.compare(integer0, integer0)
        self.assertEqual(0, int0)

    def test01(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices()
        iterator0 = uncoloredOrderedVertices0.iterator()
        self.assertIsNotNone(iterator0)

    def test00(self) -> None:

        uncoloredOrderedVertices0 = UncoloredOrderedVertices[int]()
        integer0 = -1
        uncoloredOrderedVertices0.addVertexDegree(integer0, integer0)
        int0 = uncoloredOrderedVertices0.size()
        self.assertEqual(1, int0)
