from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.joda.convert.DistanceMethodMethod import *


class SubNoAnnotations(DistanceMethodMethod):

    def __init__(self, amount: int) -> None:
        super().__init__(amount)
