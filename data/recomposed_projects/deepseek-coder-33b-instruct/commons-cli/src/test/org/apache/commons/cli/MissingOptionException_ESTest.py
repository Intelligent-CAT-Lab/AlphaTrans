from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.cli.MissingOptionException import *

# from src.main.org.apache.commons.cli.MissingOptionException_ESTest_scaffolding import *
# from src.main.org.evosuite.runtime.EvoAssertions import *
# from src.main.org.evosuite.runtime.EvoRunnerParameters import *


class MissingOptionException_ESTest(unittest.TestCase):

    @pytest.mark.test
    def test5(self) -> None:

        list0 = [
            "org.apache.commons.cli.ParseException",
            "org.apache.commons.cli.ParseException",
            "org.apache.commons.cli.ParseException",
            "org.apache.commons.cli.ParseException",
        ]
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1, list0, "org.apache.commons.cli.ParseException"
        )
        self.assertIsNotNone(missingOptionException0)

    @pytest.mark.test
    def test4(self) -> None:
        linkedList0 = LinkedList()
        missingOptionException0 = MissingOptionException(1, linkedList0, "Fu")
        list0 = missingOptionException0.getMissingOptions()
        missingOptionException1 = MissingOptionException(
            -814, list0, "y~PxelKxqCa16c;lBay"
        )
        self.assertFalse(missingOptionException1.equals(missingOptionException0))

    @pytest.mark.test
    def test3(self) -> None:

        linkedList0 = LinkedList[int]()
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1, linkedList0, "Missing required option"
        )
        list0 = missingOptionException0.getMissingOptions()
        missingOptionException1 = MissingOptionException.MissingOptionException1(
            0, list0, "Fa>ZS071}NhO^9ZY~"
        )
        list1 = missingOptionException1.getMissingOptions()
        self.assertIsNone(list1)

    @pytest.mark.test
    def test2(self) -> None:

        try:
            MissingOptionException.MissingOptionException1(1, None, ": ")
            self.fail("Expecting exception: NullPointerException")

        except NullPointerException as e:
            verifyException("org.apache.commons.cli.MissingOptionException", e)

    @pytest.mark.test
    def test1(self) -> None:

        linkedList0 = LinkedList()
        object0 = Object()
        integer0 = Integer(1)
        list0 = [
            linkedList0,
            linkedList0,
            linkedList0,
            linkedList0,
            object0,
            object0,
            linkedList0,
            object0,
            integer0,
        ]
        linkedList0.add(list0)

        try:
            MissingOptionException.MissingOptionException1(
                1, linkedList0, "org.apache.commons.cli.ParseException"
            )
            self.fail("Expecting exception: StackOverflowError")

        except StackOverflowError as e:
            pass

    @pytest.mark.test
    def test0(self) -> None:

        linkedList0 = [0]
        missingOptionException0 = MissingOptionException.MissingOptionException1(
            1, linkedList0, "Missing required option"
        )
        list0 = missingOptionException0.getMissingOptions()
        self.assertEqual(1, len(list0))
