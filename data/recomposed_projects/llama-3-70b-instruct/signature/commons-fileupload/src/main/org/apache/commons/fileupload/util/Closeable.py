from __future__ import annotations
import re
from abc import ABC
import io
import os


class Closeable(ABC):

    def isClosed(self) -> bool:
        return False

    def close(self) -> None:
        pass
