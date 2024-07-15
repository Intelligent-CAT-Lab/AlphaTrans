from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class ColoredVertices:

    __usedColor: typing.List[typing.Any] = []
    __coloredVertices: Dict[V, C] = {}

    def getRequiredColors(self) -> int:
        return len(self.__usedColor)

    def getColor(self, v: typing.Any) -> typing.Any:

        v = Assertions.checkNotNull(v, "Impossible to get the color for a null Vertex")

        return self.__coloredVertices.get(v)

    def containsColoredVertex(self, vertex: typing.Any) -> bool:
        return vertex in self.__coloredVertices

    def removeColor(self, v: typing.Any) -> None:

        color = self.__coloredVertices.pop(v, None)
        if color is not None:
            self.__usedColor.remove(color)

    def addColor(self, v: typing.Any, color: typing.Any) -> None:

        self.__coloredVertices[v] = color
        idx = self.__usedColor.index(color) if color in self.__usedColor else -1
        if idx == -1:
            self.__usedColor.append(color)
        else:
            self.__usedColor[idx] = color

    def __init__(self) -> None:
        self.__usedColor = []
        self.__coloredVertices = {}
