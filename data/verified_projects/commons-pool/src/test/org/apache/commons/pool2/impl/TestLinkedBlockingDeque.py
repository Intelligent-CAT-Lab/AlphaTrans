import pytest

from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *
import unittest
from datetime import timedelta
import sys
import asyncio
from functools import wraps
import signal

class TestLinkedBlockingDeque(unittest.TestCase):

    __TIMEOUT_50_MILLIS = timedelta(milliseconds=50)
    __ONE = 1
    __TWO = 2
    __THREE = 3


    def timeout(seconds):
        def decorator(func):
            def _handle_timeout(signum, frame):
                raise TimeoutError(f"Test timed out after {seconds} seconds")

            @wraps(func)
            def wrapper(*args, **kwargs):
                signal.signal(signal.SIGALRM, _handle_timeout)
                signal.alarm(seconds)
                try:
                    result = func(*args, **kwargs)
                finally:
                    signal.alarm(0)
                return result

            return wrapper
        return decorator

    
    def __init__(self) -> None:
        self.deque = None

    
    def setUp(self) -> None:
        self.deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)

    
    @pytest.mark.test
    def testAdd(self) -> None:
        self.assertTrue(self.deque.add(TestLinkedBlockingDeque.__ONE))
        self.assertTrue(self.deque.add(TestLinkedBlockingDeque.__TWO))
        with self.assertRaises(RuntimeError):
            self.deque.add(TestLinkedBlockingDeque.__THREE)
        with self.assertRaises((TypeError, AttributeError)):
            self.deque.add(None)

    
    @pytest.mark.test
    def testAddFirst(self) -> None:
        self.deque.addFirst(TestLinkedBlockingDeque.__ONE)
        self.deque.addFirst(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(TestLinkedBlockingDeque.__THREE)
        self.assertEqual(2, self.deque.pop())

    
    @pytest.mark.test
    def testAddLast(self) -> None:
        self.deque.addLast(TestLinkedBlockingDeque.__ONE)
        self.deque.addLast(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.add(TestLinkedBlockingDeque.__THREE)
        self.assertEqual(1, self.deque.pop())

    
    @pytest.mark.test
    def testClear(self) -> None:
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.deque.clear()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.assertEqual(1, self.deque.size())

    
    @pytest.mark.test
    def testConstructors(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertEqual(sys.maxsize, deque.remainingCapacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque3(2)
        self.assertEqual(2, deque.remainingCapacity())

        deque = LinkedBlockingDeque.LinkedBlockingDeque2(
            [TestLinkedBlockingDeque.__ONE, TestLinkedBlockingDeque.__TWO]
        )
        self.assertEqual(2, deque.size())

        with self.assertRaises((TypeError, AttributeError)):
            LinkedBlockingDeque.LinkedBlockingDeque2(
                [TestLinkedBlockingDeque.__ONE, None]
            )

    
    @pytest.mark.test
    def testContains(self) -> None:
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.assertTrue(self.deque.contains(TestLinkedBlockingDeque.__ONE))
        self.assertFalse(self.deque.contains(TestLinkedBlockingDeque.__TWO))
        self.assertFalse(self.deque.contains(None))
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertTrue(self.deque.contains(TestLinkedBlockingDeque.__TWO))
        self.assertFalse(self.deque.contains(TestLinkedBlockingDeque.__THREE))

    
    @pytest.mark.test
    def testDescendingIterator(self) -> None:
        with self.assertRaises(StopIteration):
            next(self.deque.descendingIterator())
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        iter_ = ListIterator(self.deque.descendingIterator())
        self.assertEqual(2, next(iter_))
        iter_.remove()
        self.assertEqual(1, next(iter_))

    
    @pytest.mark.test
    def testDrainTo(self) -> None:
        c = []
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.drainTo(c))
        self.assertEqual(2, len(c))

        c = []
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.drainTo(c, 1))
        self.assertEqual(1, self.deque.size())
        self.assertEqual(1, len(c))
        self.assertEqual(TestLinkedBlockingDeque.__ONE, c[0])

    
    @pytest.mark.test
    def testElement(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.element()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.element())

    
    @pytest.mark.test
    def testGetFirst(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.getFirst()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.getFirst())

    
    @pytest.mark.test
    def testGetLast(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.getLast()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.getLast())

    
    @pytest.mark.test
    def testIterator(self) -> None:
        with self.assertRaises(StopIteration):
            next(self.deque.iterator())
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        iter_ = ListIterator(self.deque.iterator())
        self.assertEqual(1, next(iter_))
        iter_.remove()
        self.assertEqual(2, next(iter_))

    
    @pytest.mark.test
    def testOffer(self) -> None:
        self.assertTrue(self.deque.offer(TestLinkedBlockingDeque.__ONE))
        self.assertTrue(self.deque.offer(TestLinkedBlockingDeque.__TWO))
        self.assertFalse(self.deque.offer(TestLinkedBlockingDeque.__THREE))
        with self.assertRaises((TypeError, AttributeError)):
            self.deque.offer(None)

    
    @pytest.mark.test
    def testOfferFirst(self) -> None:
        self.deque.offerFirst(TestLinkedBlockingDeque.__ONE)
        self.deque.offerFirst(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises((TypeError, AttributeError)):
            self.deque.offerFirst(None)
        self.assertEqual(2, self.deque.pop())

    
    @pytest.mark.test
    def testOfferFirstWithTimeout(self) -> None:
        try:
            with self.assertRaises((TypeError, AttributeError)):
                self.deque.offerFirst1(None, TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS)
            self.assertTrue(
                self.deque.offerFirst1(
                    TestLinkedBlockingDeque.__ONE,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            self.assertTrue(
                self.deque.offerFirst1(
                    TestLinkedBlockingDeque.__TWO,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            self.assertFalse(
                self.deque.offerFirst1(
                    TestLinkedBlockingDeque.__THREE,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")
    
    
    @pytest.mark.test
    def testOfferLast(self) -> None:
        self.deque.offerLast(TestLinkedBlockingDeque.__ONE)
        self.deque.offerLast(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises((TypeError, AttributeError)):
            self.deque.offerLast(None)
        self.assertEqual(1, self.deque.pop())

    
    @pytest.mark.test
    def testOfferLastWithTimeout(self) -> None:
        try:
            with self.assertRaises((TypeError, AttributeError)):
                self.deque.offerLast1(None, TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS)
            self.assertTrue(
                self.deque.offerLast1(
                    TestLinkedBlockingDeque.__ONE,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            self.assertTrue(
                self.deque.offerLast1(
                    TestLinkedBlockingDeque.__TWO,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            self.assertFalse(
                self.deque.offerLast1(
                    TestLinkedBlockingDeque.__THREE,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testOfferWithTimeout(self) -> None:
        try:
            self.assertTrue(
                self.deque.offer1(
                    TestLinkedBlockingDeque.__ONE,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            self.assertTrue(
                self.deque.offer1(
                    TestLinkedBlockingDeque.__TWO,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            self.assertFalse(
                self.deque.offer1(
                    TestLinkedBlockingDeque.__THREE,
                    TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS
                )
            )
            with self.assertRaises((TypeError, AttributeError)):
                self.deque.offer1(None, TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS)
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPeek(self) -> None:
        self.assertIsNone(self.deque.peek())
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.peek())

    
    @pytest.mark.test
    def testPeekFirst(self) -> None:
        self.assertIsNone(self.deque.peekFirst())
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.peekFirst())

    
    @pytest.mark.test
    def testPeekLast(self) -> None:
        self.assertIsNone(self.deque.peekLast())
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.peekLast())

    
    @pytest.mark.test
    def testPollFirst(self) -> None:
        self.assertIsNone(self.deque.pollFirst())
        self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__ONE))
        self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__TWO))
        self.assertEqual(2, self.deque.pollFirst())

    
    @pytest.mark.test
    def testPollFirstWithTimeout(self) -> None:
        try:
            self.assertIsNone(self.deque.pollFirst())
            self.assertIsNone(
                self.deque.pollFirst1(TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS)
            )
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPollLast(self) -> None:
        self.assertIsNone(self.deque.pollLast())
        self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__ONE))
        self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__TWO))
        self.assertEqual(1, self.deque.pollLast())

    
    @pytest.mark.test
    def testPollLastWithTimeout(self) -> None:
        try:
            self.assertIsNone(self.deque.pollLast())
            self.assertIsNone(
                self.deque.pollLast1(TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS)
            )
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPollWithTimeout(self) -> None:
        try:
            self.assertIsNone(self.deque.poll1(TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS))
            self.assertIsNone(self.deque.poll1(TestLinkedBlockingDeque.__TIMEOUT_50_MILLIS))
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPop(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.pop()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.pop())
        with self.assertRaises(StopIteration):
            self.deque.pop()
            self.deque.pop()

    
    @timeout(10)
    @pytest.mark.test
    def testPossibleBug(self) -> None:
        deque = LinkedBlockingDeque.LinkedBlockingDeque0()
        for i in range(3):
            deque.add(i)

        iter_ = ListIterator(deque.iterator())
        next(iter_)

        deque.remove(1)
        deque.remove(0)
        deque.remove(2)

        next(iter_)

    
    @pytest.mark.test
    def testPush(self) -> None:
        self.deque.push(TestLinkedBlockingDeque.__ONE)
        self.deque.push(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.size())
        with self.assertRaises(RuntimeError):
            self.deque.push(TestLinkedBlockingDeque.__THREE)
        self.assertEqual(2, self.deque.pop())

    
    @pytest.mark.test
    def testPut(self) -> None:
        try:
            with self.assertRaises((TypeError, AttributeError)):
                self.deque.put(None)
            self.deque.put(TestLinkedBlockingDeque.__ONE)
            self.deque.put(TestLinkedBlockingDeque.__TWO)
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPutFirst(self) -> None:
        try:
            with self.assertRaises((TypeError, AttributeError)):
                self.deque.putFirst(None)
            self.deque.putFirst(TestLinkedBlockingDeque.__ONE)
            self.deque.putFirst(TestLinkedBlockingDeque.__TWO)
            self.assertEqual(2, self.deque.size())
            self.assertEqual(2, self.deque.pop())
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testPutLast(self) -> None:
        try:
            with self.assertRaises((TypeError, AttributeError)):
                self.deque.putLast(None)
            self.deque.putLast(TestLinkedBlockingDeque.__ONE)
            self.deque.putLast(TestLinkedBlockingDeque.__TWO)
            self.assertEqual(2, self.deque.size())
            self.assertEqual(TestLinkedBlockingDeque.__ONE, self.deque.pop())
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testRemove(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.remove()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.remove())

    
    @pytest.mark.test
    def testRemoveFirst(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.removeFirst()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(1, self.deque.removeFirst())
        with self.assertRaises(StopIteration):
            self.deque.removeFirst()
            self.deque.removeFirst()

    
    @pytest.mark.test
    def testRemoveLast(self) -> None:
        with self.assertRaises(StopIteration):
            self.deque.removeLast()
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        self.assertEqual(2, self.deque.removeLast())
        with self.assertRaises(StopIteration):
            self.deque.removeLast()
            self.deque.removeLast()

    
    @pytest.mark.test
    def testRemoveLastOccurrence(self) -> None:
        self.assertFalse(self.deque.removeLastOccurrence(None))
        self.assertFalse(self.deque.removeLastOccurrence(TestLinkedBlockingDeque.__ONE))
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.assertTrue(self.deque.removeLastOccurrence(TestLinkedBlockingDeque.__ONE))
        self.assertEqual(1, self.deque.size())

    
    @pytest.mark.test
    def testTake(self) -> None:
        try:
            self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__ONE))
            self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__TWO))
            self.assertEqual(2, self.deque.take())
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testTakeFirst(self) -> None:
        try:
            self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__ONE))
            self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__TWO))
            self.assertEqual(2, self.deque.takeFirst())
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testTakeLast(self) -> None:
        try:
            self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__ONE))
            self.assertTrue(self.deque.offerFirst(TestLinkedBlockingDeque.__TWO))
            self.assertEqual(1, self.deque.takeLast())
        except (
            InterruptedError,
            KeyboardInterrupt,
            asyncio.CancelledError,
            BlockingIOError) as e:

            self.fail(f"An exception occurred: {e}")

    
    @pytest.mark.test
    def testToArray(self) -> None:
        self.deque.add(TestLinkedBlockingDeque.__ONE)
        self.deque.add(TestLinkedBlockingDeque.__TWO)
        arr = self.deque.toArray0()
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])

        arr = self.deque.toArray1([])
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])

        arr = self.deque.toArray1([])
        self.assertEqual(1, arr[0])
        self.assertEqual(2, arr[1])



class ListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.iterator = iter(lst)
        self.last_returned = -1
        self.current_element = None

    def __iter__(self):
        return self

    def __next__(self):
        self.current_element = next(self.iterator)
        self.last_returned = self.lst.index(self.current_element)
        return self.current_element

    def remove(self):
        if self.last_returned == -1:
            raise Exception("next() has not been called yet or remove() has already been called after the last next()")
        self.lst.pop(self.last_returned)
        self.iterator = iter(self.lst)  # Reset iterator
        # Advance iterator to the current position
        for _ in range(self.last_returned):
            next(self.iterator)
        self.last_returned = -1
