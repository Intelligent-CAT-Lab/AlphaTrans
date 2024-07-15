from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.weight.primitive.LongWeightBaseOperations import *

# from src.test.org.apache.commons.graph.weight.primitive.LongWeightBaseOperations_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class LongWeightBaseOperations_ESTest(unittest.TestCase):

    def test12(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        try:
            longWeightBaseOperations0.inverse(None)
            self.fail("Expecting exception: RuntimeError")

        except Exception as e:
            self.assertIsInstance(e, RuntimeError)
            self.assertEqual(str(e), "")
            self.verifyException(
                "org.apache.commons.graph.weight.primitive.LongWeightBaseOperations", e
            )

    def test11(self) -> None:
        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = longWeightBaseOperations0.identity()
        self.assertEqual(0, long0)

    def test10(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = int(1)
        int0 = longWeightBaseOperations0.compare(long0, long0)
        self.assertEqual(0, int0)

    def test09(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = longWeightBaseOperations0.append(None, None)
        self.assertIsNone(long0)

    def test08(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = long(1)
        long1 = longWeightBaseOperations0.append(long0, long0)
        self.assertIsNotNone(long1)
        self.assertEqual(2, long1)

    def test07(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = long(0)
        long1 = longWeightBaseOperations0.append(long0, None)
        self.assertIsNone(long1)

    def test06(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = int("_%*N7rY(JGY".encode("utf-8").hex(), 16)

        with pytest.raises(RuntimeError):
            longWeightBaseOperations0.compare(None, long0)

    def test05(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = int(0)
        long1 = int(-1532)
        long2 = longWeightBaseOperations0.append(long1, long0)
        self.assertEqual(-1532, long2)
        self.assertIsNotNone(long2)

    def test04(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = int(0)
        long1 = longWeightBaseOperations0.append(long0, long0)
        self.assertEqual(long1, long0)

    def test03(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = long(1)
        long1 = longWeightBaseOperations0.inverse(long0)
        int0 = longWeightBaseOperations0.compare(long1, long0)
        self.assertEqual((-1), int0)

    def test02(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = long(1)
        long1 = longWeightBaseOperations0.inverse(long0)
        int0 = longWeightBaseOperations0.compare(long0, long1)
        self.assertEqual(1, int0)

    def test01(self) -> None:

        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = long(1)
        long1 = longWeightBaseOperations0.inverse(long0)
        long2 = longWeightBaseOperations0.inverse(long1)
        self.assertEqual(long2, long0)

    def test00(self) -> None:
        longWeightBaseOperations0 = LongWeightBaseOperations()
        long0 = long(0)
        long1 = longWeightBaseOperations0.inverse(long0)
        self.assertEqual(0, long1)
