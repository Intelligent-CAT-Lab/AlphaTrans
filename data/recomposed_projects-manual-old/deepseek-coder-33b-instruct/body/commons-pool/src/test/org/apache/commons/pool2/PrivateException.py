from __future__ import annotations
import time
import re
import unittest
import pytest
import io


class PrivateException(RuntimeError):

    __serialVersionUID: int = 1

    def __init__(self, message: str) -> None:
        super().__init__(message)
