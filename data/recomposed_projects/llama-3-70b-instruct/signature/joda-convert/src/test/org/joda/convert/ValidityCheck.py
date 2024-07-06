from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io


class ValidityCheck(ABC):

    INVALID: ValidityCheck = None

    VALID: ValidityCheck = None

    def count(self) -> int:
        return 0
