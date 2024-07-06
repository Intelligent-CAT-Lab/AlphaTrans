from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class Monoid(ABC):

    def inverse(self, element: typing.Any) -> typing.Any:
        return element

    def identity(self) -> typing.Any:
        return None

    def append(self, e1: typing.Any, e2: typing.Any) -> typing.Any:
        return e1 + e2
