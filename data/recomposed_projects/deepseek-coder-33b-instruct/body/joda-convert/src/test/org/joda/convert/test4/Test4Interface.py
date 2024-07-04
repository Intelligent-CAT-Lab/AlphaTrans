from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
from src.main.org.joda.convert.FromStringFactory import *
from src.main.org.joda.convert.ToString import *


class Test4Interface(ABC):

    def print(self) -> str:
        pass
