from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
import typing
from typing import *
import io

# Imports End


class DefaultColorsBuilder(ColorsBuilder):

    # Class Fields Begin
    __graph: UndirectedGraph[typing.Any, typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def withColors(
        self, colors: typing.Set[typing.Any]
    ) -> ColoringAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:
        pass

    def __init__(self, graph: UndirectedGraph[typing.Any, typing.Any]) -> None:
        pass

    # Class Methods End
