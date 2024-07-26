from __future__ import annotations
import re
from abc import ABC
import io
import os


class Closeable(ABC):

    def isClosed(self) -> bool:

        # Check if the file is closed
        if self.closed:
            return True
        else:
            return False

    def close(self) -> None:

        # Python does not have a built-in IOException, so we can just use a general Exception
        try:
            # Your close logic here
            pass
        except Exception as e:
            raise e
