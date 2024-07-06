from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.PhoneticEngine import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *


class BeiderMorseEncoder(StringEncoder):

    __engine: PhoneticEngine = PhoneticEngine.PhoneticEngine0(
        NameType.GENERIC, RuleType.APPROX, True
    )

    def setMaxPhonemes(self, maxPhonemes: int) -> None:
        self.__engine = PhoneticEngine(
            self.__engine.getNameType(),
            self.__engine.getRuleType(),
            self.__engine.isConcat(),
            maxPhonemes,
        )

    def setRuleType(self, ruleType: RuleType) -> None:
        self.__engine = PhoneticEngine(
            self.__engine.getNameType(),
            ruleType,
            self.__engine.isConcat(),
            self.__engine.getMaxPhonemes(),
        )

    def setNameType(self, nameType: NameType) -> None:
        self.__engine = PhoneticEngine(
            nameType,
            self.__engine.getRuleType(),
            self.__engine.isConcat(),
            self.__engine.getMaxPhonemes(),
        )

    def setConcat(self, concat: bool) -> None:
        self.__engine = PhoneticEngine(
            self.__engine.getNameType(),
            self.__engine.getRuleType(),
            concat,
            self.__engine.getMaxPhonemes(),
        )

    def isConcat(self) -> bool:
        return self.__engine.isConcat()

    def getRuleType(self) -> RuleType:
        return self.__engine.getRuleType()

    def getNameType(self) -> NameType:
        return self.__engine.getNameType()

    def encode1(self, source: str) -> str:

        pass  # LLM could not translate this method

    def encode0(self, source: typing.Any) -> typing.Any:

        pass  # LLM could not translate this method
