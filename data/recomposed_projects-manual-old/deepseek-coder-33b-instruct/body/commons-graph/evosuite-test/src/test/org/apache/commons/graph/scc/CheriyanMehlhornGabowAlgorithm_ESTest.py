from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.DirectedGraph import *
from src.main.org.apache.commons.graph.model.DirectedMutableGraph import *
from src.main.org.apache.commons.graph.model.RevertedGraph import *
from src.main.org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm import *

# from src.test.org.apache.commons.graph.scc.CheriyanMehlhornGabowAlgorithm_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class CheriyanMehlhornGabowAlgorithm_ESTest(unittest.TestCase):

    def test3(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        cheriyanMehlhornGabowAlgorithm0 = CheriyanMehlhornGabowAlgorithm(
            directedMutableGraph0
        )
        linkedHashSet0 = set()
        directedMutableGraph0.addVertex(linkedHashSet0)
        cheriyanMehlhornGabowAlgorithm0.perform()
        set0 = cheriyanMehlhornGabowAlgorithm0.perform()
        self.assertEqual(1, len(set0))

    def test2(self) -> None:

        cheriyanMehlhornGabowAlgorithm0 = CheriyanMehlhornGabowAlgorithm(None)

        with pytest.raises(RuntimeError):
            cheriyanMehlhornGabowAlgorithm0.perform()

    def test1(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph()
        revertedGraph0 = RevertedGraph(directedMutableGraph0)
        cheriyanMehlhornGabowAlgorithm0 = CheriyanMehlhornGabowAlgorithm(revertedGraph0)
        set0 = cheriyanMehlhornGabowAlgorithm0.perform()
        self.assertEqual(0, len(set0))

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[LinkedHashSet[int], int]()
        linkedHashSet0 = LinkedHashSet[int]()
        directedMutableGraph0.addVertex(linkedHashSet0)
        integer0 = -3629
        linkedHashSet1 = LinkedHashSet[int]()
        directedMutableGraph0.addEdge(linkedHashSet1, integer0, linkedHashSet1)
        cheriyanMehlhornGabowAlgorithm0 = CheriyanMehlhornGabowAlgorithm[
            LinkedHashSet[int], int
        ](directedMutableGraph0)
        set0 = cheriyanMehlhornGabowAlgorithm0.perform()
        self.assertEqual(1, len(set0))
