from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class PhoneticEngineTest(unittest.TestCase):

    # Class Fields Begin
    __concat: bool = None
    __name: str = None
    __nameType: NameType = None
    __phoneticExpected: str = None
    __ruleType: RuleType = None
    __maxPhonemes: int = None
    __TEN: int = None
    # Class Fields End

    # Class Methods Begin
    def testEncode_test2_decomposed(self) -> None:
        pass

    def testEncode_test1_decomposed(self) -> None:
        pass

    def testEncode_test0_decomposed(self) -> None:
        pass

    @staticmethod
    def data() -> typing.List[typing.List[typing.Any]]:
        pass

    def __init__(
        self,
        name: str,
        phoneticExpected: str,
        nameType: NameType,
        ruleType: RuleType,
        concat: bool,
        maxPhonemes: int,
    ) -> None:
        pass

    # Class Methods End
