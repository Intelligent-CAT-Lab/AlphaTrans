from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations import *

# from src.test.org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class FloatWeightBaseOperations_ESTest(unittest.TestCase):

    def test12(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = floatWeightBaseOperations0.identity()
        self.assertAlmostEqual(0.0, float0, delta=0.01)

        floatWeightBaseOperations0.compare(float0, float0)
        self.assertAlmostEqual(0.0, floatWeightBaseOperations0.identity(), delta=0.01)

    def test11(self) -> None:
        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = floatWeightBaseOperations0.identity()
        float1 = floatWeightBaseOperations0.inverse(float0)
        self.assertAlmostEqual(-0.0, float1, delta=0.01)

    def test10(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = floatWeightBaseOperations0.append(None, None)
        self.assertIsNone(float0)

    def test09(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = floatWeightBaseOperations0.identity()
        float1 = floatWeightBaseOperations0.append(float0, float0)
        self.assertAlmostEqual(0.0, float1, delta=0.01)
        self.assertIsNotNone(float1)

    def test08(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = float(1509.5292578769947)
        float1 = floatWeightBaseOperations0.append(float0, None)
        self.assertIsNone(float1)

    def test07(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = float(-1.0)

        with self.assertRaises(RuntimeError):
            floatWeightBaseOperations0.compare(float0, None)

    def test06(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        # Undeclared exception
        try:
            floatWeightBaseOperations0.inverse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            # no message in exception (getMessage() returned null)
            self.verifyException(
                "org.apache.commons.graph.weight.primitive.FloatWeightBaseOperations", e
            )

    def test05(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = float(0.0)
        float1 = float(-1281.1265)
        float2 = floatWeightBaseOperations0.append(float0, float1)
        self.assertAlmostEqual(-1281.1265, float2, delta=0.01)
        self.assertIsNotNone(float2)

    def test04(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = float(1.0)
        float1 = floatWeightBaseOperations0.append(float0, float0)
        self.assertIsNotNone(float1)
        self.assertAlmostEqual(2.0, float1, delta=0.01)

    def test03(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = float(-1.0)
        float1 = floatWeightBaseOperations0.append(float0, float0)
        self.assertIsNotNone(float1)

        int0 = floatWeightBaseOperations0.compare(float1, float0)
        self.assertEqual(-1, int0)

    def test02(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = floatWeightBaseOperations0.identity()
        self.assertAlmostEqual(0.0, float0, delta=0.01)

        float1 = float(1.0)
        int0 = floatWeightBaseOperations0.compare(float1, float0)
        self.assertEqual(1, int0)

    def test01(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = 2350.746606741365
        float1 = floatWeightBaseOperations0.inverse(float0)
        self.assertAlmostEqual(-2350.7466, float1, delta=0.01)

    def test00(self) -> None:

        floatWeightBaseOperations0 = FloatWeightBaseOperations()
        float0 = float(-1.0)
        float1 = floatWeightBaseOperations0.inverse(float0)
        self.assertAlmostEqual(1.0, float1, delta=0.01)
