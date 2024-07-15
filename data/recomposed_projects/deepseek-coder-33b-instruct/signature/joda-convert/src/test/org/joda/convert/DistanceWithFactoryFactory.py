from __future__ import annotations
import re
import unittest
import pytest
import io
from src.test.org.joda.convert.DistanceWithFactory import *
from src.main.org.joda.convert.FromString import *


class DistanceWithFactoryFactory:

    @staticmethod
    def parse(amount: str) -> DistanceWithFactory:
        amount = amount[:-1]
        return DistanceWithFactory(int(amount))
