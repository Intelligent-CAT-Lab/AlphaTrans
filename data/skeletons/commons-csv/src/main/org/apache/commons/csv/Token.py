from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Type:

    # Class Fields Begin
    INVALID: typing.Type = None
    TOKEN: typing.Type = None
    EOF: typing.Type = None
    EORECORD: typing.Type = None
    COMMENT: typing.Type = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End


class Token:

    # Class Fields Begin
    __INITIAL_TOKEN_LENGTH: int = None
    content: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def reset(self) -> None:
        pass

    # Class Methods End
