from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.HasCodeInterface import *
from src.main.org.joda.convert.ToString import *


class HasCodeImpl(HasCodeInterface):

    code: str = ""

    def getCode(self) -> str:
        return self.code

    def __init__(self, code: str) -> None:
        self.code = code
