from __future__ import annotations
import math
from math import *
import re
import collections
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.graph.collections.FibonacciHeapNode import *
from src.main.org.apache.commons.graph.utils.Assertions import *


class FibonacciHeap:

    __minimumNode: FibonacciHeapNode[typing.Any] = None

    __markedNodes: int = 0
    __trees: int = 0
    __size: int = 0
    __comparator: typing.Callable[[typing.Any, typing.Any], int] = None

    __elementsIndex: Set[typing.Any] = set()
    __LOG_PHI: float = math.log((1 + math.sqrt(5)) / 2)

    def toString(self) -> str:

        if self.__minimumNode is None:
            return "FibonacciHeap=[]"

        stack = [self.__minimumNode]
        buf = io.StringIO("FibonacciHeap=[")

        while stack:
            curr = stack.pop()
            buf.write(str(curr))
            buf.write(", ")

            if curr.getChild() is not None:
                stack.append(curr.getChild())

            start = curr
            curr = curr.getRight()

            while curr != start:
                buf.write(str(curr))
                buf.write(", ")

                if curr.getChild() is not None:
                    stack.append(curr.getChild())

                curr = curr.getRight()

        buf.write("]")

        return buf.getvalue()

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:
        raise NotImplementedError()

    def toArray0(self) -> typing.List[typing.Any]:
        raise NotImplementedError("This method is not implemented yet.")

    def size(self) -> int:
        return self.__size

    def retainAll(self, c: typing.Collection[typing.Any]) -> bool:
        raise NotImplementedError("This method is not implemented yet.")

    def removeAll(self, c: typing.Collection[typing.Any]) -> bool:
        raise NotImplementedError("This method is not implemented yet.")

    def remove1(self, o: typing.Any) -> bool:
        raise NotImplementedError("This method is not implemented yet.")

    def remove0(self) -> typing.Any:

        if self.isEmpty():
            raise RuntimeError()

        return self.poll()

    def potential(self) -> int:
        return self.__trees + 2 * self.__markedNodes

    def poll(self) -> typing.Any:

        if self.isEmpty():
            return None

        z = self.__minimumNode
        numOfKids = z.getDegree()

        x = z.getChild()
        tempRight = None

        while numOfKids > 0:
            tempRight = x.getRight()

            self.__moveToRoot(x)

            x.setParent(None)

            x = tempRight
            numOfKids -= 1

        z.getLeft().setRight(z.getRight())
        z.getRight().setLeft(z.getLeft())

        if z == z.getRight():
            self.__minimumNode = None
        else:
            self.__minimumNode = z.getRight()
            self.__consolidate()

        self.__size -= 1

        minimum = z.getElement()
        self.__elementsIndex.remove(minimum)
        return minimum

    def peek(self) -> typing.Any:
        if self.isEmpty():
            return None

        return self.__minimumNode.getElement()

    def offer(self, e: typing.Any) -> bool:
        return self.add(e)

    def iterator(self) -> typing.Iterator[typing.Any]:
        raise NotImplementedError()

    def isEmpty(self) -> bool:
        return self.__minimumNode is None

    def element(self) -> typing.Any:
        if self.isEmpty():
            raise RuntimeError()
        return self.peek()

    def containsAll(self, c: typing.Collection[typing.Any]) -> bool:

        if c is None:
            return False

        for o in c:
            if not self.contains(o):
                return False

        return True

    def contains(self, o: typing.Any) -> bool:

        if o is None:
            return False

        return o in self.__elementsIndex

    def clear(self) -> None:
        self.__minimumNode = None
        self.__size = 0
        self.__trees = 0
        self.__markedNodes = 0
        self.__elementsIndex.clear()

    def addAll(self, c: typing.Collection[typing.Any]) -> bool:

        for element in c:
            self.add(element)

        return True

    def add(self, e: typing.Any) -> bool:

        Assertions.checkNotNull(
            e, "Null elements not allowed in this FibonacciHeap implementation."
        )

        node = FibonacciHeapNode(e)

        self.__moveToRoot(node)

        self.__size += 1

        self.__elementsIndex.add(e)

        return True

    @staticmethod
    def FibonacciHeap1() -> FibonacciHeap[typing.Any]:
        return FibonacciHeap(None)

    def __init__(
        self, comparator: typing.Callable[[typing.Any, typing.Any], int]
    ) -> None:
        self.__comparator = comparator

    def __moveToRoot(self, node: FibonacciHeapNode[typing.Any]) -> None:

        if self.isEmpty():
            self.__minimumNode = node
        else:
            node.getLeft().setRight(node.getRight())
            node.getRight().setLeft(node.getLeft())

            node.setLeft(self.__minimumNode)
            node.setRight(self.__minimumNode.getRight())
            self.__minimumNode.setRight(node)
            node.getRight().setLeft(node)

            if self.__compare(node, self.__minimumNode) < 0:
                self.__minimumNode = node

    def __link(
        self, y: FibonacciHeapNode[typing.Any], x: FibonacciHeapNode[typing.Any]
    ) -> None:

        y.getLeft().setRight(y.getRight())
        y.getRight().setLeft(y.getLeft())

        y.setParent(x)

        if x.getChild() == None:
            x.setChild(y)
            y.setRight(y)
            y.setLeft(y)
        else:
            y.setLeft(x.getChild())
            y.setRight(x.getChild().getRight())
            x.getChild().setRight(y)
            y.getRight().setLeft(y)

        x.incraeseDegree()

        y.setMarked(False)
        self.__markedNodes += 1

    def __cut(
        self, x: FibonacciHeapNode[typing.Any], y: FibonacciHeapNode[typing.Any]
    ) -> None:

        self.__moveToRoot(x)

        y.decraeseDegree()
        x.setParent(None)

        x.setMarked(False)
        self.__markedNodes -= 1

    def __consolidate(self) -> None:

        if self.isEmpty():
            return

        array_size = math.floor(math.log(self.__size) / self.__LOG_PHI)

        node_sequence = [None] * array_size

        num_roots = 0

        x = self.__minimumNode

        if x is not None:
            num_roots += 1
            x = x.getRight()

            while x != self.__minimumNode:
                num_roots += 1
                x = x.getRight()

        while num_roots > 0:
            degree = x.getDegree()
            next_node = x.getRight()

            while node_sequence[degree] is not None:
                y = node_sequence[degree]

                if self.__compare(x, y) > 0:
                    pointer = y
                    y = x
                    x = pointer

                self.__link(y, x)

                node_sequence[degree] = None

                degree += 1

            node_sequence[degree] = x

            x = next_node
            num_roots -= 1

        self.__minimumNode = None

        for pointer in node_sequence:
            if pointer is None:
                continue
            if self.__minimumNode is None:
                self.__minimumNode = pointer

            if self.__minimumNode is not None:
                self.__moveToRoot(pointer)

    def __compare(
        self, o1: FibonacciHeapNode[typing.Any], o2: FibonacciHeapNode[typing.Any]
    ) -> int:

        if self.__comparator is not None:
            return self.__comparator(o1.getElement(), o2.getElement())

        o1Comparable = typing.cast(Comparable[typing.Any], o1.getElement())
        return o1Comparable.compareTo(o2.getElement())

    def __cascadingCut(self, y: FibonacciHeapNode[typing.Any]) -> None:

        z = y.getParent()

        if z is not None:
            if not y.isMarked():
                y.setMarked(True)
                self.__markedNodes += 1
            else:
                self.__cut(y, z)
                self.__cascadingCut(z)
