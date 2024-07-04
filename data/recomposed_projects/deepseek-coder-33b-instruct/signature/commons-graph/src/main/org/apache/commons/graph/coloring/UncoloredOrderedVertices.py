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
            def __init__(self, outer: UncoloredOrderedVertices):
                self.outer = outer
                self.keys = iter(sorted(self.outer.__orderedVertices.keys()))
                self.pending = None
                self.next = None

            def has_next(self) -> bool:
                if self.next is not None:
                    return True

                while self.pending is None or not self.pending.has_next():
                    try:
                        key = next(self.keys)
                    except StopIteration:
                        return False
                    self.pending = iter(self.outer.__orderedVertices[key])

                self.next = next(self.pending)
                return True

            def next(self) -> typing.Any:
                if not self.has_next():
                    raise StopIteration
                returned = self.next
                self.next = None
                return returned

            def remove(self) -> None:
                self.pending.remove()

        return Iterator(self)

    def compare(self, o1: int, o2: int) -> int:
        return o2 - o1

    def addVertexDegree(self, v: typing.Any, degree: int) -> None:

        if degree not in self.__orderedVertices:
            self.__orderedVertices[degree] = set()

        self.__orderedVertices[degree].add(v)
