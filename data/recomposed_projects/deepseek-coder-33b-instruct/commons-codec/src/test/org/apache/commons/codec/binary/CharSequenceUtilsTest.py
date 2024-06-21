from __future__ import annotations
import re
from dataclasses import field
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *


class TestData:

    throwable: typing.Type[BaseException] = None
    expected: bool = None
    len: int = None
    ooffset: int = None
    other: str = None
    toffset: int = None
    ignoreCase: bool = None
    source: str = None

    def toString(self) -> str:

        sb = io.StringIO()
        sb.write(self.source + "[" + str(self.toffset) + "]")
        sb.write(" caseblind " if self.ignoreCase else " samecase ")
        sb.write(self.other + "[" + str(self.ooffset) + "]")
        sb.write(" " + str(self.len) + " => ")
        if self.throwable is not None:
            sb.write(str(self.throwable))
        else:
            sb.write(str(self.expected))
        return sb.getvalue()

    def __init__(
        self,
        constructorId: int,
        expected: bool,
        ooffset: int,
        source: str,
        throwable: typing.Type[BaseException],
        toffset: int,
        ignoreCase: bool,
        other: str,
        len: int,
    ) -> None:

        if constructorId == 0:
            self.source = source
            self.ignoreCase = ignoreCase
            self.toffset = toffset
            self.other = other
            self.ooffset = ooffset
            self.len = len
            self.expected = False
            self.throwable = throwable
        else:
            self.source = source
            self.ignoreCase = ignoreCase
            self.toffset = toffset
            self.other = other
            self.ooffset = ooffset
            self.len = len
            self.expected = expected
            self.throwable = None


class RunTest(ABC, unittest.TestCase):

    def run(self, data: TestData, id: str) -> None:

        if data.throwable is not None:
            msg = id + " Expected " + str(data.throwable)
            try:
                string_check = self.invoke()
                assert False, msg + " but nothing was thrown."
            except Exception as ex:
                assert issubclass(type(ex), data.throwable), (
                    msg + " but was " + ex.__class__.__name__
                )
        else:
            string_check = self.invoke()
            assert string_check == data.expected, id + " Failed test " + str(data)

    def invoke(self) -> bool:

        pass


class CharSequenceUtilsTest(unittest.TestCase):

    __TEST_DATA: typing.List[TestData] = None

    @staticmethod
    def initialize_fields() -> None:
        CharSequenceUtilsTest.__TEST_DATA: typing.List[TestData] = [
            TestData(1, True, 0, "a", None, 0, True, "abc", 0),
            TestData(1, True, 0, "a", None, 0, True, "abc", 1),
            TestData(1, True, 0, "Abc", None, 0, True, "abc", 3),
            TestData(1, False, 0, "Abc", None, 0, False, "abc", 3),
            TestData(1, True, 1, "Abc", None, 1, True, "abc", 2),
            TestData(1, True, 1, "Abc", None, 1, False, "abc", 2),
            TestData(1, True, 1, "Abcd", None, 1, True, "abcD", 2),
            TestData(1, True, 1, "Abcd", None, 1, False, "abcD", 2),
        ]

    def testConstructor(self) -> None:

        # In Python, you don't need to explicitly call a constructor like in Java.
        # Objects are created when they are first assigned to a variable or when they are returned from a function.
        # So, you can just create an instance of the class without calling the constructor explicitly.
        CharSequenceUtils()

    def testRegionMatches(self) -> None:

        class RunTest(ABC):
            @abstractmethod
            def invoke(self) -> bool:
                pass

            def run(self, data: TestData, id: str) -> None:
                result = self.invoke()
                # Here you can add the code to handle the result

        for data in self.__TEST_DATA:
            RunTestImpl = type(
                "RunTestImpl",
                (RunTest,),
                {
                    "invoke": lambda self: data.source.regionMatches(
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )
                },
            )
            RunTestImpl().run(data, "String")

            RunTestImpl = type(
                "RunTestImpl",
                (RunTest,),
                {
                    "invoke": lambda self: CharSequenceUtils.regionMatches(
                        data.source,
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )
                },
            )
            RunTestImpl().run(data, "CSString")

            RunTestImpl = type(
                "RunTestImpl",
                (RunTest,),
                {
                    "invoke": lambda self: CharSequenceUtils.regionMatches(
                        StringBuilder(data.source),
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )
                },
            )
            RunTestImpl().run(data, "CSNonString")


CharSequenceUtilsTest.initialize_fields()
