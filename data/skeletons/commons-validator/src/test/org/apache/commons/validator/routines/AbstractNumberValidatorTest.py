from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.validator.routines.AbstractNumberValidator import *
import unittest
import typing
from typing import *
import numbers
import io
from abc import ABC

# Imports End


class AbstractNumberValidatorTest(unittest.TestCase, ABC):

    # Class Fields Begin
    _validator: AbstractNumberValidator = None
    _strictValidator: AbstractNumberValidator = None
    _max: typing.Union[int, float, numbers.Number] = None
    _maxPlusOne: typing.Union[int, float, numbers.Number] = None
    _min: typing.Union[int, float, numbers.Number] = None
    _minMinusOne: typing.Union[int, float, numbers.Number] = None
    _invalid: typing.List[typing.List[str]] = None
    _valid: typing.List[typing.List[str]] = None
    _validCompare: typing.List[typing.Union[int, float, numbers.Number]] = None
    _invalidStrict: typing.List[typing.List[str]] = None
    _validStrict: typing.List[typing.List[str]] = None
    _validStrictCompare: typing.List[typing.Union[int, float, numbers.Number]] = None
    _testPattern: str = None
    _testNumber: typing.Union[int, float, numbers.Number] = None
    _testZero: typing.Union[int, float, numbers.Number] = None
    _testStringUS: str = None
    _testStringDE: str = None
    _localeValue: str = None
    _localePattern: str = None
    _testLocale: typing.Any = None
    _localeExpected: typing.Union[int, float, numbers.Number] = None
    # Class Fields End

    # Class Methods Begin
    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def testSerialization(self) -> None:
        pass

    def testRangeMinMax(self) -> None:
        pass

    def testFormat(self) -> None:
        pass

    def testValidateLocale(self) -> None:
        pass

    def testValidNotStrict(self) -> None:
        pass

    def testValidStrict(self) -> None:
        pass

    def testInvalidNotStrict(self) -> None:
        pass

    def testInvalidStrict(self) -> None:
        pass

    def testValidateMinMax(self) -> None:
        pass

    def testFormatType(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
