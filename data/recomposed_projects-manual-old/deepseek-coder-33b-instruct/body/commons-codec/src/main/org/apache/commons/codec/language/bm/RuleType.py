from __future__ import annotations
import re
import io
import typing
from typing import *
from enum import Enum


class RuleType(Enum):

    RULES: RuleType = 'rules'

    EXACT: RuleType = 'exact'

    APPROX: RuleType = 'approx'

    def getName(self) -> str:
        return self.value
