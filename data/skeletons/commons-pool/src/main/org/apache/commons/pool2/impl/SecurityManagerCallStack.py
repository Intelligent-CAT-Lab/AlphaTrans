from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class Snapshot:

    # Class Fields Begin
    __timestampMillis: int = None
    __stack: typing.List[weakref.ref] = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, stack: typing.List[weakref.ref]) -> None:
        pass

    # Class Methods End


class PrivateSecurityManager:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __getCallStack(self) -> typing.List[weakref.ref]:
        pass

    # Class Methods End


class SecurityManagerCallStack:

    # Class Fields Begin
    __snapshot: Snapshot = None
    # Class Fields End

    # Class Methods Begin
    def clear(self) -> None:
        pass

    # Class Methods End
