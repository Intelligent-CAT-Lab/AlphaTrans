from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *


class UsageTracking(ABC):

    def use(self, pooledObject: typing.Any) -> None:

        pass
