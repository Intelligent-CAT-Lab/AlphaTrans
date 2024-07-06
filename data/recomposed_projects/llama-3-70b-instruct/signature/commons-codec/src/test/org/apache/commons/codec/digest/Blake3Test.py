from __future__ import annotations
import re
import unittest
import pytest
import io
import unittest
from src.main.org.apache.commons.codec.digest.Blake3 import *


class Blake3Test(unittest.TestCase):

    def testshouldThrowValueErrorWhenIncorrectKeySize(self) -> None:
        for i in range(0, 32):
            self.__assertThrowsProperExceptionWithKeySize(i)
        self.__assertThrowsProperExceptionWithKeySize(33)

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:
        with pytest.raises(ValueError) as expected:
            Blake3.initKeyedHash([0] * keySize)
            assert "Blake3 keys must be 32 bytes" == expected.value.getMessage()
