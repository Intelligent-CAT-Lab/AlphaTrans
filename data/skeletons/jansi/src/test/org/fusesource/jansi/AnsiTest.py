from __future__ import annotations

# Imports Begin
from src.main.org.fusesource.jansi.AnsiMain import *
from src.main.org.fusesource.jansi.Ansi import *
import unittest
import io

# Imports End


class AnsiTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testAnsiMainWithNoConsole(self) -> None:
        pass

    def testColorDisabled(self) -> None:
        pass

    def testCursorUpLine1(self, n: int, expected: str) -> None:
        pass

    def testCursorUpLine0(self) -> None:
        pass

    def testCursorDownLine1(self, n: int, expected: str) -> None:
        pass

    def testCursorDownLine0(self) -> None:
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

    def testApply(self) -> None:
        pass

    def testClone(self) -> None:
        pass

    def testSetEnabled(self) -> None:
        pass

    @staticmethod
    def __assertAnsi(expected: str, actual: Ansi) -> None:
        pass

    # Class Methods End
