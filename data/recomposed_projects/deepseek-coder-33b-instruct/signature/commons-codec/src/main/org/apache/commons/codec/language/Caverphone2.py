from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.language.AbstractCaverphone import *


class Caverphone2(AbstractCaverphone):

    __TEN_1: str = "1111111111"

    def encode(self, source: str) -> str:

        txt = source
        if txt is None or len(txt) == 0:
            return self.__TEN_1

        txt = txt.lower()

        txt = re.sub(r"[^a-z]", "", txt)

        txt = re.sub(r"e$", "", txt)

        txt = re.sub(r"^cough", "cou2f", txt)
        txt = re.sub(r"^rough", "rou2f", txt)
        txt = re.sub(r"^tough", "tou2f", txt)
        txt = re.sub(r"^enough", "enou2f", txt)
        txt = re.sub(r"^trough", "trou2f", txt)
        txt = re.sub(r"^gn", "2n", txt)

        txt = re.sub(r"mb$", "m2", txt)

        txt = txt.replace("cq", "2q")
        txt = txt.replace("ci", "si")
        txt = txt.replace("ce", "se")
        txt = txt.replace("cy", "sy")
        txt = txt.replace("tch", "2ch")
        txt = txt.replace("c", "k")
        txt = txt.replace("q", "k")
        txt = txt.replace("x", "k")
        txt = txt.replace("v", "f")
        txt = txt.replace("dg", "2g")
        txt = txt.replace("tio", "sio")
        txt = txt.replace("tia", "sia")
        txt = txt.replace("d", "t")
        txt = txt.replace("ph", "fh")
        txt = txt.replace("b", "p")
        txt = txt.replace("sh", "s2")
        txt = txt.replace("z", "s")
        txt = re.sub(r"^[aeiou]", "A", txt)
        txt = re.sub(r"[aeiou]", "3", txt)
        txt = txt.replace("j", "y")
        txt = re.sub(r"^y3", "Y3", txt)
        txt = re.sub(r"^y", "A", txt)
        txt = txt.replace("y", "3")
        txt = txt.replace("3gh3", "3kh3")
        txt = txt.replace("gh", "22")
        txt = txt.replace("g", "k")
        txt = re.sub(r"s+", "S", txt)
        txt = re.sub(r"t+", "T", txt)
        txt = re.sub(r"p+", "P", txt)
        txt = re.sub(r"k+", "K", txt)
        txt = re.sub(r"f+", "F", txt)
        txt = re.sub(r"m+", "M", txt)
        txt = re.sub(r"n+", "N", txt)
        txt = txt.replace("w3", "W3")
        txt = txt.replace("wh3", "Wh3")
        txt = re.sub(r"w$", "3", txt)
        txt = txt.replace("w", "2")
        txt = re.sub(r"^h", "A", txt)
        txt = txt.replace("h", "2")
        txt = txt.replace("r3", "R3")
        txt = re.sub(r"r$", "3", txt)
        txt = txt.replace("r", "2")
        txt = txt.replace("l3", "L3")
        txt = re.sub(r"l$", "3", txt)
        txt = txt.replace("l", "2")

        txt = txt.replace("2", "")
        txt = re.sub(r"3$", "A", txt)
        txt = txt.replace("3", "")

        txt = txt + self.__TEN_1

        return txt[: len(self.__TEN_1)]
