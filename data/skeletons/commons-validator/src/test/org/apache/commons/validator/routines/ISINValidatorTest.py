# Imports Begin
from src.main.org.apache.commons.validator.routines.ISINValidator import *
import typing

# Imports End


class ISINValidatorTest(TestCase):

    # Class Fields Begin
    __VALIDATOR_TRUE: ISINValidator = None
    __VALIDATOR_FALSE: ISINValidator = None
    __validFormat: typing.List[str] = None
    __invalidFormat: typing.List[str] = None
    __invalidFormatTrue: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testInvalidFalse(self) -> None:
        pass

    def testIsValidFalse(self) -> None:
        pass

    def testInvalidTrue(self) -> None:
        pass

    def testIsValidTrue(self) -> None:
        pass

    def __init__(self, name: str) -> None:
        pass

    # Class Methods End
