from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class SccAlgorithm(ABC):

    def perform(self) -> typing.Set[typing.Set[typing.Any]]:
        return self.perform()
