from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.DecoderException import *


class DecoderExceptionTest(unittest.TestCase):

    __t: BaseException = Exception()
    __MSG: str = "TEST"

    def testConstructorThrowable(self) -> None:

        e = DecoderException("java.lang.Exception", DecoderExceptionTest.__t)
        self.assertEqual(DecoderExceptionTest.__t.__class__.__name__, e.getMessage())
        self.assertEqual(DecoderExceptionTest.__t, e.getCause())

    def testConstructorStringThrowable(self) -> None:

        e = DecoderException(self.__MSG, self.__t)
        self.assertEqual(self.__MSG, e.getMessage())
        self.assertEqual(self.__t, e.getCause())

    def testConstructorString(self) -> None:

        e = DecoderException(self.__MSG, None)
        self.assertEqual(self.__MSG, e.getMessage())
        self.assertIsNone(e.getCause())

    def testConstructor0(self) -> None:

        e = DecoderException(None, None)
        self.assertIsNone(e.getMessage())
        self.assertIsNone(e.getCause())
