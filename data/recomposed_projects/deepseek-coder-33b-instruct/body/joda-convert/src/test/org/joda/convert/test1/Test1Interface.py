from __future__ import annotations
import re
import unittest
import pytest
from abc import ABC
import io
from src.main.org.joda.convert.ToString import *


class Test1Interface(ABC):

    def print(self) -> str:
        pass
