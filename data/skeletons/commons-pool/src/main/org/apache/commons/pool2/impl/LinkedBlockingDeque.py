from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *
from src.main.org.apache.commons.pool2.impl.InterruptibleReentrantLock import *
import pickle
import datetime
import typing
from typing import *
import threading
import io
from abc import ABC

# Imports End


class AbstractItr(ABC):

    # Class Fields Begin
    next: Node[typing.Any] = None
    nextItem: typing.Any = None
    __lastRet: Node[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def remove(self) -> None:
        pass

    def next_(self) -> typing.Any:
        pass

    def hasNext(self) -> bool:
        pass

    def __succ(self, n: Node[typing.Any]) -> Node[typing.Any]:
        pass

    def advance(self) -> None:
        pass

    def __init__(self) -> None:
        pass

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        pass

    def firstNode(self) -> Node[typing.Any]:
        pass

    # Class Methods End


class DescendingItr(AbstractItr):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        pass

    def firstNode(self) -> Node[typing.Any]:
        pass

    # Class Methods End


class Itr(AbstractItr):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        pass

    def firstNode(self) -> Node[typing.Any]:
        pass

    # Class Methods End


class Node:

    # Class Fields Begin
    item: typing.Any = None
    prev: Node = None
    next: Node = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, x: typing.Any, p: Node, n: Node) -> None:
        pass

    # Class Methods End


class LinkedBlockingDeque(Deque):

    # Class Fields Begin
    __serialVersionUID: int = None
    __first: Node[typing.Any] = None
    __last: Node[typing.Any] = None
    __count: int = None
    __capacity: int = None
    __lock: InterruptibleReentrantLock = None
    __notEmpty: threading.Condition = None
    __notFull: threading.Condition = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:
        pass

    def size(self) -> int:
        pass

    def removeLastOccurrence(self, o: typing.Any) -> bool:
        pass

    def removeLast(self) -> typing.Any:
        pass

    def removeFirstOccurrence(self, o: typing.Any) -> bool:
        pass

    def removeFirst(self) -> typing.Any:
        pass

    def push(self, e: typing.Any) -> None:
        pass

    def pop(self) -> typing.Any:
        pass

    def pollLast(self) -> typing.Any:
        pass

    def pollFirst(self) -> typing.Any:
        pass

    def poll(self) -> typing.Any:
        pass

    def peekLast(self) -> typing.Any:
        pass

    def peekFirst(self) -> typing.Any:
        pass

    def peek(self) -> typing.Any:
        pass

    def offerFirst(self, e: typing.Any) -> bool:
        pass

    def offer(self, e: typing.Any) -> bool:
        pass

    def iterator(self) -> typing.Iterator[typing.Any]:
        pass

    def getLast(self) -> typing.Any:
        pass

    def getFirst(self) -> typing.Any:
        pass

    def element(self) -> typing.Any:
        pass

    def descendingIterator(self) -> typing.Iterator[typing.Any]:
        pass

    def contains(self, o: typing.Any) -> bool:
        pass

    def clear(self) -> None:
        pass

    def addLast(self, e: typing.Any) -> None:
        pass

    def addFirst(self, e: typing.Any) -> None:
        pass

    def add(self, e: typing.Any) -> bool:
        pass

    def toArray0(self) -> typing.List[typing.Any]:
        pass

    def takeLast(self) -> typing.Any:
        pass

    def takeFirst(self) -> typing.Any:
        pass

    def take(self) -> typing.Any:
        pass

    def remove1(self, o: typing.Any) -> bool:
        pass

    def remove0(self) -> typing.Any:
        pass

    def remainingCapacity(self) -> int:
        pass

    def putLast(self, e: typing.Any) -> None:
        pass

    def putFirst(self, e: typing.Any) -> None:
        pass

    def put(self, e: typing.Any) -> None:
        pass

    def pollLast2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        pass

    def pollLast1(self, timeout: datetime.timedelta) -> typing.Any:
        pass

    def pollLast0(self) -> typing.Any:
        pass

    def pollFirst2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        pass

    def pollFirst0(self) -> typing.Any:
        pass

    def poll2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        pass

    def poll0(self) -> typing.Any:
        pass

    def offerLast2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:
        pass

    def offerLast0(self, e: typing.Any) -> bool:
        pass

    def offerLast(self, e: typing.Any) -> bool:
        pass

    def offerFirst2(
        self, e: typing.Any, timeout: int, unit: datetime.timedelta
    ) -> bool:
        pass

    def offerFirst1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        pass

    def offerFirst0(self, e: typing.Any) -> bool:
        pass

    def offer2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:
        pass

    def offer0(self, e: typing.Any) -> bool:
        pass

    def interuptTakeWaiters(self) -> None:
        pass

    def hasTakeWaiters(self) -> bool:
        pass

    def getTakeQueueLength(self) -> int:
        pass

    def drainTo1(self, c: typing.Collection[typing.Any], maxElements: int) -> int:
        pass

    def drainTo0(self, c: typing.Collection[typing.Any]) -> int:
        pass

    def __init__(
        self,
        constructorId: int,
        capacity: int,
        fairness: bool,
        c: typing.Collection[typing.Any],
    ) -> None:
        pass

    @staticmethod
    def LinkedBlockingDeque3(capacity: int) -> LinkedBlockingDeque[typing.Any]:
        pass

    @staticmethod
    def LinkedBlockingDeque2(
        c: typing.Collection[typing.Any],
    ) -> LinkedBlockingDeque[typing.Any]:
        pass

    @staticmethod
    def LinkedBlockingDeque1(fairness: bool) -> LinkedBlockingDeque[typing.Any]:
        pass

    @staticmethod
    def LinkedBlockingDeque0() -> LinkedBlockingDeque[typing.Any]:
        pass

    def __writeObject(self, s: pickle.Pickler) -> None:
        pass

    def __unlinkLast(self) -> typing.Any:
        pass

    def __unlinkFirst(self) -> typing.Any:
        pass

    def __unlink(self, x: Node[typing.Any]) -> None:
        pass

    def __readObject(self, s: pickle.Unpickler) -> None:
        pass

    def __linkLast(self, e: typing.Any) -> bool:
        pass

    def __linkFirst(self, e: typing.Any) -> bool:
        pass

    def pollFirst1(self, timeout: datetime.timedelta) -> typing.Any:
        pass

    def poll1(self, timeout: datetime.timedelta) -> typing.Any:
        pass

    def offerLast1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        pass

    def offer1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        pass

    # Class Methods End
