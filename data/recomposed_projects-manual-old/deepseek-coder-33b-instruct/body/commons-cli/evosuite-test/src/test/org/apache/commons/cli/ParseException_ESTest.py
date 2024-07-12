from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.ParseException import *

# from src.test.org.apache.commons.cli.ParseException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ParseException_ESTest(unittest.TestCase):

    def test0(self) -> None:
        parseException0 = ParseException("org.apache.commons.cli.ParseException")
