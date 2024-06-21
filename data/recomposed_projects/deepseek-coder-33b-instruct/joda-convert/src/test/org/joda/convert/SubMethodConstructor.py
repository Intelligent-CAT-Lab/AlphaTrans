from __future__ import annotations
import io
from src.test.org.joda.convert.DistanceMethodConstructor import *
from src.main.org.joda.convert.FromString import *


class SubMethodConstructor(DistanceMethodConstructor):

    def __init__(self, amount: str) -> None:

        super().__init__(0, amount, 0)
