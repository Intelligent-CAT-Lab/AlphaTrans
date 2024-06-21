from __future__ import annotations
import re
import io
import typing
from typing import *
import os


class Codec105ErrorInputStream:

    __EOF: int = -1

    def read(self) -> int:

        try:
            return self.read0()
        except Exception as e:
            raise IOError from e

    def read1(self, b: typing.List[int], pos: int, len: int) -> int:

        if self.countdown > 0:
            b[pos] = ord("\n")
            self.countdown -= 1
            return 1
        else:
            return self.__EOF

    def read0(self) -> int:

        if self.countdown > 0:
            self.countdown -= 1
            return "\n"
        else:
            return self.__EOF
