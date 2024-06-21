from __future__ import annotations
import io
import typing
from typing import *


class DisjointSetNode:

    __rank: int = 0

    __parent: DisjointSetNode = self
    __element: typing.Any = None

    def setRank(self, rank: int) -> None:

        self.__rank = rank

    def setParent(self, parent: DisjointSetNode) -> None:

        self.__parent = parent

    def increaseRank(self) -> None:

        self.__rank += 1

    def getRank(self) -> int:

        return self.__rank

    def getParent(self) -> DisjointSetNode:

        return self.__parent

    def getElement(self) -> typing.Any:

        return self.__element

    def compareTo(self, o: DisjointSetNode) -> int:

        if self.__rank < o.getRank():
            return -1
        elif self.__rank == o.getRank():
            return 0
        else:
            return 1

    def __init__(self, element: typing.Any) -> None:

        self.__element = element
