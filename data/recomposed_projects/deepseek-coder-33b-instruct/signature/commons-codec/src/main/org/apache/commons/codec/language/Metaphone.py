from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class Metaphone(StringEncoder):

    __maxCodeLen: int = 4
    __VARSON: str = "CSPTG"
    __FRONTV: str = "EIY"
    __VOWELS: str = "AEIOU"

    def setMaxCodeLen(self, maxCodeLen: int) -> None:
        self.__maxCodeLen = maxCodeLen

    def getMaxCodeLen(self) -> int:
        return self.__maxCodeLen

    def isMetaphoneEqual(self, str1: str, str2: str) -> bool:
        return self.metaphone(str1) == self.metaphone(str2)

    def encode1(self, str: str) -> str:
        return self.metaphone(str)

    def encode0(self, obj: typing.Any) -> typing.Any:

        if not isinstance(obj, str):
            raise EncoderException(
                "Parameter supplied to Metaphone encode is not of type java.lang.String",
                None,
            )
        return self.metaphone(obj)

    def metaphone(self, txt: str) -> str:

        hard = False
        txtLength = len(txt) if txt else 0
        if txtLength == 0:
            return ""
        if txtLength == 1:
            return txt.upper()

        inwd = list(txt.upper())

        local = io.StringIO()  # manipulate
        code = io.StringIO()  # output

        if inwd[0] in ["K", "G", "P"]:  # looking for KN, etc
            if inwd[1] == "N":
                local.write("".join(inwd[1:]))
            else:
                local.write("".join(inwd))
        elif inwd[0] == "A":  # looking for AE
            if inwd[1] == "E":
                local.write("".join(inwd[1:]))
            else:
                local.write("".join(inwd))
        elif inwd[0] == "W":  # looking for WR or WH
            if inwd[1] == "R":  # WR -> R
                local.write("".join(inwd[1:]))
            elif inwd[1] == "H":
                local.write("".join(inwd[1:]))
                local.seek(0)
                local.write("W")  # WH -> W
            else:
                local.write("".join(inwd))
        elif inwd[0] == "X":  # initial X becomes S
            inwd[0] = "S"
            local.write("".join(inwd))
        else:
            local.write("".join(inwd))

        local.seek(0)
        wdsz = len(local.getvalue())
        n = 0

        while (
            len(code.getvalue()) < self.getMaxCodeLen() and n < wdsz
        ):  # max code size of 4 works well
            symb = local.getvalue()[n]
            if symb != "C" and self.__isPreviousChar(local.getvalue(), n, symb):
                n += 1
            else:  # not dup
                if symb in ["A", "E", "I", "O", "U"]:
                    if n == 0:
                        code.write(symb)
                elif symb == "B":
                    if self.__isPreviousChar(
                        local.getvalue(), n, "M"
                    ) and self.__isLastChar(
                        wdsz, n
                    ):  # B is silent if word ends in MB
                        break
                    code.write(symb)
                elif symb == "C":  # lots of C special cases
                    # discard if SCI, SCE or SCY
                    if (
                        self.__isPreviousChar(local.getvalue(), n, "S")
                        and not self.__isLastChar(wdsz, n)
                        and self.__FRONTV.find(local.getvalue()[n + 1]) >= 0
                    ):
                        break
                    if self.__regionMatch(local.getvalue(), n, "CIA"):  # "CIA" -> X
                        code.write("X")
                        break
                    if (
                        not self.__isLastChar(wdsz, n)
                        and self.__FRONTV.find(local.getvalue()[n + 1]) >= 0
                    ):
                        code.write("S")
                        break  # CI,CE,CY -> S
                    if self.__isPreviousChar(
                        local.getvalue(), n, "S"
                    ) and self.__isNextChar(
                        local.getvalue(), n, "H"
                    ):  # SCH->sk
                        code.write("K")
                        break
                    if self.__isNextChar(local.getvalue(), n, "H"):  # detect CH
                        if (
                            n == 0 and wdsz >= 3 and self.__isVowel(local.getvalue(), 2)
                        ):  # CH consonant -> K consonant
                            code.write("K")
                        else:
                            code.write("X")  # CHvowel -> X
                    else:
                        code.write("K")
                elif symb == "D":
                    if (
                        not self.__isLastChar(wdsz, n + 1)
                        and self.__isNextChar(local.getvalue(), n, "G")
                        and self.__FRONTV.find(local.getvalue()[n + 2]) >= 0
                    ):  # DGE DGI DGY -> J
                        code.write("J")
                        n += 2
                    else:
                        code.write("T")
                elif symb in ["F", "J", "L", "M", "N", "R"]:
                    code.write(symb)
                elif symb == "K":
                    if n > 0:  # not initial
                        if not self.__isPreviousChar(local.getvalue(), n, "C"):
                            code.write(symb)
                    else:
                        code.write(symb)  # initial K
                elif symb == "P":
                    if self.__isNextChar(local.getvalue(), n, "H"):
                        code.write("F")
                    else:
                        code.write(symb)
                elif symb == "Q":
                    code.write("K")
                elif symb == "S":
                    if (
                        self.__regionMatch(local.getvalue(), n, "SH")
                        or self.__regionMatch(local.getvalue(), n, "SIO")
                        or self.__regionMatch(local.getvalue(), n, "SIA")
                    ):
                        code.write("X")
                    else:
                        code.write("S")
                elif symb == "T":
                    if self.__regionMatch(
                        local.getvalue(), n, "TIA"
                    ) or self.__regionMatch(local.getvalue(), n, "TIO"):
                        code.write("X")
                        break
                    if self.__regionMatch(local.getvalue(), n, "TCH"):
                        break
                    if self.__regionMatch(local.getvalue(), n, "TH"):
                        code.write("0")
                    else:
                        code.write("T")
                elif symb == "V":
                    code.write("F")
                elif symb in ["W", "Y"]:  # silent if not followed by vowel
                    if not self.__isLastChar(wdsz, n) and self.__isVowel(
                        local.getvalue(), n + 1
                    ):
                        code.write(symb)
                elif symb == "X":
                    code.write("K")
                    code.write("S")
                elif symb == "Z":
                    code.write("S")
                n += 1
            if len(code.getvalue()) > self.getMaxCodeLen():
                code.truncate(self.getMaxCodeLen())

        return code.getvalue()

    def __init__(self) -> None:

        pass  # LLM could not translate this method

    def __isLastChar(self, wdsz: int, n: int) -> bool:
        return n + 1 == wdsz

    def __regionMatch(self, string: str, index: int, test: str) -> bool:

        matches = False
        if index >= 0 and index + len(test) - 1 < len(string):
            substring = string[index : index + len(test)]
            matches = substring == test
        return matches

    def __isNextChar(self, string: str, index: int, c: str) -> bool:

        matches = False
        if index >= 0 and index < len(string) - 1:
            matches = string[index + 1] == c
        return matches

    def __isPreviousChar(self, string: str, index: int, c: str) -> bool:

        matches = False
        if index > 0 and index < len(string):
            matches = string[index - 1] == c
        return matches

    def __isVowel(self, string: str, index: int) -> bool:
        return self.__VOWELS.find(string[index]) >= 0
