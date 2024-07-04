from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.coloring.NotEnoughColorsException import *

# from src.test.org.apache.commons.graph.coloring.NotEnoughColorsException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class NotEnoughColorsException_ESTest(unittest.TestCase):

    def test0(self) -> None:

        linkedHashSet0 = set()
        notEnoughColorsException0 = NotEnoughColorsException(linkedHashSet0)
