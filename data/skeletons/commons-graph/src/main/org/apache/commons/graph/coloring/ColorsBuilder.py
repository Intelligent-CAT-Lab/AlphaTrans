from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
import typing
from typing import *
import io
from abc import ABC

# Imports End


class ColorsBuilder(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def withColors(
        self, colors: typing.Set[typing.Any]
    ) -> ColoringAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:
        pass

    # Class Methods End
