from __future__ import annotations

# Imports Begin
import io
from abc import ABC

# Imports End


class ValidityCheck:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    # Class Methods End

    pass


class ValidityCheck(ABC):

    # Class Fields Begin
    VALID: ValidityCheck = None
    INVALID: ValidityCheck = None
    # Class Fields End

    # Class Methods Begin
    def count(self) -> int:
        pass

    # Class Methods End
