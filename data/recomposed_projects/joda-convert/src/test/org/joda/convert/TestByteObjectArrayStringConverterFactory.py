# Imports Begin
from src.main.org.joda.convert.factory.ByteObjectArrayStringConverterFactory import *
from src.main.org.joda.convert.StringConverterFactory import *
from src.main.org.joda.convert.StringConvert import *
import unittest
import typing
from typing import *

# Imports End


class TestByteObjectArrayStringConverterFactory(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test_ByteArray(self) -> None:

        self.__doTest(b"", "")
        self.__doTest(b"\x00", "00")
        self.__doTest(b"\x00", "--")
        self.__doTest(b"\x00\x01\x00\x00\x0f\x10\x7f\x80\xff", "0001----0F107F80FF")

    def __doTest(self, array: typing.List[int], str: str) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
