from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.shortestpath.ShortestDistances import *

# from src.test.org.apache.commons.graph.shortestpath.ShortestDistances_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.weight.OrderedMonoid import *
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ShortestDistances_ESTest(unittest.TestCase):

    def test7(self) -> None:

        shortestDistances0 = ShortestDistances[Integer, Integer](None)
        shortestDistances0.setWeight(None, None)

        try:
            shortestDistances0.compare(None, None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException(
                "org.apache.commons.graph.shortestpath.ShortestDistances", e
            )

    def test6(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = Integer(0)
        boolean0 = shortestDistances0.alreadyVisited(integer0)
        self.assertFalse(boolean0)

    def test5(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = Integer(0)
        int0 = shortestDistances0.compare(integer0, integer0)
        self.assertEqual(0, int0)

    def test4(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = Integer(0)
        shortestDistances0.setWeight(integer0, integer0)
        integer1 = Integer(1065)
        int0 = shortestDistances0.compare(integer1, integer0)
        self.assertEqual(1, int0)

    def test3(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = Integer(0)
        shortestDistances0.setWeight(integer0, integer0)
        integer1 = Integer(1065)
        int0 = shortestDistances0.compare(integer0, integer1)
        self.assertEqual((-1), int0)

    def test2(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = Integer(-1099)
        integer1 = shortestDistances0.getWeight(integer0)
        self.assertIsNone(integer1)

    def test1(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = -1099
        shortestDistances0.setWeight(integer0, integer0)
        boolean0 = shortestDistances0.alreadyVisited(integer0)
        self.assertTrue(boolean0)

    def test0(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        shortestDistances0 = ShortestDistances(integerWeightBaseOperations0)
        integer0 = -1099
        integer1 = integerWeightBaseOperations0.inverse(integer0)
        shortestDistances0.setWeight(integer1, integer1)
        shortestDistances0.setWeight(integer0, integer1)
        int0 = shortestDistances0.compare(integer1, integer0)
        self.assertEqual(0, int0)
