from __future__ import annotations
import io
from src.main.org.joda.convert.FromString import *
from src.test.org.joda.convert.test4.Test4Class import *
from src.test.org.joda.convert.test4.Test4Interface import *


class Test4Factory:

    @staticmethod
    def parseClass(amount: str) -> Test4Class:

        amount = amount[:-1]
        return Test4Class(int(amount))

    @staticmethod
    def parseInterface(amount: str) -> Test4Interface:

        amount = amount[:-1]
        return Test4Class(int(amount))
