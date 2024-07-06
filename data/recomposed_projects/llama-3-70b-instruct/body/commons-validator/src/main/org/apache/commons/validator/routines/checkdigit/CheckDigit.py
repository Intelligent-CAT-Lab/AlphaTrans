from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class CheckDigit(ABC):

    def isValid(self, code: str) -> bool:
        return self.generate(code[:-1]) == code[-1]

    def calculate(self, code: str) -> str:
        return code
