from __future__ import annotations
from abc import ABC
import io
import typing
from typing import *


class SwallowedExceptionListener(ABC):

    def onSwallowException(self, e: Exception) -> None:

        pass
