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

        pass  # LLM could not translate this method
