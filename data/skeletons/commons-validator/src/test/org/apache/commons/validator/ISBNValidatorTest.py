from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.ISBNValidator import *
from src.main.org.apache.commons.validator.ISBNValidator import *
import unittest
import os
import io

# Imports End


class ISBNValidatorTest(unittest.TestCase):

    # Class Fields Begin
    __VALID_ISBN_RAW: str = None
    __VALID_ISBN_DASHES: str = None
    __VALID_ISBN_SPACES: str = None
    __VALID_ISBN_X: str = None
    __INVALID_ISBN: str = None
    # Class Fields End

    # Class Methods Begin
    def testIsValid_test1_decomposed(self) -> None:
        pass

    def testIsValid_test0_decomposed(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
