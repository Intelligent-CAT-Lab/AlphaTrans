from __future__ import annotations
import time
import copy
import re
import sys
import os
import typing
from typing import *
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *

# from src.test.org.apache.commons.pool2.impl.LinkedBlockingDeque_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class LinkedBlockingDeque_ESTest(unittest.TestCase):

    def test49(self) -> None:

        linkedHashSet0 = set()
        linkedBlockingDeque0 = LinkedBlockingDeque((-2323), 0, True, linkedHashSet0)
        linkedBlockingDeque1 = LinkedBlockingDeque(
            (-3328), (-1225), True, linkedBlockingDeque0
        )
        integer0 = -1283

        with pytest.raises(RuntimeError):
            linkedBlockingDeque1.addLast(integer0)
            self.fail("Expecting exception: RuntimeError")

        verifyException(
            "org.apache.commons.pool2.impl.LinkedBlockingDeque", RuntimeError
        )

    def test48(self) -> None:

        int0 = 103
        linkedBlockingDeque0 = LinkedBlockingDeque(0, 103, True, None)

        with pytest.raises(RuntimeError):
            linkedBlockingDeque0.offerLast(None)
            self.fail("Expecting exception: RuntimeError")

    def test47(self) -> None:

        linkedBlockingDeque0 = None
        try:
            linkedBlockingDeque0 = LinkedBlockingDeque(0, 0, False, None)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test46(self) -> None:

        integer0 = Integer(2407)
        integer1 = Integer(2)
        list0 = [
            integer0,
            integer0,
            integer0,
            integer1,
            integer0,
            integer1,
            integer1,
            integer0,
            integer1,
        ]
        linkedBlockingDeque0 = LinkedBlockingDeque(4577, 0, False, list0)
        linkedBlockingDeque1 = LinkedBlockingDeque(
            5, (-663), False, linkedBlockingDeque0
        )
        boolean0 = linkedBlockingDeque1.offerLast(integer1)
        self.assertFalse(boolean0)

    def test45(self) -> None:

        linkedList0 = LinkedList()
        linkedBlockingDeque0 = LinkedBlockingDeque(
            Integer.MAX_VALUE, 1, True, linkedList0
        )
        linkedBlockingDeque1 = LinkedBlockingDeque(0, 2293, True, linkedBlockingDeque0)
        linkedBlockingDeque2 = None
        try:
            linkedBlockingDeque2 = LinkedBlockingDeque(0, 0, True, linkedBlockingDeque1)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            #
            # no message in exception (getMessage() returned null)
            #
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test44(self) -> None:

        LinkedBlockingDeque.LinkedBlockingDeque0()
        linkedList0 = LinkedList()
        linkedBlockingDeque0 = LinkedBlockingDeque(-603, 535, False, linkedList0)
        linkedBlockingDeque0.toArray0()
        linkedBlockingDeque1 = LinkedBlockingDeque(
            -603, 535, False, linkedBlockingDeque0
        )
        linkedBlockingDeque2 = LinkedBlockingDeque(
            -603, 1119, False, linkedBlockingDeque1
        )
        duration0 = Duration.ZERO
        LinkedBlockingDeque.LinkedBlockingDeque2(linkedBlockingDeque0)
        linkedBlockingDeque2.pollFirst1(duration0)
        integer0 = Integer(0)
        linkedList0.add(integer0)
        try:
            linkedBlockingDeque2.putLast(None)
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("java.util.Objects", e)

    def test43(self) -> None:

        LinkedBlockingDeque.LinkedBlockingDeque1(False)
        int0 = 4
        linkedHashSet0 = set()
        linkedBlockingDeque0 = LinkedBlockingDeque(4, 4, False, linkedHashSet0)

        try:
            linkedBlockingDeque0.pop()
            self.fail("Expecting exception: RuntimeError")

        except IndexError as e:
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test42(self) -> None:

        linkedHashSet0 = set()
        linkedBlockingDeque0 = LinkedBlockingDeque((-166), 2, True, linkedHashSet0)
        timeUnit0 = TimeUnit.HOURS
        integer0 = linkedBlockingDeque0.poll2((-639), timeUnit0)
        self.assertIsNone(integer0)

    def test41(self) -> None:

        linkedHashSet0 = set()
        linkedBlockingDeque0 = LinkedBlockingDeque(
            (-1678), (-1678), True, linkedHashSet0
        )
        linkedBlockingDeque1 = LinkedBlockingDeque(5, 0, True, linkedBlockingDeque0)
        linkedBlockingDeque2 = LinkedBlockingDeque(5, 1069, True, linkedBlockingDeque1)

        try:
            linkedBlockingDeque2.removeFirst()
            self.fail("Expecting exception: RuntimeError")

        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test40(self) -> None:

        int0 = 393
        int1 = -1
        linkedList0 = LinkedList()
        integer0 = Integer(0)
        linkedList0.removeFirstOccurrence(integer0)
        linkedBlockingDeque0 = LinkedBlockingDeque(393, -1, True, linkedList0)

        # Undeclared exception in Java code, so we'll use try-except block to handle it
        try:
            linkedBlockingDeque0.pop()
            self.fail("Expecting exception: RuntimeError")
        except RuntimeError as e:
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test39(self) -> None:

        linkedBlockingDeque0 = LinkedBlockingDeque(1029, 166, False, None)
        self.assertFalse(linkedBlockingDeque0.contains(1029))

    def test38(self) -> None:

        int0 = 0
        linkedHashSet0 = set()
        linkedBlockingDeque0 = None
        try:
            linkedBlockingDeque0 = LinkedBlockingDeque(0, -899, False, linkedHashSet0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test37(self) -> None:

        int0 = 0
        int1 = 0
        boolean0 = False
        linkedHashSet0 = set()
        linkedBlockingDeque0 = None

        try:
            linkedBlockingDeque0 = LinkedBlockingDeque(0, 0, False, linkedHashSet0)
            self.fail("Expecting exception: ValueError")

        except ValueError as e:
            verifyException("org.apache.commons.pool2.impl.LinkedBlockingDeque", e)

    def test36(self) -> None:

        int0 = 3
        integerArray0 = [None] * 8
        integer0 = Integer(-896)
        integerArray0[0] = integer0
        integer1 = Integer(3)
        integerArray0[1] = integer1
        integer2 = Integer(-3258)
        integerArray0[2] = integer2
        integer3 = Integer(0)
        integerArray0[3] = integer3
        integer4 = Integer(3)
        integerArray0[4] = integer4
        integer5 = Integer(int0)
        integerArray0[5] = integer5
        integer6 = Integer(0)
        integerArray0[6] = integer6
        integer7 = Integer(0)
        integerArray0[7] = integer7
        list0 = list(integerArray0)
        linkedBlockingDeque0 = LinkedBlockingDeque(3, 3, False, list0)
        linkedBlockingDeque0.poll0()
        timeUnit0 = TimeUnit.MINUTES
        linkedBlockingDeque0.pollLast2(long(integerArray0[2]), timeUnit0)
        linkedBlockingDeque0.putLast(integer1)
        self.assertTrue(linkedBlockingDeque0.contains(int0))

        linkedBlockingDeque0.remove0()
        objectArray0 = linkedBlockingDeque0.toArray0()
        self.assertEqual(0, len(objectArray0))

    def test35(self) -> None:

        int0 = 917
        linkedList0 = LinkedList()
        self.assertFalse(linkedList0.contains(int0))
        self.assertEqual(0, linkedList0.size())
        self.assertIsNotNone(linkedList0)

        linkedBlockingDeque0 = LinkedBlockingDeque(917, 917, True, linkedList0)
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertEqual(0, linkedList0.size())
        self.assertIsNotNone(linkedBlockingDeque0)

        timeUnit0 = TimeUnit.MILLISECONDS
        integer0 = linkedBlockingDeque0.pollLast2(371, timeUnit0)
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertEqual(0, linkedList0.size())
        self.assertIsNone(integer0)

        object0 = Object()
        self.assertIsNotNone(object0)

        boolean0 = linkedBlockingDeque0.remove1(object0)
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertFalse(boolean0)
        self.assertEqual(0, linkedList0.size())

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.removeFirst()
            verifyException(
                "org.apache.commons.pool2.impl.LinkedBlockingDeque", RuntimeError
            )

    def test34(self) -> None:

        pass  # LLM could not translate this method

    def test33(self) -> None:

        linkedHashSet0 = set()
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(1, 0, True, linkedHashSet0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertFalse(0 in linkedBlockingDeque0)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = 1
        self.assertEqual(1, integer0)
        self.assertIsNotNone(integer0)

        boolean0 = integer0 in linkedHashSet0
        self.assertTrue(integer0 in linkedHashSet0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertTrue(boolean0)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))

        boolean1 = linkedBlockingDeque0.hasTakeWaiters()
        self.assertTrue(integer0 in linkedHashSet0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertFalse(integer0 in linkedBlockingDeque0)
        self.assertFalse(boolean1)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertFalse(boolean1 == boolean0)

        boolean2 = linkedBlockingDeque0.contains(None)
        self.assertTrue(integer0 in linkedHashSet0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertFalse(integer0 in linkedBlockingDeque0)
        self.assertFalse(boolean2)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertTrue(boolean2 == boolean1)
        self.assertFalse(boolean2 == boolean0)

        boolean3 = linkedBlockingDeque0.hasTakeWaiters()
        self.assertTrue(integer0 in linkedHashSet0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertFalse(integer0 in linkedBlockingDeque0)
        self.assertFalse(boolean3)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertTrue(boolean3 == boolean2)
        self.assertFalse(boolean3 == boolean0)
        self.assertTrue(boolean3 == boolean1)

        duration0 = Duration.ZERO
        self.assertIsNotNone(duration0)

        boolean4 = linkedBlockingDeque0.offerLast1(integer0, duration0)
        self.assertTrue(integer0 in linkedHashSet0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertFalse(integer0 in linkedBlockingDeque0)
        self.assertFalse(boolean4)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertFalse(boolean4 == boolean0)
        self.assertTrue(boolean4 == boolean1)
        self.assertTrue(boolean4 == boolean2)
        self.assertTrue(boolean4 == boolean3)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.remove0()
            self.fail("Expecting exception: RuntimeError")

    def test32(self) -> None:

        linked_list0 = LinkedList()
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_list0)

        linked_blocking_deque0 = LinkedBlockingDeque(
            -2902, sys.maxsize, False, linked_list0
        )
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_blocking_deque0)

        integer0 = linked_blocking_deque0.pollLast()
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNone(integer0)

        integer1 = Integer(-2902)
        self.assertEqual(-2902, int(integer1))
        self.assertIsNotNone(integer1)

        linked_blocking_deque0.putFirst(integer1)
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(-2902))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())

        linked_blocking_deque0.addLast(integer1)
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(-2902))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())

        linked_blocking_deque0.addFirst(integer1)
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(-2902))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())

        linked_blocking_deque1 = LinkedBlockingDeque(
            sys.maxsize, 150, False, linked_list0
        )
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertFalse(linked_blocking_deque1.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque1 == linked_blocking_deque0)

        object0 = linked_blocking_deque1.pollLast0()
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertFalse(linked_blocking_deque1.contains(sys.maxsize))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque1, linked_blocking_deque0)
        self.assertIsNone(object0)
        self.assertFalse(linked_blocking_deque1 == linked_blocking_deque0)

        boolean0 = linked_blocking_deque1.removeLastOccurrence(None)
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertFalse(linked_blocking_deque1.contains(sys.maxsize))
        self.assertFalse(boolean0)
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque1, linked_blocking_deque0)
        self.assertFalse(linked_blocking_deque1 == linked_blocking_deque0)

        boolean1 = linked_blocking_deque0.contains(None)
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(integer1))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertFalse(boolean1)
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque0 == linked_blocking_deque1)
        self.assertTrue(boolean1 == boolean0)

        linked_blocking_deque2 = LinkedBlockingDeque.LinkedBlockingDeque1(True)
        self.assertIsNotNone(linked_blocking_deque2)

        integer2 = linked_blocking_deque0.poll()
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(integer1))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(-2902, int(integer2))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertIsNotNone(integer2)
        self.assertFalse(linked_blocking_deque0 == linked_blocking_deque1)

        integer3 = linked_blocking_deque0.removeFirst()
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(integer1))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertEqual(-2902, int(integer3))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertIsNotNone(integer3)
        self.assertFalse(linked_blocking_deque0 == linked_blocking_deque1)

        boolean2 = linked_blocking_deque0.offer(integer2)
        self.assertFalse(linked_list0.contains(sys.maxsize))
        self.assertTrue(linked_blocking_deque0.contains(integer1))
        self.assertFalse(linked_blocking_deque0.contains(sys.maxsize))
        self.assertTrue(boolean2)
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque0 == linked_blocking_deque1)
        self.assertFalse(boolean2 == boolean0)
        self.assertFalse(boolean2 == boolean1)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linked_blocking_deque1.removeLast()
            self.fail("Expecting exception: RuntimeError")

    def test31(self) -> None:

        linkedHashSet0 = set()
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(1359, -6730, False, linkedHashSet0)
        self.assertFalse(-6730 in linkedHashSet0)
        self.assertFalse(-6730 in linkedBlockingDeque0)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(
            1934, 183, False, linkedBlockingDeque0
        )
        self.assertFalse(183 in linkedHashSet0)
        self.assertFalse(183 in linkedBlockingDeque0)
        self.assertFalse(183 in linkedBlockingDeque1)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        integer0 = Integer(1359)
        self.assertEqual(1359, int(integer0))
        self.assertIsNotNone(integer0)

        linkedBlockingDeque1.putLast(integer0)
        self.assertFalse(-6730 in linkedHashSet0)
        self.assertFalse(-6730 in linkedBlockingDeque0)
        self.assertFalse(-6730 in linkedBlockingDeque1)
        self.assertTrue(1359 in linkedBlockingDeque1)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNot(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque0 == linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

    def test30(self) -> None:

        linkedBlockingDeque0 = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedList0 = LinkedList()
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedList0)

        linkedBlockingDeque1 = LinkedBlockingDeque(-603, 535, False, linkedList0)
        self.assertFalse(535 in linkedList0)
        self.assertFalse(535 in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque1)

        objectArray0 = linkedBlockingDeque1.toArray0()
        self.assertFalse(535 in linkedList0)
        self.assertFalse(535 in linkedBlockingDeque1)
        self.assertEqual(0, len(objectArray0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(objectArray0)

        linkedBlockingDeque2 = LinkedBlockingDeque(
            -603, 535, False, linkedBlockingDeque1
        )
        self.assertFalse(535 in linkedList0)
        self.assertFalse(535 in linkedBlockingDeque1)
        self.assertFalse(535 in linkedBlockingDeque2)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)

        linkedBlockingDeque3 = LinkedBlockingDeque(
            -603, 1119, False, linkedBlockingDeque2
        )
        self.assertFalse(535 in linkedList0)
        self.assertFalse(535 in linkedBlockingDeque1)
        self.assertFalse(535 in linkedBlockingDeque2)
        self.assertFalse(535 in linkedBlockingDeque3)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque2, linkedBlockingDeque3)

        duration0 = Duration.ZERO
        self.assertIsNotNone(duration0)

        linkedBlockingDeque4 = LinkedBlockingDeque.LinkedBlockingDeque2(
            linkedBlockingDeque1
        )
        self.assertFalse(535 in linkedList0)
        self.assertFalse(535 in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertIsNot(linkedBlockingDeque4, linkedBlockingDeque0)
        self.assertIsNotNone(linkedBlockingDeque4)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque4, linkedBlockingDeque0)

        integer0 = Integer(0)
        self.assertEqual(0, int(integer0))
        self.assertIsNotNone(integer0)

        boolean0 = linkedList0.add(integer0)
        self.assertTrue(0 in linkedList0)
        self.assertFalse(535 in linkedList0)
        self.assertTrue(boolean0)
        self.assertEqual(1, len(linkedList0))

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque3.putLast(None)

    def test29(self) -> None:

        linkedList0 = LinkedList()
        self.assertEqual(0, linkedList0.size())
        self.assertIsNotNone(linkedList0)

        linkedBlockingDeque0 = LinkedBlockingDeque(917, 917, True, linkedList0)
        self.assertFalse(linkedList0.contains(917))
        self.assertFalse(linkedBlockingDeque0.contains(917))
        self.assertEqual(0, linkedList0.size())
        self.assertIsNotNone(linkedBlockingDeque0)

        timeUnit0 = TimeUnit.MILLISECONDS
        integer0 = linkedBlockingDeque0.pollLast2(371, timeUnit0)
        self.assertFalse(linkedList0.contains(917))
        self.assertFalse(linkedBlockingDeque0.contains(917))
        self.assertEqual(0, linkedList0.size())
        self.assertIsNone(integer0)

        object0 = Object()
        self.assertIsNotNone(object0)

        boolean0 = linkedBlockingDeque0.remove1(object0)
        self.assertFalse(linkedList0.contains(917))
        self.assertFalse(linkedBlockingDeque0.contains(917))
        self.assertFalse(boolean0)
        self.assertEqual(0, linkedList0.size())

        # Undeclared exception
        with self.assertRaises(RuntimeError) as context:
            linkedBlockingDeque0.removeFirst()
        self.assertIsNone(context.exception.getMessage())
        self.verifyException(
            "org.apache.commons.pool2.impl.LinkedBlockingDeque", context.exception
        )

    def test28(self) -> None:

        linkedHashSet0 = set()
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque((-343, -343), True, linkedHashSet0)
        self.assertFalse((-343 in linkedHashSet0))
        self.assertFalse((-343 in linkedBlockingDeque0))
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(
            (-343, -1), True, linkedBlockingDeque0
        )
        self.assertFalse((-343 in linkedHashSet0))
        self.assertFalse((-343 in linkedBlockingDeque0))
        self.assertFalse((-343 in linkedBlockingDeque1))
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        int0 = linkedBlockingDeque1.drainTo1(linkedHashSet0, (-343))
        self.assertFalse((-343 in linkedHashSet0))
        self.assertFalse((-343 in linkedBlockingDeque0))
        self.assertFalse((-343 in linkedBlockingDeque1))
        self.assertEqual((-343), int0)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNot(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque0 == linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

    def test27(self) -> None:

        int0 = 0
        int1 = 2
        boolean0 = False
        int2 = 25
        linkedBlockingDeque0 = LinkedBlockingDeque(2, 25, True, None)
        self.assertFalse(linkedBlockingDeque0.contains(int2))
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(25, 0, True, linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertFalse(linkedBlockingDeque1.contains(int0))
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque0)

        stream0 = linkedBlockingDeque1.stream()
        self.assertIsNotNone(stream0)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque0)

        integer0 = Integer(1531)
        self.assertEqual(1531, integer0)
        self.assertIsNotNone(integer0)
        self.assertNotEqual(integer0, int2)
        self.assertNotEqual(integer0, int0)
        self.assertNotEqual(integer0, int1)

        boolean1 = linkedBlockingDeque0.contains(integer0)
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertFalse(boolean1)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertFalse(integer0 == int2)
        self.assertFalse(integer0 == int0)
        self.assertFalse(integer0 == int1)
        self.assertTrue(boolean1 == boolean0)

        integer1 = None
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque1.offerFirst(None)

    def test26(self) -> None:

        pass  # LLM could not translate this method

    def test25(self) -> None:

        linked_list0 = LinkedList()
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_list0)

        linked_blocking_deque0 = LinkedBlockingDeque(917, 917, True, linked_list0)
        self.assertFalse(linked_list0.contains(917))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_blocking_deque0)

        linked_hash_set0 = LinkedHashSet()
        self.assertFalse(linked_hash_set0.contains(917))
        self.assertTrue(linked_hash_set0.isEmpty())
        self.assertEqual(0, linked_hash_set0.size())
        self.assertIsNotNone(linked_hash_set0)

        linked_blocking_deque1 = LinkedBlockingDeque(917, 917, True, linked_hash_set0)
        self.assertFalse(linked_hash_set0.contains(917))
        self.assertFalse(linked_blocking_deque1.contains(917))
        self.assertTrue(linked_hash_set0.isEmpty())
        self.assertEqual(0, linked_hash_set0.size())
        self.assertIsNotNone(linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque1.equals(linked_blocking_deque0))

        integer0 = Integer(917)
        self.assertEqual(917, int(integer0))
        self.assertIsNotNone(integer0)

        boolean0 = linked_hash_set0.add(integer0)
        self.assertTrue(linked_hash_set0.contains(917))
        self.assertTrue(boolean0)
        self.assertEqual(1, linked_hash_set0.size())
        self.assertFalse(linked_hash_set0.isEmpty())

        boolean1 = linked_blocking_deque0.hasTakeWaiters()
        self.assertFalse(linked_list0.contains(917))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertFalse(boolean1)
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque0.equals(linked_blocking_deque1))
        self.assertFalse(boolean1 == boolean0)

        boolean2 = linked_blocking_deque0.contains(integer0)
        self.assertFalse(linked_list0.contains(917))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertFalse(boolean2)
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque0.equals(linked_blocking_deque1))
        self.assertTrue(boolean2 == boolean1)
        self.assertFalse(boolean2 == boolean0)

        boolean3 = linked_blocking_deque0.hasTakeWaiters()
        self.assertFalse(linked_list0.contains(917))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertFalse(boolean3)
        self.assertEqual(0, linked_list0.size())
        self.assertIsNot(linked_blocking_deque0, linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque0.equals(linked_blocking_deque1))
        self.assertTrue(boolean3 == boolean1)
        self.assertFalse(boolean3 == boolean0)
        self.assertTrue(boolean3 == boolean2)

        duration0 = Duration.ZERO
        self.assertIsNotNone(duration0)

        boolean4 = linked_blocking_deque1.offerLast1(integer0, duration0)
        self.assertTrue(linked_hash_set0.contains(917))
        self.assertTrue(linked_blocking_deque1.contains(917))
        self.assertTrue(boolean4)
        self.assertEqual(1, linked_hash_set0.size())
        self.assertFalse(linked_hash_set0.isEmpty())
        self.assertIsNot(linked_blocking_deque1, linked_blocking_deque0)
        self.assertFalse(linked_blocking_deque1.equals(linked_blocking_deque0))
        self.assertFalse(boolean4 == boolean1)
        self.assertFalse(boolean4 == boolean2)
        self.assertFalse(boolean4 == boolean3)
        self.assertTrue(boolean4 == boolean0)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linked_blocking_deque0.remove0()
            self.fail("Expecting exception: RuntimeError")

    def test24(self) -> None:

        linked_hash_set0 = LinkedHashSet(4, 1827.0)
        self.assertFalse(linked_hash_set0.contains(4))
        self.assertTrue(linked_hash_set0.is_empty())
        self.assertEqual(0, linked_hash_set0.size())
        self.assertIsNotNone(linked_hash_set0)

        linked_blocking_deque0 = LinkedBlockingDeque(-2539, -1, False, linked_hash_set0)
        self.assertFalse(linked_hash_set0.contains(-2539))
        self.assertFalse(linked_blocking_deque0.contains(-2539))
        self.assertTrue(linked_hash_set0.is_empty())
        self.assertEqual(0, linked_hash_set0.size())
        self.assertIsNotNone(linked_blocking_deque0)

        linked_blocking_deque1 = LinkedBlockingDeque(4, 4, True, linked_blocking_deque0)
        self.assertFalse(linked_hash_set0.contains(-2539))
        self.assertFalse(linked_blocking_deque0.contains(-2539))
        self.assertFalse(linked_blocking_deque1.contains(-2539))
        self.assertTrue(linked_hash_set0.is_empty())
        self.assertEqual(0, linked_hash_set0.size())
        self.assertIsNotNone(linked_blocking_deque1)
        self.assertFalse(linked_blocking_deque1.equals(linked_blocking_deque0))

        linked_blocking_deque2 = LinkedBlockingDeque(4, 4, True, linked_blocking_deque1)
        self.assertFalse(linked_hash_set0.contains(4))
        self.assertFalse(linked_blocking_deque0.contains(4))
        self.assertFalse(linked_blocking_deque1.contains(4))
        self.assertFalse(linked_blocking_deque2.contains(4))
        self.assertTrue(linked_hash_set0.is_empty())
        self.assertEqual(0, linked_hash_set0.size())
        self.assertIsNotNone(linked_blocking_deque2)
        self.assertFalse(linked_blocking_deque0.equals(linked_blocking_deque1))
        self.assertFalse(linked_blocking_deque1.equals(linked_blocking_deque0))
        self.assertFalse(linked_blocking_deque2.equals(linked_blocking_deque0))
        self.assertFalse(linked_blocking_deque2.equals(linked_blocking_deque1))

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linked_blocking_deque2.offer_last0(None)

    def test23(self) -> None:

        int0 = 1
        linkedBlockingDeque0 = LinkedBlockingDeque(1, 7, False, None)
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = None
        integer1 = Integer(2155)
        self.assertEqual(2155, int(integer1))
        self.assertIsNotNone(integer1)
        self.assertFalse(integer1 == int0)

        timeUnit0 = TimeUnit.DAYS
        boolean0 = linkedBlockingDeque0.offerLast2(integer1, 7, timeUnit0)
        self.assertTrue(linkedBlockingDeque0.contains(integer1))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertTrue(boolean0)
        self.assertFalse(integer1 == int0)

        int1 = linkedBlockingDeque0.size()
        self.assertTrue(linkedBlockingDeque0.contains(integer1))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertEqual(1, int1)
        self.assertTrue(int1 == int0)

        spliterator0 = linkedBlockingDeque0.spliterator()
        self.assertTrue(linkedBlockingDeque0.contains(integer1))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertIsNotNone(spliterator0)

        duration0 = Duration.ofDays(1665)
        self.assertIsNotNone(duration0)

        duration1 = Duration.ofSeconds(1665, 1885)
        self.assertIsNot(duration1, duration0)
        self.assertIsNotNone(duration1)
        self.assertNotEqual(duration1, duration0)

        duration2 = duration1.plusMillis(2288)
        self.assertIsNot(duration1, duration0)
        self.assertIsNot(duration1, duration2)
        self.assertIsNot(duration2, duration0)
        self.assertIsNot(duration2, duration1)
        self.assertIsNotNone(duration2)
        self.assertNotEqual(duration1, duration0)
        self.assertNotEqual(duration2, duration0)
        self.assertNotEqual(duration2, duration1)

        duration3 = duration1.abs()
        self.assertIsNot(duration1, duration0)
        self.assertIs(duration1, duration3)
        self.assertIsNot(duration1, duration2)
        self.assertIsNot(duration3, duration2)
        self.assertIs(duration3, duration1)
        self.assertIsNot(duration3, duration0)
        self.assertIsNotNone(duration3)
        self.assertNotEqual(duration1, duration0)
        self.assertNotEqual(duration1, duration2)
        self.assertNotEqual(duration3, duration2)
        self.assertNotEqual(duration3, duration0)

        duration4 = duration0.minus(duration1)
        self.assertIsNot(duration0, duration2)
        self.assertIsNot(duration0, duration4)
        self.assertIsNot(duration0, duration3)
        self.assertIsNot(duration0, duration1)
        self.assertIsNot(duration1, duration0)
        self.assertIs(duration1, duration3)
        self.assertIsNot(duration1, duration2)
        self.assertIsNot(duration1, duration4)
        self.assertIsNot(duration4, duration2)
        self.assertIsNot(duration4, duration0)
        self.assertIsNot(duration4, duration1)
        self.assertIsNot(duration4, duration3)
        self.assertIsNotNone(duration4)
        self.assertNotEqual(duration0, duration2)
        self.assertNotEqual(duration0, duration3)
        self.assertNotEqual(duration0, duration1)
        self.assertNotEqual(duration1, duration0)
        self.assertNotEqual(duration1, duration2)
        self.assertNotEqual(duration4, duration2)
        self.assertNotEqual(duration4, duration0)
        self.assertNotEqual(duration4, duration1)
        self.assertNotEqual(duration4, duration3)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.offer1(None, duration0)
            self.fail("Expecting exception: RuntimeError")

    def test22(self) -> None:

        linkedBlockingDeque0 = LinkedBlockingDeque(1, 7, False, None)
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = Integer(2155)
        self.assertEqual(2155, int(integer0))
        self.assertIsNotNone(integer0)

        timeUnit0 = TimeUnit.DAYS
        boolean0 = linkedBlockingDeque0.offerLast2(integer0, 7, timeUnit0)
        self.assertTrue(linkedBlockingDeque0.contains(integer0))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertTrue(boolean0)

        int0 = linkedBlockingDeque0.size()
        self.assertTrue(linkedBlockingDeque0.contains(integer0))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertEqual(1, int0)

        spliterator0 = linkedBlockingDeque0.spliterator()
        self.assertTrue(linkedBlockingDeque0.contains(integer0))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertIsNotNone(spliterator0)

        duration0 = Duration.ofSeconds(1665, 1885)
        self.assertIsNotNone(duration0)

        duration1 = duration0.plusMillis(2288)
        self.assertIsNot(duration0, duration1)
        self.assertIsNot(duration1, duration0)
        self.assertIsNotNone(duration1)
        self.assertFalse(duration1.equals(duration0))

        duration2 = duration0.abs()
        self.assertIsNot(duration0, duration1)
        self.assertIs(duration0, duration2)
        self.assertIs(duration2, duration0)
        self.assertIsNot(duration2, duration1)
        self.assertIsNotNone(duration2)
        self.assertFalse(duration0.equals(duration1))
        self.assertFalse(duration2.equals(duration1))

        integer1 = Integer(1)
        self.assertEqual(1, int(integer1))
        self.assertIsNotNone(integer1)
        self.assertTrue(integer1.equals(int0))
        self.assertFalse(integer1.equals(integer0))

        timeUnit1 = TimeUnit.NANOSECONDS
        integer2 = Integer(0)
        self.assertEqual(0, int(integer2))
        self.assertIsNotNone(integer2)
        self.assertFalse(integer2.equals(integer0))
        self.assertFalse(integer2.equals(int0))
        self.assertFalse(integer2.equals(integer1))

        boolean1 = linkedBlockingDeque0.offer(integer2)
        self.assertTrue(linkedBlockingDeque0.contains(integer2))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertTrue(boolean1)
        self.assertFalse(integer2.equals(integer0))
        self.assertFalse(integer2.equals(int0))
        self.assertFalse(integer2.equals(integer1))
        self.assertTrue(boolean1 == boolean0)

        integer3 = Integer(0)
        self.assertEqual(0, int(integer3))
        self.assertIsNotNone(integer3)
        self.assertFalse(integer3.equals(integer0))
        self.assertFalse(integer3.equals(int0))
        self.assertFalse(integer3.equals(integer1))
        self.assertTrue(integer3.equals(integer2))

        linkedBlockingDeque0.putFirst(integer3)
        self.assertTrue(linkedBlockingDeque0.contains(0))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertFalse(integer3.equals(integer0))
        self.assertFalse(integer3.equals(int0))
        self.assertFalse(integer3.equals(integer1))
        self.assertTrue(integer3.equals(integer2))

        boolean2 = linkedBlockingDeque0.offerFirst2(integer1, 0, timeUnit1)
        self.assertTrue(linkedBlockingDeque0.contains(0))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertTrue(boolean2)
        self.assertIsNot(timeUnit1, timeUnit0)
        self.assertTrue(integer1.equals(int0))
        self.assertFalse(integer1.equals(integer3))
        self.assertFalse(integer1.equals(integer2))
        self.assertFalse(integer1.equals(integer0))
        self.assertFalse(timeUnit1.equals(timeUnit0))
        self.assertTrue(boolean2 == boolean1)
        self.assertTrue(boolean2 == boolean0)

        linkedBlockingDeque0.interuptTakeWaiters()
        self.assertTrue(linkedBlockingDeque0.contains(0))
        self.assertFalse(linkedBlockingDeque0.contains(7))

        linkedBlockingDeque0.putLast(integer2)
        self.assertTrue(linkedBlockingDeque0.contains(0))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertTrue(integer2.equals(integer3))
        self.assertFalse(integer2.equals(integer0))
        self.assertFalse(integer2.equals(int0))
        self.assertFalse(integer2.equals(integer1))

        integer4 = linkedBlockingDeque0.removeLast()
        self.assertTrue(linkedBlockingDeque0.contains(integer4))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertEqual(0, int(integer4))
        self.assertIsNotNone(integer4)
        self.assertTrue(integer4.equals(integer3))
        self.assertFalse(integer4.equals(int0))
        self.assertFalse(integer4.equals(integer1))
        self.assertFalse(integer4.equals(integer0))

        integerArray0 = [None] * 4
        integerArray0[0] = integer0
        integerArray0[1] = integer0
        integerArray0[2] = None
        integerArray0[3] = integer4
        integerArray1 = linkedBlockingDeque0.toArray1(integerArray0)
        self.assertTrue(linkedBlockingDeque0.contains(integer4))
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertEqual(4, len(integerArray0))
        self.assertEqual(4, len(integerArray1))
        self.assertIs(integerArray0, integerArray1)
        self.assertIs(integerArray1, integerArray0)
        self.assertIsNotNone(integerArray1)

    def test21(self) -> None:

        int0 = 1
        linkedBlockingDeque0 = LinkedBlockingDeque(1, 7, False, None)
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = Integer(2155)
        self.assertEqual(2155, int(integer0))
        self.assertIsNotNone(integer0)
        self.assertFalse(integer0.equals(int0))

        timeUnit0 = TimeUnit.DAYS
        boolean0 = linkedBlockingDeque0.offerLast2(integer0, 7, timeUnit0)
        self.assertTrue(linkedBlockingDeque0.contains(2155))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertTrue(boolean0)
        self.assertFalse(integer0.equals(int0))

        int1 = linkedBlockingDeque0.size()
        self.assertTrue(linkedBlockingDeque0.contains(2155))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertEqual(1, int1)
        self.assertTrue(int1 == int0)

        spliterator0 = linkedBlockingDeque0.spliterator()
        self.assertTrue(linkedBlockingDeque0.contains(2155))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertIsNotNone(spliterator0)

        duration0 = Duration.ofDays(1665)
        self.assertIsNotNone(duration0)

        duration1 = Duration.ofSeconds(1665, 1885)
        self.assertIsNot(duration1, duration0)
        self.assertIsNotNone(duration1)
        self.assertFalse(duration1.equals(duration0))

        duration2 = duration1.plusMillis(2288)
        self.assertIsNot(duration1, duration2)
        self.assertIsNot(duration1, duration0)
        self.assertIsNot(duration2, duration0)
        self.assertIsNot(duration2, duration1)
        self.assertIsNotNone(duration2)
        self.assertFalse(duration1.equals(duration0))
        self.assertFalse(duration2.equals(duration0))
        self.assertFalse(duration2.equals(duration1))

        duration3 = duration1.abs()
        self.assertIsNot(duration1, duration2)
        self.assertIs(duration1, duration3)
        self.assertIsNot(duration1, duration0)
        self.assertIsNot(duration3, duration0)
        self.assertIs(duration3, duration1)
        self.assertIsNot(duration3, duration2)
        self.assertIsNotNone(duration3)
        self.assertFalse(duration1.equals(duration2))
        self.assertFalse(duration1.equals(duration0))
        self.assertFalse(duration3.equals(duration0))
        self.assertFalse(duration3.equals(duration2))

        duration4 = duration0.minus(duration1)
        self.assertIsNot(duration0, duration1)
        self.assertIsNot(duration0, duration4)
        self.assertIsNot(duration0, duration3)
        self.assertIsNot(duration0, duration2)
        self.assertIsNot(duration1, duration2)
        self.assertIs(duration1, duration3)
        self.assertIsNot(duration1, duration4)
        self.assertIsNot(duration1, duration0)
        self.assertIsNot(duration4, duration3)
        self.assertIsNot(duration4, duration0)
        self.assertIsNot(duration4, duration1)
        self.assertIsNot(duration4, duration2)
        self.assertIsNotNone(duration4)
        self.assertFalse(duration0.equals(duration1))
        self.assertFalse(duration0.equals(duration3))
        self.assertFalse(duration0.equals(duration2))
        self.assertFalse(duration1.equals(duration2))
        self.assertFalse(duration1.equals(duration0))
        self.assertFalse(duration4.equals(duration3))
        self.assertFalse(duration4.equals(duration0))
        self.assertFalse(duration4.equals(duration1))
        self.assertFalse(duration4.equals(duration2))

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.offer1(None, duration0)
            self.fail("Expecting exception: RuntimeError")

    def test20(self) -> None:

        linkedHashSet0 = set()
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(2359, 1, False, linkedHashSet0)
        self.assertFalse(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        int0 = 0
        # Undeclared exception in Java code
        with self.assertRaises(RuntimeError) as context:
            linkedBlockingDeque0.removeLast()
        self.assertTrue("Expecting exception: RuntimeError" in str(context.exception))
        self.assertTrue(
            "org.apache.commons.pool2.impl.LinkedBlockingDeque"
            in str(context.exception)
        )

    def test19(self) -> None:

        int0 = 5
        linkedList0 = LinkedList()
        self.assertFalse(linkedList0.contains(int0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedList0)

        linkedBlockingDeque0 = LinkedBlockingDeque(5, 5, False, linkedList0)
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque0)

        duration0 = Duration.ofMinutes(0)
        self.assertIsNotNone(duration0)

        int1 = duration0.toSecondsPart()
        self.assertEqual(0, int1)
        self.assertFalse(int1 == int0)

        integer0 = linkedBlockingDeque0.poll1(duration0)
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNone(integer0)

        stream0 = linkedBlockingDeque0.parallelStream()
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(stream0)

        int2 = 2412
        # Undeclared exception in Java code
        with self.assertRaises(IndexOutOfBoundsException):
            linkedList0.remove(2412)

    def test18(self) -> None:

        linked_hash_set0 = set()
        self.assertEqual(0, len(linked_hash_set0))
        self.assertTrue(not linked_hash_set0)
        self.assertIsNotNone(linked_hash_set0)

        linked_blocking_deque0 = LinkedBlockingDeque(-1, -1, True, linked_hash_set0)
        self.assertFalse((-1) in linked_hash_set0)
        self.assertFalse((-1) in linked_blocking_deque0)
        self.assertEqual(0, len(linked_hash_set0))
        self.assertTrue(not linked_hash_set0)
        self.assertIsNotNone(linked_blocking_deque0)

        integer0 = -1
        self.assertEqual(-1, integer0)
        self.assertIsNotNone(integer0)

        boolean0 = integer0 in linked_hash_set0
        self.assertTrue(integer0 in linked_hash_set0)
        self.assertTrue(boolean0)
        self.assertFalse(not linked_hash_set0)
        self.assertEqual(1, len(linked_hash_set0))

        linked_blocking_deque0.clear()
        self.assertTrue(integer0 in linked_hash_set0)
        self.assertFalse(integer0 in linked_blocking_deque0)
        self.assertFalse(not linked_hash_set0)
        self.assertEqual(1, len(linked_hash_set0))

        linked_blocking_deque0.clear()
        self.assertTrue(integer0 in linked_hash_set0)
        self.assertFalse(integer0 in linked_blocking_deque0)
        self.assertFalse(not linked_hash_set0)
        self.assertEqual(1, len(linked_hash_set0))

        integer1 = -1
        self.assertEqual(-1, integer1)
        self.assertIsNotNone(integer1)
        self.assertTrue(integer1 == integer0)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linked_blocking_deque0.addLast(integer1)
            self.fail("Expecting exception: RuntimeError")

    def test17(self) -> None:

        int0 = 2969
        linkedHashSet0 = set()
        self.assertFalse(int0 in linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(2969, 2969, False, linkedHashSet0)
        self.assertFalse(2969 in linkedHashSet0)
        self.assertFalse(2969 in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = int(1)
        self.assertEqual(1, integer0)
        self.assertIsNotNone(integer0)
        self.assertFalse(integer0 == int0)

        boolean0 = integer0 in linkedHashSet0
        self.assertTrue(integer0 in linkedHashSet0)
        self.assertFalse(2969 in linkedHashSet0)
        self.assertTrue(boolean0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertTrue(linkedHashSet0)
        self.assertFalse(integer0 == int0)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.getLast()
            self.fail("Expecting exception: RuntimeError")

    def test16(self) -> None:

        pass  # LLM could not translate this method

    def test15(self) -> None:

        pass  # LLM could not translate this method

    def test14(self) -> None:

        linkedHashSet0 = set()
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque((-948), (-262), True, linkedHashSet0)
        self.assertFalse((-262) in linkedHashSet0)
        self.assertFalse((-262) in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(1, 1, True, linkedBlockingDeque0)
        self.assertFalse(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertFalse(1 in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        integerArray0 = [None] * 2
        integer0 = Integer(0)
        self.assertEqual(0, integer0)
        self.assertIsNotNone(integer0)

        integerArray0[0] = integer0
        integer1 = Integer((-2340))
        self.assertEqual((-2340), integer1)
        self.assertIsNotNone(integer1)
        self.assertFalse(integer1 == integer0)

        integerArray0[1] = integer1
        integerArray1 = list(linkedHashSet0) + integerArray0[len(linkedHashSet0) :]
        self.assertFalse(1 in linkedHashSet0)
        self.assertEqual(2, len(integerArray0))
        self.assertEqual(2, len(integerArray1))
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIs(integerArray0, integerArray1)
        self.assertIs(integerArray1, integerArray0)
        self.assertIsNotNone(integerArray1)

        integer2 = Integer((-1729))
        self.assertEqual((-1729), integer2)
        self.assertIsNotNone(integer2)
        self.assertFalse(integer2 == integer0)
        self.assertFalse(integer2 == integer1)

        linkedBlockingDeque1.put(integer2)
        self.assertFalse(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertFalse(1 in linkedBlockingDeque1)
        self.assertTrue((-1729) in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNot(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque0 == linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)
        self.assertFalse(integer2 == integer0)
        self.assertFalse(integer2 == integer1)

        # Undeclared exception in Python 3.10
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.removeFirst()

    def test13(self) -> None:

        linkedList0 = LinkedList()
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedList0)

        linkedHashSet0 = LinkedHashSet(linkedList0)
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(399, -2079, False, linkedHashSet0)
        self.assertFalse(399 in linkedList0)
        self.assertFalse(399 in linkedHashSet0)
        self.assertFalse(399 in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        int0 = linkedBlockingDeque0.remainingCapacity()
        self.assertFalse(399 in linkedList0)
        self.assertFalse(399 in linkedHashSet0)
        self.assertFalse(399 in linkedBlockingDeque0)
        self.assertEqual(-2079, int0)
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)

    def test12(self) -> None:

        pass  # LLM could not translate this method

    def test11(self) -> None:

        linkedHashSet0 = set()
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(4, 1286, True, linkedHashSet0)
        self.assertFalse(4 in linkedHashSet0)
        self.assertFalse(4 in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(1286, 3, True, linkedBlockingDeque0)
        self.assertFalse(4 in linkedHashSet0)
        self.assertFalse(4 in linkedBlockingDeque0)
        self.assertFalse(4 in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        int0 = linkedBlockingDeque0.drainTo1(linkedBlockingDeque1, 0)
        self.assertFalse(3 in linkedHashSet0)
        self.assertFalse(3 in linkedBlockingDeque0)
        self.assertFalse(3 in linkedBlockingDeque1)
        self.assertEqual(0, int0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNot(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque0 == linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        integer0 = linkedBlockingDeque1.peekFirst()
        self.assertFalse(3 in linkedHashSet0)
        self.assertFalse(3 in linkedBlockingDeque0)
        self.assertFalse(3 in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNot(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertIsNone(integer0)
        self.assertFalse(linkedBlockingDeque0 == linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

    def test10(self) -> None:

        pass  # LLM could not translate this method

    def test09(self) -> None:

        linkedBlockingDeque0 = LinkedBlockingDeque.LinkedBlockingDeque0()
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedList0 = LinkedList()
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedList0)

        linkedBlockingDeque1 = LinkedBlockingDeque(-603, 535, False, linkedList0)
        self.assertNotIn(-603, linkedList0)
        self.assertNotIn(-603, linkedBlockingDeque1)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque1)

        objectArray0 = linkedBlockingDeque1.toArray0()
        self.assertNotIn(-603, linkedList0)
        self.assertNotIn(-603, linkedBlockingDeque1)
        self.assertEqual(0, len(objectArray0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(objectArray0)

        linkedBlockingDeque2 = LinkedBlockingDeque(
            -603, 535, False, linkedBlockingDeque1
        )
        self.assertNotIn(535, linkedList0)
        self.assertNotIn(535, linkedBlockingDeque1)
        self.assertNotIn(535, linkedBlockingDeque2)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)

        linkedBlockingDeque3 = LinkedBlockingDeque(
            -603, 1119, False, linkedBlockingDeque2
        )
        self.assertNotIn(535, linkedList0)
        self.assertNotIn(535, linkedBlockingDeque1)
        self.assertNotIn(535, linkedBlockingDeque2)
        self.assertNotIn(535, linkedBlockingDeque3)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque2, linkedBlockingDeque3)

        duration0 = Duration.ZERO
        self.assertIsNotNone(duration0)

        linkedBlockingDeque4 = LinkedBlockingDeque.LinkedBlockingDeque2(
            linkedBlockingDeque1
        )
        self.assertNotIn(535, linkedList0)
        self.assertNotIn(535, linkedBlockingDeque1)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertIsNot(linkedBlockingDeque4, linkedBlockingDeque0)
        self.assertIsNotNone(linkedBlockingDeque4)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque4, linkedBlockingDeque0)

        integer0 = linkedBlockingDeque3.pollFirst1(duration0)
        self.assertNotIn(535, linkedList0)
        self.assertNotIn(535, linkedBlockingDeque1)
        self.assertNotIn(535, linkedBlockingDeque2)
        self.assertNotIn(535, linkedBlockingDeque3)
        self.assertEqual(0, len(linkedList0))
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertIsNot(linkedBlockingDeque2, linkedBlockingDeque3)
        self.assertIsNot(linkedBlockingDeque2, linkedBlockingDeque1)
        self.assertIsNot(linkedBlockingDeque3, linkedBlockingDeque2)
        self.assertIsNot(linkedBlockingDeque3, linkedBlockingDeque1)
        self.assertIsNone(integer0)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque2, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque2, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque3, linkedBlockingDeque2)
        self.assertNotEqual(linkedBlockingDeque3, linkedBlockingDeque1)

        integer1 = None
        integer2 = Integer(0)
        self.assertEqual(0, int(integer2))
        self.assertIsNotNone(integer2)

        boolean0 = linkedList0.add(integer2)
        self.assertNotIn(535, linkedList0)
        self.assertIn(integer2, linkedList0)
        self.assertTrue(boolean0)
        self.assertEqual(1, len(linkedList0))

        integer3 = linkedBlockingDeque1.pollFirst1(duration0)
        self.assertNotIn(535, linkedList0)
        self.assertIn(integer2, linkedList0)
        self.assertNotIn(535, linkedBlockingDeque1)
        self.assertEqual(1, len(linkedList0))
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque2)
        self.assertIsNone(integer3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque3)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque2)

        timeUnit0 = TimeUnit.MILLISECONDS
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque1.offerFirst2(None, -1, timeUnit0)

    def test08(self) -> None:

        int0 = -626
        linkedHashSet0 = set()
        self.assertFalse(int0 in linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque((-626), 2302, True, linkedHashSet0)
        self.assertFalse((-626) in linkedHashSet0)
        self.assertFalse((-626) in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedHashSet1 = set(linkedBlockingDeque0)
        self.assertFalse((-626) in linkedHashSet0)
        self.assertFalse((-626) in linkedBlockingDeque0)
        self.assertFalse((-626) in linkedHashSet1)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertTrue(not linkedHashSet1)
        self.assertEqual(0, len(linkedHashSet1))
        self.assertIsNotNone(linkedHashSet1)
        self.assertTrue(linkedHashSet1 == linkedHashSet0)

        boolean0 = all(item in linkedBlockingDeque0 for item in linkedHashSet1)
        self.assertFalse((-626) in linkedHashSet0)
        self.assertFalse((-626) in linkedBlockingDeque0)
        self.assertFalse((-626) in linkedHashSet1)
        self.assertTrue(boolean0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertTrue(not linkedHashSet1)
        self.assertEqual(0, len(linkedHashSet1))
        self.assertIsNot(linkedHashSet0, linkedHashSet1)
        self.assertIsNot(linkedHashSet1, linkedHashSet0)
        self.assertTrue(linkedHashSet0 == linkedHashSet1)
        self.assertTrue(linkedHashSet1 == linkedHashSet0)

        integer0 = None
        duration0 = timedelta(hours=2302)
        self.assertIsNotNone(duration0)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.offerFirst1(None, duration0)

    def test07(self) -> None:

        int0 = 183
        linkedBlockingDeque0 = LinkedBlockingDeque(1828, -948, False, None)
        self.assertFalse(linkedBlockingDeque0.contains(1828))
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = linkedBlockingDeque0.pollLast0()
        self.assertFalse(linkedBlockingDeque0.contains(1828))
        self.assertIsNone(integer0)

        int1 = 1103
        linkedBlockingDeque1 = LinkedBlockingDeque(1103, 1, False, None)
        self.assertFalse(linkedBlockingDeque1.contains(1))
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        int2 = 4
        integer1 = Integer(4)
        self.assertEqual(4, int(integer1))
        self.assertIsNotNone(integer1)
        self.assertFalse(integer1 == int0)
        self.assertFalse(integer1 == int1)
        self.assertTrue(integer1 == int2)

        with self.assertRaises(RuntimeError):
            linkedBlockingDeque1.offer(None)
            verifyException("java.util.Objects", RuntimeError)

    def test06(self) -> None:

        linkedHashSet0 = set()
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(-166, 2, True, linkedHashSet0)
        self.assertFalse((-166) in linkedHashSet0)
        self.assertFalse((-166) in linkedBlockingDeque0)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque0)

        int0 = sys.maxsize
        linkedBlockingDeque1 = LinkedBlockingDeque(
            2, sys.maxsize, False, linkedHashSet0
        )
        self.assertFalse(2 in linkedHashSet0)
        self.assertFalse(2 in linkedBlockingDeque1)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)

        integer0 = Integer(-1534)
        self.assertEqual(-1534, int(integer0))
        self.assertIsNotNone(integer0)
        self.assertFalse(integer0 == int0)

        boolean0 = linkedBlockingDeque1.add(integer0)
        self.assertFalse(2 in linkedHashSet0)
        self.assertFalse(2 in linkedBlockingDeque1)
        self.assertTrue(integer0 in linkedBlockingDeque1)
        self.assertTrue(boolean0)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNot(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque1 == linkedBlockingDeque0)
        self.assertFalse(integer0 == int0)

        int1 = 903
        integer1 = Integer(903)
        self.assertEqual(903, int(integer1))
        self.assertIsNotNone(integer1)
        self.assertFalse(integer1 == int0)
        self.assertTrue(integer1 == int1)
        self.assertFalse(integer1 == integer0)

        linkedBlockingDeque2 = LinkedBlockingDeque(2, -13, True, linkedHashSet0)
        self.assertFalse(int1 in linkedHashSet0)
        self.assertFalse(int1 in linkedBlockingDeque2)
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertIsNotNone(linkedBlockingDeque2)
        self.assertFalse(linkedBlockingDeque2 == linkedBlockingDeque0)
        self.assertFalse(linkedBlockingDeque2 == linkedBlockingDeque1)

        integer2 = Integer(1)
        self.assertEqual(1, int(integer2))
        self.assertIsNotNone(integer2)
        self.assertFalse(integer2 == int0)
        self.assertFalse(integer2 == integer1)
        self.assertFalse(integer2 == integer0)
        self.assertFalse(integer2 == int1)

        chronoUnit0 = ChronoUnit.DECADES
        self.assertEqual(ChronoUnit.DECADES, chronoUnit0)

        # Undeclared exception
        try:
            Duration.of(sys.maxsize, chronoUnit0)
            self.fail("Expecting exception: UnsupportedTemporalTypeException")

        except UnsupportedTemporalTypeException as e:
            # Unit must not have an estimated duration
            self.verifyException("java.time.Duration", e)

    def test05(self) -> None:

        linked_list0 = LinkedList()
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_list0)

        linked_blocking_deque0 = LinkedBlockingDeque(917, 917, True, linked_list0)
        self.assertFalse(linked_list0.contains(917))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(linked_blocking_deque0)

        time_unit0 = TimeUnit.MILLISECONDS
        integer0 = Integer(-1800)
        self.assertEqual(-1800, int(integer0))
        self.assertIsNotNone(integer0)

        boolean0 = linked_blocking_deque0.offerLast(integer0)
        self.assertFalse(linked_list0.contains(-1800))
        self.assertTrue(linked_blocking_deque0.contains(-1800))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertTrue(boolean0)
        self.assertEqual(0, linked_list0.size())

        integer1 = linked_blocking_deque0.pollLast2(371, time_unit0)
        self.assertFalse(linked_list0.contains(-1800))
        self.assertFalse(linked_blocking_deque0.contains(-1800))
        self.assertEqual(-1800, int(integer1))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(integer1)

        linked_blocking_deque0.push(integer1)
        self.assertFalse(linked_list0.contains(-1800))
        self.assertTrue(linked_blocking_deque0.contains(-1800))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertEqual(0, linked_list0.size())

        object0 = Object()
        self.assertIsNotNone(object0)

        boolean1 = linked_blocking_deque0.remove1(object0)
        self.assertFalse(linked_list0.contains(-1800))
        self.assertTrue(linked_blocking_deque0.contains(-1800))
        self.assertFalse(linked_blocking_deque0.contains(917))
        self.assertFalse(boolean1)
        self.assertEqual(0, linked_list0.size())
        self.assertFalse(boolean1 == boolean0)

        integer2 = linked_blocking_deque0.removeFirst()
        self.assertFalse(linked_list0.contains(integer2))
        self.assertFalse(linked_blocking_deque0.contains(integer2))
        self.assertEqual(-1800, int(integer2))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(integer2)

        integer3 = Integer(0)
        self.assertEqual(0, int(integer3))
        self.assertIsNotNone(integer3)
        self.assertFalse(integer3.equals(integer0))
        self.assertFalse(integer3.equals(integer1))
        self.assertFalse(integer3.equals(integer2))

        object_array0 = linked_blocking_deque0.toArray()
        self.assertFalse(linked_list0.contains(integer2))
        self.assertFalse(linked_blocking_deque0.contains(integer2))
        self.assertEqual(0, len(object_array0))
        self.assertEqual(0, linked_list0.size())
        self.assertIsNotNone(object_array0)

        boolean2 = linked_blocking_deque0.offerLast0(integer3)
        self.assertFalse(linked_list0.contains(integer2))
        self.assertTrue(linked_blocking_deque0.contains(integer3))
        self.assertFalse(linked_blocking_deque0.contains(integer2))
        self.assertTrue(boolean2)
        self.assertEqual(0, linked_list0.size())
        self.assertFalse(integer3.equals(integer0))
        self.assertFalse(integer3.equals(integer1))
        self.assertFalse(integer3.equals(integer2))
        self.assertTrue(boolean2 == boolean0)
        self.assertFalse(boolean2 == boolean1)

        # Undeclared exception
        with self.assertRaises(ValueError):
            LinkedBlockingDeque.LinkedBlockingDeque3(0)

    def test04(self) -> None:

        linkedHashSet0 = set()
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(1, 0, True, linkedHashSet0)
        self.assertFalse(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = 1
        self.assertEqual(1, integer0)
        self.assertIsNotNone(integer0)

        boolean0 = integer0 in linkedHashSet0
        self.assertFalse(0 in linkedHashSet0)
        self.assertTrue(1 in linkedHashSet0)
        self.assertTrue(boolean0)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))

        boolean1 = linkedBlockingDeque0.offerFirst0(integer0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertTrue(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertFalse(boolean1)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertFalse(boolean1 == boolean0)

        boolean2 = linkedBlockingDeque0.contains(None)
        self.assertFalse(0 in linkedHashSet0)
        self.assertTrue(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertFalse(boolean2)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertFalse(boolean2 == boolean0)
        self.assertTrue(boolean2 == boolean1)

        boolean3 = linkedBlockingDeque0.hasTakeWaiters()
        self.assertFalse(0 in linkedHashSet0)
        self.assertTrue(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertFalse(boolean3)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertTrue(boolean3 == boolean2)
        self.assertTrue(boolean3 == boolean1)
        self.assertFalse(boolean3 == boolean0)

        duration0 = Duration.ZERO
        self.assertIsNotNone(duration0)

        boolean4 = linkedBlockingDeque0.offerLast1(integer0, duration0)
        self.assertFalse(0 in linkedHashSet0)
        self.assertTrue(1 in linkedHashSet0)
        self.assertFalse(1 in linkedBlockingDeque0)
        self.assertFalse(boolean4)
        self.assertFalse(not linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertTrue(boolean4 == boolean1)
        self.assertFalse(boolean4 == boolean0)
        self.assertTrue(boolean4 == boolean2)
        self.assertTrue(boolean4 == boolean3)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.remove0()
            self.fail("Expecting exception: RuntimeError")

    def test03(self) -> None:

        pass  # LLM could not translate this method

    def test02(self) -> None:

        int0 = 0
        boolean0 = True
        int1 = 2
        linkedList0 = LinkedList()
        self.assertFalse(linkedList0.contains(int0))
        self.assertEqual(0, len(linkedList0))
        self.assertIsNotNone(linkedList0)

        list0 = list(linkedList0)
        self.assertFalse(linkedList0.contains(int0))
        self.assertFalse(list0.contains(int0))
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(list0))
        self.assertTrue(not list0)
        self.assertIsNotNone(list0)

        linkedBlockingDeque0 = LinkedBlockingDeque(1, 2, True, list0)
        self.assertFalse(linkedList0.contains(1))
        self.assertFalse(list0.contains(1))
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(list0))
        self.assertTrue(not list0)
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(
            -6730, 0, False, linkedBlockingDeque0
        )
        self.assertFalse(linkedList0.contains(0))
        self.assertFalse(list0.contains(0))
        self.assertFalse(linkedBlockingDeque0.contains(0))
        self.assertFalse(linkedBlockingDeque1.contains(0))
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(list0))
        self.assertTrue(not list0)
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque0)
        integer0 = linkedBlockingDeque1.pollLast2(0, TimeUnit.HOURS)
        self.assertFalse(linkedList0.contains(0))
        self.assertFalse(list0.contains(0))
        self.assertFalse(linkedBlockingDeque0.contains(0))
        self.assertFalse(linkedBlockingDeque1.contains(0))
        self.assertEqual(0, len(linkedList0))
        self.assertEqual(0, len(list0))
        self.assertTrue(not list0)
        self.assertIsNotNone(linkedBlockingDeque0)
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertIsNone(integer0)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque0)

        object0 = object()
        self.assertIsNotNone(object0)

        # Undeclared exception
        with self.assertRaises(RuntimeError):
            linkedBlockingDeque0.removeFirst()

    def test01(self) -> None:

        linkedBlockingDeque0 = LinkedBlockingDeque(1, 7, False, None)
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertIsNotNone(linkedBlockingDeque0)

        integer0 = Integer(2155)
        self.assertEqual(2155, int(integer0))
        self.assertIsNotNone(integer0)

        timeUnit0 = TimeUnit.DAYS
        boolean0 = linkedBlockingDeque0.offerLast2(integer0, 7, timeUnit0)
        self.assertFalse(linkedBlockingDeque0.contains(1))
        self.assertTrue(linkedBlockingDeque0.contains(2155))
        self.assertTrue(boolean0)

        int0 = linkedBlockingDeque0.size()
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(2155))
        self.assertEqual(1, int0)

        spliterator0 = linkedBlockingDeque0.spliterator()
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(2155))
        self.assertIsNotNone(spliterator0)

        duration0 = Duration.ofSeconds(1665, 1885)
        self.assertIsNotNone(duration0)

        duration1 = duration0.plusMillis(2288)
        self.assertIsNot(duration0, duration1)
        self.assertIsNot(duration1, duration0)
        self.assertIsNotNone(duration1)
        self.assertNotEqual(duration1, duration0)

        duration2 = duration0.abs()
        self.assertIs(duration0, duration2)
        self.assertIsNot(duration0, duration1)
        self.assertIs(duration2, duration0)
        self.assertIsNot(duration2, duration1)
        self.assertIsNotNone(duration2)
        self.assertNotEqual(duration0, duration1)
        self.assertNotEqual(duration2, duration1)

        timeUnit1 = TimeUnit.NANOSECONDS
        integer1 = Integer(0)
        self.assertEqual(0, int(integer1))
        self.assertIsNotNone(integer1)
        self.assertNotEqual(integer1, int0)
        self.assertNotEqual(integer1, integer0)

        boolean1 = linkedBlockingDeque0.offer(integer1)
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(0))
        self.assertTrue(boolean1)
        self.assertNotEqual(integer1, int0)
        self.assertNotEqual(integer1, integer0)
        self.assertEqual(boolean1, boolean0)

        integer2 = Integer(0)
        self.assertEqual(0, int(integer2))
        self.assertIsNotNone(integer2)
        self.assertNotEqual(integer2, int0)
        self.assertNotEqual(integer2, integer0)
        self.assertEqual(integer2, integer1)

        linkedBlockingDeque0.putFirst(integer2)
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(integer2))
        self.assertNotEqual(integer2, int0)
        self.assertNotEqual(integer2, integer0)
        self.assertEqual(integer2, integer1)

        boolean2 = linkedBlockingDeque0.offerFirst2(integer0, 0, timeUnit1)
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(integer2))
        self.assertTrue(boolean2)
        self.assertIsNot(timeUnit1, timeUnit0)
        self.assertNotEqual(integer0, int0)
        self.assertNotEqual(integer0, integer2)
        self.assertNotEqual(integer0, integer1)
        self.assertNotEqual(timeUnit1, timeUnit0)
        self.assertEqual(boolean2, boolean0)
        self.assertEqual(boolean2, boolean1)

        linkedBlockingDeque0.interuptTakeWaiters()
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(integer2))

        linkedBlockingDeque0.putLast(integer1)
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(integer2))
        self.assertEqual(integer1, integer2)
        self.assertNotEqual(integer1, int0)
        self.assertNotEqual(integer1, integer0)

        integer3 = linkedBlockingDeque0.removeLast()
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(integer2))
        self.assertEqual(0, int(integer3))
        self.assertIsNotNone(integer3)
        self.assertNotEqual(integer3, int0)
        self.assertNotEqual(integer3, integer0)
        self.assertEqual(integer3, integer2)

        integerArray0 = [None] * 4
        integerArray0[0] = integer0
        integerArray0[1] = integer0
        integerArray0[2] = None
        integerArray0[3] = integer3
        string0 = linkedBlockingDeque0.toString()
        self.assertFalse(linkedBlockingDeque0.contains(int0))
        self.assertTrue(linkedBlockingDeque0.contains(integer2))
        self.assertEqual("[2155, 0, 2155, 0]", string0)
        self.assertIsNotNone(string0)

        integer4 = linkedBlockingDeque0.takeLast()
        self.assertFalse(linkedBlockingDeque0.contains(7))
        self.assertTrue(linkedBlockingDeque0.contains(0))
        self.assertEqual(0, int(integer4))
        self.assertIsNotNone(integer4)
        self.assertEqual(integer4, integer2)
        self.assertNotEqual(integer4, int0)
        self.assertNotEqual(integer4, integer0)

    def test00(self) -> None:

        linkedHashSet0 = set()
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedHashSet0)

        linkedBlockingDeque0 = LinkedBlockingDeque(917, 917, False, linkedHashSet0)
        self.assertFalse(917 in linkedHashSet0)
        self.assertFalse(917 in linkedBlockingDeque0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque0)

        linkedBlockingDeque1 = LinkedBlockingDeque(
            917, 917, False, linkedBlockingDeque0
        )
        self.assertFalse(917 in linkedHashSet0)
        self.assertFalse(917 in linkedBlockingDeque0)
        self.assertFalse(917 in linkedBlockingDeque1)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque0)

        integer0 = -403
        self.assertEqual(-403, integer0)
        self.assertIsNotNone(integer0)

        boolean0 = linkedBlockingDeque1.add(integer0)
        self.assertFalse(917 in linkedHashSet0)
        self.assertFalse(917 in linkedBlockingDeque0)
        self.assertFalse(917 in linkedBlockingDeque1)
        self.assertTrue(integer0 in linkedBlockingDeque1)
        self.assertTrue(boolean0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque1, linkedBlockingDeque0)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)

        objectArray0 = linkedBlockingDeque0.toArray0()
        self.assertFalse(917 in linkedHashSet0)
        self.assertFalse(917 in linkedBlockingDeque0)
        self.assertEqual(0, len(objectArray0))
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertIsNotNone(objectArray0)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)

        integer1 = -403
        self.assertEqual(-403, integer1)
        self.assertIsNotNone(integer1)
        self.assertEqual(integer1, integer0)

        linkedHashSet1 = linkedHashSet0.copy()
        self.assertFalse(integer1 in linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet0))
        self.assertTrue(not linkedHashSet0)
        self.assertEqual(0, len(linkedHashSet1))
        self.assertIsNotNone(linkedHashSet1)

        integer2 = -2083
        self.assertEqual(-2083, integer2)
        self.assertIsNotNone(integer2)
        self.assertNotEqual(integer2, integer1)
        self.assertNotEqual(integer2, integer0)

        boolean1 = linkedHashSet0.add(integer2)
        self.assertTrue(integer2 in linkedHashSet0)
        self.assertFalse(integer1 in linkedHashSet0)
        self.assertTrue(boolean1)
        self.assertTrue(linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertNotEqual(integer2, integer1)
        self.assertNotEqual(integer2, integer0)
        self.assertEqual(boolean1, boolean0)

        timeUnit0 = TimeUnit.MICROSECONDS
        boolean2 = linkedBlockingDeque0.offer2(integer1, -403, timeUnit0)
        self.assertTrue(integer2 in linkedHashSet0)
        self.assertFalse(integer1 in linkedHashSet0)
        self.assertTrue(integer1 in linkedBlockingDeque0)
        self.assertFalse(integer2 in linkedBlockingDeque0)
        self.assertTrue(boolean2)
        self.assertTrue(linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertEqual(integer1, integer0)
        self.assertNotEqual(integer1, integer2)
        self.assertEqual(boolean2, boolean0)
        self.assertEqual(boolean2, boolean1)

        integer3 = linkedBlockingDeque0.takeFirst()
        self.assertTrue(integer2 in linkedHashSet0)
        self.assertFalse(integer3 in linkedHashSet0)
        self.assertFalse(integer3 in linkedBlockingDeque0)
        self.assertEqual(-403, integer3)
        self.assertTrue(linkedHashSet0)
        self.assertEqual(1, len(linkedHashSet0))
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertIsNotNone(integer3)
        self.assertNotEqual(linkedBlockingDeque0, linkedBlockingDeque1)
        self.assertEqual(integer3, integer0)
        self.assertNotEqual(integer3, integer2)
