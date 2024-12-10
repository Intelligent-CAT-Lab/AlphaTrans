from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.net.RFC1522Codec import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class RFC1522TestCodec(RFC1522Codec):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _getEncoding(self) -> str:
        pass

    def _doEncoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    def _doDecoding(self, bytes_: typing.List[int]) -> typing.List[int]:
        pass

    # Class Methods End


class RFC1522CodecTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def testDecodeInvalid_test0_decomposed(self) -> None:
        pass

    def testNullInput_test2_decomposed(self) -> None:
        pass

    def testNullInput_test1_decomposed(self) -> None:
        pass

    def testNullInput_test0_decomposed(self) -> None:
        pass

    def __assertExpectedDecoderException(self, s: str) -> None:
        pass

    # Class Methods End
