from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.EncoderException import *


class EncoderExceptionTest(unittest.TestCase):

    __t: BaseException = Exception()

    __MSG: str = "TEST"

    def testConstructorThrowable(self) -> None:

        try:
            e = EncoderException("java.lang.Exception", self.__t)
            self.assertEqual(self.__t.__class__.__name__, e.getMessage())
            self.assertEqual(self.__t, e.getCause())
        except Exception as ex:
            print(f"An error occurred: {ex}")

    def testConstructorStringThrowable(self) -> None:

        e = EncoderException(self.__MSG, self.__t)
        assert self.__MSG == e.getMessage()
        assert self.__t == e.getCause()

    def testConstructorString(self) -> None:

        e = EncoderException(self.__MSG, None)
        self.assertEqual(self.__MSG, e.getMessage())
        self.assertIsNone(e.getCause())

    def testConstructor0(self) -> None:

        e = EncoderException(None, None)
        assert e.getMessage() is None
        assert e.getCause() is None
