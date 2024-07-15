from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class FromStringFactory(ABC):

    def factory(self) -> typing.Type[typing.Any]:
        pass
