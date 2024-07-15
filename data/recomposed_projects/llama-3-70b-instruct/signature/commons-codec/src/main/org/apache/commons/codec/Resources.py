from __future__ import annotations
import re
from io import StringIO
import io
from io import BytesIO
import typing
from typing import *


class Resources:

    @staticmethod
    def getInputStream(
        name: str,
    ) -> typing.Union[io.BytesIO, io.StringIO, io.BufferedReader]:
        inputStream = typing.cast(
            typing.Union[io.BytesIO, io.StringIO, io.BufferedReader],
            Resources.__class__.__loader__.get_data(name),
        )
        if inputStream is None:
            raise ValueError(f"Unable to resolve required resource: {name}")
        return inputStream
