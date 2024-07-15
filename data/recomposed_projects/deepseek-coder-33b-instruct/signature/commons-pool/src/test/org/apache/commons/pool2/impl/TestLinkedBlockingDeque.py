from __future__ import annotations
import time
import re
import sys
import unittest
import pytest
import io
import typing
from typing import *
import datetime
import os
import unittest
from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *


class TestLinkedBlockingDeque(unittest.TestCase):

    __THREE: int = 3
    __TWO: int = 2
    __ONE: int = 1
    __TIMEOUT_50_MILLIS: datetime.timedelta = datetime.timedelta(milliseconds=50)
    deque: LinkedBlockingDeque[int] = None

    def testToArray(self) -> None:

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        arr = self.deque.toArray()
        self.assertEqual(Integer.valueOf(1), arr[0])
        self.assertEqual(Integer.valueOf(2), arr[1])

        arr = self.deque.toArray(Integer[0])
        self.assertEqual(Integer.valueOf(1), arr[0])
        self.assertEqual(Integer.valueOf(2), arr[1])

        arr = self.deque.toArray(Integer[0])
        self.assertEqual(Integer.valueOf(1), arr[0])
        self.assertEqual(Integer.valueOf(2), arr[1])

    def testTakeLast(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        self.assertEqual(1, self.deque.takeLast())

    def testTakeFirst(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.takeFirst())

    def testTake(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.take())

    def testRemoveLastOccurrence(self) -> None:

        assert not self.deque.removeLastOccurrence(None)
        assert not self.deque.removeLastOccurrence(self.__ONE)
        self.deque.add(self.__ONE)
        self.deque.add(self.__ONE)
        assert self.deque.removeLastOccurrence(self.__ONE)
        self.assertEqual(1, self.deque.size())

    def testRemoveLast(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.removeLast()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        assert self.deque.removeLast() == Integer.valueOf(2)

        with pytest.raises(RuntimeError):
            self.deque.removeLast()
            self.deque.removeLast()

    def testRemoveFirst(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.removeFirst()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        assert self.deque.removeFirst() == self.__ONE

        with pytest.raises(RuntimeError):
            self.deque.removeFirst()
            self.deque.removeFirst()

    def testRemove(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.remove()

        self.deque.add(1)
        self.deque.add(2)
        assert self.deque.remove() == 1

    def testPutLast(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.putLast(None)

        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)

        assert self.deque.size() == 2
        assert self.deque.pop() == Integer.valueOf(1)

    def testPutFirst(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.putFirst(None)

        self.deque.putFirst(1)
        self.deque.putFirst(2)

        assert self.deque.size() == 2
        assert self.deque.pop() == 2

    def testPut(self) -> None:

        with pytest.raises(TypeError):
            self.deque.put(None)

        self.deque.put(self.__ONE)
        self.deque.put(self.__TWO)

    def testPush(self) -> None:

        self.deque = LinkedBlockingDeque()
        self.__ONE = 1
        self.__TWO = 2
        self.__THREE = 3

        self.deque.push(self.__ONE)
        self.deque.push(self.__TWO)
        self.assertEqual(2, len(self.deque))
        with self.assertRaises(RuntimeError):
            self.deque.push(self.__THREE)
        self.assertEqual(2, self.deque.pop())

    def testPossibleBug(self) -> None:

        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            self.deque.add(i)

        iter = self.deque.iterator()
        next(iter)

        self.deque.remove(1)
        self.deque.remove(0)
        self.deque.remove(2)

        with pytest.raises(RuntimeError):
            next(iter)

    def testPop(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.pop()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        assert self.deque.pop() == self.__ONE

        with pytest.raises(RuntimeError):
            self.deque.pop()
            self.deque.pop()

    def testPollWithTimeout(self) -> None:

        # Assuming that the poll1 method is a blocking method that waits for a specified timeout before returning.
        # If the timeout expires, it returns None.
        # Here we are asserting that the poll1 method returns None within the specified timeout.

        assert self.deque.poll1(self.__TIMEOUT_50_MILLIS) is None
        assert self.deque.poll1(self.__TIMEOUT_50_MILLIS) is None

    def testPollLastWithTimeout(self) -> None:

        # Check if the deque is None
        if self.deque is None:
            raise ValueError("Deque is not initialized")

        # Check if the deque is empty
        if len(self.deque) == 0:
            raise ValueError("Deque is empty")

        # Check if the deque is not empty
        if len(self.deque) > 0:
            # Poll the last element from the deque
            last_element = self.deque.pollLast()

            # Check if the last element is None
            if last_element is None:
                raise ValueError("Last element is None")

            # Check if the last element is not None
            if last_element is not None:
                # Poll the last element from the deque with a timeout
                last_element_with_timeout = self.deque.pollLast(
                    self.__TIMEOUT_50_MILLIS
                )

                # Check if the last element with timeout is None
                if last_element_with_timeout is None:
                    raise ValueError("Last element with timeout is None")

                # Check if the last element with timeout is not None
                if last_element_with_timeout is not None:
                    # Check if the last element is the same as the last element with timeout
                    if last_element != last_element_with_timeout:
                        raise ValueError(
                            "Last element is not the same as the last element with timeout"
                        )

    def testPollLast(self) -> None:

        self.assertIsNone(self.deque.pollLast())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(1, self.deque.pollLast())

    def testPollFirstWithTimeout(self) -> None:

        pass  # LLM could not translate this method

    def testPollFirst(self) -> None:

        # assertNull(deque.pollFirst());
        self.assertIsNone(self.deque.pollFirst())

        # assertTrue(deque.offerFirst(ONE));
        self.assertTrue(self.deque.offerFirst(self.__ONE))

        # assertTrue(deque.offerFirst(TWO));
        self.assertTrue(self.deque.offerFirst(self.__TWO))

        # assertEquals(Integer.valueOf(2), deque.pollFirst());
        self.assertEqual(self.__TWO, self.deque.pollFirst())

    def testPeekLast(self) -> None:

        self.assertIsNone(self.deque.peekLast())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.peekLast())

    def testPeekFirst(self) -> None:

        self.assertIsNone(self.deque.peekFirst())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.peekFirst())

    def testPeek(self) -> None:

        self.assertIsNone(self.deque.peek())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.peek())

    def testOfferWithTimeout(self) -> None:

        # Initialize the deque
        self.deque = LinkedBlockingDeque()

        # Initialize the constants
        self.__THREE = 3
        self.__TWO = 2
        self.__ONE = 1
        self.__TIMEOUT_50_MILLIS = datetime.timedelta(milliseconds=50)

        # Test the offer1 method with timeout
        self.assertTrue(self.deque.offer1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offer1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offer1(self.__THREE, self.__TIMEOUT_50_MILLIS))

        # Test the offer1 method with timeout and null value
        with self.assertRaises(RuntimeError):
            self.deque.offer1(None, self.__TIMEOUT_50_MILLIS)

    def testOfferLastWithTimeout(self) -> None:

        with self.assertRaises(RuntimeError):
            self.deque.offerLast1(None, self.__TIMEOUT_50_MILLIS)

        self.assertTrue(self.deque.offerLast1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offerLast1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offerLast1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferLast(self) -> None:

        self.deque = LinkedBlockingDeque()
        self.__ONE = 1
        self.__TWO = 2

        self.deque.offerLast(self.__ONE)
        self.deque.offerLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerLast(None)
        self.assertEqual(1, self.deque.pop())

    def testOfferFirstWithTimeout(self) -> None:

        with self.assertRaises(RuntimeError):
            self.deque.offerFirst1(None, self.__TIMEOUT_50_MILLIS)

        self.assertTrue(self.deque.offerFirst1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offerFirst1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offerFirst1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferFirst(self) -> None:

        self.deque = LinkedBlockingDeque()
        self.__ONE = 1
        self.__TWO = 2

        self.deque.offerFirst(self.__ONE)
        self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.qsize())
        with self.assertRaises(RuntimeError):
            self.deque.offerFirst(None)
        self.assertEqual(2, self.deque.pop())

    def testOffer(self) -> None:

        ONE = 1
        TWO = 2
        THREE = 3

        assert self.deque.offer(ONE)
        assert self.deque.offer(TWO)
        assert not self.deque.offer(THREE)

        with pytest.raises(TypeError):
            self.deque.offer(None)

    def testIterator(self) -> None:

        with pytest.raises(StopIteration):
            next(self.deque.iterator())

        self.deque.add(1)
        self.deque.add(2)
        iter = self.deque.iterator()
        assert next(iter) == 1
        iter.remove()
        assert next(iter) == 2

    def testGetLast(self) -> None:

        # assertThrows(RuntimeError.class, () -> deque.getLast());
        with self.assertRaises(RuntimeError):
            self.deque.getLast()

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(2), deque.getLast());
        self.assertEqual(self.__TWO, self.deque.getLast())

    def testGetFirst(self) -> None:

        # assertThrows(RuntimeError.class, () -> deque.getFirst());
        with self.assertRaises(RuntimeError):
            self.deque.getFirst()

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.getFirst());
        self.assertEqual(self.__ONE, self.deque.getFirst())

    def testElement(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.element()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        assert self.deque.element() == Integer.valueOf(1)

    def testDrainTo(self) -> None:

        c = []
        self.deque.append(self.__ONE)
        self.deque.append(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.append(self.__ONE)
        self.deque.append(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, len(self.deque))
        self.assertEqual(1, len(c))
        self.assertEqual(self.__ONE, next(iter(c)))

    def testDescendingIterator(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.descendingIterator().next()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter = self.deque.descendingIterator()
        assert Integer.valueOf(2) == iter.next()
        iter.remove()
        assert Integer.valueOf(1) == iter.next()

    def testContains(self) -> None:

        self.deque = LinkedBlockingDeque()
        self.__ONE = 1
        self.__TWO = 2
        self.__THREE = 3

        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.contains(self.__ONE))
        self.assertFalse(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(None))
        self.deque.add(self.__TWO)
        self.assertTrue(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(self.__THREE))

    def testConstructors(self) -> None:

        # Testing LinkedBlockingDeque0()
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, self.deque.remainingCapacity())

        # Testing LinkedBlockingDeque3(2)
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, self.deque.remainingCapacity())

        # Testing LinkedBlockingDeque2([ONE, TWO])
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, self.__TWO])
        self.assertEqual(2, self.deque.size())

        # Testing LinkedBlockingDeque2([ONE, null])
        with self.assertRaises(RuntimeError):
            LinkedBlockingDeque.LinkedBlockingDeque2([self.__ONE, None])

    def testClear(self) -> None:

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.deque.clear()
        self.deque.add(self.__ONE)
        self.assertEqual(1, self.deque.size())

    def testAddLast(self) -> None:

        self.deque = LinkedBlockingDeque()
        self.__ONE = 1
        self.__TWO = 2
        self.__THREE = 3

        self.deque.addLast(self.__ONE)
        self.deque.addLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        self.assertEqual(1, self.deque.pop())

    def testAddFirst(self) -> None:

        self.deque = LinkedBlockingDeque()
        self.__ONE = 1
        self.__TWO = 2
        self.__THREE = 3

        self.deque.addFirst(self.__ONE)
        self.deque.addFirst(self.__TWO)
        self.assertEqual(2, self.deque.qsize())
        with self.assertRaises(Exception):
            self.deque.put(self.__THREE)
        self.assertEqual(2, self.deque.pop())

    def testAdd(self) -> None:

        # Initialize the deque
        self.deque = LinkedBlockingDeque()

        # Test adding elements
        self.__ONE = 1
        self.__TWO = 2
        self.__THREE = 3

        self.assertTrue(self.deque.add(self.__ONE))
        self.assertTrue(self.deque.add(self.__TWO))

        # Test adding an element when the deque is full
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)

        # Test adding a null element
        with self.assertRaises(RuntimeError):
            self.deque.add(None)

    def setUp(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
