from __future__ import annotations
import time
import re
import collections
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.collections.DisjointSetNode import *

# from src.test.org.apache.commons.graph.collections.DisjointSetNode_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DisjointSetNode_ESTest(unittest.TestCase):

    def test10(self) -> None:

        disjointSetNode0 = DisjointSetNode(None)
        disjointSetNode1 = disjointSetNode0.getParent()
        self.assertEqual(0, disjointSetNode1.getRank())

    def test09(self) -> None:

        object0 = object()
        disjointSetNode0 = DisjointSetNode(object0)
        disjointSetNode0.getElement()
        self.assertEqual(0, disjointSetNode0.getRank())

    def test08(self) -> None:

        integer0 = Integer(0)
        disjointSetNode0 = DisjointSetNode(integer0)
        disjointSetNode1 = DisjointSetNode(disjointSetNode0)
        disjointSetNode1.compareTo(disjointSetNode1)
        self.assertEqual(0, disjointSetNode1.getRank())

    def test07(self) -> None:

        integer0 = Integer(0)
        disjointSetNode0 = DisjointSetNode(integer0)
        integer1 = disjointSetNode0.getRank()
        self.assertEqual(0, integer1)

    def test06(self) -> None:

        disjointSetNode0 = DisjointSetNode(None)

        with self.assertRaises(RuntimeError):
            disjointSetNode0.compareTo(None)
            self.fail("Expecting exception: RuntimeError")

    def test05(self) -> None:

        object0 = object()
        disjointSetNode0 = DisjointSetNode(object0)
        disjointSetNode1 = DisjointSetNode(disjointSetNode0)
        disjointSetNode1.set_rank(-2439)
        disjointSetNode2 = DisjointSetNode(disjointSetNode0)
        int0 = disjointSetNode1.compare_to(disjointSetNode2)
        self.assertEqual(-2439, disjointSetNode1.get_rank())
        self.assertEqual(-1, int0)

    def test04(self) -> None:

        integer0 = Integer(0)
        disjointSetNode0 = DisjointSetNode(integer0)
        disjointSetNode1 = DisjointSetNode(disjointSetNode0)
        disjointSetNode2 = DisjointSetNode(integer0)
        disjointSetNode2.increase_rank()
        int0 = disjointSetNode2.compare_to(disjointSetNode1)
        self.assertEqual(1, disjointSetNode2.get_rank())
        self.assertEqual(1, int0)

    def test03(self) -> None:

        disjointSetNode0 = DisjointSetNode(None)
        disjointSetNode0.getElement()
        self.assertEqual(0, disjointSetNode0.getRank())

    def test02(self) -> None:

        object0 = object()
        disjointSetNode0 = DisjointSetNode(object0)
        disjointSetNode1 = DisjointSetNode(disjointSetNode0)
        disjointSetNode1.set_parent(None)
        disjointSetNode2 = disjointSetNode1.get_parent()
        self.assertIsNone(disjointSetNode2)
        self.assertEqual(0, disjointSetNode1.get_rank())

    def test01(self) -> None:

        disjointSetNode0 = DisjointSetNode(None)
        disjointSetNode0.setRank(-537)
        disjointSetNode0.getRank()
        self.assertEqual(-537, disjointSetNode0.getRank())

    def test00(self) -> None:

        integer0 = Integer(-2439)
        disjointSetNode0 = DisjointSetNode(integer0)
        self.assertEqual(0, disjointSetNode0.getRank())

        disjointSetNode0.setRank(1)
        integer1 = disjointSetNode0.getRank()
        self.assertEqual(1, integer1)
