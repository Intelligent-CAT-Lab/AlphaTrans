from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
import typing
from typing import *
import io

# Imports End


class DoubleMetaphone2Test(StringEncoderAbstractTest):

    # Class Fields Begin
    __ALTERNATE_INDEX: int = None
    __PRIMARY_INDEX: int = None
    __TEST_DATA: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testDoubleMetaphonePrimary(self) -> None:
        pass

    def testDoubleMetaphoneAlternate(self) -> None:
        pass

    def _createStringEncoder(self) -> DoubleMetaphone:
        pass

    def __checkDoubleMetaphone(self, typeIndex: int, alternate: bool) -> None:
        pass

    # Class Methods End
