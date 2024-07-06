from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *


class ColorsBuilder(ABC):

    def withColors(
        self, colors: typing.Set[typing.Any]
    ) -> ColoringAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:
        return ColoringAlgorithmsSelector(colors)
