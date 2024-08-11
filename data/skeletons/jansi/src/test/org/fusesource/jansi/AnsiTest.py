from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.AnsiMain import *
from src.main.org.fusesource.jansi.Ansi import *
import unittest
import os
import io

# Imports End


class AnsiTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testColorDisabled_test1_decomposed(self) -> None:
        pass

    def testColorDisabled_test0_decomposed(self) -> None:
        pass

    def testCursorUpLine0_test1_decomposed(self) -> None:
        pass

    def testCursorUpLine0_test0_decomposed(self) -> None:
        pass

    def testCursorDownLine0_test1_decomposed(self) -> None:
        pass

    def testCursorDownLine0_test0_decomposed(self) -> None:
        pass

    def testApply_test2_decomposed(self) -> None:
        pass

    def testApply_test1_decomposed(self) -> None:
        pass

    def testApply_test0_decomposed(self) -> None:
        pass

    def testClone(self) -> None:
        pass

    def testClone_test6_decomposed(self) -> None:
        pass

    def testClone_test5_decomposed(self) -> None:
        pass

    def testClone_test4_decomposed(self) -> None:
        pass

    def testClone_test3_decomposed(self) -> None:
        pass

    def testClone_test2_decomposed(self) -> None:
        pass

    def testClone_test1_decomposed(self) -> None:
        pass

    def testClone_test0_decomposed(self) -> None:
        pass

    def testSetEnabled_test5_decomposed(self) -> None:
        pass

    def testSetEnabled_test4_decomposed(self) -> None:
        pass

    def testSetEnabled_test3_decomposed(self) -> None:
        pass

    def testSetEnabled_test2_decomposed(self) -> None:
        pass

    def testSetEnabled_test1_decomposed(self) -> None:
        pass

    def testSetEnabled_test0_decomposed(self) -> None:
        pass

    def testAnsiMainWithNoConsole(self) -> None:
        pass

    def testCursorUpLine1(self, n: int, expected: str) -> None:
        pass

    def testCursorDownLine1(self, n: int, expected: str) -> None:
        pass

    def testCursorMove(self, x: int, y: int, expected: str) -> None:
        pass

    def testCursorLeft(self, x: int, expected: str) -> None:
        pass

    def testCursorRight(self, x: int, expected: str) -> None:
        pass

    def testCursorDown(self, y: int, expected: str) -> None:
        pass

    def testCursorUp(self, y: int, expected: str) -> None:
        pass

    def testCursorToColumn(self, x: int, expected: str) -> None:
        pass

    def testCursor(self, x: int, y: int, expected: str) -> None:
        pass

    def testScrollDown(self, x: int, expected: str) -> None:
        pass

    def testScrollUp(self, x: int, expected: str) -> None:
        pass

    @staticmethod
    def __assertAnsi(expected: str, actual: Ansi) -> None:
        pass

    # Class Methods End
