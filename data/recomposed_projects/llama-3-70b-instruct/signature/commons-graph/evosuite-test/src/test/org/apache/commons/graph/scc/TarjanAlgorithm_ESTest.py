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
from src.main.org.apache.commons.graph.scc.TarjanAlgorithm import *

# from src.test.org.apache.commons.graph.scc.TarjanAlgorithm_ESTest_scaffolding import *
from src.main.org.apache.commons.graph.scc.TarjanVertexMetaInfo import *

# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class TarjanAlgorithm_ESTest(unittest.TestCase):

    def test4(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            LinkedHashSet[TarjanVertexMetaInfo], LinkedHashSet[TarjanVertexMetaInfo]
        ]()
        linkedHashSet0 = LinkedHashSet[TarjanVertexMetaInfo]()
        directedMutableGraph0.addVertex(linkedHashSet0)
        directedMutableGraph0.addEdge(linkedHashSet0, linkedHashSet0, linkedHashSet0)
        tarjanAlgorithm0 = TarjanAlgorithm[
            LinkedHashSet[TarjanVertexMetaInfo], LinkedHashSet[TarjanVertexMetaInfo]
        ](directedMutableGraph0)
        set0 = tarjanAlgorithm0.perform()
        self.assertEqual(1, len(set0))

    def test3(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            LinkedHashSet[TarjanVertexMetaInfo], LinkedHashSet[TarjanVertexMetaInfo]
        ]()
        linkedHashSet0 = LinkedHashSet[TarjanVertexMetaInfo]()
        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()
        linkedHashSet0.add(tarjanVertexMetaInfo0)
        directedMutableGraph0.addVertex(linkedHashSet0)
        linkedHashSet1 = LinkedHashSet[TarjanVertexMetaInfo]()
        directedMutableGraph0.addVertex(linkedHashSet1)
        directedMutableGraph0.addEdge(linkedHashSet0, linkedHashSet0, linkedHashSet1)
        tarjanAlgorithm0 = TarjanAlgorithm[
            LinkedHashSet[TarjanVertexMetaInfo], LinkedHashSet[TarjanVertexMetaInfo]
        ](directedMutableGraph0)
        set0 = tarjanAlgorithm0.perform()
        self.assertEqual(2, len(set0))

    def test2(self) -> None:

        # Create a DirectedMutableGraph
        directedMutableGraph0 = DirectedMutableGraph()

        # Create a LinkedHashSet
        linkedHashSet0 = LinkedHashSet()

        # Add the LinkedHashSet to the DirectedMutableGraph
        directedMutableGraph0.addVertex(linkedHashSet0)

        # Create a TarjanVertexMetaInfo
        tarjanVertexMetaInfo0 = TarjanVertexMetaInfo()

        # Add the TarjanVertexMetaInfo to the LinkedHashSet
        linkedHashSet0.add(tarjanVertexMetaInfo0)

        # Add the LinkedHashSet to the DirectedMutableGraph again
        directedMutableGraph0.addVertex(linkedHashSet0)

        # Create a TarjanAlgorithm
        tarjanAlgorithm0 = TarjanAlgorithm(directedMutableGraph0)

        # Perform the TarjanAlgorithm
        set0 = tarjanAlgorithm0.perform()

        # Assert that the size of the result is 1
        self.assertEqual(1, len(set0))

    def test1(self) -> None:

        tarjanAlgorithm0 = TarjanAlgorithm[TarjanVertexMetaInfo, TarjanVertexMetaInfo](
            None
        )

        try:
            tarjanAlgorithm0.perform()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.graph.scc.TarjanAlgorithm", e)

    def test0(self) -> None:

        directedMutableGraph0 = DirectedMutableGraph[
            TarjanVertexMetaInfo, TarjanVertexMetaInfo
        ]()
        tarjanAlgorithm0 = TarjanAlgorithm[TarjanVertexMetaInfo, TarjanVertexMetaInfo](
            directedMutableGraph0
        )
        set0 = tarjanAlgorithm0.perform()
        self.assertTrue(set0.isEmpty())
