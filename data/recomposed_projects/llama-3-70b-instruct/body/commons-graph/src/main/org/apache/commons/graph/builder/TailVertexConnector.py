from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class TailVertexConnector(ABC):

    def to(self, tail: typing.Any) -> None:
        pass
