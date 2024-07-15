from __future__ import annotations
import re
import io
import typing
from typing import *


class DisjointSetNode:

    __rank: int = 0
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
        return self.__rank - o.getRank()

    def __init__(self, element: typing.Any) -> None:
        self.__element = element
