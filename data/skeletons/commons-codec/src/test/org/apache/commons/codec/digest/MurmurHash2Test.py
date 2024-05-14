# Imports Begin
from src.main.org.apache.commons.codec.digest.MurmurHash2 import *
import typing

# Imports End


class MurmurHash2Test:

    # Class Fields Begin
    results32_standard: typing.List[int] = None
    results32_seed: typing.List[int] = None
    results64_standard: typing.List[int] = None
    results64_seed: typing.List[int] = None
    text: str = None
    input: typing.List[typing.List[int]] = None
    # Class Fields End

    # Class Methods Begin
    def testHash64StringIntInt(self) -> None:
        pass

    def testHash64String(self) -> None:
        pass

    def testHash64ByteArrayInt(self) -> None:
        pass

    def testHash64ByteArrayIntInt(self) -> None:
        pass

    def testHash32StringIntInt(self) -> None:
        pass

    def testHash32String(self) -> None:
        pass

    def testHash32ByteArrayInt(self) -> None:
        pass

    def testHash32ByteArrayIntInt(self) -> None:
        pass

    # Class Methods End
