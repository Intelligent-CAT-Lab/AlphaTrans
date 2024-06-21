from __future__ import annotations
import re
from dataclasses import field
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.language.SoundexUtils import *


class Nysiis(StringEncoder):

    __strict: bool = None

    __TRUE_LENGTH: int = 6

    __SPACE: str = " "
    __PAT_DT_ETC: re.Pattern = None  # LLM could not translate this field
    __PAT_EE_IE: re.Pattern = None  # LLM could not translate this field
    __PAT_SCH: re.Pattern = None  # LLM could not translate this field
    __PAT_PH_PF: re.Pattern = None  # LLM could not translate this field
    __PAT_K: re.Pattern = None  # LLM could not translate this field
    __PAT_KN: re.Pattern = None  # LLM could not translate this field
    __PAT_MAC: re.Pattern = None  # LLM could not translate this field

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

        if not str:
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
            aNext_char = chars[i + 2] if i < len_chars - 2 else self.__SPACE
            transcoded = self.__transcodeRemaining(
                chars[i - 1], chars[i], next_char, aNext_char
            )
            chars[i : i + 1] = transcoded

            if chars[i] != chars[i - 1]:
                key.append(chars[i])

        if len(key) > 1:
            lastChar = key[-1]

            if lastChar == "S":
                key = key[:-1]
                lastChar = key[-1]

            if len(key) > 2:
                last2Char = key[-2]
                if last2Char == "A" and lastChar == "Y":
                    key = key[:-2]

            if lastChar == "A":
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
        elif curr == "Z":
            return Nysiis.__CHARS_S
        elif curr == "M":
            return Nysiis.__CHARS_N
        elif curr == "K":
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

        return c.upper() in ["A", "E", "I", "O", "U"]
