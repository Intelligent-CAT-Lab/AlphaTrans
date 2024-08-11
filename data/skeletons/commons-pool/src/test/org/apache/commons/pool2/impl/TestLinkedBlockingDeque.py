from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.pool2.impl.LinkedBlockingDeque import *
import unittest
import os
import datetime
import typing
from typing import *
import io

# Imports End


class TestLinkedBlockingDeque(unittest.TestCase):

    # Class Fields Begin
    __TIMEOUT_50_MILLIS: datetime.timedelta = None
    __ONE: int = None
    __TWO: int = None
    __THREE: int = None
    deque: LinkedBlockingDeque[int] = None
    # Class Fields End

    # Class Methods Begin
    def testToArray_test4_decomposed(self) -> None:
        pass

    def testToArray_test3_decomposed(self) -> None:
        pass

    def testToArray_test2_decomposed(self) -> None:
        pass

    def testToArray_test1_decomposed(self) -> None:
        pass

    def testToArray_test0_decomposed(self) -> None:
        pass

    def testTakeLast_test1_decomposed(self) -> None:
        pass

    def testTakeLast_test0_decomposed(self) -> None:
        pass

    def testTakeFirst_test1_decomposed(self) -> None:
        pass

    def testTakeFirst_test0_decomposed(self) -> None:
        pass

    def testTake_test1_decomposed(self) -> None:
        pass

    def testTake_test0_decomposed(self) -> None:
        pass

    def testRemoveLastOccurrence_test3_decomposed(self) -> None:
        pass

    def testRemoveLastOccurrence_test2_decomposed(self) -> None:
        pass

    def testRemoveLastOccurrence_test1_decomposed(self) -> None:
        pass

    def testRemoveLastOccurrence_test0_decomposed(self) -> None:
        pass

    def testRemoveLast_test2_decomposed(self) -> None:
        pass

    def testRemoveLast_test1_decomposed(self) -> None:
        pass

    def testRemoveLast_test0_decomposed(self) -> None:
        pass

    def testRemoveFirst_test2_decomposed(self) -> None:
        pass

    def testRemoveFirst_test1_decomposed(self) -> None:
        pass

    def testRemoveFirst_test0_decomposed(self) -> None:
        pass

    def testRemove_test2_decomposed(self) -> None:
        pass

    def testRemove_test1_decomposed(self) -> None:
        pass

    def testRemove_test0_decomposed(self) -> None:
        pass

    def testPutLast_test2_decomposed(self) -> None:
        pass

    def testPutLast_test1_decomposed(self) -> None:
        pass

    def testPutLast_test0_decomposed(self) -> None:
        pass

    def testPutFirst_test2_decomposed(self) -> None:
        pass

    def testPutFirst_test1_decomposed(self) -> None:
        pass

    def testPutFirst_test0_decomposed(self) -> None:
        pass

    def testPut_test0_decomposed(self) -> None:
        pass

    def testPush_test3_decomposed(self) -> None:
        pass

    def testPush_test2_decomposed(self) -> None:
        pass

    def testPush_test1_decomposed(self) -> None:
        pass

    def testPush_test0_decomposed(self) -> None:
        pass

    def testPossibleBug_test5_decomposed(self) -> None:
        pass

    def testPossibleBug_test4_decomposed(self) -> None:
        pass

    def testPossibleBug_test3_decomposed(self) -> None:
        pass

    def testPossibleBug_test2_decomposed(self) -> None:
        pass

    def testPossibleBug_test1_decomposed(self) -> None:
        pass

    def testPossibleBug_test0_decomposed(self) -> None:
        pass

    def testPop_test2_decomposed(self) -> None:
        pass

    def testPop_test1_decomposed(self) -> None:
        pass

    def testPop_test0_decomposed(self) -> None:
        pass

    def testPollWithTimeout_test0_decomposed(self) -> None:
        pass

    def testPollLastWithTimeout_test1_decomposed(self) -> None:
        pass

    def testPollLastWithTimeout_test0_decomposed(self) -> None:
        pass

    def testPollLast_test2_decomposed(self) -> None:
        pass

    def testPollLast_test1_decomposed(self) -> None:
        pass

    def testPollLast_test0_decomposed(self) -> None:
        pass

    def testPollFirstWithTimeout_test1_decomposed(self) -> None:
        pass

    def testPollFirstWithTimeout_test0_decomposed(self) -> None:
        pass

    def testPollFirst_test2_decomposed(self) -> None:
        pass

    def testPollFirst_test1_decomposed(self) -> None:
        pass

    def testPollFirst_test0_decomposed(self) -> None:
        pass

    def testPeekLast_test2_decomposed(self) -> None:
        pass

    def testPeekLast_test1_decomposed(self) -> None:
        pass

    def testPeekLast_test0_decomposed(self) -> None:
        pass

    def testPeekFirst_test2_decomposed(self) -> None:
        pass

    def testPeekFirst_test1_decomposed(self) -> None:
        pass

    def testPeekFirst_test0_decomposed(self) -> None:
        pass

    def testPeek_test2_decomposed(self) -> None:
        pass

    def testPeek_test1_decomposed(self) -> None:
        pass

    def testPeek_test0_decomposed(self) -> None:
        pass

    def testOfferWithTimeout_test0_decomposed(self) -> None:
        pass

    def testOfferLastWithTimeout_test0_decomposed(self) -> None:
        pass

    def testOfferLast_test3_decomposed(self) -> None:
        pass

    def testOfferLast_test2_decomposed(self) -> None:
        pass

    def testOfferLast_test1_decomposed(self) -> None:
        pass

    def testOfferLast_test0_decomposed(self) -> None:
        pass

    def testOfferFirstWithTimeout_test0_decomposed(self) -> None:
        pass

    def testOfferFirst_test3_decomposed(self) -> None:
        pass

    def testOfferFirst_test2_decomposed(self) -> None:
        pass

    def testOfferFirst_test1_decomposed(self) -> None:
        pass

    def testOfferFirst_test0_decomposed(self) -> None:
        pass

    def testOffer_test0_decomposed(self) -> None:
        pass

    def testIterator_test5_decomposed(self) -> None:
        pass

    def testIterator_test4_decomposed(self) -> None:
        pass

    def testIterator_test3_decomposed(self) -> None:
        pass

    def testIterator_test2_decomposed(self) -> None:
        pass

    def testIterator_test1_decomposed(self) -> None:
        pass

    def testIterator_test0_decomposed(self) -> None:
        pass

    def testGetLast_test2_decomposed(self) -> None:
        pass

    def testGetLast_test1_decomposed(self) -> None:
        pass

    def testGetLast_test0_decomposed(self) -> None:
        pass

    def testGetFirst_test2_decomposed(self) -> None:
        pass

    def testGetFirst_test1_decomposed(self) -> None:
        pass

    def testGetFirst_test0_decomposed(self) -> None:
        pass

    def testElement_test2_decomposed(self) -> None:
        pass

    def testElement_test1_decomposed(self) -> None:
        pass

    def testElement_test0_decomposed(self) -> None:
        pass

    def testDrainTo_test10_decomposed(self) -> None:
        pass

    def testDrainTo_test9_decomposed(self) -> None:
        pass

    def testDrainTo_test8_decomposed(self) -> None:
        pass

    def testDrainTo_test7_decomposed(self) -> None:
        pass

    def testDrainTo_test6_decomposed(self) -> None:
        pass

    def testDrainTo_test5_decomposed(self) -> None:
        pass

    def testDrainTo_test4_decomposed(self) -> None:
        pass

    def testDrainTo_test3_decomposed(self) -> None:
        pass

    def testDrainTo_test2_decomposed(self) -> None:
        pass

    def testDrainTo_test1_decomposed(self) -> None:
        pass

    def testDrainTo_test0_decomposed(self) -> None:
        pass

    def testDescendingIterator_test5_decomposed(self) -> None:
        pass

    def testDescendingIterator_test4_decomposed(self) -> None:
        pass

    def testDescendingIterator_test3_decomposed(self) -> None:
        pass

    def testDescendingIterator_test2_decomposed(self) -> None:
        pass

    def testDescendingIterator_test1_decomposed(self) -> None:
        pass

    def testDescendingIterator_test0_decomposed(self) -> None:
        pass

    def testContains_test3_decomposed(self) -> None:
        pass

    def testContains_test2_decomposed(self) -> None:
        pass

    def testContains_test1_decomposed(self) -> None:
        pass

    def testContains_test0_decomposed(self) -> None:
        pass

    def testConstructors_test6_decomposed(self) -> None:
        pass

    def testConstructors_test5_decomposed(self) -> None:
        pass

    def testConstructors_test4_decomposed(self) -> None:
        pass

    def testConstructors_test3_decomposed(self) -> None:
        pass

    def testConstructors_test2_decomposed(self) -> None:
        pass

    def testConstructors_test1_decomposed(self) -> None:
        pass

    def testConstructors_test0_decomposed(self) -> None:
        pass

    def testClear_test3_decomposed(self) -> None:
        pass

    def testClear_test2_decomposed(self) -> None:
        pass

    def testClear_test1_decomposed(self) -> None:
        pass

    def testClear_test0_decomposed(self) -> None:
        pass

    def testAddLast_test3_decomposed(self) -> None:
        pass

    def testAddLast_test2_decomposed(self) -> None:
        pass

    def testAddLast_test1_decomposed(self) -> None:
        pass

    def testAddLast_test0_decomposed(self) -> None:
        pass

    def testAddFirst_test3_decomposed(self) -> None:
        pass

    def testAddFirst_test2_decomposed(self) -> None:
        pass

    def testAddFirst_test1_decomposed(self) -> None:
        pass

    def testAddFirst_test0_decomposed(self) -> None:
        pass

    def testAdd_test0_decomposed(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    # Class Methods End
