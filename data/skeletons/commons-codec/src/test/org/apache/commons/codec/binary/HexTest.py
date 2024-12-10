from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
import unittest
import os
import typing
from typing import *
import io

# Imports End


class HexTest(unittest.TestCase):

    # Class Fields Begin
    __BAD_ENCODING_NAME: str = None
    __LOG: bool = None
    # Class Fields End

    # Class Methods Begin
    def testRequiredCharset_test0_decomposed(self) -> None:
        pass

    def testGetCharsetName_test0_decomposed(self) -> None:
        pass

    def testGetCharset_test0_decomposed(self) -> None:
        pass

    def testEncodeStringEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeHexReadOnlyByteBuffer_test1_decomposed(self) -> None:
        pass

    def testEncodeHexReadOnlyByteBuffer_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test3_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test2_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test1_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test3_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test2_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test1_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test2_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test1_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test2_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test1_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteArrayBoolean_ToUpperCase_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteArrayOfZeroes_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteString_ByteArrayOfZeroes_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test3_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test2_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test1_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit_test0_decomposed(
        self,
    ) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroes_test2_decomposed(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroes_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroes_test0_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInputOverbounds_test2_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInputOverbounds_test1_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInputOverbounds_test0_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInputUnderbounds_test2_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInputUnderbounds_test1_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInputUnderbounds_test0_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test8_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test7_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test6_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test5_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test4_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test3_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test2_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test1_decomposed(self) -> None:
        pass

    def testEncodeHexPartialInput_test0_decomposed(self) -> None:
        pass

    def testEncodeHex_ByteBufferWithLimit_test2_decomposed(self) -> None:
        pass

    def testEncodeHex_ByteBufferWithLimit_test1_decomposed(self) -> None:
        pass

    def testEncodeHex_ByteBufferWithLimit_test0_decomposed(self) -> None:
        pass

    def testEncodeHex_ByteBufferOfZeroes_test2_decomposed(self) -> None:
        pass

    def testEncodeHex_ByteBufferOfZeroes_test1_decomposed(self) -> None:
        pass

    def testEncodeHex_ByteBufferOfZeroes_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test6_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test5_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test4_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test3_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test2_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test6_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test5_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test4_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test3_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test2_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferEmpty_test3_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferEmpty_test2_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteBufferEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayZeroes_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayZeroes_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test4_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test3_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test2_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldUpperCaseHex_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test4_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test3_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test2_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldLowerCaseHex_test0_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeHexByteArrayEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeHexCharArrayRandomToOutput_test0_decomposed(self) -> None:
        pass

    def testEncodeDecodeHexCharArrayRandom_test1_decomposed(self) -> None:
        pass

    def testEncodeDecodeHexCharArrayRandom_test0_decomposed(self) -> None:
        pass

    def testEncodeClassCastException_test0_decomposed(self) -> None:
        pass

    def testEncodeByteBufferObjectEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeByteBufferObjectEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeByteBufferAllocatedButEmpty_test2_decomposed(self) -> None:
        pass

    def testEncodeByteBufferAllocatedButEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeByteBufferAllocatedButEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeByteBufferEmpty_test1_decomposed(self) -> None:
        pass

    def testEncodeByteBufferEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeByteArrayObjectEmpty_test0_decomposed(self) -> None:
        pass

    def testEncodeByteArrayEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeByteBufferWithLimit_test1_decomposed(self) -> None:
        pass

    def testDecodeByteBufferWithLimit_test0_decomposed(self) -> None:
        pass

    def testDecodeStringEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeHexStringOddCharacters_test0_decomposed(self) -> None:
        pass

    def testDecodeHexCharArrayOutBufferUnderSizedByOffset_test0_decomposed(
        self,
    ) -> None:
        pass

    def testDecodeHexCharArrayOutBufferUnderSized_test0_decomposed(self) -> None:
        pass

    def testDecodeHexCharArrayOddCharacters5_test0_decomposed(self) -> None:
        pass

    def testDecodeHexCharArrayOddCharacters3_test0_decomposed(self) -> None:
        pass

    def testDecodeHexStringOddCharacters1_test0_decomposed(self) -> None:
        pass

    def testDecodeHexCharArrayOddCharacters1_test0_decomposed(self) -> None:
        pass

    def testDecodeClassCastException_test0_decomposed(self) -> None:
        pass

    def testDecodeHexStringEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeHexCharArrayEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeByteBufferWithLimitOddCharacters_test2_decomposed(self) -> None:
        pass

    def testDecodeByteBufferWithLimitOddCharacters_test1_decomposed(self) -> None:
        pass

    def testDecodeByteBufferWithLimitOddCharacters_test0_decomposed(self) -> None:
        pass

    def testDecodeByteBufferOddCharacters_test2_decomposed(self) -> None:
        pass

    def testDecodeByteBufferOddCharacters_test1_decomposed(self) -> None:
        pass

    def testDecodeByteBufferOddCharacters_test0_decomposed(self) -> None:
        pass

    def testDecodeByteBufferObjectEmpty_test1_decomposed(self) -> None:
        pass

    def testDecodeByteBufferObjectEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeByteBufferAllocatedButEmpty_test2_decomposed(self) -> None:
        pass

    def testDecodeByteBufferAllocatedButEmpty_test1_decomposed(self) -> None:
        pass

    def testDecodeByteBufferAllocatedButEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeByteBufferEmpty_test1_decomposed(self) -> None:
        pass

    def testDecodeByteBufferEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeByteArrayOddCharacters_test0_decomposed(self) -> None:
        pass

    def testDecodeByteArrayObjectEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeByteArrayEmpty_test0_decomposed(self) -> None:
        pass

    def testDecodeBadCharacterPos1_test0_decomposed(self) -> None:
        pass

    def testDecodeBadCharacterPos0_test0_decomposed(self) -> None:
        pass

    def testCustomCharsetToString_test0_decomposed(self) -> None:
        pass

    def testCustomCharsetBadName_test0_decomposed(self) -> None:
        pass

    def testCustomCharset0_test0_decomposed(self) -> None:
        pass

    def _allocate(self, capacity: int) -> typing.Union[bytearray, memoryview]:
        pass

    def __testCustomCharset1(self, name: str, parent: str) -> None:
        pass

    def __log1(self, t: BaseException) -> None:
        pass

    def __log0(self, s: str) -> None:
        pass

    def __checkDecodeHexCharArrayOddCharacters1(self, data: str) -> None:
        pass

    def __checkDecodeHexByteBufferOddCharacters(
        self, data: typing.Union[bytearray, memoryview]
    ) -> None:
        pass

    def __checkDecodeHexCharArrayOddCharacters0(self, data: typing.List[str]) -> None:
        pass

    def __charsetSanityCheck(self, name: str) -> bool:
        pass

    def __getByteBufferUtf8(self, string: str) -> typing.Union[bytearray, memoryview]:
        pass

    # Class Methods End
