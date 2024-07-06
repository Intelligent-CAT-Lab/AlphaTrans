from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class Nysiis(StringEncoder):

    __strict: bool = False

    __TRUE_LENGTH: int = 6
    __SPACE: str = " "
    __PAT_DT_ETC: re.Pattern = re.compile("(DT|RT|RD|NT|ND)$")
    __PAT_EE_IE: re.Pattern = re.compile("(EE|IE)$")
    __PAT_SCH: re.Pattern = re.compile("^SCH")
    __PAT_PH_PF: re.Pattern = re.compile("^(PH|PF)")
    __PAT_K: re.Pattern = re.compile("^K")
    __PAT_KN: re.Pattern = re.compile("^KN")
    __PAT_MAC: re.Pattern = re.compile("^MAC")
    __CHARS_SSS: typing.List[str] = ["S", "S", "S"]
    __CHARS_S: typing.List[str] = ["S"]
    __CHARS_NN: typing.List[str] = ["N", "N"]
    __CHARS_N: typing.List[str] = ["N"]
    __CHARS_G: typing.List[str] = ["G"]
    __CHARS_FF: typing.List[str] = ["F", "F"]
    __CHARS_C: typing.List[str] = ["C"]
    __CHARS_AF: typing.List[str] = ["A", "F"]
    __CHARS_A: typing.List[str] = ["A"]

    def nysiis(self, str: str) -> str:
        if str is None:
            return None
        str = SoundexUtils.clean(str)
        if str == "":
            return str
        str = Nysiis.__PAT_MAC.sub("MCC", str)
        str = Nysiis.__PAT_KN.sub("NN", str)
        str = Nysiis.__PAT_K.sub("C", str)
        str = Nysiis.__PAT_PH_PF.sub("FF", str)
        str = Nysiis.__PAT_SCH.sub("SSS", str)
        str = Nysiis.__PAT_EE_IE.sub("Y", str)
        str = Nysiis.__PAT_DT_ETC.sub("D", str)
        key = [str[0]]
        chars = list(str)
        len = len(chars)
        for i in range(1, len):
            next = chars[i + 1] if i < len - 1 else Nysiis.__SPACE
            aNext = chars[i + 2] if i < len - 2 else Nysiis.__SPACE
            transcoded = Nysiis.__transcodeRemaining(
                chars[i - 1], chars[i], next, aNext
            )
            chars[i : i + len(transcoded)] = transcoded
            if chars[i] != chars[i - 1]:
                key.append(chars[i])
        if len(key) > 1:
            lastChar = key[-1]
            if lastChar == "S":
                key.pop()
                lastChar = key[-1]
            if len(key) > 2:
                last2Char = key[-2]
                if last2Char == "A" and lastChar == "Y":
                    key.pop(-2)
            if lastChar == "A":
                key.pop()
        string = "".join(key)
        return (
            string[: min(Nysiis.__TRUE_LENGTH, len(string))]
            if self.isStrict()
            else string
        )

    def isStrict(self) -> bool:
        return self.__strict

    def encode1(self, str: str) -> str:
        return self.nysiis(str)

    def encode0(self, obj: typing.Any) -> typing.Any:
        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Nysiis encode is not of type java.lang.String",
                None,
            )
        return self.nysiis(obj)

    @staticmethod
    def Nysiis1() -> Nysiis:
        return Nysiis(True)

    def __init__(self, strict: bool) -> None:
        self.__strict = strict

    @staticmethod
    def __transcodeRemaining(
        prev: str, curr: str, next: str, aNext: str
    ) -> typing.List[str]:
        if curr == "E" and next == "V":
            return Nysiis.__CHARS_AF
        if Nysiis.__isVowel(curr):
            return Nysiis.__CHARS_A
        if curr == "Q":
            return Nysiis.__CHARS_G
        if curr == "Z":
            return Nysiis.__CHARS_S
        if curr == "M":
            return Nysiis.__CHARS_N
        if curr == "K":
            if next == "N":
                return Nysiis.__CHARS_NN
            return Nysiis.__CHARS_C
        if curr == "S" and next == "C" and aNext == "H":
            return Nysiis.__CHARS_SSS
        if curr == "P" and next == "H":
            return Nysiis.__CHARS_FF
        if curr == "H" and (not Nysiis.__isVowel(prev) or not Nysiis.__isVowel(next)):
            return [prev]
        if curr == "W" and Nysiis.__isVowel(prev):
            return [prev]
        return [curr]

    @staticmethod
    def __isVowel(c: str) -> bool:
        return c == "A" or c == "E" or c == "I" or c == "O" or c == "U"
