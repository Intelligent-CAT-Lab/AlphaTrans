from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.csv.Token import *

# from src.test.org.apache.commons.csv.Token_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class Token_ESTest(unittest.TestCase):

    def test1(self) -> None:

        token0 = Token()
        token0.reset()

    def test0(self) -> None:

        token0 = Token()
        string0 = token0.toString()
        self.assertEqual("INVALID []", string0)
