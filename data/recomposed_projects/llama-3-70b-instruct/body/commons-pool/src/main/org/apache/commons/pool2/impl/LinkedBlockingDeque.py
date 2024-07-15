from __future__ import annotations
import time
import re
import os
from abc import ABC
import io
import threading
import typing
from typing import *
import datetime
import pickle
from src.main.org.apache.commons.pool2.impl.InterruptibleReentrantLock import *
from src.main.org.apache.commons.pool2.impl.PoolImplUtils import *


class AbstractItr(ABC):

    __lastRet: Node[typing.Any] = None

    nextItem: typing.Any = None

    next: Node[typing.Any] = None

    def remove(self) -> None:
        n: Node[typing.Any] = self.__lastRet
        if n == None:
            raise RuntimeError()
        self.__lastRet = None
        self.__lock.lock()
        try:
            if n.item != None:
                self.__unlink(n)
        finally:
            self.__lock.unlock()

    def next(self) -> typing.Any:
        if self.next is None:
            raise RuntimeError()
        self.lastRet = self.next
        x = self.nextItem
        self.advance()
        return x

    def hasNext(self) -> bool:
        return self.next is not None

    def __succ(self, n: Node[typing.Any]) -> Node[typing.Any]:
        while True:
            s = self.nextNode(n)
            if s is None:
                return None
            if s.item is not None:
                return s
            if s == n:
                return self.firstNode()
            n = s

    def advance(self) -> None:
        self.lock.lock()
        try:
            self.next = self.__succ(self.next)
            self.nextItem = self.next.item if self.next is not None else None
        finally:
            self.lock.unlock()

    def __init__(self) -> None:

        pass  # LLM could not translate this method

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        return n.next

    def firstNode(self) -> Node[typing.Any]:
        return self.head


class DescendingItr(AbstractItr):

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        return n.prev

    def firstNode(self) -> Node[typing.Any]:
        return self.last


class Itr(AbstractItr):

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        return n.next

    def firstNode(self) -> Node[typing.Any]:
        return self.first


class Node:

    next: Node = None

    prev: Node = None

    item: typing.Any = None

    def __init__(self, x: typing.Any, p: Node, n: Node) -> None:
        self.item = x
        self.prev = p
        self.next = n


