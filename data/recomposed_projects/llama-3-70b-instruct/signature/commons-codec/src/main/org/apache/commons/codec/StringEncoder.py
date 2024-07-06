from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.codec.Encoder import *
from src.main.org.apache.commons.codec.EncoderException import *


class StringEncoder(ABC):

    def encode(self, source: str) -> str:
        return source
