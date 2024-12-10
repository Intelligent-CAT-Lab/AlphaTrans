from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.graph.utils.Assertions import *
from src.main.org.apache.commons.graph.collections.FibonacciHeapNode import *
import typing
from typing import *
import io

# Imports End


class FibonacciHeap:

    # Class Fields Begin
    __LOG_PHI: float = None
    __elementsIndex: typing.Set[typing.Any] = None
    __comparator: typing.Callable[[typing.Any, typing.Any], int] = None
    __size: int = None
    __trees: int = None
    __markedNodes: int = None
    __minimumNode: FibonacciHeapNode[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:
        pass

    def toArray(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:
        pass

    def toArray0(self) -> typing.List[typing.Any]:
        pass

    def toArray(self) -> typing.List[typing.Any]:
        pass

    def size(self) -> int:
        pass

    def retainAll(self, c: typing.Collection[typing.Any]) -> bool:
        pass

    def removeAll(self, c: typing.Collection[typing.Any]) -> bool:
        pass

    def remove1(self, o: typing.Any) -> bool:
        pass

    def remove(self, o: typing.Any) -> bool:
        pass

    def remove0(self) -> typing.Any:
        pass

    def remove(self) -> typing.Any:
        pass

    def potential(self) -> int:
        pass

    def poll(self) -> typing.Any:
        pass

    def peek(self) -> typing.Any:
        pass

    def offer(self, e: typing.Any) -> bool:
        pass

    def iterator(self) -> typing.Iterator[typing.Any]:
        pass

    def isEmpty(self) -> bool:
        pass

    def element(self) -> typing.Any:
        pass

    def containsAll(self, c: typing.Collection[typing.Any]) -> bool:
        pass

    def contains(self, o: typing.Any) -> bool:
        pass

    def clear(self) -> None:
        pass

    def addAll(self, c: typing.Collection[typing.Any]) -> bool:
        pass

    def add(self, e: typing.Any) -> bool:
        pass

    @staticmethod
    def FibonacciHeap1() -> FibonacciHeap[typing.Any]:
        pass

    def __init__(
        self, comparator: typing.Callable[[typing.Any, typing.Any], int]
    ) -> None:
        pass

    def __moveToRoot(self, node: FibonacciHeapNode[typing.Any]) -> None:
        pass

    def __link(
        self, y: FibonacciHeapNode[typing.Any], x: FibonacciHeapNode[typing.Any]
    ) -> None:
        pass

    def __cut(
        self, x: FibonacciHeapNode[typing.Any], y: FibonacciHeapNode[typing.Any]
    ) -> None:
        pass

    def __consolidate(self) -> None:
        pass

    def __compare(
        self, o1: FibonacciHeapNode[typing.Any], o2: FibonacciHeapNode[typing.Any]
    ) -> int:
        pass

    def __cascadingCut(self, y: FibonacciHeapNode[typing.Any]) -> None:
        pass

    # Class Methods End
