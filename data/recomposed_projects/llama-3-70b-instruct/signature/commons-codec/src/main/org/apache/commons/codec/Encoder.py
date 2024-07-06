from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.EncoderException import *


class Encoder(ABC):

    def encode(self, source: typing.Any) -> typing.Any:
        pass
