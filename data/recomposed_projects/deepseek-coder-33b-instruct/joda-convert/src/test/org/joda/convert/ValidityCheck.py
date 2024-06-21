from __future__ import annotations
from abc import ABC
import io


class ValidityCheck(ABC):

    INVALID: ValidityCheck = None
    VALID: ValidityCheck = None

    def count(self) -> int:

        pass
