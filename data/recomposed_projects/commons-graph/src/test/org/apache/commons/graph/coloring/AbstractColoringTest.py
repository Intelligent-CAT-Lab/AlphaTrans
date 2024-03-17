# Imports Begin
from src.main.org.apache.commons.graph.model.UndirectedMutableGraph import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
from src.main.org.apache.commons.graph.VertexPair import *
import unittest
import typing
from typing import *
import numbers
from abc import ABC

# Imports End


class AbstractColoringTest(unittest.TestCase, ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _createColorsList(self, colorNumber: int) -> typing.Set[int]:

        colors = set()
        for j in range(colorNumber):
            colors.add(j)
        return colors

    def _createColorMap(self, numColor: int) -> typing.Dict[int, str]:

        colorCodes = {}
        for i in range(100):
            rnd = random.Random(i)
            colorCodes[i] = (
                f"\"#{'%2x' % rnd.nextInt(255)}{'%2x' % rnd.nextInt(255)}{'%2x' % rnd.nextInt(255)}\""
            )
        return colorCodes

    def _checkColoring(
        self,
        g: UndirectedMutableGraph[typing.Any, typing.Any],
        coloredVertices: ColoredVertices[typing.Any, typing.Any],
    ) -> None:

        for e in g.getEdges():
            vp = g.getVertices1(e)
            h = coloredVertices.getColor(vp.getHead())
            t = coloredVertices.getColor(vp.getTail())
            assert h is not None
            assert t is not None
            assert h != t

    def __init__(self) -> None:

        pass

    # Class Methods End
