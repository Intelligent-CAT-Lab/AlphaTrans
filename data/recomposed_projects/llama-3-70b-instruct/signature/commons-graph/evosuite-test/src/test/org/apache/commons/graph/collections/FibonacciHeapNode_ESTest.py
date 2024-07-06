from __future__ import annotations
import time
import re
import collections
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.collections.FibonacciHeapNode import *

# from src.test.org.apache.commons.graph.collections.FibonacciHeapNode_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class FibonacciHeapNode_ESTest(unittest.TestCase):

    def test26(self) -> None:

        object0 = object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        boolean0 = fibonacciHeapNode0.isMarked()
        self.assertEqual(0, fibonacciHeapNode0.getDegree())
        self.assertFalse(boolean0)

    def test25(self) -> None:

        integer0 = -24
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.decraeseDegree()
        fibonacciHeapNode0.setChild(fibonacciHeapNode0)
        fibonacciHeapNode0.getChild()
        self.assertEqual(-1, fibonacciHeapNode0.getDegree())

    def test24(self) -> None:

        object0 = object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        fibonacciHeapNode1 = fibonacciHeapNode0.getParent()

        self.assertFalse(fibonacciHeapNode0.isMarked())
        self.assertEqual(0, fibonacciHeapNode0.getDegree())
        self.assertIsNone(fibonacciHeapNode1)

    def test23(self) -> None:

        fibonacciHeapNode0 = FibonacciHeapNode(None)
        try:
            fibonacciHeapNode0.toString()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.evosuite.runtime.System", e)

    def test22(self) -> None:

        integer0 = -24
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode1 = fibonacciHeapNode0.getChild()

        self.assertFalse(fibonacciHeapNode0.isMarked())
        self.assertIsNone(fibonacciHeapNode1)
        self.assertEqual(0, fibonacciHeapNode0.getDegree())

    def test21(self) -> None:

        object0 = Object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        fibonacciHeapNode0.getElement()
        self.assertEqual(0, fibonacciHeapNode0.getDegree())
        self.assertFalse(fibonacciHeapNode0.isMarked())

    def test20(self) -> None:

        object0 = object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        int0 = fibonacciHeapNode0.getDegree()
        self.assertEqual(0, int0)
        self.assertFalse(fibonacciHeapNode0.isMarked())

    def test19(self) -> None:

        integer0 = Integer(823)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.incraeseDegree()
        fibonacciHeapNode0.setChild(fibonacciHeapNode0)
        fibonacciHeapNode0.getChild()
        self.assertEqual(1, fibonacciHeapNode0.getDegree())

    def test18(self) -> None:

        integer0 = Integer(-613)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.setChild(fibonacciHeapNode0)
        fibonacciHeapNode1 = fibonacciHeapNode0.getChild()

        self.assertFalse(fibonacciHeapNode1.isMarked())
        self.assertEqual(0, fibonacciHeapNode1.getDegree())

    def test17(self) -> None:

        integer0 = Integer(823)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.setChild(fibonacciHeapNode0)
        assert not fibonacciHeapNode0.isMarked()

        fibonacciHeapNode0.setMarked(True)
        fibonacciHeapNode0.getChild()
        assert fibonacciHeapNode0.isMarked()

    def test16(self) -> None:

        integer0 = Integer(1)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.decraeseDegree()
        int0 = fibonacciHeapNode0.getDegree()
        self.assertEqual(-1, int0)

    def test15(self) -> None:

        integer0 = Integer(0)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.incraeseDegree()
        int0 = fibonacciHeapNode0.getDegree()
        self.assertEqual(1, int0)

    def test14(self) -> None:

        fibonacciHeapNode0 = FibonacciHeapNode(None)
        fibonacciHeapNode0.getElement()
        self.assertEqual(0, fibonacciHeapNode0.getDegree())
        self.assertFalse(fibonacciHeapNode0.isMarked())

    def test13(self) -> None:

        integer0 = -24
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.decraeseDegree()
        fibonacciHeapNode0.getLeft()
        self.assertEqual(-1, fibonacciHeapNode0.getDegree())

    def test12(self) -> None:

        integer0 = Integer(823)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.incraeseDegree()
        fibonacciHeapNode0.getLeft()
        self.assertEqual(1, fibonacciHeapNode0.getDegree())

    def test11(self) -> None:

        integer0 = Integer(992)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        assert not fibonacciHeapNode0.isMarked()

        fibonacciHeapNode0.setMarked(True)
        fibonacciHeapNode0.getLeft()
        assert fibonacciHeapNode0.isMarked()

    def test10(self) -> None:

        object0 = object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        fibonacciHeapNode0.set_left(None)
        fibonacciHeapNode1 = fibonacciHeapNode0.get_left()

        assert not fibonacciHeapNode0.is_marked()
        assert fibonacciHeapNode1 is None
        assert fibonacciHeapNode0.get_degree() == 0

    def test09(self) -> None:

        object0 = object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        fibonacciHeapNode0.decraeseDegree()
        fibonacciHeapNode0.setParent(fibonacciHeapNode0)
        fibonacciHeapNode0.getParent()
        self.assertEqual(-1, fibonacciHeapNode0.getDegree())

    def test08(self) -> None:

        integer0 = Integer(852)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.incraeseDegree()
        fibonacciHeapNode0.setParent(fibonacciHeapNode0)
        fibonacciHeapNode0.getParent()
        self.assertEqual(1, fibonacciHeapNode0.getDegree())

    def test07(self) -> None:

        integer0 = Integer(0)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.setParent(fibonacciHeapNode0)
        fibonacciHeapNode1 = fibonacciHeapNode0.getParent()

        self.assertFalse(fibonacciHeapNode1.isMarked())
        self.assertEqual(0, fibonacciHeapNode1.getDegree())

    def test06(self) -> None:

        integer0 = Integer(0)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        self.assertFalse(fibonacciHeapNode0.isMarked())

        fibonacciHeapNode0.setMarked(True)
        fibonacciHeapNode0.setParent(fibonacciHeapNode0)
        fibonacciHeapNode0.getParent()
        self.assertEqual(0, fibonacciHeapNode0.getDegree())

    def test05(self) -> None:

        integer0 = -24
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.decraeseDegree()
        fibonacciHeapNode0.getRight()
        self.assertEqual(-1, fibonacciHeapNode0.getDegree())

    def test04(self) -> None:

        integer0 = -613
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.incraeseDegree()
        fibonacciHeapNode0.getRight()
        self.assertEqual(1, fibonacciHeapNode0.getDegree())

    def test03(self) -> None:

        integer0 = Integer(0)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        self.assertFalse(fibonacciHeapNode0.isMarked())

        fibonacciHeapNode0.setMarked(True)
        fibonacciHeapNode0.getRight()
        self.assertTrue(fibonacciHeapNode0.isMarked())

    def test02(self) -> None:

        object0 = object()
        fibonacciHeapNode0 = FibonacciHeapNode(object0)
        fibonacciHeapNode0.setRight(None)
        fibonacciHeapNode1 = fibonacciHeapNode0.getRight()

        assert not fibonacciHeapNode0.isMarked()
        assert fibonacciHeapNode1 is None
        assert fibonacciHeapNode0.getDegree() == 0

    def test01(self) -> None:

        integer0 = Integer(0)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        self.assertFalse(fibonacciHeapNode0.isMarked())

        fibonacciHeapNode0.setMarked(True)
        boolean0 = fibonacciHeapNode0.isMarked()
        self.assertTrue(boolean0)

    def test00(self) -> None:

        integer0 = Integer(0)
        fibonacciHeapNode0 = FibonacciHeapNode(integer0)
        fibonacciHeapNode0.toString()
        self.assertFalse(fibonacciHeapNode0.isMarked())
        self.assertEqual(0, fibonacciHeapNode0.getDegree())
