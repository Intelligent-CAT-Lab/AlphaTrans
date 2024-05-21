from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.DoubleMetaphone import *
from src.test.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io

# Imports End


class DoubleMetaphoneTest(StringEncoderAbstractTest):

    # Class Fields Begin
    __FIXTURE: typing.List[typing.List[str]] = None
    __MATCHES: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def testSetMaxCodeLength(self) -> None:
        pass

    def testNTilde(self) -> None:
        pass

    def testIsDoubleMetaphoneNotEqual(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualWithMATCHES(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended3(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended2(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualExtended1(self) -> None:
        pass

    def testIsDoubleMetaphoneEqualBasic(self) -> None:
        pass

    def testEmpty(self) -> None:
        pass

    def testDoubleMetaphone(self) -> None:
        pass

    def testCodec184(self) -> None:
        pass

    def testCCedilla(self) -> None:
        pass

    def _createStringEncoder(self) -> DoubleMetaphone:
        pass

    def validateFixture(self, pairs: typing.List[typing.List[str]]) -> None:
        pass

    def doubleMetaphoneNotEqualTest(self, alternate: bool) -> None:
        pass

    def doubleMetaphoneEqualTest(
        self, pairs: typing.List[typing.List[str]], useAlternate: bool
    ) -> None:
        pass

    def assertDoubleMetaphoneAlt(self, expected: str, source: str) -> None:
        pass

    def __assertDoubleMetaphone(self, expected: str, source: str) -> None:
        pass

    # Class Methods End
