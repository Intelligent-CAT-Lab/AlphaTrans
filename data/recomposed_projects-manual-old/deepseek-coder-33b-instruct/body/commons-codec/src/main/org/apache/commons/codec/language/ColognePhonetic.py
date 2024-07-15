from __future__ import annotations
import copy
import re
from abc import ABC
import io
import typing
from typing import *
import os
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class CologneBuffer(ABC):

    _length: int = 0
    _data: typing.List[str] = None

    def toString(self) -> str:
        return "".join(self._copyData(0, self._length))

    def isEmpty(self) -> bool:
        return self.length() == 0

    def length(self) -> int:
        return self._length

    def __init__(
        self, constructorId: int, data: typing.List[str], buffSize: int
    ) -> None:

        if constructorId == 0:
            self._data = [""] * buffSize
            self._length = 0
        else:
            self._data = data
            self._length = len(data)

    def _copyData(self, start: int, length: int) -> typing.List[str]:
        return self._data[start : start + length]


class CologneInputBuffer(CologneBuffer):

    def _copyData(self, start: int, length: int) -> typing.List[str]:

        newData = [""] * length
        newData = self.data[
            len(self.data)
            - self.length
            + start : len(self.data)
            - self.length
            + start
            + length
        ]
        return newData

    def removeNext(self) -> str:
        ch = self.getNextChar()
        self.length -= 1
        return ch

    def _getNextPos(self) -> int:
        return len(self.data) - self.length

    def getNextChar(self) -> str:
        return self.data[self._getNextPos()]

    def __init__(self, data: typing.List[str]) -> None:

        super().__init__(1, data, 0)


class CologneOutputBuffer(CologneBuffer):

    __lastCode: str = ""

    def _copyData(self, start: int, length: int) -> typing.List[str]:

        newData = [""] * length
        newData[0:length] = self.data[start : start + length]
        return newData

    def put(self, code: str) -> None:

        if (
            code != self.CHAR_IGNORE
            and self.__lastCode != code
            and (code != "0" or self.length == 0)
        ):
            self.data[self.length] = code
            self.length += 1

        self.__lastCode = code

    def __init__(self, buffSize: int) -> None:

        super().__init__(0, None, buffSize)
        self.__lastCode = "/"  # impossible value


