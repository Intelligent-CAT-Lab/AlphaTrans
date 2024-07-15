from __future__ import annotations
import time
import re
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.utils.Objects import *

# from src.test.org.apache.commons.graph.utils.Objects_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Objects_ESTest(unittest.TestCase):

    def test6(self) -> None:
        boolean0 = Objects.eq(None, None)
        self.assertTrue(boolean0)

    def test5(self) -> None:

        integer0 = Integer(1)
        object0 = Object()
        boolean0 = Objects.eq(integer0, object0)
        self.assertFalse(boolean0)

    def test4(self) -> None:

        integer0 = Integer(-589)
        boolean0 = Objects.eq(None, integer0)
        self.assertFalse(boolean0)

    def test3(self) -> None:

        objectArray0 = []
        int0 = Objects.hash(1, 1, objectArray0)
        self.assertEqual(1, int0)

    def test2(self) -> None:

        object0 = object()
        objectArray0 = [None] * 5
        objectArray0[0] = object0
        int0 = Objects.hash(0, 0, objectArray0)
        self.assertEqual(0, int0)

    def test1(self) -> None:

        try:
            Objects.hash(0, 0, None)
            self.fail("Expecting exception: RuntimeError")

        except TypeError as e:
            self.verifyException("org.apache.commons.graph.utils.Objects", e)

    def test0(self) -> None:

        object0 = object()
        objectArray0 = [None] * 5
        objectArray0[0] = object0
        int0 = Objects.hash(-419, 1335, objectArray0)
        self.assertEqual(-1871240068, int0)
