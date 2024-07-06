from __future__ import annotations
import re
import io
import typing
from typing import *


class Type:

    COMMENT: typing.Type = None

    EORECORD: typing.Type = None

    EOF: typing.Type = None

    TOKEN: typing.Type = None

    INVALID: typing.Type = None


class Token:

    content: str = ""
    __INITIAL_TOKEN_LENGTH: int = 50
    isQuoted: bool = False

    isReady: bool = False

    type: Type = INVALID

    def toString(self) -> str:
        return self.type.name() + " [" + self.content + "]"

    def reset(self) -> None:
        self.content = ""
        self.type = Type.INVALID
        self.isReady = False
        self.isQuoted = False
