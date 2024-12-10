from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.validator.routines.checkdigit.CheckDigitException import *


class CheckDigit(ABC):

    def isValid(self, code: str) -> bool:

        pass

    def calculate(self, code: str) -> str:


        pass
