from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.StringEncoder import *


class SoundexUtils:

    @staticmethod
    def differenceEncoded(es1: str, es2: str) -> int:

        if es1 is None or es2 is None:
            return 0
        length_to_match = min(len(es1), len(es2))
        diff = 0
        for i in range(length_to_match):
            if es1[i] == es2[i]:
                diff += 1
        return diff

    @staticmethod
    def difference(encoder: StringEncoder, s1: str, s2: str) -> int:

        try:
            return SoundexUtils.differenceEncoded(
                encoder.encode(s1), encoder.encode(s2)
            )
        except EncoderException as e:
            print("Error in difference method: " + str(e))
            return 0

    @staticmethod
    def clean(str: str) -> str:

        if str is None or len(str) == 0:
            return str

        len_str = len(str)
        chars = [""] * len_str
        count = 0

        for i in range(len_str):
            if str[i].isalpha():
                chars[count] = str[i]
                count += 1

        if count == len_str:
            return str.upper()

        return "".join(chars[:count]).upper()
