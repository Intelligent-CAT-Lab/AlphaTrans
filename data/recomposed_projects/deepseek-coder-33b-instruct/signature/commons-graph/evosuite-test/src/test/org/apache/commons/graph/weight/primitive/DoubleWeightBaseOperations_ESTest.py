from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations import *

# from src.test.org.apache.commons.graph.weight.primitive.DoubleWeightBaseOperations_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class DoubleWeightBaseOperations_ESTest(unittest.TestCase):

    def test10(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()

        with pytest.raises(RuntimeError):
            doubleWeightBaseOperations0.inverse(None)

    def test09(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = doubleWeightBaseOperations0.identity()

        with pytest.raises(RuntimeError):
            doubleWeightBaseOperations0.compare(double0, None)

    def test08(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = 50.34
        int0 = doubleWeightBaseOperations0.compare(double0, double0)
        self.assertEqual(0, int0)

    def test07(self) -> None:
        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = doubleWeightBaseOperations0.append(None, None)
        self.assertIsNone(double0)

    def test06(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = 50.34
        double1 = doubleWeightBaseOperations0.append(double0, double0)
        self.assertIsNotNone(double1)
        self.assertAlmostEqual(100.68, double1, delta=0.01)

    def test05(self) -> None:
        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = 50.34
        double1 = doubleWeightBaseOperations0.append(double0, None)
        self.assertIsNone(double1)

    def test04(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = -1839.848443836
        double1 = doubleWeightBaseOperations0.append(double0, double0)
        self.assertAlmostEqual(-3679.696887672, double1, delta=0.01)
        self.assertIsNotNone(double1)

    def test03(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = 50.34
        double1 = doubleWeightBaseOperations0.inverse(double0)
        double2 = doubleWeightBaseOperations0.append(double0, double1)

        self.assertAlmostEqual(0.0, double2, delta=0.01)
        self.assertIsNotNone(double2)

    def test02(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = 50.34
        double1 = doubleWeightBaseOperations0.inverse(double0)
        int0 = doubleWeightBaseOperations0.compare(double1, double0)
        self.assertEqual((-1), int0)

    def test01(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = doubleWeightBaseOperations0.identity()
        double1 = doubleWeightBaseOperations0.inverse(double0)
        self.assertAlmostEqual(-0.0, double1, delta=0.01)

        int0 = doubleWeightBaseOperations0.compare(double0, double1)
        self.assertEqual(1, int0)

    def test00(self) -> None:

        doubleWeightBaseOperations0 = DoubleWeightBaseOperations()
        double0 = -3519.0
        double1 = doubleWeightBaseOperations0.inverse(double0)
        self.assertAlmostEqual(3519.0, double1, delta=0.01)
