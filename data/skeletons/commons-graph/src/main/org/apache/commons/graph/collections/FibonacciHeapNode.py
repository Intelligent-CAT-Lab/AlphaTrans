from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class FibonacciHeapNode:

    # Class Fields Begin
    __element: typing.Any = None
    __parent: FibonacciHeapNode = None
    __left: FibonacciHeapNode = None
    __right: FibonacciHeapNode = None
    __child: FibonacciHeapNode = None
    __degree: int = None
    __marked: bool = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def setRight(self, right: FibonacciHeapNode) -> None:
        pass

    def setParent(self, parent: FibonacciHeapNode) -> None:
        pass

    def setMarked(self, marked: bool) -> None:
        pass

    def setLeft(self, left: FibonacciHeapNode) -> None:
        pass

    def setChild(self, child: FibonacciHeapNode) -> None:
        pass

    def isMarked(self) -> bool:
        pass

    def incraeseDegree(self) -> None:
        pass

    def getRight(self) -> FibonacciHeapNode:
        pass

    def getParent(self) -> FibonacciHeapNode:
        pass

    def getLeft(self) -> FibonacciHeapNode:
        pass

    def getElement(self) -> typing.Any:
        pass

    def getDegree(self) -> int:
        pass

    def getChild(self) -> FibonacciHeapNode:
        pass

    def decraeseDegree(self) -> None:
        pass

    def __init__(self, element: typing.Any) -> None:
        pass

    # Class Methods End
