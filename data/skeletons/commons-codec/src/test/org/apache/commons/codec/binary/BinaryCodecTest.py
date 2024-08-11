from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.BinaryCodec import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class BinaryCodecTest(unittest.TestCase):

    # Class Fields Begin
    __CHARSET_UTF8: str = None
    __BIT_0: int = None
    __BIT_1: int = None
    __BIT_2: int = None
    __BIT_3: int = None
    __BIT_4: int = None
    __BIT_5: int = None
    __BIT_6: int = None
    __BIT_7: int = None
    instance: BinaryCodec = None
    # Class Fields End

    # Class Methods Begin
    def testEncodeObject_test26_decomposed(self) -> None:
        pass

    def testEncodeObject_test25_decomposed(self) -> None:
        pass

    def testEncodeObject_test24_decomposed(self) -> None:
        pass

    def testEncodeObject_test23_decomposed(self) -> None:
        pass

    def testEncodeObject_test22_decomposed(self) -> None:
        pass

    def testEncodeObject_test21_decomposed(self) -> None:
        pass

    def testEncodeObject_test20_decomposed(self) -> None:
        pass

    def testEncodeObject_test19_decomposed(self) -> None:
        pass

    def testEncodeObject_test18_decomposed(self) -> None:
        pass

    def testEncodeObject_test17_decomposed(self) -> None:
        pass

    def testEncodeObject_test16_decomposed(self) -> None:
        pass

    def testEncodeObject_test15_decomposed(self) -> None:
        pass

    def testEncodeObject_test14_decomposed(self) -> None:
        pass

    def testEncodeObject_test13_decomposed(self) -> None:
        pass

    def testEncodeObject_test12_decomposed(self) -> None:
        pass

    def testEncodeObject_test11_decomposed(self) -> None:
        pass

    def testEncodeObject_test10_decomposed(self) -> None:
        pass

    def testEncodeObject_test9_decomposed(self) -> None:
        pass

    def testEncodeObject_test8_decomposed(self) -> None:
        pass

    def testEncodeObject_test7_decomposed(self) -> None:
        pass

    def testEncodeObject_test6_decomposed(self) -> None:
        pass

    def testEncodeObject_test5_decomposed(self) -> None:
        pass

    def testEncodeObject_test4_decomposed(self) -> None:
        pass

    def testEncodeObject_test3_decomposed(self) -> None:
        pass

    def testEncodeObject_test2_decomposed(self) -> None:
        pass

    def testEncodeObject_test1_decomposed(self) -> None:
        pass

    def testEncodeObject_test0_decomposed(self) -> None:
        pass

    def testEncodeObjectException_test1_decomposed(self) -> None:
        pass

    def testEncodeObjectException_test0_decomposed(self) -> None:
        pass

    def testEncodeObjectNull_test0_decomposed(self) -> None:
        pass

    def testToAsciiString_test26_decomposed(self) -> None:
        pass

    def testToAsciiString_test25_decomposed(self) -> None:
        pass

    def testToAsciiString_test24_decomposed(self) -> None:
        pass

    def testToAsciiString_test23_decomposed(self) -> None:
        pass

    def testToAsciiString_test22_decomposed(self) -> None:
        pass

    def testToAsciiString_test21_decomposed(self) -> None:
        pass

    def testToAsciiString_test20_decomposed(self) -> None:
        pass

    def testToAsciiString_test19_decomposed(self) -> None:
        pass

    def testToAsciiString_test18_decomposed(self) -> None:
        pass

    def testToAsciiString_test17_decomposed(self) -> None:
        pass

    def testToAsciiString_test16_decomposed(self) -> None:
        pass

    def testToAsciiString_test15_decomposed(self) -> None:
        pass

    def testToAsciiString_test14_decomposed(self) -> None:
        pass

    def testToAsciiString_test13_decomposed(self) -> None:
        pass

    def testToAsciiString_test12_decomposed(self) -> None:
        pass

    def testToAsciiString_test11_decomposed(self) -> None:
        pass

    def testToAsciiString_test10_decomposed(self) -> None:
        pass

    def testToAsciiString_test9_decomposed(self) -> None:
        pass

    def testToAsciiString_test8_decomposed(self) -> None:
        pass

    def testToAsciiString_test7_decomposed(self) -> None:
        pass

    def testToAsciiString_test6_decomposed(self) -> None:
        pass

    def testToAsciiString_test5_decomposed(self) -> None:
        pass

    def testToAsciiString_test4_decomposed(self) -> None:
        pass

    def testToAsciiString_test3_decomposed(self) -> None:
        pass

    def testToAsciiString_test2_decomposed(self) -> None:
        pass

    def testToAsciiString_test1_decomposed(self) -> None:
        pass

    def testToAsciiString_test0_decomposed(self) -> None:
        pass

    def testToAsciiChars_test26_decomposed(self) -> None:
        pass

    def testToAsciiChars_test25_decomposed(self) -> None:
        pass

    def testToAsciiChars_test24_decomposed(self) -> None:
        pass

    def testToAsciiChars_test23_decomposed(self) -> None:
        pass

    def testToAsciiChars_test22_decomposed(self) -> None:
        pass

    def testToAsciiChars_test21_decomposed(self) -> None:
        pass

    def testToAsciiChars_test20_decomposed(self) -> None:
        pass

    def testToAsciiChars_test19_decomposed(self) -> None:
        pass

    def testToAsciiChars_test18_decomposed(self) -> None:
        pass

    def testToAsciiChars_test17_decomposed(self) -> None:
        pass

    def testToAsciiChars_test16_decomposed(self) -> None:
        pass

    def testToAsciiChars_test15_decomposed(self) -> None:
        pass

    def testToAsciiChars_test14_decomposed(self) -> None:
        pass

    def testToAsciiChars_test13_decomposed(self) -> None:
        pass

    def testToAsciiChars_test12_decomposed(self) -> None:
        pass

    def testToAsciiChars_test11_decomposed(self) -> None:
        pass

    def testToAsciiChars_test10_decomposed(self) -> None:
        pass

    def testToAsciiChars_test9_decomposed(self) -> None:
        pass

    def testToAsciiChars_test8_decomposed(self) -> None:
        pass

    def testToAsciiChars_test7_decomposed(self) -> None:
        pass

    def testToAsciiChars_test6_decomposed(self) -> None:
        pass

    def testToAsciiChars_test5_decomposed(self) -> None:
        pass

    def testToAsciiChars_test4_decomposed(self) -> None:
        pass

    def testToAsciiChars_test3_decomposed(self) -> None:
        pass

    def testToAsciiChars_test2_decomposed(self) -> None:
        pass

    def testToAsciiChars_test1_decomposed(self) -> None:
        pass

    def testToAsciiChars_test0_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test26_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test25_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test24_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test23_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test22_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test21_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test20_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test19_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test18_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test17_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test16_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test15_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test14_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test13_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test12_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test11_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test10_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test9_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test8_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test7_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test6_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test5_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test4_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test3_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test2_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test1_decomposed(self) -> None:
        pass

    def testToAsciiBytes_test0_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test26_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test25_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test24_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test23_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test22_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test21_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test20_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test19_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test18_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test17_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test16_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test15_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test14_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test13_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test12_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test11_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test10_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test9_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test8_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test7_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test6_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test5_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test4_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test3_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test2_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test1_decomposed(self) -> None:
        pass

    def testEncodeByteArray_test0_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test37_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test36_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test35_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test34_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test33_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test32_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test31_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test30_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test29_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test28_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test27_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test26_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test25_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test24_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test23_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test22_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test21_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test20_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test19_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test18_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test17_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test16_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test15_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test14_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test13_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test12_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test11_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test10_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test9_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test8_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test7_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test6_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test5_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test4_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test3_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test2_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test1_decomposed(self) -> None:
        pass

    def testFromAsciiByteArray_test0_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test19_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test18_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test17_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test16_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test15_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test14_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test13_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test12_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test11_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test10_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test9_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test8_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test7_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test6_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test5_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test4_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test3_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test2_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test1_decomposed(self) -> None:
        pass

    def testFromAsciiCharArray_test0_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test18_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test17_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test16_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test15_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test14_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test13_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test12_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test11_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test10_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test9_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test8_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test7_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test6_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test5_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test4_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test3_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test2_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test1_decomposed(self) -> None:
        pass

    def testToByteArrayFromString_test0_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test36_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test35_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test34_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test33_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test32_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test31_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test30_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test29_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test28_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test27_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test26_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test25_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test24_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test23_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test22_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test21_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test20_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test19_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test18_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test17_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test16_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test15_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test14_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test13_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test12_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test11_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test10_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test9_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test8_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test7_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test6_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test5_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test4_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test3_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test2_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test1_decomposed(self) -> None:
        pass

    def testDecodeByteArray_test0_decomposed(self) -> None:
        pass

    def testDecodeObject_test18_decomposed(self) -> None:
        pass

    def testDecodeObject_test17_decomposed(self) -> None:
        pass

    def testDecodeObject_test16_decomposed(self) -> None:
        pass

    def testDecodeObject_test15_decomposed(self) -> None:
        pass

    def testDecodeObject_test14_decomposed(self) -> None:
        pass

    def testDecodeObject_test13_decomposed(self) -> None:
        pass

    def testDecodeObject_test12_decomposed(self) -> None:
        pass

    def testDecodeObject_test11_decomposed(self) -> None:
        pass

    def testDecodeObject_test10_decomposed(self) -> None:
        pass

    def testDecodeObject_test9_decomposed(self) -> None:
        pass

    def testDecodeObject_test8_decomposed(self) -> None:
        pass

    def testDecodeObject_test7_decomposed(self) -> None:
        pass

    def testDecodeObject_test6_decomposed(self) -> None:
        pass

    def testDecodeObject_test5_decomposed(self) -> None:
        pass

    def testDecodeObject_test4_decomposed(self) -> None:
        pass

    def testDecodeObject_test3_decomposed(self) -> None:
        pass

    def testDecodeObject_test2_decomposed(self) -> None:
        pass

    def testDecodeObject_test1_decomposed(self) -> None:
        pass

    def testDecodeObject_test0_decomposed(self) -> None:
        pass

    def testDecodeObjectException_test1_decomposed(self) -> None:
        pass

    def testDecodeObjectException_test0_decomposed(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def setUp(self) -> None:
        pass

    def assertDecodeObject(self, bits: typing.List[int], encodeMe: str) -> None:
        pass

    # Class Methods End
