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
            buffer.write(self.__patterns[i].pattern)
        buffer.write("}")
        return buffer.getvalue()

    def validate(self, value: str) -> str:

        if value is None:
            return None
        for pattern in self.__patterns:
            matcher = re.match(pattern, value)

            if matcher:
                count = len(matcher.groups())

                if count == 1:
                    return matcher.group(1)

                buffer = ""
                for j in range(count):
                    component = matcher.group(j + 1)
                    if component is not None:
                        buffer += component

                return buffer

        return None

    def match(self, value: str) -> typing.List[typing.List[str]]:

        if value is None:
            return None

        for pattern in self.__patterns:
            matcher = pattern.match(value)
            if matcher:
                groups = list(matcher.groups())
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
    def RegexValidator1(regexs: typing.List[typing.List[str]]) -> RegexValidator:

        return RegexValidator(regexs, True)

    def __init__(
        self, regexs: typing.List[typing.List[str]], caseSensitive: bool
    ) -> None:

        if regexs is None or len(regexs) == 0:
            raise ValueError("Regular expressions are missing")

        self.__patterns = [None] * len(regexs)
        flags = re.IGNORECASE if not caseSensitive else 0

        for i in range(len(regexs)):
            if regexs[i] is None or len(regexs[i]) == 0:
                raise ValueError(f"Regular expression[{i}] is missing")
            self.__patterns[i] = re.compile(regexs[i], flags)
