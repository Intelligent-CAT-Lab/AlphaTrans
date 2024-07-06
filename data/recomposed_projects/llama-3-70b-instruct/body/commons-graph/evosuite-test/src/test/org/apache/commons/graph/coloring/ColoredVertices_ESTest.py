from __future__ import annotations
import time
import re
import os
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *

# from src.test.org.apache.commons.graph.coloring.ColoredVertices_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class ColoredVertices_ESTest(unittest.TestCase):

    def test7(self) -> None:

        coloredVertices0 = ColoredVertices()
        int0 = coloredVertices0.getRequiredColors()
        self.assertEqual(0, int0)

    def test6(self) -> None:

        coloredVertices0 = ColoredVertices()
        integer0 = -1193
        integer1 = coloredVertices0.getColor(integer0)
        coloredVertices0.addColor(integer0, integer1)
        self.assertEqual(1, coloredVertices0.getRequiredColors())

    def test5(self) -> None:

        coloredVertices0 = ColoredVertices()
        integer0 = -1193
        coloredVertices0.removeColor(integer0)
        self.assertEqual(0, coloredVertices0.getRequiredColors())

    def test4(self) -> None:

        coloredVertices0 = ColoredVertices()
        integer0 = -1193
        boolean0 = coloredVertices0.containsColoredVertex(integer0)
        self.assertFalse(boolean0)

    def test3(self) -> None:

        coloredVertices0 = ColoredVertices()
        integer0 = -1193
        coloredVertices0.addColor(integer0, integer0)
        boolean0 = coloredVertices0.containsColoredVertex(integer0)
        self.assertTrue(boolean0)

    def test2(self) -> None:

        coloredVertices0 = ColoredVertices()
        try:
            coloredVertices0.getColor(None)
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            # Impossible to get the color for a null Vertex
            self.verifyException("org.apache.commons.graph.utils.Assertions", e)

    def test1(self) -> None:

        coloredVertices0 = ColoredVertices()
        integer0 = -1193
        coloredVertices0.addColor(integer0, integer0)
        int0 = coloredVertices0.getRequiredColors()
        self.assertEqual(1, int0)

    def test0(self) -> None:

        coloredVertices0 = ColoredVertices()
        integer0 = Integer(0)
        integer1 = coloredVertices0.getColor(integer0)
        coloredVertices0.addColor(integer0, integer0)
        coloredVertices0.addColor(integer1, integer0)
        self.assertEqual(1, coloredVertices0.getRequiredColors())
