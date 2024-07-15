from __future__ import annotations
import re
import io
import typing
from typing import *


class UncoloredOrderedVertices:

    __orderedVertices: typing.Dict[int, typing.Set[typing.Any]] = {}

    def size(self) -> int:
        return len(self.__orderedVertices)

    def iterator(self) -> typing.Iterator[typing.Any]:
        return self.__orderedVertices.keys().__iter__()

    def compare(self, o1: int, o2: int) -> int:
        return o2 - o1

    def addVertexDegree(self, v: typing.Any, degree: int) -> None:
        vertices = self.__orderedVertices.get(degree)

        if vertices == None:
            vertices = set()

        vertices.add(v)
        self.__orderedVertices[degree] = vertices
