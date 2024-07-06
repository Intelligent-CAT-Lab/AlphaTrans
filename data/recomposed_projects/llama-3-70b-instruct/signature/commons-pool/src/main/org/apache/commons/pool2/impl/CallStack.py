from __future__ import annotations
import re
from abc import ABC
from io import StringIO
import io
import typing
from typing import *


class CallStack(ABC):

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:
        writer.write(self.toString())
        return True

    def fillInStackTrace(self) -> None:
        pass

    def clear(self) -> None:
        pass
