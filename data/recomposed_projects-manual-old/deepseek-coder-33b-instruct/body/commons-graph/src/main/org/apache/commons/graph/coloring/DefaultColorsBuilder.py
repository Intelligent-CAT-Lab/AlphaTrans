from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.UndirectedGraph import *
from src.main.org.apache.commons.graph.coloring.ColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.coloring.ColorsBuilder import *
from src.main.org.apache.commons.graph.coloring.DefaultColoringAlgorithmsSelector import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class DefaultColorsBuilder(ColorsBuilder):

    __graph: UndirectedGraph[typing.Any, typing.Any] = None

    def withColors(
        self, colors: typing.Set[typing.Any]
    ) -> ColoringAlgorithmsSelector[typing.Any, typing.Any, typing.Any]:

        colors = Assertions.checkNotNull(colors, "Colors set must be not null")
        return DefaultColoringAlgorithmsSelector(self.__graph, colors)

    def __init__(self, graph: UndirectedGraph[typing.Any, typing.Any]) -> None:
        self.__graph = graph
