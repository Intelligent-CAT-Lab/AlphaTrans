from __future__ import annotations
import io
import typing
from typing import *
import datetime
import os
from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *


class TestLinkedBlockingDeque:

    __THREE: int = 3

    __TWO: int = Integer.valueOf(2)

    __ONE: int = 1

    __TIMEOUT_50_MILLIS: datetime.timedelta = datetime.timedelta(milliseconds=50)

    def testToArray(self) -> None:

        deque = LinkedBlockingDeque()
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        arr = deque.toArray()
        assert arr[0] == Integer.valueOf(1)
        assert arr[1] == Integer.valueOf(2)

        arr = deque.toArray(Integer[0])
        assert arr[0] == Integer.valueOf(1)
        assert arr[1] == Integer.valueOf(2)

        arr = deque.toArray(Integer[0])
        assert arr[0] == Integer.valueOf(1)
        assert arr[1] == Integer.valueOf(2)

    def testTakeLast(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        assert self.deque.takeLast() == Integer.valueOf(1)

    def testTakeFirst(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        assert self.deque.takeFirst() == Integer.valueOf(2)

    def testTake(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        assert self.deque.take() == Integer.valueOf(2)

    def testRemoveLastOccurrence(self) -> None:

        deque = LinkedBlockingDeque()

        assert not deque.removeLastOccurrence(None)
        assert not deque.removeLastOccurrence(self.__ONE)

        deque.add(self.__ONE)
        deque.add(self.__ONE)

        assert deque.removeLastOccurrence(self.__ONE)
        assert deque.size() == 1

    def testRemoveLast(self) -> None:

        with self.assertRaises(NoSuchElementException):
            self.deque.removeLast()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        self.assertEqual(Integer.valueOf(2), self.deque.removeLast())

        with self.assertRaises(NoSuchElementException):
            self.deque.removeLast()
            self.deque.removeLast()

    def testRemoveFirst(self) -> None:

        # assertThrows(NoSuchElementException.class, deque::removeFirst);
        try:
            self.deque.removeFirst()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.removeFirst());
        assert self.deque.removeFirst() == Integer.valueOf(1)

        # assertThrows(
        #         NoSuchElementException.class,
        #         () -> {
        #             deque.removeFirst();
        #             deque.removeFirst();
        #         });
        try:
            self.deque.removeFirst()
            self.deque.removeFirst()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

    def testRemove(self) -> None:

        # assertThrows(NoSuchElementException.class, deque::remove);
        try:
            self.deque.remove()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.remove());
        assert self.deque.remove() == Integer.valueOf(1)

    def testPutLast(self) -> None:

        # assertThrows(NullPointerException.class, () -> deque.putLast(null));
        try:
            self.deque.putLast(None)
            assert False, "Expected NullPointerException"
        except NullPointerException:
            pass

        # deque.putLast(ONE);
        # deque.putLast(TWO);
        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)

        # assertEquals(2, deque.size());
        assert self.deque.size() == 2, "Expected size 2"

        # assertEquals(Integer.valueOf(1), deque.pop());
        assert self.deque.pop() == Integer.valueOf(1), "Expected popped value to be 1"

    def testPutFirst(self) -> None:

        with self.assertRaises(NullPointerException):
            self.deque.putFirst(None)

        self.deque.putFirst(self.__ONE)
        self.deque.putFirst(self.__TWO)

        self.assertEqual(2, self.deque.size())
        self.assertEqual(Integer.valueOf(2), self.deque.pop())

    def testPut(self) -> None:

        try:
            self.deque.put(None)
            assert False, "Expected NullPointerException"
        except NullPointerException:
            pass

        self.deque.put(self.__ONE)
        self.deque.put(self.__TWO)

    def testPush(self) -> None:

        deque = LinkedBlockingDeque()
        deque.push(self.__ONE)
        deque.push(self.__TWO)
        assert deque.size() == 2
        try:
            deque.push(self.__THREE)
            assert False
        except IllegalStateException:
            assert True
        assert deque.pop() == Integer.valueOf(2)

    def testPossibleBug(self) -> None:

        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            deque.add(i)

        iter = deque.__iter__()
        next(iter)

        deque.remove(1)
        deque.remove(0)
        deque.remove(2)

        next(iter)

    def testPop(self) -> None:

        deque = LinkedBlockingDeque()

        try:
            deque.pop()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        deque.add(self.__ONE)
        deque.add(self.__TWO)

        assert deque.pop() == Integer.valueOf(1)

        try:
            deque.pop()
            deque.pop()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

    def testPollWithTimeout(self) -> None:

        assert self.deque.poll1(self.__TIMEOUT_50_MILLIS) is None
        assert self.deque.poll1(self.__TIMEOUT_50_MILLIS) is None

    def testPollLastWithTimeout(self) -> None:

        assert self.deque.pollLast() is None
        assert self.deque.pollLast(self.__TIMEOUT_50_MILLIS) is None

    def testPollLast(self) -> None:

        deque = LinkedBlockingDeque()

        assert deque.pollLast() is None
        assert deque.offerFirst(self.__ONE)
        assert deque.offerFirst(self.__TWO)
        assert deque.pollLast() == 1

    def testPollFirstWithTimeout(self) -> None:

        assert self.deque.pollFirst() is None
        assert self.deque.pollFirst(self.__TIMEOUT_50_MILLIS) is None

    def testPollFirst(self) -> None:

        deque = LinkedBlockingDeque()

        assert deque.pollFirst() is None
        assert deque.offerFirst(self.__ONE)
        assert deque.offerFirst(self.__TWO)
        assert deque.pollFirst() == 2

    def testPeekLast(self) -> None:

        deque = LinkedBlockingDeque()
        assert deque.peekLast() is None
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        assert deque.peekLast() == 2

    def testPeekFirst(self) -> None:

        deque = LinkedBlockingDeque()
        assert deque.peekFirst() is None
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        assert deque.peekFirst() == 1

    def testPeek(self) -> None:

        deque = LinkedBlockingDeque()
        assert deque.peek() is None
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        assert deque.peek() == 1

    def testOfferWithTimeout(self) -> None:

        assert self.deque.offer1(self.__ONE, self.__TIMEOUT_50_MILLIS)
        assert self.deque.offer1(self.__TWO, self.__TIMEOUT_50_MILLIS)
        assert not self.deque.offer1(self.__THREE, self.__TIMEOUT_50_MILLIS)

        try:
            self.deque.offer1(None, self.__TIMEOUT_50_MILLIS)
            assert False
        except NullPointerException:
            assert True

    def testOfferLastWithTimeout(self) -> None:

        with self.assertRaises(NullPointerException):
            self.deque.offerLast1(None, self.__TIMEOUT_50_MILLIS)

        assert self.deque.offerLast1(self.__ONE, self.__TIMEOUT_50_MILLIS)
        assert self.deque.offerLast1(self.__TWO, self.__TIMEOUT_50_MILLIS)
        assert not self.deque.offerLast1(self.__THREE, self.__TIMEOUT_50_MILLIS)

    def testOfferLast(self) -> None:

        deque = LinkedBlockingDeque()
        deque.offerLast(self.__ONE)
        deque.offerLast(self.__TWO)
        assert deque.size() == 2
        try:
            deque.offerLast(None)
            assert False, "Expected NullPointerException"
        except NullPointerException:
            pass
        assert deque.pop() == Integer.valueOf(1)

    def testOfferFirstWithTimeout(self) -> None:

        with self.assertRaises(NullPointerException):
            self.deque.offerFirst1(None, self.__TIMEOUT_50_MILLIS)

        assert self.deque.offerFirst1(self.__ONE, self.__TIMEOUT_50_MILLIS)
        assert self.deque.offerFirst1(self.__TWO, self.__TIMEOUT_50_MILLIS)
        assert not self.deque.offerFirst1(self.__THREE, self.__TIMEOUT_50_MILLIS)

    def testOfferFirst(self) -> None:

        deque = LinkedBlockingDeque()
        deque.offerFirst(self.__ONE)
        deque.offerFirst(self.__TWO)
        assert deque.size() == 2
        try:
            deque.offerFirst(None)
            assert False
        except NullPointerException:
            assert True
        assert deque.pop() == Integer.valueOf(2)

    def testOffer(self) -> None:

        deque = LinkedBlockingDeque()

        assert deque.offer(self.__ONE)
        assert deque.offer(self.__TWO)
        assert not deque.offer(self.__THREE)

        try:
            deque.offer(None)
            assert False, "Expected NullPointerException"
        except NullPointerException:
            pass

    def testIterator(self) -> None:

        deque = LinkedBlockingDeque()

        try:
            deque.iterator().next()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        deque.add(self.__ONE)
        deque.add(self.__TWO)
        iter = deque.iterator()
        assert Integer.valueOf(1) == iter.next()
        iter.remove()
        assert Integer.valueOf(2) == iter.next()

    def testGetLast(self) -> None:

        # assertThrows(NoSuchElementException.class, () -> deque.getLast());
        try:
            self.deque.getLast()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(2), deque.getLast());
        assert self.deque.getLast() == Integer.valueOf(2), "Expected 2"

    def testGetFirst(self) -> None:

        # assertThrows(NoSuchElementException.class, () -> deque.getFirst());
        try:
            self.deque.getFirst()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.getFirst());
        assert self.deque.getFirst() == Integer.valueOf(1), "Expected 1"

    def testElement(self) -> None:

        # assertThrows(NoSuchElementException.class, () -> deque.element());
        try:
            self.deque.element()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.element());
        assert self.deque.element() == Integer.valueOf(1), "Expected element to be 1"

    def testDrainTo(self) -> None:

        c: Collection[int] = []
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        assert 2 == deque.drainTo0(c)
        assert 2 == len(c)

        c = []
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        assert 1 == deque.drainTo1(c, 1)
        assert 1 == len(deque)
        assert 1 == len(c)
        assert Integer.valueOf(1) == next(iter(c))

    def testDescendingIterator(self) -> None:

        deque = LinkedBlockingDeque()

        try:
            deque.descendingIterator().next()
            assert False, "Expected NoSuchElementException"
        except NoSuchElementException:
            pass

        deque.add(self.__ONE)
        deque.add(self.__TWO)
        iter = deque.descendingIterator()
        assert iter.next() == 2, "Expected 2"
        iter.remove()
        assert iter.next() == 1, "Expected 1"

    def testContains(self) -> None:

        self.deque.add(self.__ONE)
        assert self.__ONE in self.deque
        assert self.__TWO not in self.deque
        assert None not in self.deque
        self.deque.add(self.__TWO)
        assert self.__TWO in self.deque
        assert self.__THREE not in self.deque

    def testConstructors(self) -> None:

        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        assert deque.remainingCapacity() == float("inf")

        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        assert deque.remainingCapacity() == 2

        deque = LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, self.__TWO])
        assert deque.size() == 2

        with pytest.raises(NullPointerException):
            LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, None])

    def testClear(self) -> None:

        deque = LinkedBlockingDeque()
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        deque.clear()
        deque.add(self.__ONE)
        assert deque.size() == 1

    def testAddLast(self) -> None:

        deque = LinkedBlockingDeque()
        deque.addLast(self.__ONE)
        deque.addLast(self.__TWO)
        assert deque.size() == 2
        try:
            deque.add(self.__THREE)
            assert False
        except IllegalStateException:
            assert True
        assert deque.pop() == Integer.valueOf(1)

    def testAddFirst(self) -> None:

        deque = LinkedBlockingDeque()
        deque.addFirst(self.__ONE)
        deque.addFirst(self.__TWO)
        assert deque.size() == 2
        with self.assertRaises(IllegalStateException):
            deque.add(self.__THREE)
        assert deque.pop() == Integer.valueOf(2)

    def testAdd(self) -> None:

        assert self.deque.add(self.__ONE)
        assert self.deque.add(self.__TWO)

        try:
            self.deque.add(self.__THREE)
            assert False
        except IllegalStateException:
            pass

        try:
            self.deque.add(None)
            assert False
        except NullPointerException:
            pass

    def setUp(self) -> None:

        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
