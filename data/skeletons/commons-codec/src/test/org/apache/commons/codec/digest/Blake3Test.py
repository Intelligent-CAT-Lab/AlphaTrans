from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.digest.Blake3 import *
import unittest
import os
import io

# Imports End


class Blake3Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def shouldThrowIllegalArgumentExceptionWhenIncorrectKeySize_test0_decomposed(
        self,
    ) -> None:
        pass

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:
        pass

    # Class Methods End
