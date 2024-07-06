from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *


class RegexValidator:

    __patterns: typing.List[re.Pattern] = None

    __serialVersionUID: int = -8832409930574867162

    def toString(self) -> str:
        buffer = io.StringIO()
        buffer.write("RegexValidator{")
        for i in range(len(self.__patterns)):
            if i > 0:
                buffer.write(",")
            buffer.write(self.__patterns[i].pattern())
        buffer.write("}")
        return buffer.getvalue()

    def validate(self, value: str) -> str:
        if value is None:
            return None
        for i in range(len(self.__patterns)):
            matcher = self.__patterns[i].matcher(value)
            if matcher.matches():
                count = matcher.groupCount()
                if count == 1:
                    return matcher.group(1)
                buffer = StringBuilder()
                for j in range(count):
                    component = matcher.group(j + 1)
                    if component is not None:
                        buffer.append(component)
                return buffer.toString()
        return None

    def match(self, value: str) -> typing.List[str]:
        if value is None:
            return None
        for i in range(len(self.__patterns)):
            matcher = self.__patterns[i].match(value)
            if matcher is not None:
                count = matcher.lastindex
                groups = [None] * count
                for j in range(count):
                    groups[j] = matcher.group(j + 1)
                return groups
        return None

    def isValid(self, value: str) -> bool:
        if value is None:
            return False
        for pattern in self.__patterns:
            if pattern.match(value):
                return True
        return False

    @staticmethod
    def RegexValidator3(regex: str) -> RegexValidator:
        return RegexValidator.RegexValidator2(regex, True)

    @staticmethod
    def RegexValidator2(regex: str, caseSensitive: bool) -> RegexValidator:
        return RegexValidator([regex], caseSensitive)

    @staticmethod
    def RegexValidator1(regexs: typing.List[str]) -> RegexValidator:
        return RegexValidator(regexs, True)

    def __init__(self, regexs: typing.List[str], caseSensitive: bool) -> None:

        pass  # LLM could not translate this method
