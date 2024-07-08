from __future__ import annotations
import re
import io
import typing
from typing import *


class RuleType:

    RULES: RuleType = None

    EXACT: RuleType = None

    APPROX: RuleType = None

    __name: str = ""

    def getName(self) -> str:
        return self.__name

    def __init__(self, name: str) -> None:
        self.__name = name
