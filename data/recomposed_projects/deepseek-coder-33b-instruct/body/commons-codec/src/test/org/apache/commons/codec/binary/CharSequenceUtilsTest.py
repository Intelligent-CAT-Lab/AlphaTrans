from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *
import unittest
from src.main.org.apache.commons.codec.binary.CharSequenceUtils import *


class TestData:

    throwable: typing.Type[BaseException] = None

    expected: bool = False

    len: int = 0

    ooffset: int = 0

    other: str = ""

    toffset: int = 0

    ignoreCase: bool = False

    source: str = ""

    def toString(self) -> str:

        sb = []
        sb.append(self.source)
        sb.append("[")
        sb.append(str(self.toffset))
        sb.append("]")
        sb.append(" caseblind " if self.ignoreCase else " samecase ")
        sb.append(self.other)
        sb.append("[")
        sb.append(str(self.ooffset))
        sb.append("]")
        sb.append(" ")
        sb.append(str(self.len))
        sb.append(" => ")
        if self.throwable is not None:
            sb.append(str(self.throwable))
        else:
            sb.append(str(self.expected))
        return "".join(sb)

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


class RunTest(ABC):

    def run(self, data: TestData, id: str) -> None:

        if data.throwable is not None:
            msg = f"{id} Expected {data.throwable}"
            try:
                result = self.invoke()
                pytest.fail(f"{msg} but nothing was thrown.")
            except Exception as ex:
                assert issubclass(
                    type(ex), data.throwable
                ), f"{msg} but was {type(ex).__name__}"
        else:
            result = self.invoke()
            assert result == data.expected, f"{id} Failed test {data}"

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
        CharSequenceUtils()

    def testRegionMatches(self) -> None:

        for data in self.__TEST_DATA:

            class RunTestImpl(RunTest):
                def invoke(self) -> bool:
                    return data.source.regionMatches(
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )

            RunTestImpl().run(data, "String")

            class RunTestImpl(RunTest):
                def invoke(self) -> bool:
                    return CharSequenceUtils.regionMatches(
                        data.source,
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )

            RunTestImpl().run(data, "CSString")

            class RunTestImpl(RunTest):
                def invoke(self) -> bool:
                    return CharSequenceUtils.regionMatches(
                        StringBuilder(data.source),
                        data.ignoreCase,
                        data.toffset,
                        data.other,
                        data.ooffset,
                        data.len,
                    )

            RunTestImpl().run(data, "CSNonString")


CharSequenceUtilsTest.initialize_fields()