class ColognePhonetic(StringEncoder):

    __CHAR_IGNORE: str = "-"
    __DTX: typing.List[str] = ["D", "T", "X"]
    __AHKOQUX: typing.List[str] = ["A", "H", "K", "O", "Q", "U", "X"]
    __SZ: typing.List[str] = ["S", "Z"]
    __AHKLOQRUX: typing.List[str] = ["A", "H", "K", "L", "O", "Q", "R", "U", "X"]
    __CKQ: typing.List[str] = ["C", "K", "Q"]
    __GKQ: typing.List[str] = ["G", "K", "Q"]
    __FPVW: typing.List[str] = ["F", "P", "V", "W"]
    __CSZ: typing.List[str] = ["C", "S", "Z"]
    __AEIJOUY: typing.List[str] = ["A", "E", "I", "J", "O", "U", "Y"]

    def isEncodeEqual(self, text1: str, text2: str) -> bool:
        return self.colognePhonetic(text1) == self.colognePhonetic(text2)

    def encode1(self, text: str) -> str:

        if text is None:
            return None

        input = CologneInputBuffer(self.__preprocess(text))
        output = CologneOutputBuffer(input.length() * 2)

        nextChar = None

        lastChar = self.__CHAR_IGNORE
        chr = None

        while not input.isEmpty():
            chr = input.removeNext()

            if not input.isEmpty():
                nextChar = input.getNextChar()
            else:
                nextChar = self.__CHAR_IGNORE

            if chr < "A" or chr > "Z":
                continue  # ignore unwanted characters

            if self.__arrayContains(self.__AEIJOUY, chr):
                output.put("0")
            elif chr == "B" or (chr == "P" and nextChar != "H"):
                output.put("1")
            elif (chr == "D" or chr == "T") and not self.__arrayContains(
                self.__CSZ, nextChar
            ):
                output.put("2")
            elif self.__arrayContains(self.__FPVW, chr):
                output.put("3")
            elif self.__arrayContains(self.__GKQ, chr):
                output.put("4")
            elif chr == "X" and not self.__arrayContains(self.__CKQ, lastChar):
                output.put("4")
                output.put("8")
            elif chr == "S" or chr == "Z":
                output.put("8")
            elif chr == "C":
                if output.isEmpty():
                    if self.__arrayContains(self.__AHKLOQRUX, nextChar):
                        output.put("4")
                    else:
                        output.put("8")
                elif self.__arrayContains(
                    self.__SZ, lastChar
                ) or not self.__arrayContains(self.__AHKOQUX, nextChar):
                    output.put("8")
                else:
                    output.put("4")
            elif self.__arrayContains(self.__DTX, chr):
                output.put("8")
            else:
                if chr == "R":
                    output.put("7")
                elif chr == "L":
                    output.put("5")
                elif chr == "M" or chr == "N":
                    output.put("6")
                elif chr == "H":
                    output.put(self.__CHAR_IGNORE)  # needed by put

            lastChar = chr

        return output.toString()

    def encode0(self, object: typing.Any) -> typing.Any:

        if not isinstance(object, str):
            raise EncoderException(
                "This method's parameter was expected to be of the type "
                + str.__name__
                + ". But actually it was of the type "
                + type(object).__name__
                + ".",
                None,
            )
        return self.encode1(object)

    def colognePhonetic(self, text: str) -> str:

        if text is None:
            return None

        input = CologneInputBuffer(self.__preprocess(text))
        output = CologneOutputBuffer(input.length() * 2)

        nextChar = None

        lastChar = self.__CHAR_IGNORE
        chr = None

        while not input.isEmpty():
            chr = input.removeNext()

            if not input.isEmpty():
                nextChar = input.getNextChar()
            else:
                nextChar = self.__CHAR_IGNORE

            if chr < "A" or chr > "Z":
                continue  # ignore unwanted characters

            if self.__arrayContains(self.__AEIJOUY, chr):
                output.put("0")
            elif chr == "B" or (chr == "P" and nextChar != "H"):
                output.put("1")
            elif (chr == "D" or chr == "T") and not self.__arrayContains(
                self.__CSZ, nextChar
            ):
                output.put("2")
            elif self.__arrayContains(self.__FPVW, chr):
                output.put("3")
            elif self.__arrayContains(self.__GKQ, chr):
                output.put("4")
            elif chr == "X" and not self.__arrayContains(self.__CKQ, lastChar):
                output.put("4")
                output.put("8")
            elif chr == "S" or chr == "Z":
                output.put("8")
            elif chr == "C":
                if output.isEmpty():
                    if self.__arrayContains(self.__AHKLOQRUX, nextChar):
                        output.put("4")
                    else:
                        output.put("8")
                elif self.__arrayContains(
                    self.__SZ, lastChar
                ) or not self.__arrayContains(self.__AHKOQUX, nextChar):
                    output.put("8")
                else:
                    output.put("4")
            elif self.__arrayContains(self.__DTX, chr):
                output.put("8")
            else:
                if chr == "R":
                    output.put("7")
                elif chr == "L":
                    output.put("5")
                elif chr == "M" or chr == "N":
                    output.put("6")
                elif chr == "H":
                    output.put(self.__CHAR_IGNORE)  # needed by put

            lastChar = chr

        return output.toString()

    def __preprocess(self, text: str) -> typing.List[str]:

        chrs = list(text.upper())

        for index in range(len(chrs)):
            if chrs[index] == "\u00C4":  # capital A, umlaut mark
                chrs[index] = "A"
            elif chrs[index] == "\u00DC":  # capital U, umlaut mark
                chrs[index] = "U"
            elif chrs[index] == "\u00D6":  # capital O, umlaut mark
                chrs[index] = "O"

        return chrs

    @staticmethod
    def __arrayContains(arr: typing.List[str], key: str) -> bool:
        for element in arr:
            if element == key:
                return True
        return False