class LinkedBlockingDeque(Deque):

    __notFull: threading.Condition = None

    __notEmpty: threading.Condition = None

    __lock: InterruptibleReentrantLock = None

    __capacity: int = 0

    __count: int = 0

    __last: Node[typing.Any] = None

    __first: Node[typing.Any] = None

    __serialVersionUID: int = -387911632671998426

    def toString(self) -> str:
        self.__lock.lock()
        try:
            return super().toString()
        finally:
            self.__lock.unlock()

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:

        pass  # LLM could not translate this method

    def size(self) -> int:
        with self.__lock:
            return self.__count

    def removeLastOccurrence(self, o: typing.Any) -> bool:
        if o == None:
            return False
        self.__lock.lock()
        try:
            p: Node[typing.Any] = self.__last
            while p != None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.prev
            return False
        finally:
            self.__lock.unlock()

    def removeLast(self) -> typing.Any:
        x = self.pollLast0()
        if x == None:
            raise RuntimeError()
        return x

    def removeFirstOccurrence(self, o: typing.Any) -> bool:
        if o == None:
            return False
        self.__lock.lock()
        try:
            p: Node[typing.Any] = self.__first
            while p != None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.next
            return False
        finally:
            self.__lock.unlock()

    def removeFirst(self) -> typing.Any:
        x = self.pollFirst0()
        if x == None:
            raise RuntimeError()
        return x

    def push(self, e: typing.Any) -> None:
        self.addFirst(e)

    def pop(self) -> typing.Any:
        return self.removeFirst()

    def pollLast(self) -> typing.Any:
        return self.pollLast0()

    def pollFirst(self) -> typing.Any:
        return self.pollFirst0()

    def poll(self) -> typing.Any:
        return self.poll0()

    def peekLast(self) -> typing.Any:
        with self.__lock:
            return self.__last.item if self.__last is not None else None

    def peekFirst(self) -> typing.Any:
        self.__lock.lock()
        try:
            return self.__first.item if self.__first is not None else None
        finally:
            self.__lock.unlock()

    def peek(self) -> typing.Any:
        return self.peekFirst()

    def offerFirst(self, e: typing.Any) -> bool:
        return self.offerFirst0(e)

    def offer(self, e: typing.Any) -> bool:
        return self.offer0(e)

    def iterator(self) -> typing.Iterator[typing.Any]:
        return Itr()

    def getLast(self) -> typing.Any:
        with self.__lock:
            x = self.peekLast()
            if x is None:
                raise RuntimeError()
            return x

    def getFirst(self) -> typing.Any:
        self.__lock.lock()
        try:
            x = self.peekFirst()
            if x is None:
                raise RuntimeError()
            return x
        finally:
            self.__lock.unlock()

    def element(self) -> typing.Any:
        return self.getFirst()

    def descendingIterator(self) -> typing.Iterator[typing.Any]:
        return DescendingItr()

    def contains(self, o: typing.Any) -> bool:
        if o == None:
            return False
        self.__lock.lock()
        try:
            p = self.__first
            while p != None:
                if o == p.item:
                    return True
                p = p.next
            return False
        finally:
            self.__lock.unlock()

    def clear(self) -> None:
        self.__lock.lock()
        try:
            f = self.__first
            while f is not None:
                f.item = None
                n = f.next
                f.prev = None
                f.next = None
                f = n
            self.__first = self.__last = None
            self.__count = 0
            self.__notFull.notifyAll()
        finally:
            self.__lock.unlock()

    def addLast(self, e: typing.Any) -> None:
        if not self.offerLast0(e):
            raise RuntimeError("Deque full")

    def addFirst(self, e: typing.Any) -> None:
        if not self.offerFirst0(e):
            raise RuntimeError("Deque full")

    def add(self, e: typing.Any) -> bool:
        self.addLast(e)
        return True

    def toArray0(self) -> typing.List[typing.Any]:
        self.__lock.lock()
        try:
            a = [None] * self.__count
            k = 0
            p = self.__first
            while p is not None:
                a[k] = p.item
                k += 1
                p = p.next
            return a
        finally:
            self.__lock.unlock()

    def takeLast(self) -> typing.Any:

        pass  # LLM could not translate this method

    def takeFirst(self) -> typing.Any:

        pass  # LLM could not translate this method

    def take(self) -> typing.Any:
        return self.takeFirst()

    def remove1(self, o: typing.Any) -> bool:
        return self.removeFirstOccurrence(o)

    def remove0(self) -> typing.Any:
        return self.removeFirst()

    def remainingCapacity(self) -> int:
        self.__lock.lock()
        try:
            return self.__capacity - self.__count
        finally:
            self.__lock.unlock()

    def putLast(self, e: typing.Any) -> None:

        pass  # LLM could not translate this method

    def putFirst(self, e: typing.Any) -> None:

        pass  # LLM could not translate this method

    def put(self, e: typing.Any) -> None:
        self.putLast(e)

    def pollLast2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        return self.pollLast1(PoolImplUtils.toDuration(timeout, unit))

    def pollLast1(self, timeout: datetime.timedelta) -> typing.Any:
        nanos: int = timeout.total_seconds() * 1000000000
        self.__lock.lockInterruptibly()
        try:
            x: typing.Any = None
            while x == None:
                x = self.__unlinkLast()
                if nanos <= 0:
                    return None
                nanos = self.__notEmpty.awaitNanos(nanos)
            return x
        finally:
            self.__lock.unlock()

    def pollLast0(self) -> typing.Any:
        self.__lock.lock()
        try:
            return self.__unlinkLast()
        finally:
            self.__lock.unlock()

    def pollFirst2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        return self.pollFirst1(PoolImplUtils.toDuration(timeout, unit))

    def pollFirst0(self) -> typing.Any:
        self.__lock.lock()
        try:
            return self.__unlinkFirst()
        finally:
            self.__lock.unlock()

    def poll2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:
        return self.pollFirst2(timeout, unit)

    def poll0(self) -> typing.Any:
        return self.pollFirst0()

    def offerLast2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:
        return self.offerLast1(e, PoolImplUtils.toDuration(timeout, unit))

    def offerLast0(self, e: typing.Any) -> bool:
        Objects.requireNonNull(e, "e")
        self.__lock.lock()
        try:
            return self.__linkLast(e)
        finally:
            self.__lock.unlock()

    def offerLast(self, e: typing.Any) -> bool:
        return self.offerLast0(e)

    def offerFirst2(
        self, e: typing.Any, timeout: int, unit: datetime.timedelta
    ) -> bool:
        return self.offerFirst1(e, PoolImplUtils.toDuration(timeout, unit))

    def offerFirst1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        if e is None:
            raise ValueError("e")
        nanos = timeout.total_seconds() * 1000000000
        self.__lock.lockInterruptibly()
        try:
            while not self.__linkFirst(e):
                if nanos <= 0:
                    return False
                nanos = self.__notFull.awaitNanos(nanos)
            return True
        finally:
            self.__lock.unlock()

    def offerFirst0(self, e: typing.Any) -> bool:
        Objects.requireNonNull(e, "e")
        self.__lock.lock()
        try:
            return self.__linkFirst(e)
        finally:
            self.__lock.unlock()

    def offer2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:
        return self.offerLast2(e, timeout, unit)

    def offer0(self, e: typing.Any) -> bool:
        return self.offerLast0(e)

    def interuptTakeWaiters(self) -> None:
        self.__lock.lock()
        try:
            self.__lock.interruptWaiters(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def hasTakeWaiters(self) -> bool:
        self.__lock.lock()
        try:
            return self.__lock.hasWaiters(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def getTakeQueueLength(self) -> int:
        self.__lock.lock()
        try:
            return self.__lock.getWaitQueueLength(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def drainTo1(self, c: typing.Collection[typing.Any], maxElements: int) -> int:
        Objects.requireNonNull(c, "c")
        if c == self:
            raise ValueError()
        self.__lock.lock()
        try:
            n: int = min(maxElements, self.__count)
            for i in range(n):
                c.add(self.__first.item)  # In this order, in case add() throws.
                self.__unlinkFirst()
            return n
        finally:
            self.__lock.unlock()

    def drainTo0(self, c: typing.Collection[typing.Any]) -> int:
        return self.drainTo1(c, Integer.MAX_VALUE)

    def __init__(
        self,
        constructorId: int,
        capacity: int,
        fairness: bool,
        c: typing.Collection[typing.Any],
    ) -> None:
        if constructorId == 0:
            if capacity <= 0:
                raise ValueError()
            self.__capacity = capacity
            self.__lock = InterruptibleReentrantLock(fairness)
            self.__notEmpty = self.__lock.newCondition()
            self.__notFull = self.__lock.newCondition()

            if c is not None:
                self.__lock.lock()  # Never contended, but necessary for visibility
                try:
                    for e in c:
                        Objects.requireNonNull(e)
                        if not self.__linkLast(e):
                            raise RuntimeError("Deque full")
                finally:
                    self.__lock.unlock()
        else:
            self.__capacity = capacity
            self.__lock = InterruptibleReentrantLock(fairness)
            self.__notEmpty = self.__lock.newCondition()
            self.__notFull = self.__lock.newCondition()

    @staticmethod
    def LinkedBlockingDeque3(capacity: int) -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, capacity, False, None)

    @staticmethod
    def LinkedBlockingDeque2(
        c: typing.Collection[typing.Any],
    ) -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, Integer.MAX_VALUE, False, c)

    @staticmethod
    def LinkedBlockingDeque1(fairness: bool) -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, Integer.MAX_VALUE, fairness, None)

    @staticmethod
    def LinkedBlockingDeque0() -> LinkedBlockingDeque[typing.Any]:
        return LinkedBlockingDeque(0, Integer.MAX_VALUE, False, None)

    def __writeObject(self, s: pickle.Pickler) -> None:
        self.__lock.lock()
        try:
            s.defaultWriteObject()
            p = self.__first
            while p is not None:
                s.writeObject(p.item)
                p = p.next
            s.writeObject(None)
        finally:
            self.__lock.unlock()

    def __unlinkLast(self) -> typing.Any:
        l: Node[typing.Any] = self.__last
        if l == None:
            return None
        p: Node[typing.Any] = l.prev
        item: typing.Any = l.item
        l.item = None
        l.prev = l
        self.__last = p
        if p == None:
            self.__first = None
        else:
            p.next = None
        self.__count -= 1
        self.__notFull.signal()
        return item

    def __unlinkFirst(self) -> typing.Any:
        f: Node[typing.Any] = self.__first
        if f is None:
            return None
        n: Node[typing.Any] = f.next
        item: typing.Any = f.item
        f.item = None
        f.next = f  # help GC
        self.__first = n
        if n is None:
            self.__last = None
        else:
            n.prev = None
        self.__count -= 1
        self.__notFull.signal()
        return item

    def __unlink(self, x: Node[typing.Any]) -> None:
        p: Node[typing.Any] = x.prev
        n: Node[typing.Any] = x.next
        if p == None:
            self.__unlinkFirst()
        elif n == None:
            self.__unlinkLast()
        else:
            p.next = n
            n.prev = p
            x.item = None
            self.__count -= 1
            self.__notFull.signal()

    def __readObject(self, s: pickle.Unpickler) -> None:
        s.defaultReadObject()
        self.__count = 0
        self.__first = None
        self.__last = None
        while True:
            item = s.readObject()
            if item is None:
                break
            self.add(item)

    def __linkLast(self, e: typing.Any) -> bool:
        if self.__count >= self.__capacity:
            return False
        l = self.__last
        x = Node(e, l, None)
        self.__last = x
        if self.__first is None:
            self.__first = x
        else:
            l.next = x
        self.__count += 1
        self.__notEmpty.notify()
        return True

    def __linkFirst(self, e: typing.Any) -> bool:
        if self.__count >= self.__capacity:
            return False
        f = self.__first
        x = Node(e, None, f)
        self.__first = x
        if self.__last is None:
            self.__last = x
        else:
            f.prev = x
        self.__count += 1
        self.__notEmpty.notify()
        return True

    def pollFirst1(self, timeout: datetime.timedelta) -> typing.Any:
        nanos: int = timeout.total_seconds() * 1000000000
        self.__lock.lockInterruptibly()
        try:
            x: typing.Any
            while (x := self.__unlinkFirst()) is None:
                if nanos <= 0:
                    return None
                nanos = self.__notEmpty.awaitNanos(nanos)
            return x
        finally:
            self.__lock.unlock()

    def poll1(self, timeout: datetime.timedelta) -> typing.Any:
        return self.pollFirst1(timeout)

    def offerLast1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        if e is None:
            raise ValueError("e")
        nanos = timeout.total_seconds() * 1000000000
        self.__lock.lockInterruptibly()
        try:
            while not self.__linkLast(e):
                if nanos <= 0:
                    return False
                nanos = self.__notFull.awaitNanos(nanos)
            return True
        finally:
            self.__lock.unlock()

    def offer1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:
        return self.offerLast1(e, timeout)
