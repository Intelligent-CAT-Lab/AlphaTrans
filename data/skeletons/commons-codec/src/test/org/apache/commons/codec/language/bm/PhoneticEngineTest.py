# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
import typing

# Imports End


class PhoneticEngineTest:

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
    def testEncode(self) -> None:
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
