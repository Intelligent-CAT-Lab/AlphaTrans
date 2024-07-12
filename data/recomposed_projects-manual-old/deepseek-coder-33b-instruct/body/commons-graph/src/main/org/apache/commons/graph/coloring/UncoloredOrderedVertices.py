from __future__ import annotations
import re
import collections
import io
import typing
from typing import *


class UncoloredOrderedVertices:

    __orderedVertices: typing.Dict[int, typing.Set[typing.Any]] = (
        collections.defaultdict(set)
    )

    def size(self) -> int:
        return len(self.__orderedVertices)

    def iterator(self) -> typing.Iterator[typing.Any]:

        class Iterator:
            def __init__(self):
                self.keys = iter(self.__orderedVertices.keys())
                self.pending = None
                self.next = None

            def hasNext(self) -> bool:
                if self.next is not None:
                    return True

                while (self.pending is None) or (not self.pending.hasNext()):
                    if not self.keys.hasNext():
                        return False
                    self.pending = iter(self.__orderedVertices[next(self.keys)])

                self.next = next(self.pending)
                return True

            def next(self) -> typing.Any:
                if not self.hasNext():
                    raise StopIteration
                returned = self.next
                self.next = None
                return returned

            def remove(self) -> None:
                self.pending.remove()

        return Iterator()

    def compare(self, o1: int, o2: int) -> int:
        return o2 - o1

    def addVertexDegree(self, v: typing.Any, degree: int) -> None:

        vertices = self.__orderedVertices.get(degree)

        if vertices is None:
            vertices = set()

        vertices.add(v)
        self.__orderedVertices[degree] = vertices
