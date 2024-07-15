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

        deque = LinkedBlockingDeque()
        deque.add(self.__ONE)
        deque.add(self.__TWO)

        arr = deque.toArray()
        self.assertEqual(self.__ONE, arr[0])
        self.assertEqual(self.__TWO, arr[1])

        arr = deque.toArray([])
        self.assertEqual(self.__ONE, arr[0])
        self.assertEqual(self.__TWO, arr[1])

        arr = deque.toArray([])
        self.assertEqual(self.__ONE, arr[0])
        self.assertEqual(self.__TWO, arr[1])

    def testTakeLast(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        self.assertEqual(self.__ONE, self.deque.takeLast())

    def testTakeFirst(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        self.assertEqual(Integer.valueOf(2), self.deque.takeFirst())

    def testTake(self) -> None:

        assert self.deque.offerFirst(self.__ONE)
        assert self.deque.offerFirst(self.__TWO)
        self.assertEqual(Integer.valueOf(2), self.deque.take())

    def testRemoveLastOccurrence(self) -> None:

        deque = LinkedBlockingDeque()

        assert not deque.removeLastOccurrence(None)
        assert not deque.removeLastOccurrence(self.__ONE)
        deque.add(self.__ONE)
        deque.add(self.__ONE)
        assert deque.removeLastOccurrence(self.__ONE)
        self.assertEqual(1, deque.size())

    def testRemoveLast(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.removeLast()

        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        assert self.deque.removeLast() == self.__TWO

        with pytest.raises(RuntimeError):
            self.deque.removeLast()
            self.deque.removeLast()

    def testRemoveFirst(self) -> None:

        # Create an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        # Test that removing from an empty deque raises a RuntimeError
        with pytest.raises(RuntimeError):
            deque.removeFirst()

        # Add elements to the deque
        deque.add(self.__ONE)
        deque.add(self.__TWO)

        # Test that the first element is removed correctly
        assert deque.removeFirst() == self.__ONE

        # Test that removing from an empty deque raises a RuntimeError
        with pytest.raises(RuntimeError):
            deque.removeFirst()
            deque.removeFirst()

    def testRemove(self) -> None:

        # Create a deque
        deque = LinkedBlockingDeque()

        # Test that removing from an empty deque raises a RuntimeError
        with pytest.raises(RuntimeError):
            deque.remove()

        # Add elements to the deque
        deque.add(self.__ONE)
        deque.add(self.__TWO)

        # Test that removing an element from the deque returns the expected value
        assert deque.remove() == self.__ONE

    def testPutLast(self) -> None:

        with pytest.raises(TypeError):
            self.deque.putLast(None)

        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)
        assert self.deque.size() == 2
        assert self.deque.pop() == self.__ONE

    def testPutFirst(self) -> None:

        with pytest.raises(TypeError):
            self.deque.putFirst(None)

        self.deque.putFirst(self.__ONE)
        self.deque.putFirst(self.__TWO)
        assert self.deque.size() == 2
        assert self.deque.pop() == self.__TWO

    def testPut(self) -> None:

        with pytest.raises(TypeError):
            self.deque.put(None)

        self.deque.put(self.__ONE)
        self.deque.put(self.__TWO)

    def testPush(self) -> None:

        deque = LinkedBlockingDeque()
        deque.push(self.__ONE)
        deque.push(self.__TWO)
        self.assertEqual(2, deque.size())
        with self.assertRaises(RuntimeError):
            deque.push(self.__THREE)
        self.assertEqual(Integer.valueOf(2), deque.pop())

    def testPossibleBug(self) -> None:

        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            deque.add(i)

        iter = deque.iterator()
        next(iter)

        deque.remove(1)
        deque.remove(0)
        deque.remove(2)

        with pytest.raises(RuntimeError):
            next(iter)

    def testPop(self) -> None:

        # assertThrows(RuntimeError.class, () -> deque.pop());
        with pytest.raises(IndexError):
            self.deque.pop()

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.append(self.__ONE)
        self.deque.append(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.pop());
        assert self.deque.pop() == self.__ONE

        # assertThrows(RuntimeError.class, () -> {deque.pop(); deque.pop();});
        with pytest.raises(IndexError):
            self.deque.pop()
            self.deque.pop()

    def testPollWithTimeout(self) -> None:

        # Assuming deque is an instance of LinkedBlockingDeque
        self.assertIsNone(deque.poll1(self.__TIMEOUT_50_MILLIS))
        self.assertIsNone(deque.poll1(self.__TIMEOUT_50_MILLIS))

    def testPollLastWithTimeout(self) -> None:

        # Create an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        # Assert that pollLast() returns None
        self.assertIsNone(deque.pollLast())

        # Assert that pollLast1() with TIMEOUT_50_MILLIS returns None
        self.assertIsNone(deque.pollLast1(self.__TIMEOUT_50_MILLIS))

    def testPollLast(self) -> None:

        # Initialize deque
        deque = LinkedBlockingDeque()

        self.assertIsNone(deque.pollLast())
        self.assertTrue(deque.offerFirst(self.__ONE))
        self.assertTrue(deque.offerFirst(self.__TWO))
        self.assertEqual(self.__ONE, deque.pollLast())

    def testPollFirstWithTimeout(self) -> None:

        # Create an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        # Assert that pollFirst returns None
        self.assertIsNone(deque.pollFirst())

        # Assert that pollFirst1 with timeout returns None
        self.assertIsNone(deque.pollFirst1(self.__TIMEOUT_50_MILLIS))

    def testPollFirst(self) -> None:

        # Create an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        self.assertIsNone(deque.pollFirst())
        self.assertTrue(deque.offerFirst(self.__ONE))
        self.assertTrue(deque.offerFirst(self.__TWO))
        self.assertEqual(self.__TWO, deque.pollFirst())

    def testPeekLast(self) -> None:

        deque = LinkedBlockingDeque()

        self.assertIsNone(deque.peekLast())
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        self.assertEqual(self.__TWO, deque.peekLast())

    def testPeekFirst(self) -> None:

        deque = LinkedBlockingDeque()

        self.assertIsNone(deque.peekFirst())
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        self.assertEqual(self.__ONE, deque.peekFirst())

    def testPeek(self) -> None:

        deque = LinkedBlockingDeque()

        self.assertIsNone(deque.peek())
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        self.assertEqual(self.__ONE, deque.peek())

    def testOfferWithTimeout(self) -> None:

        # Assuming deque is an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        assert deque.offer1(self.__ONE, self.__TIMEOUT_50_MILLIS)
        assert deque.offer1(self.__TWO, self.__TIMEOUT_50_MILLIS)
        assert not deque.offer1(self.__THREE, self.__TIMEOUT_50_MILLIS)

        with pytest.raises(RuntimeError):
            deque.offer1(None, self.__TIMEOUT_50_MILLIS)

    def testOfferLastWithTimeout(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.offerLast1(None, self.__TIMEOUT_50_MILLIS)

        assert self.deque.offerLast1(self.__ONE, self.__TIMEOUT_50_MILLIS)
        assert self.deque.offerLast1(self.__TWO, self.__TIMEOUT_50_MILLIS)
        assert not self.deque.offerLast1(self.__THREE, self.__TIMEOUT_50_MILLIS)

    def testOfferLast(self) -> None:

        deque = LinkedBlockingDeque()
        deque.offerLast(self.__ONE)
        deque.offerLast(self.__TWO)
        self.assertEqual(2, deque.size())
        with self.assertRaises(RuntimeError):
            deque.offerLast(None)
        self.assertEqual(self.__ONE, deque.pop())

    def testOfferFirstWithTimeout(self) -> None:

        with pytest.raises(RuntimeError):
            self.deque.offerFirst1(None, self.__TIMEOUT_50_MILLIS)

        assert self.deque.offerFirst1(self.__ONE, self.__TIMEOUT_50_MILLIS)
        assert self.deque.offerFirst1(self.__TWO, self.__TIMEOUT_50_MILLIS)
        assert not self.deque.offerFirst1(self.__THREE, self.__TIMEOUT_50_MILLIS)

    def testOfferFirst(self) -> None:

        deque = LinkedBlockingDeque()

        deque.offerFirst(self.__ONE)
        deque.offerFirst(self.__TWO)
        self.assertEqual(2, deque.size())
        with self.assertRaises(RuntimeError):
            deque.offerFirst(None)
        self.assertEqual(Integer.valueOf(2), deque.pop())

    def testOffer(self) -> None:

        deque = LinkedBlockingDeque()

        self.assertTrue(deque.offer(self.__ONE))
        self.assertTrue(deque.offer(self.__TWO))
        self.assertFalse(deque.offer(self.__THREE))

        with self.assertRaises(RuntimeError):
            deque.offer(None)

    def testIterator(self) -> None:

        # Create an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        # Test if RuntimeError is raised when calling next() on an empty iterator
        with pytest.raises(RuntimeError):
            deque.iterator().next()

        # Add elements to the deque
        deque.add(self.__ONE)
        deque.add(self.__TWO)

        # Get the iterator
        iter = deque.iterator()

        # Test if the first element is 1
        assert iter.next() == self.__ONE

        # Remove the first element
        iter.remove()

        # Test if the next element is 2
        assert iter.next() == self.__TWO

    def testGetLast(self) -> None:

        # Create an instance of LinkedBlockingDeque
        deque = LinkedBlockingDeque()

        # Test that getLast() raises a RuntimeError when the deque is empty
        with pytest.raises(RuntimeError):
            deque.getLast()

        # Add elements to the deque
        deque.add(self.__ONE)
        deque.add(self.__TWO)

        # Test that getLast() returns the last element added to the deque
        assert deque.getLast() == self.__TWO

    def testGetFirst(self) -> None:

        # assertThrows(RuntimeError.class, () -> deque.getFirst());
        with pytest.raises(RuntimeError):
            self.deque.getFirst()

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.getFirst());
        assert self.deque.getFirst() == self.__ONE

    def testElement(self) -> None:

        # assertThrows(RuntimeError.class, () -> deque.element());
        with pytest.raises(RuntimeError):
            self.deque.element()

        # deque.add(ONE);
        # deque.add(TWO);
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)

        # assertEquals(Integer.valueOf(1), deque.element());
        assert self.deque.element() == self.__ONE

    def testDrainTo(self) -> None:

        c: List[int] = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, len(self.deque))
        self.assertEqual(1, len(c))
        self.assertEqual(self.__ONE, next(iter(c)))

    def testDescendingIterator(self) -> None:

        deque = LinkedBlockingDeque()

        with pytest.raises(RuntimeError):
            deque.descendingIterator().next()

        deque.add(self.__ONE)
        deque.add(self.__TWO)
        iter = deque.descendingIterator()

        assert iter.next() == self.__TWO
        iter.remove()
        assert iter.next() == self.__ONE

    def testContains(self) -> None:

        deque = LinkedBlockingDeque()
        deque.add(self.__ONE)
        self.assertTrue(deque.contains(self.__ONE))
        self.assertFalse(deque.contains(self.__TWO))
        self.assertFalse(deque.contains(None))
        deque.add(self.__TWO)
        self.assertTrue(deque.contains(self.__TWO))
        self.assertFalse(deque.contains(self.__THREE))

    def testConstructors(self) -> None:

        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remainingCapacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, deque.remainingCapacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque2([1, 2])
        self.assertEqual(2, deque.size())

        with self.assertRaises(RuntimeError):
            LinkedBlockingDeque.LinkedBlockingDeque2([1, None])

    def testClear(self) -> None:

        deque = LinkedBlockingDeque()
        deque.add(self.__ONE)
        deque.add(self.__TWO)
        deque.clear()
        deque.add(self.__ONE)
        self.assertEqual(1, deque.size())

    def testAddLast(self) -> None:

        deque = LinkedBlockingDeque()
        deque.addLast(self.__ONE)
        deque.addLast(self.__TWO)
        self.assertEqual(2, deque.size())
        with self.assertRaises(RuntimeError):
            deque.add(self.__THREE)
        self.assertEqual(Integer.valueOf(1), deque.pop())

    def testAddFirst(self) -> None:

        deque = LinkedBlockingDeque()
        deque.addFirst(self.__ONE)
        deque.addFirst(self.__TWO)
        self.assertEqual(2, deque.size())
        with self.assertRaises(RuntimeError):
            deque.add(self.__THREE)
        self.assertEqual(Integer.valueOf(2), deque.pop())

    def testAdd(self) -> None:

        deque = LinkedBlockingDeque()

        self.assertTrue(deque.add(self.__ONE))
        self.assertTrue(deque.add(self.__TWO))

        with self.assertRaises(RuntimeError):
            deque.add(self.__THREE)

        with self.assertRaises(RuntimeError):
            deque.add(None)

    def setUp(self) -> None:

        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
