from __future__ import annotations

# Imports Begin
from src.main.me.lemire.integercompression.differential.SkippableIntegratedIntegerCODEC import *
from src.main.me.lemire.integercompression.differential.IntegratedIntCompressor import *
from src.main.me.lemire.integercompression.VariableByte import *
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
from src.main.me.lemire.integercompression.IntCompressor import *
from src.main.me.lemire.integercompression.FastPFOR128 import *
from src.main.me.lemire.integercompression.FastPFOR import *
from src.main.me.lemire.integercompression.BinaryPacking import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class ResourcedTest(unittest.TestCase):

    # Class Fields Begin
    codecs: typing.List[SkippableIntegerCODEC] = None
    # Class Fields End

    # Class Methods Begin
    def IntCompressorTest_test3_decomposed(self) -> None:
        pass

    def IntCompressorTest_test2_decomposed(self) -> None:
        pass

    def IntCompressorTest_test1_decomposed(self) -> None:
        pass

    def IntCompressorTest_test0_decomposed(self) -> None:
        pass

    # Class Methods End
