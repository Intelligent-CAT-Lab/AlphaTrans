from __future__ import annotations
import re
import os
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class MatchRatingApproachEncoder(StringEncoder):

    __DOUBLE_CONSONANT: typing.List[str] = [
        "BB",
        "CC",
        "DD",
        "FF",
        "GG",
        "HH",
        "JJ",
        "KK",
        "LL",
        "MM",
        "NN",
        "PP",
        "QQ",
        "RR",
        "SS",
        "TT",
        "VV",
        "WW",
        "XX",
        "YY",
        "ZZ",
    ]
    __UNICODE: str = (
        "\u00C0\u00E0\u00C8\u00E8\u00CC\u00EC\u00D2\u00F2\u00D9\u00F9\u00C1\u00E1\u00C9\u00E9\u00CD\u00ED\u00D3\u00F3\u00DA\u00FA\u00DD\u00FD\u00C2\u00E2\u00CA\u00EA\u00CE\u00EE\u00D4\u00F4\u00DB\u00FB\u0176\u0177\u00C3\u00E3\u00D5\u00F5\u00D1\u00F1\u00C4\u00E4\u00CB\u00EB\u00CF\u00EF\u00D6\u00F6\u00DC\u00FC\u0178\u00FF\u00C5\u00E5\u00C7\u00E7\u0150\u0151\u0170\u0171"
    )
    __PLAIN_ASCII: str = (
        "AaEeIiOoUu"
        + "AaEeIiOoUuYy"
        + "AaEeIiOoUuYy"
        + "AaOoNn"
        + "AaEeIiOoUuYy"
        + "Aa"
        + "Cc"
        + "OoUu"
    )
    __EMPTY: str = ""
    __SPACE: str = " "

    def isEncodeEquals(self, name1: str, name2: str) -> bool:
        if name1 is None or self.__EMPTY == name1 or self.__SPACE == name1:
            return False
        if name2 is None or self.__EMPTY == name2 or self.__SPACE == name2:
            return False
        if len(name1) == 1 or len(name2) == 1:
            return False
        if name1 == name2:
            return True

        name1 = self.cleanName(name1)
        name2 = self.cleanName(name2)

        name1 = self.removeVowels(name1)
        name2 = self.removeVowels(name2)

        name1 = self.removeDoubleConsonants(name1)
        name2 = self.removeDoubleConsonants(name2)

        name1 = self.getFirst3Last3(name1)
        name2 = self.getFirst3Last3(name2)

        if abs(len(name1) - len(name2)) >= 3:
            return False

        sumLength = abs(len(name1) + len(name2))
        minRating = self.getMinRating(sumLength)

        count = self.leftToRightThenRightToLeftProcessing(name1, name2)

        return count >= minRating

    def encode1(self, name: str) -> str:
        if (
            name is None
            or self.__EMPTY == name
            or self.__SPACE == name
            or len(name) == 1
        ):
            return self.__EMPTY

        name = self.cleanName(name)

        name = self.removeVowels(name)

        name = self.removeDoubleConsonants(name)

        name = self.getFirst3Last3(name)

        return name

    def encode0(self, pObject: typing.Any) -> typing.Any:
        if not isinstance(pObject, str):
            raise EncoderException(
                "Parameter supplied to Match Rating Approach encoder is not of type"
                " java.lang.String",
                None,
            )
        return self.encode1(pObject)

    def removeVowels(self, name: str) -> str:
        firstLetter: str = name[0:1]

        name = name.replace("A", self.__EMPTY)
        name = name.replace("E", self.__EMPTY)
        name = name.replace("I", self.__EMPTY)
        name = name.replace("O", self.__EMPTY)
        name = name.replace("U", self.__EMPTY)

        name = re.sub(r"\s{2,}\b", self.__SPACE, name)

        if self.isVowel(firstLetter):
            return firstLetter + name
        return name

    def removeDoubleConsonants(self, name: str) -> str:
        replacedName = name.upper()
        for dc in self.__DOUBLE_CONSONANT:
            if dc in replacedName:
                singleLetter = dc[0]
                replacedName = replacedName.replace(dc, singleLetter)
        return replacedName

    def removeAccents(self, accentedWord: str) -> str:
        if accentedWord is None:
            return None

        sb = StringBuilder()
        n = len(accentedWord)

        for i in range(n):
            c = accentedWord[i]
            pos = UNICODE.index(c)
            if pos > -1:
                sb.append(PLAIN_ASCII[pos])
            else:
                sb.append(c)

        return sb.toString()

    def leftToRightThenRightToLeftProcessing(self, name1: str, name2: str) -> int:
        name1Char = list(name1)
        name2Char = list(name2)

        name1Size = len(name1) - 1
        name2Size = len(name2) - 1

        name1LtRStart = self.__EMPTY
        name1LtREnd = self.__EMPTY

        name2RtLStart = self.__EMPTY
        name2RtLEnd = self.__EMPTY

        for i in range(len(name1Char)):
            if i > name2Size:
                break

            name1LtRStart = name1[i : i + 1]
            name1LtREnd = name1[name1Size - i : name1Size - i + 1]

            name2RtLStart = name2[i : i + 1]
            name2RtLEnd = name2[name2Size - i : name2Size - i + 1]

            if name1LtRStart == name2RtLStart:
                name1Char[i] = " "
                name2Char[i] = " "

            if name1LtREnd == name2RtLEnd:
                name1Char[name1Size - i] = " "
                name2Char[name2Size - i] = " "

        strA = "".join(name1Char).replace(" ", "")
        strB = "".join(name2Char).replace(" ", "")

        if len(strA) > len(strB):
            return abs(6 - len(strA))
        return abs(6 - len(strB))

    def isVowel(self, letter: str) -> bool:
        return letter.lower() in ["e", "a", "o", "i", "u"]

    def getMinRating(self, sumLength: int) -> int:
        minRating = 0

        if sumLength <= 4:
            minRating = 5
        elif sumLength <= 7:  # aready know it is at least 5
            minRating = 4
        elif sumLength <= 11:  # aready know it is at least 8
            minRating = 3
        elif sumLength == 12:
            minRating = 2
        else:
            minRating = 1  # docs said little here.

        return minRating

    def getFirst3Last3(self, name: str) -> str:

        pass  # LLM could not translate this method

    def cleanName(self, name: str) -> str:
        upperName = name.upper()

        charsToTrim = ["\\-", "[&]", "\\'", "\\.", "[\\,]"]
        for str in charsToTrim:
            upperName = upperName.replace(str, self.__EMPTY)

        upperName = self.removeAccents(upperName)
        upperName = upperName.replace("\\s+", self.__EMPTY)

        return upperName
