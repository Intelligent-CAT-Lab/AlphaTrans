from __future__ import annotations
import re
from io import StringIO
import io
import typing
from typing import *
from src.main.org.apache.commons.pool2.impl.CallStack import *


class NoOpCallStack(CallStack):

    INSTANCE: CallStack = None

    @staticmethod
    def initialize_fields() -> None:
        NoOpCallStack.INSTANCE: CallStack = NoOpCallStack()

    def printStackTrace(
        self, writer: typing.Union[io.TextIOWrapper, io.StringIO]
    ) -> bool:
        return False

    def fillInStackTrace(self) -> None:
        pass

    def clear(self) -> None:
        pass

    def __init__(self) -> None:
        pass


NoOpCallStack.initialize_fields()
