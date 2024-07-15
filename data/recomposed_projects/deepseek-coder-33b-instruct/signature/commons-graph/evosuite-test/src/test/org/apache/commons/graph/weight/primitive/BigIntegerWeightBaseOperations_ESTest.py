from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations import *

# from src.test.org.apache.commons.graph.weight.primitive.BigIntegerWeightBaseOperations_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BigIntegerWeightBaseOperations_ESTest(unittest.TestCase):

    def test10(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        try:
            bigIntegerWeightBaseOperations0.inverse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")

    def test09(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()

        try:
            bigIntegerWeightBaseOperations0.compare(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "")
            self.assertEqual(type(e), RuntimeError)

    def test08(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = bigIntegerWeightBaseOperations0.append(None, None)
        self.assertIsNone(bigInteger0)

    def test07(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = 2
        bigInteger1 = bigIntegerWeightBaseOperations0.append(bigInteger0, None)
        self.assertIsNone(bigInteger1)

    def test06(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = 10
        bigInteger1 = bigIntegerWeightBaseOperations0.append(bigInteger0, bigInteger0)
        self.assertNotEqual(bigInteger1, bigInteger0)

    def test05(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = 2
        bigInteger1 = bigIntegerWeightBaseOperations0.inverse(bigInteger0)
        bigInteger2 = bigIntegerWeightBaseOperations0.append(bigInteger1, bigInteger1)
        self.assertEqual(-4, bigInteger2)

    def test04(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = 2
        bigInteger1 = bigIntegerWeightBaseOperations0.inverse(bigInteger0)
        int0 = bigIntegerWeightBaseOperations0.compare(bigInteger1, bigInteger0)
        self.assertEqual((-1), int0)

    def test03(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = 1293
        bigInteger1 = 2
        int0 = bigIntegerWeightBaseOperations0.compare(bigInteger0, bigInteger1)
        self.assertEqual(1, int0)

    def test02(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = bigIntegerWeightBaseOperations0.identity()
        int0 = bigIntegerWeightBaseOperations0.compare(bigInteger0, bigInteger0)
        self.assertEqual(0, int0)

    def test01(self) -> None:
        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = bigIntegerWeightBaseOperations0.identity()
        bigInteger1 = bigInteger0**0
        bigInteger2 = bigIntegerWeightBaseOperations0.inverse(bigInteger1)
        bigInteger3 = bigIntegerWeightBaseOperations0.inverse(bigInteger2)
        self.assertNotEqual(bigInteger2, bigInteger3)

    def test00(self) -> None:

        bigIntegerWeightBaseOperations0 = BigIntegerWeightBaseOperations()
        bigInteger0 = bigIntegerWeightBaseOperations0.identity()
        bigInteger1 = bigIntegerWeightBaseOperations0.inverse(bigInteger0)
        bigInteger2 = bigIntegerWeightBaseOperations0.append(bigInteger1, bigInteger0)
        assert bigInteger2 is not None
        assert bigInteger2 != bigInteger0
