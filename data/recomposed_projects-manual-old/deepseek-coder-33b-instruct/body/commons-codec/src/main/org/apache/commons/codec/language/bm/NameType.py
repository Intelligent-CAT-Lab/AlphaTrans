from __future__ import annotations
from enum import Enum
import re
import io
import typing
from typing import *


class NameType(Enum):

    SEPHARDIC: NameType = 'sep'

    GENERIC: NameType = 'gen'

    ASHKENAZI: NameType = 'ash'

    def getName(self) -> str:
        return self.value
