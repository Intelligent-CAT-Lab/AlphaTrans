# Imports Begin
from src.main.org.apache.commons.codec.language.ColognePhonetic import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing

# Imports End


class ColognePhoneticTest(StringEncoderAbstractTest):

    # Class Fields Begin
    __TESTSET: typing.Set[str] = None
    __MATCHES: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testSpecialCharsBetweenSameLetters(self) -> None:
        pass

    def testVariationsMeyer(self) -> None:
        pass

    def testVariationsMella(self) -> None:
        pass

    def testIsEncodeEquals(self) -> None:
        pass

    def testHyphen(self) -> None:
        pass

    def testExamples(self) -> None:
        pass

    def testEdgeCases(self) -> None:
        pass

    def testAychlmajrForCodec122(self) -> None:
        pass

    def testAaclan(self) -> None:
        pass

    def testAabjoe(self) -> None:
        pass

    def testCanFail(self) -> None:
        pass

    def _createStringEncoder(self) -> ColognePhonetic:
        pass

    def checkEncoding(self, expected: str, source: str) -> None:
        pass

    @staticmethod
    def finishTests() -> None:
        pass

    @staticmethod
    def main(args: typing.List[str]) -> None:
        pass

    @staticmethod
    def __hasTestCase(re: str) -> bool:
        pass

    # Class Methods End
