from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.CharEncoding import *
from src.main.org.apache.commons.codec.language.bm.RuleType import *
from src.main.org.apache.commons.codec.language.bm.Rule1 import *
from src.main.org.apache.commons.codec.language.bm.ResourceConstants import *
from src.main.org.apache.commons.codec.language.bm.NameType import *
from src.main.org.apache.commons.codec.language.bm.Languages import *
from src.main.org.apache.commons.codec.Resources import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class Branch:

    # Class Fields Begin
    __builder: typing.Union[typing.List[str], io.StringIO] = None
    __cachedString: str = None
    __lastReplacement: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, other: typing.Any) -> bool:
        pass

    def processNextReplacement(self, replacement: str, forceAppend: bool) -> None:
        pass

    def finish(self) -> None:
        pass

    def createBranch(self) -> Branch:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End


class Rule:

    # Class Fields Begin
    __pattern: str = None
    __replacementAtStart: typing.List[typing.List[str]] = None
    __replacementBeforeVowel: typing.List[typing.List[str]] = None
    __replacementDefault: typing.List[typing.List[str]] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def matches(self, context: str) -> bool:
        pass

    def getReplacements(
        self, context: str, atStart: bool
    ) -> typing.List[typing.List[str]]:
        pass

    def getPatternLength(self) -> int:
        pass

    def __init__(
        self,
        pattern: str,
        replacementAtStart: str,
        replacementBeforeVowel: str,
        replacementDefault: str,
    ) -> None:
        pass

    def __isVowel(self, ch: str) -> bool:
        pass

    # Class Methods End


class DaitchMokotoffSoundex(StringEncoder):

    # Class Fields Begin
    __COMMENT: str = None
    __DOUBLE_QUOTE: str = None
    __MULTILINE_COMMENT_END: str = None
    __MULTILINE_COMMENT_START: str = None
    __RESOURCE_FILE: str = None
    __MAX_LENGTH: int = None
    __RULES: typing.Dict[str, typing.List[Rule]] = None
    __FOLDINGS: typing.Dict[str, str] = None
    __folding: bool = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, source: str) -> str:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    def soundex0(self, source: str) -> str:
        pass

    def encode1(self, source: str) -> str:
        pass

    def encode0(self, obj: typing.Any) -> typing.Any:
        pass

    @staticmethod
    def DaitchMokotoffSoundex1() -> DaitchMokotoffSoundex:
        pass

    def __init__(self, folding: bool) -> None:
        pass

    def __soundex1(self, source: str, branching: bool) -> typing.List[typing.List[str]]:
        pass

    def __cleanup(self, input_: str) -> str:
        pass

    @staticmethod
    def __stripQuotes(str_: str) -> str:
        pass

    @staticmethod
    def __parseRules(
        scanner: typing.Any,
        location: str,
        ruleMapping: typing.Dict[str, typing.List[Rule]],
        asciiFoldings: typing.Dict[str, str],
    ) -> None:
        pass

    # Class Methods End
