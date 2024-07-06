from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.language.AbstractCaverphone import *


class Caverphone2(AbstractCaverphone):

    __TEN_1: str = "1111111111"

    def encode(self, source: str) -> str:
        txt = source
        if txt is None or txt == "":
            return self.__TEN_1

        txt = txt.lower()

        txt = txt.replace("[^a-z]", "")

        txt = txt.replace("e$", "")  # 2.0 only

        txt = txt.replace("^cough", "cou2f")
        txt = txt.replace("^rough", "rou2f")
        txt = txt.replace("^tough", "tou2f")
        txt = txt.replace("^enough", "enou2f")  # 2.0 only
        txt = txt.replace("^trough", "trou2f")  # 2.0 only
        txt = txt.replace("^gn", "2n")

        txt = txt.replace("mb$", "m2")

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
        txt = txt.replace("^[aeiou]", "A")
        txt = txt.replace("[aeiou]", "3")
        txt = txt.replace("j", "y")  # 2.0 only
        txt = txt.replace("^y3", "Y3")  # 2.0 only
        txt = txt.replace("^y", "A")  # 2.0 only
        txt = txt.replace("y", "3")  # 2.0 only
        txt = txt.replace("3gh3", "3kh3")
        txt = txt.replace("gh", "22")
        txt = txt.replace("g", "k")
        txt = txt.replace("s+", "S")
        txt = txt.replace("t+", "T")
        txt = txt.replace("p+", "P")
        txt = txt.replace("k+", "K")
        txt = txt.replace("f+", "F")
        txt = txt.replace("m+", "M")
        txt = txt.replace("n+", "N")
        txt = txt.replace("w3", "W3")
        txt = txt.replace("wh3", "Wh3")
        txt = txt.replace("w$", "3")  # 2.0 only
        txt = txt.replace("w", "2")
        txt = txt.replace("^h", "A")
        txt = txt.replace("h", "2")
        txt = txt.replace("r3", "R3")
        txt = txt.replace("r$", "3")  # 2.0 only
        txt = txt.replace("r", "2")
        txt = txt.replace("l3", "L3")
        txt = txt.replace("l$", "3")  # 2.0 only
        txt = txt.replace("l", "2")

        txt = txt.replace("2", "")
        txt = txt.replace("3$", "A")  # 2.0 only
        txt = txt.replace("3", "")

        txt = txt + self.__TEN_1

        return txt[0 : self.__TEN_1.__len__()]
