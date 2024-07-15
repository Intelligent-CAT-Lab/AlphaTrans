from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
import typing
from typing import *


class HasCodeInterface(ABC):

    def getCode(self) -> typing.Any:
        pass
