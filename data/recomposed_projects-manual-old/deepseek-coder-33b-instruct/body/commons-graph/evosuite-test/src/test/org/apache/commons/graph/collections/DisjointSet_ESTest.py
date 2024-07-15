from __future__ import annotations
import time
import re
import collections
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.collections.DisjointSet import *
from src.main.org.apache.commons.graph.collections.DisjointSetNode import *

# from src.test.org.apache.commons.graph.collections.DisjointSet_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DisjointSet_ESTest(unittest.TestCase):

    def test4(self) -> None:

        disjointSet0 = DisjointSet()
        object0 = object()
        disjointSet0.union(disjointSet0, object0)
        object1 = disjointSet0.find1(object0)
        self.assertIsNotNone(object1)

    def test3(self) -> None:

        disjointSet0 = DisjointSet()
        object0 = object()
        disjointSetNode0 = DisjointSetNode(object0)
        disjointSet0.union(disjointSetNode0, disjointSetNode0)
        self.assertEqual(0, disjointSetNode0.getRank())

    def test2(self) -> None:

        integer0 = Integer(2211)
        integer1 = Integer(0)
        integer2 = Integer(-1892)
        disjointSet0 = DisjointSet()
        disjointSet0.union(integer0, integer1)
        disjointSet0.union(integer2, integer0)
        assert not integer2.equals(integer0)

    def test1(self) -> None:

        integer0 = Integer(1477)
        disjointSet0 = DisjointSet()
        integer1 = Integer(512)
        disjointSet0.union(None, integer1)
        disjointSet0.union(integer1, integer0)
        assert not integer0.equals(integer1)

    def test0(self) -> None:

        disjointSet0 = DisjointSet()
        object0 = disjointSet0.find1(None)
        self.assertIsNone(object0)
