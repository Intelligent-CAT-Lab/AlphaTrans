from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.test.org.apache.commons.codec.binary.BaseNTestData import *
from src.main.org.apache.commons.codec.binary.BaseNCodec import *
from src.test.org.apache.commons.codec.binary.Base16TestData import *
from src.main.org.apache.commons.codec.binary.Base16 import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
from src.main.org.apache.commons.codec.CodecPolicy import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class Base16Test(unittest.TestCase):

    # Class Fields Begin
    __CHARSET_UTF8: str = None
    __random: random.Random = None
    # Class Fields End

    # Class Methods Begin
    def testLenientDecoding_test4_decomposed(self) -> None:
        pass

    def testLenientDecoding_test3_decomposed(self) -> None:
        pass

    def testLenientDecoding_test2_decomposed(self) -> None:
        pass

    def testLenientDecoding_test1_decomposed(self) -> None:
        pass

    def testLenientDecoding_test0_decomposed(self) -> None:
        pass

    def testStrictDecoding_test3_decomposed(self) -> None:
        pass

    def testStrictDecoding_test2_decomposed(self) -> None:
        pass

    def testStrictDecoding_test1_decomposed(self) -> None:
        pass

    def testStrictDecoding_test0_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test6_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test5_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test4_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test3_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test2_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test1_decomposed(self) -> None:
        pass

    def testDecodeSingleBytesOptimisation_test0_decomposed(self) -> None:
        pass

    def testDecodeSingleBytes_test5_decomposed(self) -> None:
        pass

    def testDecodeSingleBytes_test4_decomposed(self) -> None:
        pass

    def testDecodeSingleBytes_test3_decomposed(self) -> None:
        pass

    def testDecodeSingleBytes_test2_decomposed(self) -> None:
        pass

    def testDecodeSingleBytes_test1_decomposed(self) -> None:
        pass

    def testDecodeSingleBytes_test0_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test5_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test4_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test3_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test2_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test1_decomposed(self) -> None:
        pass

    def testIsInAlphabet_test0_decomposed(self) -> None:
        pass

    def checkEncodeLengthBounds_test1_decomposed(self) -> None:
        pass

    def checkEncodeLengthBounds_test0_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test20_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test19_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test18_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test17_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test16_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test15_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test14_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test13_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test12_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test11_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test10_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test9_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test8_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test7_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test6_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test5_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test4_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test3_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test2_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test1_decomposed(self) -> None:
        pass

    def testStringToByteVariations_test0_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test13_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test12_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test11_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test10_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test9_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test8_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test7_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test6_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test5_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test4_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test3_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test2_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test1_decomposed(self) -> None:
        pass

    def testByteToStringVariations_test0_decomposed(self) -> None:
        pass

    def testTriplets_test31_decomposed(self) -> None:
        pass

    def testTriplets_test30_decomposed(self) -> None:
        pass

    def testTriplets_test29_decomposed(self) -> None:
        pass

    def testTriplets_test28_decomposed(self) -> None:
        pass

    def testTriplets_test27_decomposed(self) -> None:
        pass

    def testTriplets_test26_decomposed(self) -> None:
        pass

    def testTriplets_test25_decomposed(self) -> None:
        pass

    def testTriplets_test24_decomposed(self) -> None:
        pass

    def testTriplets_test23_decomposed(self) -> None:
        pass

    def testTriplets_test22_decomposed(self) -> None:
        pass

    def testTriplets_test21_decomposed(self) -> None:
        pass

    def testTriplets_test20_decomposed(self) -> None:
        pass

    def testTriplets_test19_decomposed(self) -> None:
        pass

    def testTriplets_test18_decomposed(self) -> None:
        pass

    def testTriplets_test17_decomposed(self) -> None:
        pass

    def testTriplets_test16_decomposed(self) -> None:
        pass

    def testTriplets_test15_decomposed(self) -> None:
        pass

    def testTriplets_test14_decomposed(self) -> None:
        pass

    def testTriplets_test13_decomposed(self) -> None:
        pass

    def testTriplets_test12_decomposed(self) -> None:
        pass

    def testTriplets_test11_decomposed(self) -> None:
        pass

    def testTriplets_test10_decomposed(self) -> None:
        pass

    def testTriplets_test9_decomposed(self) -> None:
        pass

    def testTriplets_test8_decomposed(self) -> None:
        pass

    def testTriplets_test7_decomposed(self) -> None:
        pass

    def testTriplets_test6_decomposed(self) -> None:
        pass

    def testTriplets_test5_decomposed(self) -> None:
        pass

    def testTriplets_test4_decomposed(self) -> None:
        pass

    def testTriplets_test3_decomposed(self) -> None:
        pass

    def testTriplets_test2_decomposed(self) -> None:
        pass

    def testTriplets_test1_decomposed(self) -> None:
        pass

    def testTriplets_test0_decomposed(self) -> None:
        pass

    def testSingletons_test210_decomposed(self) -> None:
        pass

    def testSingletons_test209_decomposed(self) -> None:
        pass

    def testSingletons_test208_decomposed(self) -> None:
        pass

    def testSingletons_test207_decomposed(self) -> None:
        pass

    def testSingletons_test206_decomposed(self) -> None:
        pass

    def testSingletons_test205_decomposed(self) -> None:
        pass

    def testSingletons_test204_decomposed(self) -> None:
        pass

    def testSingletons_test203_decomposed(self) -> None:
        pass

    def testSingletons_test202_decomposed(self) -> None:
        pass

    def testSingletons_test201_decomposed(self) -> None:
        pass

    def testSingletons_test200_decomposed(self) -> None:
        pass

    def testSingletons_test199_decomposed(self) -> None:
        pass

    def testSingletons_test198_decomposed(self) -> None:
        pass

    def testSingletons_test197_decomposed(self) -> None:
        pass

    def testSingletons_test196_decomposed(self) -> None:
        pass

    def testSingletons_test195_decomposed(self) -> None:
        pass

    def testSingletons_test194_decomposed(self) -> None:
        pass

    def testSingletons_test193_decomposed(self) -> None:
        pass

    def testSingletons_test192_decomposed(self) -> None:
        pass

    def testSingletons_test191_decomposed(self) -> None:
        pass

    def testSingletons_test190_decomposed(self) -> None:
        pass

    def testSingletons_test189_decomposed(self) -> None:
        pass

    def testSingletons_test188_decomposed(self) -> None:
        pass

    def testSingletons_test187_decomposed(self) -> None:
        pass

    def testSingletons_test186_decomposed(self) -> None:
        pass

    def testSingletons_test185_decomposed(self) -> None:
        pass

    def testSingletons_test184_decomposed(self) -> None:
        pass

    def testSingletons_test183_decomposed(self) -> None:
        pass

    def testSingletons_test182_decomposed(self) -> None:
        pass

    def testSingletons_test181_decomposed(self) -> None:
        pass

    def testSingletons_test180_decomposed(self) -> None:
        pass

    def testSingletons_test179_decomposed(self) -> None:
        pass

    def testSingletons_test178_decomposed(self) -> None:
        pass

    def testSingletons_test177_decomposed(self) -> None:
        pass

    def testSingletons_test176_decomposed(self) -> None:
        pass

    def testSingletons_test175_decomposed(self) -> None:
        pass

    def testSingletons_test174_decomposed(self) -> None:
        pass

    def testSingletons_test173_decomposed(self) -> None:
        pass

    def testSingletons_test172_decomposed(self) -> None:
        pass

    def testSingletons_test171_decomposed(self) -> None:
        pass

    def testSingletons_test170_decomposed(self) -> None:
        pass

    def testSingletons_test169_decomposed(self) -> None:
        pass

    def testSingletons_test168_decomposed(self) -> None:
        pass

    def testSingletons_test167_decomposed(self) -> None:
        pass

    def testSingletons_test166_decomposed(self) -> None:
        pass

    def testSingletons_test165_decomposed(self) -> None:
        pass

    def testSingletons_test164_decomposed(self) -> None:
        pass

    def testSingletons_test163_decomposed(self) -> None:
        pass

    def testSingletons_test162_decomposed(self) -> None:
        pass

    def testSingletons_test161_decomposed(self) -> None:
        pass

    def testSingletons_test160_decomposed(self) -> None:
        pass

    def testSingletons_test159_decomposed(self) -> None:
        pass

    def testSingletons_test158_decomposed(self) -> None:
        pass

    def testSingletons_test157_decomposed(self) -> None:
        pass

    def testSingletons_test156_decomposed(self) -> None:
        pass

    def testSingletons_test155_decomposed(self) -> None:
        pass

    def testSingletons_test154_decomposed(self) -> None:
        pass

    def testSingletons_test153_decomposed(self) -> None:
        pass

    def testSingletons_test152_decomposed(self) -> None:
        pass

    def testSingletons_test151_decomposed(self) -> None:
        pass

    def testSingletons_test150_decomposed(self) -> None:
        pass

    def testSingletons_test149_decomposed(self) -> None:
        pass

    def testSingletons_test148_decomposed(self) -> None:
        pass

    def testSingletons_test147_decomposed(self) -> None:
        pass

    def testSingletons_test146_decomposed(self) -> None:
        pass

    def testSingletons_test145_decomposed(self) -> None:
        pass

    def testSingletons_test144_decomposed(self) -> None:
        pass

    def testSingletons_test143_decomposed(self) -> None:
        pass

    def testSingletons_test142_decomposed(self) -> None:
        pass

    def testSingletons_test141_decomposed(self) -> None:
        pass

    def testSingletons_test140_decomposed(self) -> None:
        pass

    def testSingletons_test139_decomposed(self) -> None:
        pass

    def testSingletons_test138_decomposed(self) -> None:
        pass

    def testSingletons_test137_decomposed(self) -> None:
        pass

    def testSingletons_test136_decomposed(self) -> None:
        pass

    def testSingletons_test135_decomposed(self) -> None:
        pass

    def testSingletons_test134_decomposed(self) -> None:
        pass

    def testSingletons_test133_decomposed(self) -> None:
        pass

    def testSingletons_test132_decomposed(self) -> None:
        pass

    def testSingletons_test131_decomposed(self) -> None:
        pass

    def testSingletons_test130_decomposed(self) -> None:
        pass

    def testSingletons_test129_decomposed(self) -> None:
        pass

    def testSingletons_test128_decomposed(self) -> None:
        pass

    def testSingletons_test127_decomposed(self) -> None:
        pass

    def testSingletons_test126_decomposed(self) -> None:
        pass

    def testSingletons_test125_decomposed(self) -> None:
        pass

    def testSingletons_test124_decomposed(self) -> None:
        pass

    def testSingletons_test123_decomposed(self) -> None:
        pass

    def testSingletons_test122_decomposed(self) -> None:
        pass

    def testSingletons_test121_decomposed(self) -> None:
        pass

    def testSingletons_test120_decomposed(self) -> None:
        pass

    def testSingletons_test119_decomposed(self) -> None:
        pass

    def testSingletons_test118_decomposed(self) -> None:
        pass

    def testSingletons_test117_decomposed(self) -> None:
        pass

    def testSingletons_test116_decomposed(self) -> None:
        pass

    def testSingletons_test115_decomposed(self) -> None:
        pass

    def testSingletons_test114_decomposed(self) -> None:
        pass

    def testSingletons_test113_decomposed(self) -> None:
        pass

    def testSingletons_test112_decomposed(self) -> None:
        pass

    def testSingletons_test111_decomposed(self) -> None:
        pass

    def testSingletons_test110_decomposed(self) -> None:
        pass

    def testSingletons_test109_decomposed(self) -> None:
        pass

    def testSingletons_test108_decomposed(self) -> None:
        pass

    def testSingletons_test107_decomposed(self) -> None:
        pass

    def testSingletons_test106_decomposed(self) -> None:
        pass

    def testSingletons_test105_decomposed(self) -> None:
        pass

    def testSingletons_test104_decomposed(self) -> None:
        pass

    def testSingletons_test103_decomposed(self) -> None:
        pass

    def testSingletons_test102_decomposed(self) -> None:
        pass

    def testSingletons_test101_decomposed(self) -> None:
        pass

    def testSingletons_test100_decomposed(self) -> None:
        pass

    def testSingletons_test99_decomposed(self) -> None:
        pass

    def testSingletons_test98_decomposed(self) -> None:
        pass

    def testSingletons_test97_decomposed(self) -> None:
        pass

    def testSingletons_test96_decomposed(self) -> None:
        pass

    def testSingletons_test95_decomposed(self) -> None:
        pass

    def testSingletons_test94_decomposed(self) -> None:
        pass

    def testSingletons_test93_decomposed(self) -> None:
        pass

    def testSingletons_test92_decomposed(self) -> None:
        pass

    def testSingletons_test91_decomposed(self) -> None:
        pass

    def testSingletons_test90_decomposed(self) -> None:
        pass

    def testSingletons_test89_decomposed(self) -> None:
        pass

    def testSingletons_test88_decomposed(self) -> None:
        pass

    def testSingletons_test87_decomposed(self) -> None:
        pass

    def testSingletons_test86_decomposed(self) -> None:
        pass

    def testSingletons_test85_decomposed(self) -> None:
        pass

    def testSingletons_test84_decomposed(self) -> None:
        pass

    def testSingletons_test83_decomposed(self) -> None:
        pass

    def testSingletons_test82_decomposed(self) -> None:
        pass

    def testSingletons_test81_decomposed(self) -> None:
        pass

    def testSingletons_test80_decomposed(self) -> None:
        pass

    def testSingletons_test79_decomposed(self) -> None:
        pass

    def testSingletons_test78_decomposed(self) -> None:
        pass

    def testSingletons_test77_decomposed(self) -> None:
        pass

    def testSingletons_test76_decomposed(self) -> None:
        pass

    def testSingletons_test75_decomposed(self) -> None:
        pass

    def testSingletons_test74_decomposed(self) -> None:
        pass

    def testSingletons_test73_decomposed(self) -> None:
        pass

    def testSingletons_test72_decomposed(self) -> None:
        pass

    def testSingletons_test71_decomposed(self) -> None:
        pass

    def testSingletons_test70_decomposed(self) -> None:
        pass

    def testSingletons_test69_decomposed(self) -> None:
        pass

    def testSingletons_test68_decomposed(self) -> None:
        pass

    def testSingletons_test67_decomposed(self) -> None:
        pass

    def testSingletons_test66_decomposed(self) -> None:
        pass

    def testSingletons_test65_decomposed(self) -> None:
        pass

    def testSingletons_test64_decomposed(self) -> None:
        pass

    def testSingletons_test63_decomposed(self) -> None:
        pass

    def testSingletons_test62_decomposed(self) -> None:
        pass

    def testSingletons_test61_decomposed(self) -> None:
        pass

    def testSingletons_test60_decomposed(self) -> None:
        pass

    def testSingletons_test59_decomposed(self) -> None:
        pass

    def testSingletons_test58_decomposed(self) -> None:
        pass

    def testSingletons_test57_decomposed(self) -> None:
        pass

    def testSingletons_test56_decomposed(self) -> None:
        pass

    def testSingletons_test55_decomposed(self) -> None:
        pass

    def testSingletons_test54_decomposed(self) -> None:
        pass

    def testSingletons_test53_decomposed(self) -> None:
        pass

    def testSingletons_test52_decomposed(self) -> None:
        pass

    def testSingletons_test51_decomposed(self) -> None:
        pass

    def testSingletons_test50_decomposed(self) -> None:
        pass

    def testSingletons_test49_decomposed(self) -> None:
        pass

    def testSingletons_test48_decomposed(self) -> None:
        pass

    def testSingletons_test47_decomposed(self) -> None:
        pass

    def testSingletons_test46_decomposed(self) -> None:
        pass

    def testSingletons_test45_decomposed(self) -> None:
        pass

    def testSingletons_test44_decomposed(self) -> None:
        pass

    def testSingletons_test43_decomposed(self) -> None:
        pass

    def testSingletons_test42_decomposed(self) -> None:
        pass

    def testSingletons_test41_decomposed(self) -> None:
        pass

    def testSingletons_test40_decomposed(self) -> None:
        pass

    def testSingletons_test39_decomposed(self) -> None:
        pass

    def testSingletons_test38_decomposed(self) -> None:
        pass

    def testSingletons_test37_decomposed(self) -> None:
        pass

    def testSingletons_test36_decomposed(self) -> None:
        pass

    def testSingletons_test35_decomposed(self) -> None:
        pass

    def testSingletons_test34_decomposed(self) -> None:
        pass

    def testSingletons_test33_decomposed(self) -> None:
        pass

    def testSingletons_test32_decomposed(self) -> None:
        pass

    def testSingletons_test31_decomposed(self) -> None:
        pass

    def testSingletons_test30_decomposed(self) -> None:
        pass

    def testSingletons_test29_decomposed(self) -> None:
        pass

    def testSingletons_test28_decomposed(self) -> None:
        pass

    def testSingletons_test27_decomposed(self) -> None:
        pass

    def testSingletons_test26_decomposed(self) -> None:
        pass

    def testSingletons_test25_decomposed(self) -> None:
        pass

    def testSingletons_test24_decomposed(self) -> None:
        pass

    def testSingletons_test23_decomposed(self) -> None:
        pass

    def testSingletons_test22_decomposed(self) -> None:
        pass

    def testSingletons_test21_decomposed(self) -> None:
        pass

    def testSingletons_test20_decomposed(self) -> None:
        pass

    def testSingletons_test19_decomposed(self) -> None:
        pass

    def testSingletons_test18_decomposed(self) -> None:
        pass

    def testSingletons_test17_decomposed(self) -> None:
        pass

    def testSingletons_test16_decomposed(self) -> None:
        pass

    def testSingletons_test15_decomposed(self) -> None:
        pass

    def testSingletons_test14_decomposed(self) -> None:
        pass

    def testSingletons_test13_decomposed(self) -> None:
        pass

    def testSingletons_test12_decomposed(self) -> None:
        pass

    def testSingletons_test11_decomposed(self) -> None:
        pass

    def testSingletons_test10_decomposed(self) -> None:
        pass

    def testSingletons_test9_decomposed(self) -> None:
        pass

    def testSingletons_test8_decomposed(self) -> None:
        pass

    def testSingletons_test7_decomposed(self) -> None:
        pass

    def testSingletons_test6_decomposed(self) -> None:
        pass

    def testSingletons_test5_decomposed(self) -> None:
        pass

    def testSingletons_test4_decomposed(self) -> None:
        pass

    def testSingletons_test3_decomposed(self) -> None:
        pass

    def testSingletons_test2_decomposed(self) -> None:
        pass

    def testSingletons_test1_decomposed(self) -> None:
        pass

    def testSingletons_test0_decomposed(self) -> None:
        pass

    def testPairs_test36_decomposed(self) -> None:
        pass

    def testPairs_test35_decomposed(self) -> None:
        pass

    def testPairs_test34_decomposed(self) -> None:
        pass

    def testPairs_test33_decomposed(self) -> None:
        pass

    def testPairs_test32_decomposed(self) -> None:
        pass

    def testPairs_test31_decomposed(self) -> None:
        pass

    def testPairs_test30_decomposed(self) -> None:
        pass

    def testPairs_test29_decomposed(self) -> None:
        pass

    def testPairs_test28_decomposed(self) -> None:
        pass

    def testPairs_test27_decomposed(self) -> None:
        pass

    def testPairs_test26_decomposed(self) -> None:
        pass

    def testPairs_test25_decomposed(self) -> None:
        pass

    def testPairs_test24_decomposed(self) -> None:
        pass

    def testPairs_test23_decomposed(self) -> None:
        pass

    def testPairs_test22_decomposed(self) -> None:
        pass

    def testPairs_test21_decomposed(self) -> None:
        pass

    def testPairs_test20_decomposed(self) -> None:
        pass

    def testPairs_test19_decomposed(self) -> None:
        pass

    def testPairs_test18_decomposed(self) -> None:
        pass

    def testPairs_test17_decomposed(self) -> None:
        pass

    def testPairs_test16_decomposed(self) -> None:
        pass

    def testPairs_test15_decomposed(self) -> None:
        pass

    def testPairs_test14_decomposed(self) -> None:
        pass

    def testPairs_test13_decomposed(self) -> None:
        pass

    def testPairs_test12_decomposed(self) -> None:
        pass

    def testPairs_test11_decomposed(self) -> None:
        pass

    def testPairs_test10_decomposed(self) -> None:
        pass

    def testPairs_test9_decomposed(self) -> None:
        pass

    def testPairs_test8_decomposed(self) -> None:
        pass

    def testPairs_test7_decomposed(self) -> None:
        pass

    def testPairs_test6_decomposed(self) -> None:
        pass

    def testPairs_test5_decomposed(self) -> None:
        pass

    def testPairs_test4_decomposed(self) -> None:
        pass

    def testPairs_test3_decomposed(self) -> None:
        pass

    def testPairs_test2_decomposed(self) -> None:
        pass

    def testPairs_test1_decomposed(self) -> None:
        pass

    def testPairs_test0_decomposed(self) -> None:
        pass

    def testObjectEncode_test2_decomposed(self) -> None:
        pass

    def testObjectEncode_test1_decomposed(self) -> None:
        pass

    def testObjectEncode_test0_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test5_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test4_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test3_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test2_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectEncodeWithValidParameter_test0_decomposed(self) -> None:
        pass

    def testObjectEncodeWithInvalidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectEncodeWithInvalidParameter_test0_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test5_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test4_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test3_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test2_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectDecodeWithValidParameter_test0_decomposed(self) -> None:
        pass

    def testObjectDecodeWithInvalidParameter_test1_decomposed(self) -> None:
        pass

    def testObjectDecodeWithInvalidParameter_test0_decomposed(self) -> None:
        pass

    def testNonBase16Test_test0_decomposed(self) -> None:
        pass

    def testKnownEncodings_test17_decomposed(self) -> None:
        pass

    def testKnownEncodings_test16_decomposed(self) -> None:
        pass

    def testKnownEncodings_test15_decomposed(self) -> None:
        pass

    def testKnownEncodings_test14_decomposed(self) -> None:
        pass

    def testKnownEncodings_test13_decomposed(self) -> None:
        pass

    def testKnownEncodings_test12_decomposed(self) -> None:
        pass

    def testKnownEncodings_test11_decomposed(self) -> None:
        pass

    def testKnownEncodings_test10_decomposed(self) -> None:
        pass

    def testKnownEncodings_test9_decomposed(self) -> None:
        pass

    def testKnownEncodings_test8_decomposed(self) -> None:
        pass

    def testKnownEncodings_test7_decomposed(self) -> None:
        pass

    def testKnownEncodings_test6_decomposed(self) -> None:
        pass

    def testKnownEncodings_test5_decomposed(self) -> None:
        pass

    def testKnownEncodings_test4_decomposed(self) -> None:
        pass

    def testKnownEncodings_test3_decomposed(self) -> None:
        pass

    def testKnownEncodings_test2_decomposed(self) -> None:
        pass

    def testKnownEncodings_test1_decomposed(self) -> None:
        pass

    def testKnownEncodings_test0_decomposed(self) -> None:
        pass

    def testKnownDecodings_test17_decomposed(self) -> None:
        pass

    def testKnownDecodings_test16_decomposed(self) -> None:
        pass

    def testKnownDecodings_test15_decomposed(self) -> None:
        pass

    def testKnownDecodings_test14_decomposed(self) -> None:
        pass

    def testKnownDecodings_test13_decomposed(self) -> None:
        pass

    def testKnownDecodings_test12_decomposed(self) -> None:
        pass

    def testKnownDecodings_test11_decomposed(self) -> None:
        pass

    def testKnownDecodings_test10_decomposed(self) -> None:
        pass

    def testKnownDecodings_test9_decomposed(self) -> None:
        pass

    def testKnownDecodings_test8_decomposed(self) -> None:
        pass

    def testKnownDecodings_test7_decomposed(self) -> None:
        pass

    def testKnownDecodings_test6_decomposed(self) -> None:
        pass

    def testKnownDecodings_test5_decomposed(self) -> None:
        pass

    def testKnownDecodings_test4_decomposed(self) -> None:
        pass

    def testKnownDecodings_test3_decomposed(self) -> None:
        pass

    def testKnownDecodings_test2_decomposed(self) -> None:
        pass

    def testKnownDecodings_test1_decomposed(self) -> None:
        pass

    def testKnownDecodings_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeSmall_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeRandom_test0_decomposed(self) -> None:
        pass

    def testEmptyBase16_test11_decomposed(self) -> None:
        pass

    def testEmptyBase16_test10_decomposed(self) -> None:
        pass

    def testEmptyBase16_test9_decomposed(self) -> None:
        pass

    def testEmptyBase16_test8_decomposed(self) -> None:
        pass

    def testEmptyBase16_test7_decomposed(self) -> None:
        pass

    def testEmptyBase16_test6_decomposed(self) -> None:
        pass

    def testEmptyBase16_test5_decomposed(self) -> None:
        pass

    def testEmptyBase16_test4_decomposed(self) -> None:
        pass

    def testEmptyBase16_test3_decomposed(self) -> None:
        pass

    def testEmptyBase16_test2_decomposed(self) -> None:
        pass

    def testEmptyBase16_test1_decomposed(self) -> None:
        pass

    def testEmptyBase16_test0_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_DecodingPolicy_test3_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_DecodingPolicy_test2_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_DecodingPolicy_test1_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_DecodingPolicy_test0_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_test3_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_test2_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_test1_decomposed(self) -> None:
        pass

    def testConstructor_LowerCase_test0_decomposed(self) -> None:
        pass

    def testConstructors_test3_decomposed(self) -> None:
        pass

    def testConstructors_test2_decomposed(self) -> None:
        pass

    def testConstructors_test1_decomposed(self) -> None:
        pass

    def testConstructors_test0_decomposed(self) -> None:
        pass

    def testCodec68_test1_decomposed(self) -> None:
        pass

    def testCodec68_test0_decomposed(self) -> None:
        pass

    def testBase16_test7_decomposed(self) -> None:
        pass

    def testBase16_test6_decomposed(self) -> None:
        pass

    def testBase16_test5_decomposed(self) -> None:
        pass

    def testBase16_test4_decomposed(self) -> None:
        pass

    def testBase16_test3_decomposed(self) -> None:
        pass

    def testBase16_test2_decomposed(self) -> None:
        pass

    def testBase16_test1_decomposed(self) -> None:
        pass

    def testBase16_test0_decomposed(self) -> None:
        pass

    def getRandom(self) -> random.Random:
        pass

    def __toString(self, data: typing.List[int]) -> str:
        pass

    # Class Methods End
