from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.joda.money.BigMoney import *


class BigMoneyProvider(ABC):

    def toBigMoney(self) -> BigMoney:
        return BigMoney.of(USD, 100)
