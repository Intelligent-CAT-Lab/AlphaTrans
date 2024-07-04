from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *


class ColoringAlgorithmsSelector(ABC):

    def applyingGreedyAlgorithm(self) -> ColoredVertices[typing.Any, typing.Any]:

        # Your code here
        pass

    def applyingBackTrackingAlgorithm1(
        self, partialColoredVertex: ColoredVertices[typing.Any, typing.Any]
    ) -> ColoredVertices[typing.Any, typing.Any]:

        # Your implementation here
        pass

    def applyingBackTrackingAlgorithm0(self) -> ColoredVertices[typing.Any, typing.Any]:

        # Here you would implement the backtracking algorithm
        # The actual implementation depends on the specifics of the algorithm
        # and the ColoredVertices class.

        pass
