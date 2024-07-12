from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.language.Caverphone2 import *

# from src.test.org.apache.commons.codec.language.Caverphone2_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Caverphone2_ESTest(unittest.TestCase):

    def test1(self) -> None:

        caverphone2_0 = Caverphone2()
        boolean0 = caverphone2_0.isEncodeEqual(None, "vDUr@!/?[a^")
        self.assertFalse(boolean0)

    def test0(self) -> None:

        caverphone2_0 = Caverphone2()
        string0 = caverphone2_0.encode("")
        self.assertEqual("1111111111", string0)
