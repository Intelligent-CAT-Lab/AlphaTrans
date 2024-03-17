# Imports Begin
from src.main.org.apache.commons.codec.DecoderException import *
import unittest

# Imports End


class DecoderExceptionTest(unittest.TestCase):

    # Class Fields Begin
    __MSG: str = ""  # LLM could not translate field
    __t: BaseException = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def testConstructorThrowable(self) -> None:

        e = DecoderException("java.lang.Exception", t)
        self.assertEqual(t.getClass().getName(), e.getMessage())
        self.assertEqual(t, e.getCause())

    def testConstructorStringThrowable(self) -> None:

        e = DecoderException(self.__MSG, self.__t)
        self.assertEqual(self.__MSG, e.getMessage())
        self.assertEqual(self.__t, e.getCause())

    def testConstructorString(self) -> None:

        e = DecoderException(MSG, None)
        self.assertEqual(MSG, e.getMessage())
        assertNull(e.getCause())

    def testConstructor0(self) -> None:

        e = DecoderException(None, None)
        assert e.getMessage() is None
        assert e.getCause() is None

    # Class Methods End
