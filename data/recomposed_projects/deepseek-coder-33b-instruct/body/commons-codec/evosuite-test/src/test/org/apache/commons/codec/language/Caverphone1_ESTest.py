from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.Caverphone1 import *

# from src.test.org.apache.commons.codec.language.Caverphone1_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Caverphone1_ESTest(unittest.TestCase):

    def test2(self) -> None:

        caverphone1_0 = Caverphone1()
        boolean0 = caverphone1_0.isEncodeEqual("KM1111", None)
        self.assertFalse(boolean0)

    def test1(self) -> None:

        caverphone1_0 = Caverphone1()
        boolean0 = caverphone1_0.isEncodeEqual("KzzvlW3 ;C", "")
        self.assertFalse(boolean0)

    def test0(self) -> None:

        caverphone1_0 = Caverphone1()
        string0 = caverphone1_0.encode("yWl8")
        self.assertEqual("111111", string0)
