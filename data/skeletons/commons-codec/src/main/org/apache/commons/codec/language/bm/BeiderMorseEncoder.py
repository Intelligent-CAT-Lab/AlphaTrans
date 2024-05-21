from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io

# Imports End


class BeiderMorseEncoder(StringEncoder):

    # Class Fields Begin
    __engine: PhoneticEngine = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: str) -> str:
        pass

    def encode(self, source: typing.Any) -> typing.Any:
        pass

    def setMaxPhonemes(self, maxPhonemes: int) -> None:
        pass

    def setRuleType(self, ruleType: RuleType) -> None:
        pass

    def setNameType(self, nameType: NameType) -> None:
        pass

    def setConcat(self, concat: bool) -> None:
        pass

    def isConcat(self) -> bool:
        pass

    def getRuleType(self) -> RuleType:
        pass

    def getNameType(self) -> NameType:
        pass

    def encode1(self, source: str) -> str:
        pass

    def encode0(self, source: typing.Any) -> typing.Any:
        pass

    # Class Methods End
