from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *


class ProgressListener(ABC):

    def update(self, pBytesRead: int, pContentLength: int, pItems: int) -> None:
        pass
