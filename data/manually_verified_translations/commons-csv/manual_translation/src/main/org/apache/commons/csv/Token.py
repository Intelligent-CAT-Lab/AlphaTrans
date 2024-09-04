from __future__ import annotations
import re
from io import StringIO
import io
import typing


class Token:

    class Type:

        COMMENT = 1

        EORECORD = 2

        EOF = 3

        TOKEN = 4

        INVALID = 5

    content: io.StringIO = io.StringIO()
    __INITIAL_TOKEN_LENGTH: int = 50
    isQuoted: bool = False

    isReady: bool = False

    type: int = None

    @staticmethod
    def initialize_fields() -> None:
        Token.type: int = Token.Type.INVALID

    def toString(self) -> str:
        return self.type.name + " [" + self.content.getvalue() + "]"

    def reset(self) -> None:

        self.content = io.StringIO()
        self.type = Token.Type.INVALID
        self.isReady = False
        self.isQuoted = False


Token.initialize_fields()
