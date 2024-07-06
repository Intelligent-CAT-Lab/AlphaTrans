from __future__ import annotations
import time
import re
import sys
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

        n = self.__lastRet
        if n is None:
            raise RuntimeError()
        self.__lastRet = None
        self.__lock.lock()
        try:
            if n.item is not None:
                self.__unlink(n)
        finally:
            self.__lock.unlock()

    def next(self) -> typing.Any:
        if self.next is None:
            raise StopIteration
        self.__lastRet = self.next
        x = self.nextItem
        self.advance()
        return x

    def hasNext(self) -> bool:
        return self.next() is not None

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
        with self.lock:
            try:
                self.next = self.__succ(self.next)
                self.nextItem = self.next.item if self.next is not None else None
            finally:
                self.lock.unlock()

    def __init__(self) -> None:
        self.lock = InterruptibleReentrantLock()
        with self.lock:
            self.next = self.firstNode()
            self.nextItem = self.next.item if self.next is not None else None

    def nextNode(self, n: Node[typing.Any]) -> Node[typing.Any]:
        pass

    def firstNode(self) -> Node[typing.Any]:
        pass


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
        with self.__lock:
            return super().__str__()

    def toArray1(self, a: typing.List[typing.Any]) -> typing.List[typing.Any]:

        with self.__lock:
            if len(a) < self.__count:
                a = [None] * self.__count
            k = 0
            p = self.__first
            while p is not None:
                a[k] = p.item
                k += 1
                p = p.next
            if len(a) > k:
                a[k] = None
            return a

    def size(self) -> int:
        with self.__lock:
            return self.__count

    def removeLastOccurrence(self, o: typing.Any) -> bool:

        if o is None:
            return False

        self.__lock.lock()

        try:
            p = self.__last

            while p is not None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.prev

            return False

        finally:
            self.__lock.unlock()

    def removeLast(self) -> typing.Any:

        x = self.pollLast0()
        if x is None:
            raise IndexError("deque is empty")
        return x

    def removeFirstOccurrence(self, o: typing.Any) -> bool:

        if o is None:
            return False

        self.__lock.lock()

        try:
            p = self.__first

            while p is not None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.next

            return False

        finally:
            self.__lock.unlock()

    def removeFirst(self) -> typing.Any:

        x = self.pollFirst0()
        if x is None:
            raise RuntimeError()
        return x

    def push(self, e: typing.Any) -> None:

        if not self.offerFirst0(e):
            raise RuntimeError("Deque full")

    def pop(self) -> typing.Any:

        x = self.removeFirst()
        if x is None:
            raise IndexError("pop from empty list")
        return x

    def pollLast(self) -> typing.Any:

        self.__lock.acquire()
        try:
            return self.__unlinkLast()
        finally:
            self.__lock.release()

    def pollFirst(self) -> typing.Any:

        self.__lock.acquire()
        try:
            return self.__unlinkFirst()
        finally:
            self.__lock.release()

    def poll(self) -> typing.Any:

        self.__lock.acquire()
        try:
            return self.__unlinkFirst()
        finally:
            self.__lock.release()

    def peekLast(self) -> typing.Any:

        with self.__lock:
            return self.__last.item if self.__last is not None else None

    def peekFirst(self) -> typing.Any:

        with self.__lock:
            return self.__first.item if self.__first is not None else None

    def peek(self) -> typing.Any:

        with self.__lock:
            return self.__first.item if self.__first is not None else None

    def offerFirst(self, e: typing.Any) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            return self.__linkFirst(e)

    def offer(self, e: typing.Any) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            return self.offerLast0(e)

    def iterator(self) -> typing.Iterator[typing.Any]:
        return Itr(self)

    def getLast(self) -> typing.Any:

        with self.__lock:
            if self.__last is None:
                raise RuntimeError()
            return self.__last.item

    def getFirst(self) -> typing.Any:

        with self.__lock:
            if self.__first is None:
                raise RuntimeError()
            return self.__first.item

    def element(self) -> typing.Any:

        with self.__lock:
            if self.__first is None:
                raise RuntimeError()
            return self.__first.item

    def descendingIterator(self) -> typing.Iterator[typing.Any]:
        return DescendingItr(self)

    def contains(self, o: typing.Any) -> bool:

        if o is None:
            return False

        with self.__lock:
            p = self.__first
            while p is not None:
                if o == p.item:
                    return True
                p = p.next
            return False

    def clear(self) -> None:

        self.__lock.acquire()
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
            self.__notFull.notify_all()
        finally:
            self.__lock.release()

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

        self.__lock.acquire()
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
            self.__lock.release()

    def takeLast(self) -> typing.Any:

        self.__lock.acquire()
        try:
            x = None
            while (x := self.__unlinkLast()) is None:
                self.__notEmpty.wait()
            return x
        finally:
            self.__lock.release()

    def takeFirst(self) -> typing.Any:

        self.__lock.acquire()
        try:
            x = None
            while (x := self.__unlinkFirst()) is None:
                self.__notEmpty.wait()
            return x
        finally:
            self.__lock.release()

    def take(self) -> typing.Any:

        self.__lock.acquire()
        try:
            x = None
            while (x := self.__unlinkFirst()) is None:
                self.__notEmpty.wait()
            return x
        finally:
            self.__lock.release()

    def remove1(self, o: typing.Any) -> bool:

        if o is None:
            return False

        self.__lock.lock()

        try:
            p = self.__first

            while p is not None:
                if o == p.item:
                    self.__unlink(p)
                    return True
                p = p.next

            return False

        finally:
            self.__lock.unlock()

    def remove0(self) -> typing.Any:

        x = self.removeFirst()
        if x is None:
            raise RuntimeError()
        return x

    def remainingCapacity(self) -> int:
        with self.__lock:
            return self.__capacity - self.__count

    def putLast(self, e: typing.Any) -> None:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            while not self.__linkLast(e):
                self.__notFull.wait()

    def putFirst(self, e: typing.Any) -> None:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            while not self.__linkFirst(e):
                self.__notFull.wait()

    def put(self, e: typing.Any) -> None:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            while not self.__linkLast(e):
                self.__notFull.wait()

    def pollLast2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:

        duration = PoolImplUtils.toDuration(timeout, unit)
        return self.pollLast1(duration)

    def pollLast1(self, timeout: datetime.timedelta) -> typing.Any:

        nanos = timeout.total_seconds() * 1e9
        self.__lock.acquire()
        try:
            x = None
            while (x := self.__unlinkLast()) is None:
                if nanos <= 0:
                    return None
                nanos = self.__notEmpty.wait(nanos)
            return x
        finally:
            self.__lock.release()

    def pollLast0(self) -> typing.Any:

        self.__lock.lock()
        try:
            return self.__unlinkLast()
        finally:
            self.__lock.unlock()

    def pollFirst2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:

        duration = PoolImplUtils.toDuration(timeout, unit)
        return self.pollFirst1(duration)

    def pollFirst0(self) -> typing.Any:

        self.__lock.lock()
        try:
            return self.__unlinkFirst()
        finally:
            self.__lock.unlock()

    def poll2(self, timeout: int, unit: datetime.timedelta) -> typing.Any:

        duration = PoolImplUtils.toDuration(timeout, unit)
        return self.pollFirst1(duration)

    def poll0(self) -> typing.Any:

        self.__lock.acquire()
        try:
            return self.__unlinkFirst()
        finally:
            self.__lock.release()

    def offerLast2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        duration = PoolImplUtils.toDuration(timeout, unit)
        return self.offerLast1(e, duration)

    def offerLast0(self, e: typing.Any) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            return self.__linkLast(e)

    def offerLast(self, e: typing.Any) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            return self.__linkLast(e)

    def offerFirst2(
        self, e: typing.Any, timeout: int, unit: datetime.timedelta
    ) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        duration = PoolImplUtils.toDuration(timeout, unit)
        return self.offerFirst1(e, duration)

    def offerFirst1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        nanos = timeout.total_seconds() * 1e9
        self.__lock.acquire()
        try:
            while not self.__linkFirst(e):
                if nanos <= 0:
                    return False
                nanos = self.__notFull.wait(nanos / 1e9)
        finally:
            self.__lock.release()

        return True

    def offerFirst0(self, e: typing.Any) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            return self.__linkFirst(e)

    def offer2(self, e: typing.Any, timeout: int, unit: datetime.timedelta) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        duration = PoolImplUtils.toDuration(timeout, unit)
        return self.offerLast2(e, duration)

    def offer0(self, e: typing.Any) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        with self.__lock:
            return self.offerLast0(e)

    def interuptTakeWaiters(self) -> None:

        self.__lock.lock()
        try:
            self.__lock.interruptWaiters(self.__notEmpty)
        finally:
            self.__lock.unlock()

    def hasTakeWaiters(self) -> bool:
        with self.__lock:
            return self.__lock.has_waiters(self.__notEmpty)

    def getTakeQueueLength(self) -> int:
        with self.__lock:
            return self.__lock.getWaitQueueLength(self.__notEmpty)

    def drainTo1(self, c: typing.Collection[typing.Any], maxElements: int) -> int:

        if c is self:
            raise ValueError()

        self.__lock.acquire()
        try:
            n = min(maxElements, self.__count)
            for i in range(n):
                c.add(self.__first.item)
                self.__unlinkFirst()
            return n
        finally:
            self.__lock.release()

    def drainTo0(self, c: typing.Collection[typing.Any]) -> int:

        if c is self:
            raise ValueError()

        self.__lock.acquire()
        try:
            n = self.__count
            for i in range(n):
                c.add(self.__first.item)
                self.__unlinkFirst()
            return n
        finally:
            self.__lock.release()

    def __init__(
        self,
        constructorId: int,
        capacity: int,
        fairness: bool,
        c: typing.Collection[typing.Any],
    ) -> None:

        if constructorId == 0:
            if capacity <= 0:
                raise ValueError("Illegal Capacity: " + str(capacity))
            self.__capacity = capacity
            self.__lock = InterruptibleReentrantLock(fairness)
            self.__notEmpty = self.__lock.newCondition()
            self.__notFull = self.__lock.newCondition()

            if c is not None:
                self.__lock.acquire()
                try:
                    for e in c:
                        if e is None:
                            raise ValueError("Null element")
                        if not self.__linkLast(e):
                            raise ValueError("Deque full")
                finally:
                    self.__lock.release()
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
        return LinkedBlockingDeque(0, sys.maxsize, False, c)

    @staticmethod
    def LinkedBlockingDeque1(fairness: bool) -> LinkedBlockingDeque[typing.Any]:

        return LinkedBlockingDeque(0, sys.maxsize, fairness, None)

    @staticmethod
    def LinkedBlockingDeque0() -> LinkedBlockingDeque[typing.Any]:

        return LinkedBlockingDeque(0, sys.maxsize, False, None)

    def __writeObject(self, s: pickle.Pickler) -> None:

        with self.__lock:
            s.save(self)
            p = self.__first
            while p is not None:
                s.save(p.item)
                p = p.next
            s.save(None)

    def __unlinkLast(self) -> typing.Any:

        l = self.__last
        if l is None:
            return None
        p = l.prev
        item = l.item
        l.item = None
        l.prev = l  # help GC
        self.__last = p
        if p is None:
            self.__first = None
        else:
            p.next = None
        self.__count -= 1
        self.__notFull.notify()
        return item

    def __unlinkFirst(self) -> typing.Any:

        f = self.__first
        if f is None:
            return None
        n = f.next
        item = f.item
        f.item = None
        f.next = f
        self.__first = n
        if n is None:
            self.__last = None
        else:
            n.prev = None
        self.__count -= 1
        self.__notFull.notify()
        return item

    def __unlink(self, x: Node[typing.Any]) -> None:

        p = x.prev
        n = x.next
        if p is None:
            self.__unlinkFirst()
        elif n is None:
            self.__unlinkLast()
        else:
            p.next = n
            n.prev = p
            x.item = None
            self.__count -= 1
            self.__notFull.notify()

    def __readObject(self, s: pickle.Unpickler) -> None:

        s.restore_state()
        self.__count = 0
        self.__first = None
        self.__last = None
        while True:
            try:
                item = s.load()
                if item is None:
                    break
                self.add(item)
            except EOFError:
                break

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

        nanos = timeout.total_seconds() * 1e9
        self.__lock.lockInterruptibly()
        try:
            x = None
            while (x := self.__unlinkFirst()) is None:
                if nanos <= 0:
                    return None
                nanos = self.__notEmpty.wait(nanos)
            return x
        finally:
            self.__lock.unlock()

    def poll1(self, timeout: datetime.timedelta) -> typing.Any:

        return self.pollFirst1(timeout)

    def offerLast1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        nanos = timeout.total_seconds() * 1e9
        self.__lock.acquire()
        try:
            while not self.__linkLast(e):
                if nanos <= 0:
                    return False
                nanos = self.__notFull.wait(nanos / 1e9)
        finally:
            self.__lock.release()

        return True

    def offer1(self, e: typing.Any, timeout: datetime.timedelta) -> bool:

        if e is None:
            raise ValueError("e cannot be None")

        nanos = timeout.total_seconds() * 1e9
        self.__lock.acquire()
        try:
            while not self.__linkLast(e):
                if nanos <= 0:
                    return False
                nanos = self.__notFull.wait(nanos / 1e9)
        finally:
            self.__lock.release()

        return True
