from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.HasCodeInterface import *
from src.main.org.joda.convert.ToString import *


class HasCodeImpl(HasCodeInterface):

    code: str = None

    def getCode(self) -> str:

        return self.code

    def __init__(self, code: str) -> None:

        self.code = code
