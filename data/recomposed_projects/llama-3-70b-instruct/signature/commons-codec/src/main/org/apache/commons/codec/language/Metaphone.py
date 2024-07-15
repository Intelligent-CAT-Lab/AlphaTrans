from __future__ import annotations
import re
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
        hard: bool = False
        txtLength: int = 0
        if txt is None or (txtLength := len(txt)) == 0:
            return ""
        if txtLength == 1:
            return txt.upper()
        inwd: List[str] = list(txt.upper())
        local: List[str] = []  # manipulate
        code: List[str] = []  #   output
        match inwd[0]:
            case "K" | "G" | "P":  # looking for KN, etc
                if inwd[1] == "N":
                    local.extend(inwd[1:])
                else:
                    local.extend(inwd)
            case "A":  # looking for AE
                if inwd[1] == "E":
                    local.extend(inwd[1:])
                else:
                    local.extend(inwd)
            case "W":  # looking for WR or WH
                if inwd[1] == "R":  # WR -> R
                    local.extend(inwd[1:])
                elif inwd[1] == "H":
                    local.extend(inwd[1:])
                    local[0] = "W"  # WH -> W
                else:
                    local.extend(inwd)
            case "X":  # initial X becomes S
                inwd[0] = "S"
                local.extend(inwd)
            case _:
                local.extend(inwd)
        # now local has working string with initials fixed
        wdsz: int = len(local)
        n: int = 0
        while (
            len(code) < self.getMaxCodeLen() and n < wdsz
        ):  # max code size of 4 works well
            symb: str = local[n]
            if symb != "C" and self.__isPreviousChar(local, n, symb):
                n += 1
            else:  # not dup
                match symb:
                    case "A" | "E" | "I" | "O" | "U":
                        if n == 0:
                            code.append(symb)
                    case "B":
                        if self.__isPreviousChar(local, n, "M") and self.__isLastChar(
                            wdsz, n
                        ):  # B is silent if word ends in MB
                            pass
                        else:
                            code.append(symb)
                    case "C":  # lots of C special cases
                        # discard if SCI, SCE or SCY
                        if (
                            self.__isPreviousChar(local, n, "S")
                            and not self.__isLastChar(wdsz, n)
                            and self.__FRONTV.find(local[n + 1]) >= 0
                        ):
                            pass
                        if self.__regionMatch(local, n, "CIA"):  # "CIA" -> X
                            code.append("X")
                        elif (
                            not self.__isLastChar(wdsz, n)
                            and self.__FRONTV.find(local[n + 1]) >= 0
                        ):
                            code.append("S")  # CI,CE,CY -> S
                        elif self.__isPreviousChar(local, n, "S") and self.__isNextChar(
                            local, n, "H"
                        ):
                            code.append("K")  # SCH->sk
                        elif self.__isNextChar(local, n, "H"):  # detect CH
                            if n == 0 and wdsz >= 3 and self.__isVowel(local, 2):
                                code.append("K")  # CH consonant -> K consonant
                            else:
                                code.append("X")  # CHvowel -> X
                        else:
                            code.append("K")
                    case "D":
                        if (
                            not self.__isLastChar(wdsz, n + 1)
                            and self.__isNextChar(local, n, "G")
                            and self.__FRONTV.find(local[n + 2]) >= 0
                        ):
                            code.append("J")  # DGE DGI DGY -> J
                            n += 2
                        else:
                            code.append("T")
                    case "G":  # GH silent at end or before consonant
                        if self.__isLastChar(wdsz, n + 1) and self.__isNextChar(
                            local, n, "H"
                        ):
                            pass
                        elif (
                            not self.__isLastChar(wdsz, n + 1)
                            and self.__isNextChar(local, n, "H")
                            and not self.__isVowel(local, n + 2)
                        ):
                            pass
                        elif n > 0 and (
                            self.__regionMatch(local, n, "GN")
                            or self.__regionMatch(local, n, "GNED")
                        ):
                            pass  # silent G
                        else:
                            hard = self.__isPreviousChar(local, n, "G")
                            if (
                                not self.__isLastChar(wdsz, n)
                                and self.__FRONTV.find(local[n + 1]) >= 0
                                and not hard
                            ):
                                code.append("J")
                            else:
                                code.append("K")
                    case "H":
                        if self.__isLastChar(wdsz, n):
                            pass  # terminal H
                        elif n > 0 and self.__VARSON.find(local[n - 1]) >= 0:
                            pass
                        elif self.__isVowel(local, n + 1):
                            code.append("H")  # Hvowel
                    case "F" | "J" | "L" | "M" | "N" | "R":
                        code.append(symb)
                    case "K":
                        if n > 0:  # not initial
                            if not self.__isPreviousChar(local, n, "C"):
                                code.append(symb)
                        else:
                            code.append(symb)  # initial K
                    case "P":
                        if self.__isNextChar(local, n, "H"):
                            code.append("F")
                        else:
                            code.append(symb)
                    case "Q":
                        code.append("K")
                    case "S":
                        if (
                            self.__regionMatch(local, n, "SH")
                            or self.__regionMatch(local, n, "SIO")
                            or self.__regionMatch(local, n, "SIA")
                        ):
                            code.append("X")
                        else:
                            code.append("S")
                    case "T":
                        if self.__regionMatch(local, n, "TIA") or self.__regionMatch(
                            local, n, "TIO"
                        ):
                            code.append("X")
                            break
                        elif self.__regionMatch(local, n, "TCH"):
                            pass
                        elif self.__regionMatch(local, n, "TH"):
                            code.append("0")
                        else:
                            code.append("T")
                    case "V":
                        code.append("F")
                    case "W" | "Y":  # silent if not followed by vowel
                        if not self.__isLastChar(wdsz, n) and self.__isVowel(
                            local, n + 1
                        ):
                            code.append(symb)
                    case "X":
                        code.append("K")
                        code.append("S")
                    case "Z":
                        code.append("S")
                    case _:
                        pass
            # end switch
            n += 1
        if len(code) > self.getMaxCodeLen():
            code = code[: self.getMaxCodeLen()]
        return "".join(code)

    def __init__(self) -> None:
        pass

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
