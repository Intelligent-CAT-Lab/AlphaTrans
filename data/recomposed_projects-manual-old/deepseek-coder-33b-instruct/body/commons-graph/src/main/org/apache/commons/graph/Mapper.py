from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class Mapper(ABC):

    def map(self, input: typing.Any) -> typing.Any:
        pass
