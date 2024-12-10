from __future__ import annotations

# Imports Begin
import typing
from typing import *
from io import BytesIO
import io
from io import StringIO

# Imports End


class Resources:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getInputStream(
        name: str,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        pass

    # Class Methods End
