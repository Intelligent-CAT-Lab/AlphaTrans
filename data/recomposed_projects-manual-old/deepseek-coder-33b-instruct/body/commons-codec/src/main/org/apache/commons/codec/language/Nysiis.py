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

        str = re.sub(self.__PAT_MAC, "MCC", str)
        str = re.sub(self.__PAT_KN, "NN", str)
        str = re.sub(self.__PAT_K, "C", str)
        str = re.sub(self.__PAT_PH_PF, "FF", str)
        str = re.sub(self.__PAT_SCH, "SSS", str)

        str = re.sub(self.__PAT_EE_IE, "Y", str)
        str = re.sub(self.__PAT_DT_ETC, "D", str)

        key = [str[0]]

        chars = list(str)
        len_chars = len(chars)

        for i in range(1, len_chars):
            next_char = chars[i + 1] if i < len_chars - 1 else self.__SPACE
            aNext = chars[i + 2] if i < len_chars - 2 else self.__SPACE
            transcoded = self.__transcodeRemaining(
                chars[i - 1], chars[i], next_char, aNext
            )
            chars[i : i + len(transcoded)] = transcoded

            if chars[i] != chars[i - 1]:
                key.append(chars[i])

        if len(key) > 1:
            last_char = key[-1]

            if last_char == "S":
                key = key[:-1]
                last_char = key[-1]

            if len(key) > 2:
                last_2_char = key[-2]
                if last_2_char == "A" and last_char == "Y":
                    key = key[:-2]

            if last_char == "A":
                key = key[:-1]

        string = "".join(key)
        return (
            string[: min(self.__TRUE_LENGTH, len(string))]
            if self.isStrict()
            else string
        )

    def isStrict(self) -> bool:
        return self.__strict

    def encode1(self, str: str) -> str:

        if str is None:
            return None

        str = SoundexUtils.clean(str)

        if str == "":
            return str

        str = re.sub(self.__PAT_MAC, "MCC", str)
        str = re.sub(self.__PAT_KN, "NN", str)
        str = re.sub(self.__PAT_K, "C", str)
        str = re.sub(self.__PAT_PH_PF, "FF", str)
        str = re.sub(self.__PAT_SCH, "SSS", str)

        str = re.sub(self.__PAT_EE_IE, "Y", str)
        str = re.sub(self.__PAT_DT_ETC, "D", str)

        key = [str[0]]

        chars = list(str)
        len_chars = len(chars)

        for i in range(1, len_chars):
            next_char = chars[i + 1] if i < len_chars - 1 else self.__SPACE
            aNext = chars[i + 2] if i < len_chars - 2 else self.__SPACE
            transcoded = self.__transcodeRemaining(
                chars[i - 1], chars[i], next_char, aNext
            )
            chars[i : i + len(transcoded)] = transcoded

            if chars[i] != chars[i - 1]:
                key.append(chars[i])

        if len(key) > 1:
            last_char = key[-1]

            if last_char == "S":
                key = key[:-1]
                last_char = key[-1]

            if len(key) > 2:
                last_2_char = key[-2]
                if last_2_char == "A" and last_char == "Y":
                    key = key[:-2]

            if last_char == "A":
                key = key[:-1]

        string = "".join(key)
        return (
            string[: min(self.__TRUE_LENGTH, len(string))]
            if self.isStrict()
            else string
        )

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
        self.__TRUE_LENGTH = 6
        self.__SPACE = " "
        self.__PAT_DT_ETC = re.compile("(DT|RT|RD|NT|ND)$")
        self.__PAT_EE_IE = re.compile("(EE|IE)$")
        self.__PAT_SCH = re.compile("^SCH")
        self.__PAT_PH_PF = re.compile("^(PH|PF)")
        self.__PAT_K = re.compile("^K")
        self.__PAT_KN = re.compile("^KN")
        self.__PAT_MAC = re.compile("^MAC")
        self.__CHARS_SSS = ["S", "S", "S"]
        self.__CHARS_S = ["S"]
        self.__CHARS_NN = ["N", "N"]
        self.__CHARS_N = ["N"]
        self.__CHARS_G = ["G"]
        self.__CHARS_FF = ["F", "F"]
        self.__CHARS_C = ["C"]
        self.__CHARS_AF = ["A", "F"]
        self.__CHARS_A = ["A"]

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
        elif curr == "Z":
            return Nysiis.__CHARS_S
        elif curr == "M":
            return Nysiis.__CHARS_N
        elif curr == "K":
            if next == "N":
                return Nysiis.__CHARS_NN
            else:
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
