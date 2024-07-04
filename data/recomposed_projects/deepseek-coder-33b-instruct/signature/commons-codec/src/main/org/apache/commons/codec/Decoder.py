from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.DecoderException import *


class Decoder(ABC):

    def decode(self, source: typing.Any) -> typing.Any:
        raise NotImplementedError("Subclass must implement abstract method")
