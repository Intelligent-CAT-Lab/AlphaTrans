# Imports Begin
from src.main.org.apache.commons.codec.digest.MurmurHash2 import *
import unittest
import typing
from typing import *

# Imports End


class MurmurHash2Test(unittest.TestCase):

    # Class Fields Begin
    results32_standard: typing.List[int] = ""  # LLM could not translate field
    results32_seed: List = [
        0xD92E493E,
        0x8B50903B,
        0xC3372A7B,
        0x48F07E9E,
        0x8A5E4A6E,
        0x57916DF4,
        0xA346171F,
        0x1E319C86,
        0x9E1A03CD,
        0x9F973E6C,
        0x2D8C77F5,
        0xABED8751,
        0x296708B6,
        0x24F8078B,
        0x111B1553,
        0xA7DA1996,
        0xFE776C70,
    ]
    results64_standard: typing.List[int] = ""  # LLM could not translate field
    results64_seed: List = [
        0x0822B1481A92E97B,
        0xF8A9223FEF0822DD,
        0x4B49E56AFFAE3A89,
        0xC970296E32E1D1C1,
        0xE2F9F88789F1B08F,
        0x2B0459D9B4C10C61,
        0x377E97EA9197EE89,
        0xD2CCAD460751E0E7,
        0xFF162CA8D6DA8C47,
        0xF12E051405769857,
        0xDABBA41293D5B035,
        0xACF326B0BB690D0E,
        0x0617F431BC1A8E04,
        0x15B81F28D576E1B2,
        0x28C1FE59E4F8E5BA,
        0x694DD315C9354CA9,
        0xA97052A8F088AE6C,
    ]
    text: str = "Lorem ipsum dolor sit amet, consectetur adipisicing elit"
    input: typing.List[typing.List[int]] = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    def testHash64StringIntInt(self) -> None:

        hash = self.hash643(self.text, 2, len(self.text) - 4)
        self.assertEqual(0xA8B33145194985A2, hash)

    def testHash64String(self) -> None:

        hash = self.hash642(self.text)
        self.assertEqual(0x0920E0C1B7EEB261, hash)

    def testHash64ByteArrayInt(self) -> None:

        for i in range(len(self.input)):
            hash = self.hash641(self.input[i], len(self.input[i]))
            if hash != self.results64_standard[i]:
                Assert.fail(
                    "Unexpected hash64 result for example {}: 0x{:016x} instead of"
                    " 0x{:016x}".format(i, hash, self.results64_standard[i])
                )

    def testHash64ByteArrayIntInt(self) -> None:

        for i in range(len(self.input)):
            hash = MurmurHash2.hash640(self.input[i], len(self.input[i]), 0x344D1F5C)
            if hash != self.results64_seed[i]:
                Assert.fail(
                    f"Unexpected hash64 result for example {i}: 0x{hash:016x} instead of"
                    + f" 0x{self.results64_seed[i]:016x}"
                )

    def testHash32StringIntInt(self) -> None:

        pass  # LLM could not translate method body

    def testHash32String(self) -> None:

        hash = MurmurHash2.hash322(self.text)
        Assert.self.assertEqual(0xB3BF597E, hash)

    def testHash32ByteArrayInt(self) -> None:

        for i in range(len(self.input)):
            hash = self.hash321(self.input[i], len(self.input[i]))
            if hash != self.results32_standard[i]:
                Assert.fail(
                    f"Unexpected hash32 result for example {i}: 0x{hash:08x} instead of 0x{self.results32_standard[i]:08x}"
                )

    def testHash32ByteArrayIntInt(self) -> None:

        for i in range(len(self.input)):
            hash = MurmurHash2.hash320(self.input[i], len(self.input[i]), 0x71B4954D)
            if hash != self.results32_seed[i]:
                Assert.fail(
                    f"Unexpected hash32 result for example {i}: 0x{hash:08x} instead of 0x{self.results32_seed[i]:08x}"
                )

    # Class Methods End
