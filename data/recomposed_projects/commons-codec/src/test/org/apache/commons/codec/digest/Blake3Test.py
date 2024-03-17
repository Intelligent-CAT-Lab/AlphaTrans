# Imports Begin
from src.main.org.apache.commons.codec.digest.Blake3 import *
import unittest

# Imports End


class Blake3Test(unittest.TestCase):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def shouldThrowIllegalArgumentExceptionWhenIncorrectKeySize(self) -> None:

        for i in range(32):
            self.__assertThrowsProperExceptionWithKeySize(i)
        self.__assertThrowsProperExceptionWithKeySize(33)

    @staticmethod
    def __assertThrowsProperExceptionWithKeySize(keySize: int) -> None:

        pass  # LLM could not translate method body

    # Class Methods End
