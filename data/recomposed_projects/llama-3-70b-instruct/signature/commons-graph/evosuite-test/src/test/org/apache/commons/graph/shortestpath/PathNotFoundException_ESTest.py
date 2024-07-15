from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import pathlib
import io
import unittest
from src.main.org.apache.commons.graph.shortestpath.PathNotFoundException import *

# from src.test.org.apache.commons.graph.shortestpath.PathNotFoundException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class PathNotFoundException_ESTest(unittest.TestCase):

    def test0(self) -> None:
        pathNotFoundException0 = PathNotFoundException("", None)
