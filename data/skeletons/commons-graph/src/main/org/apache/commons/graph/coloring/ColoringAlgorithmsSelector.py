from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.coloring.ColoredVertices import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ColoringAlgorithmsSelector(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def applyingGreedyAlgorithm(self) -> ColoredVertices[typing.Any, typing.Any]:
        pass

    def applyingBackTrackingAlgorithm1(
        self, partialColoredVertex: ColoredVertices[typing.Any, typing.Any]
    ) -> ColoredVertices[typing.Any, typing.Any]:
        pass

    def applyingBackTrackingAlgorithm0(self) -> ColoredVertices[typing.Any, typing.Any]:
        pass

    # Class Methods End
