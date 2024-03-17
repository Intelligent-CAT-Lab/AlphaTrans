# Imports Begin
from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *
import unittest
import os
import datetime
import typing
from typing import *
# Imports End

class TestLinkedBlockingDeque(unittest.TestCase):

    # Class Fields Begin
    __TIMEOUT_50_MILLIS: datetime.timedelta = datetime.timedelta(milliseconds=50)
    __ONE: int = 1
    __TWO: int = "" # LLM could not translate field
    __THREE: int = "" # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def testToArray(self) -> None:


        pass # LLM could not translate method body

    def testTakeLast(self) -> None:

            self.assertTrue(self.deque.offerFirst(self.__ONE))
            self.assertTrue(self.deque.offerFirst(self.__TWO))
            self.assertEqual(self.__ONE, self.deque.takeLast())

    def testTakeFirst(self) -> None:

            self.assertTrue(self.deque.offerFirst(self.__ONE))
            self.assertTrue(self.deque.offerFirst(self.__TWO))
            self.assertEqual(self.__TWO, self.deque.takeFirst())

    def testTake(self) -> None:

            self.assertTrue(self.deque.offerFirst(self.__ONE))
            self.assertTrue(self.deque.offerFirst(self.__TWO))
            self.assertEqual(self.__TWO, self.deque.take())

    def testRemoveLastOccurrence(self) -> None:

            self.assertFalse(self.deque.removeLastOccurrence(None))
            self.assertFalse(self.deque.removeLastOccurrence(ONE))
            self.deque.add(ONE)
            self.deque.add(ONE)
            self.assertTrue(self.deque.removeLastOccurrence(ONE))
            self.assertEqual(1, self.deque.size())

    def testRemoveLast(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.removeLast()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__TWO, self.deque.removeLast())
            with self.assertRaises(NoSuchElementException):
                self.deque.removeLast()
                self.deque.removeLast()

    def testRemoveFirst(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.removeFirst()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__ONE, self.deque.removeFirst())
            with self.assertRaises(NoSuchElementException):
                self.deque.removeFirst()
                self.deque.removeFirst()

    def testRemove(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.remove()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__ONE, self.deque.remove())

    def testPutLast(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.putLast(None)
            self.deque.putLast(self.__ONE)
            self.deque.putLast(self.__TWO)
            self.assertEqual(2, self.deque.size())
            self.assertEqual(self.__ONE, self.deque.pop())

    def testPutFirst(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.putFirst(None)
            self.deque.putFirst(self.__ONE)
            self.deque.putFirst(self.__TWO)
            self.assertEqual(2, self.deque.size())
            self.assertEqual(self.__TWO, self.deque.pop())

    def testPut(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.put(None)
            self.deque.put(self.__ONE)
            self.deque.put(self.__TWO)

    def testPush(self) -> None:

            self.deque.push(self.__ONE)
            self.deque.push(self.__TWO)
            assert self.deque.size() == 2
            assertThrows(IllegalStateException, self.deque.push(self.__THREE))
            assert self.deque.pop() == 2

    def testPossibleBug(self) -> None:

            deque = LinkedBlockingDeque.LinkedBlockingDeque0()
            for i in range(3):
                deque.add(i)
            iter = deque.iterator()
            iter.next()
            deque.remove(1)
            deque.remove(0)
            deque.remove(2)
            iter.next()

    def testPop(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.pop()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__ONE, self.deque.pop())
            with self.assertRaises(NoSuchElementException):
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
            self.assertEqual(self.__ONE, self.deque.pollLast())

    def testPollFirstWithTimeout(self) -> None:

            self.assertIsNone(self.deque.pollFirst())
            self.assertIsNone(self.deque.pollFirst1(self.__TIMEOUT_50_MILLIS))

    def testPollFirst(self) -> None:

            self.assertIsNone(self.deque.pollFirst())
            self.assertTrue(self.deque.offerFirst(self.__ONE))
            self.assertTrue(self.deque.offerFirst(self.__TWO))
            self.assertEqual(self.__TWO, self.deque.pollFirst())

    def testPeekLast(self) -> None:

            self.assertIsNone(self.deque.peekLast())
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__TWO, self.deque.peekLast())

    def testPeekFirst(self) -> None:

            self.assertIsNone(self.deque.peekFirst())
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__ONE, self.deque.peekFirst())

    def testPeek(self) -> None:

            self.assertIsNone(self.deque.peek())
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__ONE, self.deque.peek())

    def testOfferWithTimeout(self) -> None:

            assert self.deque.offer1(self.__ONE, self.__TIMEOUT_50_MILLIS)
            assert self.deque.offer1(self.__TWO, self.__TIMEOUT_50_MILLIS)
            assert not self.deque.offer1(self.__THREE, self.__TIMEOUT_50_MILLIS)
            with self.assertRaises(NullPointerException):
                self.deque.offer1(None, self.__TIMEOUT_50_MILLIS)

    def testOfferLastWithTimeout(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.offerLast1(None, self.__TIMEOUT_50_MILLIS)
            self.assertTrue(self.deque.offerLast1(self.__ONE, self.__TIMEOUT_50_MILLIS))
            self.assertTrue(self.deque.offerLast1(self.__TWO, self.__TIMEOUT_50_MILLIS))
            self.assertFalse(self.deque.offerLast1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferLast(self) -> None:

            self.deque.offerLast(self.__ONE)
            self.deque.offerLast(self.__TWO)
            self.assertEqual(2, self.deque.size())
            assertThrows(NullPointerException, lambda: self.deque.offerLast(None))
            self.assertEqual(self.__ONE, self.deque.pop())

    def testOfferFirstWithTimeout(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.offerFirst1(None, self.__TIMEOUT_50_MILLIS)
            self.assertTrue(self.deque.offerFirst1(self.__ONE, self.__TIMEOUT_50_MILLIS))
            self.assertTrue(self.deque.offerFirst1(self.__TWO, self.__TIMEOUT_50_MILLIS))
            self.assertFalse(self.deque.offerFirst1(self.__THREE, self.__TIMEOUT_50_MILLIS))

    def testOfferFirst(self) -> None:

            self.deque.offerFirst(self.__ONE)
            self.deque.offerFirst(self.__TWO)
            assert self.deque.size() == 2
            assertThrows(self.deque.offerFirst(None), NullPointerException)
            assert self.deque.pop() == self.__TWO

    def testOffer(self) -> None:

            self.assertTrue(self.deque.offer(self.__ONE))
            self.assertTrue(self.deque.offer(self.__TWO))
            self.assertFalse(self.deque.offer(self.__THREE))
            self.assertRaises(TypeError, self.deque.offer, None)

    def testIterator(self) -> None:

            with self.assertRaises(NoSuchElementException):
                iter(self.deque).next()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            iter = self.deque.iterator()
            self.assertEqual(iter.next(), self.__ONE)
            iter.remove()
            self.assertEqual(iter.next(), self.__TWO)

    def testGetLast(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.getLast()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__TWO, self.deque.getLast())

    def testGetFirst(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.getFirst()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(1, self.deque.getFirst())

    def testElement(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.element()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(self.__ONE, self.deque.element())

    def testDrainTo(self) -> None:

            c = []
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(2, self.deque.drainTo0(c))
            self.assertEqual(2, len(c))
            c = []
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.assertEqual(1, self.deque.drainTo1(c, 1))
            self.assertEqual(1, self.deque.size())
            self.assertEqual(1, len(c))
            self.assertEqual(1, next(iter(c)))

    def testDescendingIterator(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.descendingIterator().next()
            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            iter = self.deque.descendingIterator()
            self.assertEqual(2, iter.next())
            iter.remove()
            self.assertEqual(1, iter.next())

    def testContains(self) -> None:

            self.deque.add(self.__ONE)
            assert self.deque.contains(self.__ONE)
            assert not self.deque.contains(self.__TWO)
            assert not self.deque.contains(None)
            self.deque.add(self.__TWO)
            assert self.deque.contains(self.__TWO)
            assert not self.deque.contains(self.__THREE)

    def testConstructors(self) -> None:

            deque = LinkedBlockingDeque0()
            self.assertEqual(Integer.MAX_VALUE, deque.remainingCapacity())
            deque = LinkedBlockingDeque3(2)
            self.assertEqual(2, deque.remainingCapacity())
            deque = LinkedBlockingDeque2(Arrays.asList(ONE, TWO))
            self.assertEqual(2, deque.size())
            assertThrows(
                    NullPointerException,
                    lambda: LinkedBlockingDeque2(Arrays.asList(ONE, None)))

    def testClear(self) -> None:

            self.deque.add(self.__ONE)
            self.deque.add(self.__TWO)
            self.deque.clear()
            self.deque.add(self.__ONE)
            assert self.deque.size() == 1

    def testAddLast(self) -> None:

            self.deque.addLast(self.__ONE)
            self.deque.addLast(self.__TWO)
            self.assertEqual(2, self.deque.size())
            self.assertRaises(IllegalStateException, self.deque.add, self.__THREE)
            self.assertEqual(1, self.deque.pop())

    def testAddFirst(self) -> None:

            self.deque.addFirst(self.__ONE)
            self.deque.addFirst(self.__TWO)
            assert self.deque.size() == 2
            assertThrows(IllegalStateException, self.deque.add, self.__THREE)
            assert self.deque.pop() == 2

    def testAdd(self) -> None:

            self.assertTrue(self.deque.add(self.__ONE))
            self.assertTrue(self.deque.add(self.__TWO))
            self.assertRaises(IllegalStateException, self.deque.add(self.__THREE))
            self.assertRaises(NullPointerException, self.deque.add(None))

    def setUp(self) -> None:

            self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)

    # Class Methods End


class new Executable(...) { ... }(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def execute(self) -> None:

            with self.assertRaises(IllegalStateException):
                self.deque.add(THREE)

    def execute(self) -> None:


        pass # LLM could not translate method body

    def execute(self) -> None:

            with self.assertRaises(IllegalStateException):
                self.deque.add(THREE)

    def execute(self) -> None:

            with self.assertRaises(IllegalStateException):
                self.deque.add(THREE)

    def execute(self) -> None:

            self.LinkedBlockingDeque2(Arrays.asList(ONE, None))

    def execute(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.descendingIterator().next()

    def execute(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.element()

    def execute(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.getFirst()

    def execute(self) -> None:

            with self.assertRaises(NoSuchElementException):
                self.deque.getLast()

    def execute(self) -> None:

            with pytest.raises(NoSuchElementException):
                deque.iterator().next()

    def execute(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.offer(None)

    def execute(self) -> None:

        with self.assertRaises(NullPointerException):
            self.deque.offerFirst(None)

    def execute(self) -> None:

        assertThrows(NullPointerException, lambda: deque.offerFirst1(None, TIMEOUT_50_MILLIS))

    def execute(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.offerLast(None)

    def execute(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.offerLast1(None, TIMEOUT_50_MILLIS)

    def execute(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.offer1(None, TIMEOUT_50_MILLIS)

    def execute(self) -> None:

            with pytest.raises(NoSuchElementException):
                deque.pop()

    def execute(self) -> None:

            self.deque.pop()
            self.deque.pop()

    def execute(self) -> None:

            with self.assertRaises(IllegalStateException):
                self.deque.push(THREE)

    def execute(self) -> None:

            with pytest.raises(NullPointerException):
                self.deque.put(None)

    def execute(self) -> None:

            with self.assertRaises(NullPointerException):
                self.deque.putFirst(None)

    def execute(self) -> None:

        with pytest.raises(NullPointerException):
            self.deque.putLast(None)

    def execute(self) -> typing.Any:

            try:
                deque.remove()
            except NoSuchElementException:
                pass

    def execute(self) -> typing.Any:

            try:
                self.deque.removeFirst()
            except NoSuchElementException:
                pass

    def execute(self) -> None:

            self.deque.removeFirst()
            self.deque.removeFirst()

    def execute(self) -> typing.Any:

            with pytest.raises(NoSuchElementException):
                self.deque.removeLast()

    def execute(self) -> None:

            deque.removeLast()
            deque.removeLast()

    # Class Methods End


