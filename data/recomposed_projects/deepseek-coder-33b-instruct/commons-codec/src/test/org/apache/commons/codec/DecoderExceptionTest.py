from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.DecoderException import *


class DecoderExceptionTest(unittest.TestCase):

    __t: BaseException = Exception()

    __MSG: str = "TEST"

    def testConstructorThrowable(self) -> None:

        try:
            raise self.__t
        except BaseException as t:
            e = DecoderException(t.__class__.__name__, t)
            assert t.__class__.__name__ == e.getMessage()
            assert t == e.getCause()

    def testConstructorStringThrowable(self) -> None:

        e = DecoderException(self.__MSG, self.__t)
        assert self.__MSG == e.getMessage()
        assert self.__t == e.getCause()

    def testConstructorString(self) -> None:

        e = DecoderException(self.__MSG, None)
        self.assertEqual(self.__MSG, e.getMessage())
        self.assertIsNone(e.getCause())

    def testConstructor0(self) -> None:

        e = DecoderException(None, None)
        assert e.getMessage() is None
        assert e.getCause() is None
