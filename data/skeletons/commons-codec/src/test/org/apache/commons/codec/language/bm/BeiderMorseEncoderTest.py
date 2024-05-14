# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.Rule import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.language.bm.Lang import *
from src.main.org.apache.commons.codec.language.bm.BeiderMorseEncoder import *
from src.main.org.apache.commons.codec.StringEncoderAbstractTest import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing

# Imports End


class BeiderMorseEncoderTest(StringEncoderAbstractTest):

    # Class Fields Begin
    __TEST_CHARS: typing.List[str] = None
    # Class Fields End

    # Class Methods Begin
    def testSpeedCheck3(self) -> None:
        pass

    def testSpeedCheck2(self) -> None:
        pass

    def testSpeedCheck(self) -> None:
        pass

    def testSetRuleTypeToRulesIllegalArgumentException(self) -> None:
        pass

    def testSetRuleTypeExact(self) -> None:
        pass

    def testSetNameTypeAsh(self) -> None:
        pass

    def testSetConcat(self) -> None:
        pass

    def testOOM(self) -> None:
        pass

    def testNegativeIndexForRuleMatchIndexOutOfBoundsException(self) -> None:
        pass

    def testLongestEnglishSurname(self) -> None:
        pass

    def testInvalidLanguageIllegalArgumentException(self) -> None:
        pass

    def testInvalidLangIllegalStateException(self) -> None:
        pass

    def testInvalidLangIllegalArgumentException(self) -> None:
        pass

    def testEncodeGna(self) -> None:
        pass

    def testEncodeAtzNotEmpty(self) -> None:
        pass

    def testAsciiEncodeNotEmpty2Letters(self) -> None:
        pass

    def testAsciiEncodeNotEmpty1Letter(self) -> None:
        pass

    def testAllChars(self) -> None:
        pass

    def _createStringEncoder(self) -> StringEncoder:
        pass

    def __createGenericApproxEncoder(self) -> BeiderMorseEncoder:
        pass

    def __assertNotEmpty(self, bmpm: BeiderMorseEncoder, value: str) -> None:
        pass

    # Class Methods End
