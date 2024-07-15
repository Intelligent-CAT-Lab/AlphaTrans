from __future__ import annotations
import math
import time
import re
import os
import decimal
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations import *

# from src.test.org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class BigDecimalWeightBaseOperations_ESTest(unittest.TestCase):

    def test13(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal(10)
        int0 = bigDecimalWeightBaseOperations0.compare(bigDecimal0, bigDecimal0)
        self.assertEqual(0, int0)

    def test12(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()

        try:
            bigDecimalWeightBaseOperations0.inverse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertEqual(str(e), "Expecting exception: RuntimeError")
            self.assertEqual(type(e), RuntimeError)

    def test11(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = bigDecimalWeightBaseOperations0.identity()
        bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0)
        self.assertEqual(bigDecimal0, bigDecimal1)

    def test10(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = bigDecimalWeightBaseOperations0.append(None, None)
        self.assertIsNone(bigDecimal0)

    def test09(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal(4972)
        bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0)
        self.assertIsNotNone(bigDecimal1)

        int0 = bigDecimalWeightBaseOperations0.compare(bigDecimal0, bigDecimal1)
        self.assertEqual(-1, int0)

    def test08(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal(-620)
        bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, None)
        self.assertIsNone(bigDecimal1)

    def test07(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        try:
            bigDecimalWeightBaseOperations0.compare(None, None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.verifyException(
                "org.apache.commons.graph.weight.primitive.BigDecimalWeightBaseOperations",
                e,
            )

    def test06(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal(10)
        bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0)
        self.assertIsNot(bigDecimal1, bigDecimal0)

    def test05(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal((-647))
        bigDecimal1 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal0)
        self.assertEqual(short((-1294)), bigDecimal1.to_eng_string())

    def test04(self) -> None:
        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = bigDecimalWeightBaseOperations0.identity()
        bigDecimal1 = decimal.Decimal(-647)
        int0 = bigDecimalWeightBaseOperations0.compare(bigDecimal0, bigDecimal1)
        self.assertEqual(1, int0)

    def test03(self) -> None:
        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal(-647)
        bigDecimal1 = bigDecimalWeightBaseOperations0.inverse(bigDecimal0)
        self.assertNotEqual(bigDecimal1, bigDecimal0)

    def test02(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = decimal.Decimal(0)
        bigDecimal1 = decimal.Decimal(-1227)
        mathContext0 = decimal.Context(prec=128)
        bigDecimal2 = bigDecimal0.subtract(bigDecimal1, mathContext0)
        bigDecimal3 = bigDecimalWeightBaseOperations0.inverse(bigDecimal2)
        self.assertNotEqual(bigDecimal1, bigDecimal3)

    def test01(self) -> None:
        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = bigDecimalWeightBaseOperations0.identity()
        bigDecimal1 = bigDecimalWeightBaseOperations0.inverse(bigDecimal0)
        self.assertEqual(0, bigDecimal1)

    def test00(self) -> None:

        bigDecimalWeightBaseOperations0 = BigDecimalWeightBaseOperations()
        bigDecimal0 = bigDecimalWeightBaseOperations0.identity()
        bigDecimal1 = decimal.Decimal(-647)
        bigDecimal2 = bigDecimalWeightBaseOperations0.append(bigDecimal0, bigDecimal1)
        self.assertEqual(short(-647), bigDecimal2.shortValue())
