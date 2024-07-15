from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.VariableByte import *
from src.test.me.lemire.integercompression.TestUtils import *
from src.main.me.lemire.integercompression.SkippableIntegerCODEC import *
from src.main.me.lemire.integercompression.SkippableComposition import *
from src.main.me.lemire.integercompression.Simple9 import *
from src.main.me.lemire.integercompression.Simple16 import *
from src.main.me.lemire.integercompression.OptPFDS9 import *
from src.main.me.lemire.integercompression.OptPFDS16 import *
from src.main.me.lemire.integercompression.OptPFD import *
from src.main.me.lemire.integercompression.NewPFDS9 import *
from src.main.me.lemire.integercompression.NewPFDS16 import *
from src.main.me.lemire.integercompression.NewPFD import *
from src.main.me.lemire.integercompression.JustCopy import *
from src.main.me.lemire.integercompression.IntWrapper import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import unittest
import typing
from typing import *
import io

# Imports End


class SkippableBasicTest(unittest.TestCase):

    # Class Fields Begin
    codecs: typing.List[SkippableIntegerCODEC] = None
    # Class Fields End

    # Class Methods Begin
    def varyingLengthTest2(self) -> None:
        pass

    def varyingLengthTest(self) -> None:
        pass

    def consistentTest(self) -> None:
        pass

    # Class Methods End
