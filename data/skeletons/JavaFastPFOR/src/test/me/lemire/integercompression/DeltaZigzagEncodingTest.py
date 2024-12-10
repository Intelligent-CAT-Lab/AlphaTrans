from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.DeltaZigzagEncoding import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class SpotChecker:

    # Class Fields Begin
    __encoder: Encoder = None
    __decoder: Decoder = None
    # Class Fields End

    # Class Methods Begin
    def check(self, value: int) -> None:
        pass

    # Class Methods End


class DeltaZigzagEncodingTest(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def checkSpots_test1_decomposed(self) -> None:
        pass

    def checkSpots_test0_decomposed(self) -> None:
        pass

    def checkDecodeSimple_test1_decomposed(self) -> None:
        pass

    def checkDecodeSimple_test0_decomposed(self) -> None:
        pass

    def checkEncodeSimple_test1_decomposed(self) -> None:
        pass

    def checkEncodeSimple_test0_decomposed(self) -> None:
        pass

    def checkZigzagDecoder_test1_decomposed(self) -> None:
        pass

    def checkZigzagDecoder_test0_decomposed(self) -> None:
        pass

    def checkZigzagEncode_test1_decomposed(self) -> None:
        pass

    def checkZigzagEncode_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def _checkDecode(
        d: Decoder, data: typing.List[int], expected: typing.List[int]
    ) -> None:
        pass

    @staticmethod
    def _checkEncode(
        e: Encoder, data: typing.List[int], expected: typing.List[int]
    ) -> None:
        pass

    @staticmethod
    def _zigzagDecode(d: Decoder, value: int) -> int:
        pass

    @staticmethod
    def _zigzagEncode(e: Encoder, value: int) -> int:
        pass

    # Class Methods End
