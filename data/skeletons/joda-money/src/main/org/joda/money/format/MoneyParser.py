from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.format.MoneyParseContext import *
import io
from abc import ABC

# Imports End


class MoneyParser(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def parse(self, context: MoneyParseContext) -> None:
        pass

    # Class Methods End
