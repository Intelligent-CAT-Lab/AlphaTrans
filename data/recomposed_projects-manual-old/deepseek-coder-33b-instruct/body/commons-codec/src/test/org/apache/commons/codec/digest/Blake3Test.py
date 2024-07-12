from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Blake3 import *


class Blake3Test(unittest.TestCase):

    def testshouldThrowValueErrorWhenIncorrectKeySize(self) -> None:

        for i in range(33):
            self.__assertThrowsProperExceptionWithKeySize(i)

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:

        try:
            Blake3.initKeyedHash(bytearray(keySize))
            self.fail("Should have thrown exception")
        except ValueError as expected:
            self.assertEqual("Blake3 keys must be 32 bytes", str(expected))
