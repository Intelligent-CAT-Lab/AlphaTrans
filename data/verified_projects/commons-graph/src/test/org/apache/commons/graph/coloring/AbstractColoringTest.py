import pytest

from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.VertexPair import *
import unittest
import typing
from typing import *
import random
from abc import ABC


class AbstractColoringTest(unittest.TestCase, ABC):

    __test__ = False
    
    def _checkColoring(
        self,
        g: UndirectedMutableGraph,
        coloredVertices: ColoredVertices,
    ) -> None:
        for e in g.getEdges():
            vp = g.getVertices1(e)
            h = coloredVertices.getColor(vp.getHead())
            t = coloredVertices.getColor(vp.getTail())

            self.assertIsNotNone(h)
            self.assertIsNotNone(t)
            self.assertTrue(not h == t)

    
    def _createColorMap(self, numColor: int) -> typing.Dict[int, str]:
        colorCodes = {}
        for i in range(100):
            rnd = random.Random(i)
            colorCodes[i] = (
                f"\"#{'%2x' % rnd.randint(0, 255)}"
                f"{'%2x' % rnd.randint(0, 255)}"
                f"{'%2x' % rnd.randint(0, 255)}\""
            )
        return colorCodes
    
    
    def _createColorsList(self, colorNumber: int) -> typing.Set[int]:
        colors = set()
        for j in range(colorNumber):
            colors.add(j)
        return colors
