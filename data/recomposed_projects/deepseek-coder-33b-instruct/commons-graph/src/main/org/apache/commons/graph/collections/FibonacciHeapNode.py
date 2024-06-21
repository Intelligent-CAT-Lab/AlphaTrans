from __future__ import annotations
import io
import typing
from typing import *


class FibonacciHeapNode:

    __marked: bool = None
    __degree: int = None
    __child: FibonacciHeapNode = None

    __right: FibonacciHeapNode = self

    __left: FibonacciHeapNode = self
    __parent: FibonacciHeapNode = None
    __element: typing.Any = None

    def toString(self) -> str:

        return str(self.__element)

    def setRight(self, right: FibonacciHeapNode) -> None:

        self.__right = right

    def setParent(self, parent: FibonacciHeapNode) -> None:

        self.__parent = parent

    def setMarked(self, marked: bool) -> None:

        self.__marked = marked

    def setLeft(self, left: FibonacciHeapNode) -> None:

        self.__left = left

    def setChild(self, child: FibonacciHeapNode) -> None:

        self.__child = child

    def isMarked(self) -> bool:

        return self.__marked

    def incraeseDegree(self) -> None:

        self.__degree += 1

    def getRight(self) -> FibonacciHeapNode:

        return self.__right

    def getParent(self) -> FibonacciHeapNode:

        return self.__parent

    def getLeft(self) -> FibonacciHeapNode:

        return self.__left

    def getElement(self) -> typing.Any:

        return self.__element

    def getDegree(self) -> int:

        return self.__degree

    def getChild(self) -> FibonacciHeapNode:

        return self.__child

    def decraeseDegree(self) -> None:

        self.__degree -= 1

    def __init__(self, element: typing.Any) -> None:

        self.__degree = 0
        self.setParent(None)
        self.setChild(None)
        self.setLeft(self)
        self.setRight(self)
        self.setMarked(False)

        self.__element = element
