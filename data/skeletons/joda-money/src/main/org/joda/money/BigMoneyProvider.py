from __future__ import annotations

# Imports Begin
from src.main.org.joda.money.BigMoney import *
import io
from abc import ABC

# Imports End


class BigMoneyProvider(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def toBigMoney(self) -> BigMoney:
        pass

    # Class Methods End
