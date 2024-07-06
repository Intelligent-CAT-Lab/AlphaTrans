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

    @staticmethod
    def initialize_fields() -> None:
        RuleType.RULES: RuleType = None
        RuleType.EXACT: RuleType = None
        RuleType.APPROX: RuleType = None

    def getName(self) -> str:
        return self.__name

    def __init__(self, name: str) -> None:
        self.__name = name


RuleType.initialize_fields()
