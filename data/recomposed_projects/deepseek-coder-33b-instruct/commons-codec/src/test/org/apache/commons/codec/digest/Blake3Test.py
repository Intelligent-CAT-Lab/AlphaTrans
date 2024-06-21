from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.apache.commons.codec.digest.Blake3 import *


class Blake3Test(unittest.TestCase):

    def shouldThrowValueErrorWhenIncorrectKeySize(self) -> None:

        for i in range(33):
            self.__assertThrowsProperExceptionWithKeySize(i)

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:
        try:
            Blake3.digest(keySize)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected ValueError for keySize: " + str(keySize))

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:

        try:
            Blake3.initKeyedHash(bytearray(keySize))
            assert False, "Should have thrown exception"
        except ValueError as expected:
            assert (
                expected.getMessage() == "Blake3 keys must be 32 bytes"
            ), "Exception message does not match"
