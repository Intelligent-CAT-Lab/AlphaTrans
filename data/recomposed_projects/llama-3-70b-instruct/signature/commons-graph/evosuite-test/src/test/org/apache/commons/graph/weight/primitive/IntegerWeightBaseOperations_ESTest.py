from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations import *

# from src.test.org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class IntegerWeightBaseOperations_ESTest(unittest.TestCase):

    def test11(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = -84
        int0 = integerWeightBaseOperations0.compare(integer0, integer0)
        self.assertEqual(0, int0)

    def test10(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.identity()

        with pytest.raises(RuntimeError):
            integerWeightBaseOperations0.compare(integer0, None)

    def test09(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        try:
            integerWeightBaseOperations0.inverse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertEqual(str(e), "")
            self.verifyException(
                "org.apache.commons.graph.weight.primitive.IntegerWeightBaseOperations",
                e,
            )

    def test08(self) -> None:
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = integerWeightBaseOperations0.append(None, None)
        self.assertIsNone(integer0)

    def test07(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = -181
        integer1 = integerWeightBaseOperations0.append(integer0, integer0)
        self.assertIsNotNone(integer1)

        int0 = integerWeightBaseOperations0.compare(integer1, integer0)
        self.assertEqual(-1, int0)

    def test06(self) -> None:
        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(2490)
        integer1 = integerWeightBaseOperations0.append(integer0, None)
        self.assertIsNone(integer1)

    def test05(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(183)
        integer1 = integerWeightBaseOperations0.append(integer0, integer0)
        self.assertEqual(366, integer1)

    def test04(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = Integer(0)
        integer1 = integerWeightBaseOperations0.append(integer0, integer0)
        self.assertEqual(0, integer1)

    def test03(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = -181
        integer1 = integerWeightBaseOperations0.inverse(integer0)
        int0 = integerWeightBaseOperations0.compare(integer1, integer0)
        self.assertEqual(1, int0)

    def test02(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = 3019
        integer1 = integerWeightBaseOperations0.inverse(integer0)
        self.assertNotEqual(integer1, integer0)

    def test01(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = 0
        integer1 = integerWeightBaseOperations0.inverse(integer0)
        self.assertEqual(0, integer1)

    def test00(self) -> None:

        integerWeightBaseOperations0 = IntegerWeightBaseOperations()
        integer0 = -181
        integer1 = -181
        integer2 = integerWeightBaseOperations0.append(integer0, integer1)
        self.assertEqual(-362, integer2)
