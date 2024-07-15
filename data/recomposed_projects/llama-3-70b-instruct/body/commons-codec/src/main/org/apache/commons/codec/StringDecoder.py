from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.codec.Decoder import *
from src.main.org.apache.commons.codec.DecoderException import *


class StringDecoder(ABC):

    def decode(self, source: str) -> str:
        return source
