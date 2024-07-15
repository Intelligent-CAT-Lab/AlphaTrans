from __future__ import annotations
import time
import re
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

        pass  # LLM could not translate this method

    def testTakeLast(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(Integer.valueOf(1), self.deque.takeLast())

    def testTakeFirst(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(Integer.valueOf(2), self.deque.takeFirst())

    def testTake(self) -> None:
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(Integer.valueOf(2), self.deque.take())

    def testRemoveLastOccurrence(self) -> None:
        self.assertFalse(self.deque.removeLastOccurrence(None))
        self.assertFalse(self.deque.removeLastOccurrence(self.__ONE))
        self.deque.add(self.__ONE)
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.removeLastOccurrence(self.__ONE))
        self.assertEqual(1, self.deque.size())

    def testRemoveLast(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.removeLast()
        deque.add(ONE)
        deque.add(TWO)
        self.assertEqual(Integer.valueOf(2), deque.removeLast())
        with self.assertRaises(RuntimeError):
            deque.removeLast()
            deque.removeLast()

    def testRemoveFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.removeFirst()
        deque.add(ONE)
        deque.add(TWO)
        self.assertEqual(Integer.valueOf(1), deque.removeFirst())
        with self.assertRaises(RuntimeError):
            deque.removeFirst()
            deque.removeFirst()

    def testRemove(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.remove()
        deque.add(ONE)
        deque.add(TWO)
        self.assertEqual(Integer.valueOf(1), deque.remove())

    def testPutLast(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putLast(None)
        self.deque.putLast(self.__ONE)
        self.deque.putLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        self.assertEqual(Integer.valueOf(1), self.deque.pop())

    def testPutFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.putFirst(None)
        self.deque.putFirst(self.__ONE)
        self.deque.putFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        self.assertEqual(Integer.valueOf(2), self.deque.pop())

    def testPut(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.put(None)
        self.deque.put(self.__ONE)
        self.deque.put(self.__TWO)

    def testPush(self) -> None:
        self.deque.push(self.__ONE)
        self.deque.push(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.push(self.__THREE)
        self.assertEqual(Integer.valueOf(2), self.deque.pop())

    def testPossibleBug(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            deque.add(Integer.valueOf(i))

        iter = deque.iterator()
        iter.next()

        deque.remove(Integer.valueOf(1))
        deque.remove(Integer.valueOf(0))
        deque.remove(Integer.valueOf(2))

        iter.next()

    def testPop(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.pop()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(Integer.valueOf(1), self.deque.pop())
        with self.assertRaises(RuntimeError):
            self.deque.pop()
            self.deque.pop()

    def testPollWithTimeout(self) -> None:
        self.assertIsNone(self.deque.poll1(self.__TIMEOUT_50_MILLIS))
        self.assertIsNone(self.deque.poll1(self.__TIMEOUT_50_MILLIS))

    def testPollLastWithTimeout(self) -> None:
        self.assertIsNone(self.deque.pollLast())
        self.assertIsNone(self.deque.pollLast1(self.__TIMEOUT_50_MILLIS))

    def testPollLast(self) -> None:
        self.assertIsNone(self.deque.pollLast())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(Integer.valueOf(1), self.deque.pollLast())

    def testPollFirstWithTimeout(self) -> None:
        self.assertIsNone(self.deque.pollFirst())
        self.assertIsNone(self.deque.pollFirst1(self.__TIMEOUT_50_MILLIS))

    def testPollFirst(self) -> None:
        self.assertIsNone(self.deque.pollFirst())
        self.assertTrue(self.deque.offerFirst(self.__ONE))
        self.assertTrue(self.deque.offerFirst(self.__TWO))
        self.assertEqual(Integer.valueOf(2), self.deque.pollFirst())

    def testPeekLast(self) -> None:
        self.assertIsNone(self.deque.peekLast())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(Integer.valueOf(2), self.deque.peekLast())

    def testPeekFirst(self) -> None:
        self.assertIsNone(self.deque.peekFirst())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(Integer.valueOf(1), self.deque.peekFirst())

    def testPeek(self) -> None:
        self.assertIsNone(self.deque.peek())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(Integer.valueOf(1), self.deque.peek())

    def testOfferWithTimeout(self) -> None:
        self.assertTrue(self.deque.offer1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offer1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offer1(self.__THREE, self.__TIMEOUT_50_MILLIS))
        with self.assertRaises(RuntimeError):
            self.deque.offer1(None, self.__TIMEOUT_50_MILLIS)

    def testOfferLastWithTimeout(self) -> None:
        assertRaises(
            RuntimeError, lambda: self.deque.offerLast1(None, self.__TIMEOUT_50_MILLIS)
        )
        assertTrue(self.deque.offerLast1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        assertTrue(self.deque.offerLast1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        assertFalse(self.deque.offerLast1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferLast(self) -> None:
        self.deque.offerLast(self.__ONE)
        self.deque.offerLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerLast(None)
        self.assertEqual(Integer.valueOf(1), self.deque.pop())

    def testOfferFirstWithTimeout(self) -> None:
        with self.assertRaises(RuntimeError):
            self.deque.offerFirst1(None, self.__TIMEOUT_50_MILLIS)
        self.assertTrue(self.deque.offerFirst1(self.__ONE, self.__TIMEOUT_50_MILLIS))
        self.assertTrue(self.deque.offerFirst1(self.__TWO, self.__TIMEOUT_50_MILLIS))
        self.assertFalse(self.deque.offerFirst1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferFirst(self) -> None:
        self.deque.offerFirst(self.__ONE)
        self.deque.offerFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.offerFirst(None)
        self.assertEqual(Integer.valueOf(2), self.deque.pop())

    def testOffer(self) -> None:
        self.assertTrue(self.deque.offer(self.__ONE))
        self.assertTrue(self.deque.offer(self.__TWO))
        self.assertFalse(self.deque.offer(self.__THREE))
        with self.assertRaises(RuntimeError):
            self.deque.offer(None)

    def testIterator(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.iterator().next()
        deque.add(ONE)
        deque.add(TWO)
        iter: Iterator[int] = deque.iterator()
        self.assertEqual(Integer.valueOf(1), iter.next())
        iter.remove()
        self.assertEqual(Integer.valueOf(2), iter.next())

    def testGetLast(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.getLast()
        deque.add(ONE)
        deque.add(TWO)
        self.assertEqual(Integer.valueOf(2), deque.getLast())

    def testGetFirst(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.getFirst()
        deque.add(ONE)
        deque.add(TWO)
        self.assertEqual(Integer.valueOf(1), deque.getFirst())

    def testElement(self) -> None:
        with self.assertRaises(RuntimeError):
            deque.element()
        deque.add(ONE)
        deque.add(TWO)
        self.assertEqual(Integer.valueOf(1), deque.element())

    def testDrainTo(self) -> None:
        c: Collection[int] = ArrayList()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(2, self.deque.drainTo0(c))
        self.assertEqual(2, c.size())

        c = ArrayList()
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.assertEqual(1, self.deque.drainTo1(c, 1))
        self.assertEqual(1, self.deque.size())
        self.assertEqual(1, c.size())
        self.assertEqual(Integer.valueOf(1), c.iterator().next())

    def testDescendingIterator(self) -> None:
        self.assertRaises(RuntimeError, lambda: self.deque.descendingIterator().next())
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        iter: Iterator[int] = self.deque.descendingIterator()
        self.assertEqual(Integer.valueOf(2), iter.next())
        iter.remove()
        self.assertEqual(Integer.valueOf(1), iter.next())

    def testContains(self) -> None:
        self.deque.add(self.__ONE)
        self.assertTrue(self.deque.contains(self.__ONE))
        self.assertFalse(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(None))
        self.deque.add(self.__TWO)
        self.assertTrue(self.deque.contains(self.__TWO))
        self.assertFalse(self.deque.contains(self.__THREE))

    def testConstructors(self) -> None:

        pass  # LLM could not translate this method

    def testClear(self) -> None:
        self.deque.add(self.__ONE)
        self.deque.add(self.__TWO)
        self.deque.clear()
        self.deque.add(self.__ONE)
        self.assertEqual(1, self.deque.size())

    def testAddLast(self) -> None:
        self.deque.addLast(self.__ONE)
        self.deque.addLast(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        self.assertEqual(Integer.valueOf(1), self.deque.pop())

    def testAddFirst(self) -> None:
        self.deque.addFirst(self.__ONE)
        self.deque.addFirst(self.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        self.assertEqual(Integer.valueOf(2), self.deque.pop())

    def testAdd(self) -> None:
        self.assertTrue(self.deque.add(self.__ONE))
        self.assertTrue(self.deque.add(self.__TWO))
        with self.assertRaises(RuntimeError):
            self.deque.add(self.__THREE)
        with self.assertRaises(RuntimeError):
            self.deque.add(None)

    def setUp(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
