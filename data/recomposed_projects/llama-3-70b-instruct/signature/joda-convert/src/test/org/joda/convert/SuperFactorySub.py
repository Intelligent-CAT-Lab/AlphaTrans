from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.joda.convert.SuperFactorySuper import *


class SuperFactorySub(SuperFactorySuper):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
