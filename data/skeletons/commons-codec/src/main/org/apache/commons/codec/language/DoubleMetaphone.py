from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import typing
from typing import *
import io
from io import StringIO

# Imports End


class DoubleMetaphoneResult:

    # Class Fields Begin
    __primary: typing.Union[typing.List[str], io.StringIO] = None
    __alternate: typing.Union[typing.List[str], io.StringIO] = None
    __maxLength: int = None
    # Class Fields End

    # Class Methods Begin
    def isComplete(self) -> bool:
        pass

    def getAlternate(self) -> str:
        pass

    def getPrimary(self) -> str:
        pass

    def appendAlternate1(self, value: str) -> None:
        pass

    def appendPrimary1(self, value: str) -> None:
        pass

    def append3(self, primary: str, alternate: str) -> None:
        pass

    def append2(self, value: str) -> None:
        pass

    def appendAlternate0(self, value: str) -> None:
        pass

    def appendPrimary0(self, value: str) -> None:
        pass

    def append1(self, primary: str, alternate: str) -> None:
        pass

    def append0(self, value: str) -> None:
        pass

    def __init__(self, maxLength: int) -> None:
        pass

    # Class Methods End


class DoubleMetaphone(StringEncoder):

    # Class Fields Begin
    __VOWELS: str = None
    __SILENT_START: typing.List[typing.List[str]] = None
    __L_R_N_M_B_H_F_V_W_SPACE: typing.List[typing.List[str]] = None
    __ES_EP_EB_EL_EY_IB_IL_IN_IE_EI_ER: typing.List[typing.List[str]] = None
    __L_T_K_S_N_M_B_Z: typing.List[typing.List[str]] = None
    __maxCodeLen: int = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, value: str) -> str:
        pass

    def encode(self, obj: typing.Any) -> typing.Any:
        pass

    @staticmethod
    def _contains(
        value: str, start: int, length: int, criteria: typing.List[typing.List[str]]
    ) -> bool:
        pass

    def _charAt(self, value: str, index: int) -> str:
        pass

    def setMaxCodeLen(self, maxCodeLen: int) -> None:
        pass

    def getMaxCodeLen(self) -> int:
        pass

    def isDoubleMetaphoneEqual1(
        self, value1: str, value2: str, alternate: bool
    ) -> bool:
        pass

    def isDoubleMetaphoneEqual0(self, value1: str, value2: str) -> bool:
        pass

    def encode1(self, value: str) -> str:
        pass

    def encode0(self, obj: typing.Any) -> typing.Any:
        pass

    def doubleMetaphone1(self, value: str, alternate: bool) -> str:
        pass

    def doubleMetaphone0(self, value: str) -> str:
        pass

    def __init__(self) -> None:
        pass

    def __cleanInput(self, input_: str) -> str:
        pass

    def __isSilentStart(self, value: str) -> bool:
        pass

    def __isVowel(self, ch: str) -> bool:
        pass

    def __isSlavoGermanic(self, value: str) -> bool:
        pass

    def __conditionM0(self, value: str, index: int) -> bool:
        pass

    def __conditionL0(self, value: str, index: int) -> bool:
        pass

    def __conditionCH1(self, value: str, index: int) -> bool:
        pass

    def __conditionCH0(self, value: str, index: int) -> bool:
        pass

    def __conditionC0(self, value: str, index: int) -> bool:
        pass

    def __handleZ(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        pass

    def __handleX(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleW(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleT(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleSC(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleS(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        pass

    def __handleR(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        pass

    def __handleP(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleL(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleJ(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        pass

    def __handleH(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleGH(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleG(
        self, value: str, result: DoubleMetaphoneResult, index: int, slavoGermanic: bool
    ) -> int:
        pass

    def __handleD(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleCH(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleCC(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleC(self, value: str, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    def __handleAEIOUY(self, result: DoubleMetaphoneResult, index: int) -> int:
        pass

    # Class Methods End
