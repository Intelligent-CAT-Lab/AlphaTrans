from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.Graph import *
from src.main.org.apache.commons.graph.SynchronizedUndirectedGraph import *

# from src.test.org.apache.commons.graph.SynchronizedUndirectedGraph_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class SynchronizedUndirectedGraph_ESTest(unittest.TestCase):

    def test0(self) -> None:
        synchronizedUndirectedGraph0 = SynchronizedUndirectedGraph(None)
