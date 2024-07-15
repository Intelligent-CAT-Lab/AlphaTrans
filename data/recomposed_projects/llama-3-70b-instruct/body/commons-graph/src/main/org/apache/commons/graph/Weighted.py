from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class Weighted(ABC):

    def getWeight(self) -> typing.Any:
        return self.weight
