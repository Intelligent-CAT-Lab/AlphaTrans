# Imports Begin
from src.main.org.apache.commons.codec.binary.StringUtils import *
from src.main.org.apache.commons.codec.binary.Hex import *
from src.main.org.apache.commons.codec.EncoderException import *
from src.main.org.apache.commons.codec.DecoderException import *
import typing

# Imports End


class HexTest:

    # Class Fields Begin
    __BAD_ENCODING_NAME: str = None
    __LOG: bool = None
    # Class Fields End

    # Class Methods Begin
    def testRequiredCharset(self) -> None:
        pass

    def testGetCharsetName(self) -> None:
        pass

    def testGetCharset(self) -> None:
        pass

    def testEncodeStringEmpty(self) -> None:
        pass

    def testEncodeHexReadOnlyByteBuffer(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToUpperCase(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferWithLimitBoolean_ToLowerCase(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToUpperCase(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferBoolean_ToLowerCase(self) -> None:
        pass

    def testEncodeHexByteString_ByteArrayBoolean_ToUpperCase(self) -> None:
        pass

    def testEncodeHexByteString_ByteArrayBoolean_ToLowerCase(self) -> None:
        pass

    def testEncodeHexByteString_ByteArrayOfZeroes(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroesWithLimit(self) -> None:
        pass

    def testEncodeHexByteString_ByteBufferOfZeroes(self) -> None:
        pass

    def testEncodeHexPartialInputOverbounds(self) -> None:
        pass

    def testEncodeHexPartialInputUnderbounds(self) -> None:
        pass

    def testEncodeHexPartialInput(self) -> None:
        pass

    def testEncodeHex_ByteBufferWithLimit(self) -> None:
        pass

    def testEncodeHex_ByteBufferOfZeroes(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldUpperCaseHex(self) -> None:
        pass

    def testEncodeHexByteBufferHelloWorldLowerCaseHex(self) -> None:
        pass

    def testEncodeHexByteBufferEmpty(self) -> None:
        pass

    def testEncodeHexByteArrayZeroes(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldUpperCaseHex(self) -> None:
        pass

    def testEncodeHexByteArrayHelloWorldLowerCaseHex(self) -> None:
        pass

    def testEncodeHexByteArrayEmpty(self) -> None:
        pass

    def testEncodeDecodeHexCharArrayRandomToOutput(self) -> None:
        pass

    def testEncodeDecodeHexCharArrayRandom(self) -> None:
        pass

    def testEncodeClassCastException(self) -> None:
        pass

    def testEncodeByteBufferObjectEmpty(self) -> None:
        pass

    def testEncodeByteBufferAllocatedButEmpty(self) -> None:
        pass

    def testEncodeByteBufferEmpty(self) -> None:
        pass

    def testEncodeByteArrayObjectEmpty(self) -> None:
        pass

    def testEncodeByteArrayEmpty(self) -> None:
        pass

    def testDecodeByteBufferWithLimit(self) -> None:
        pass

    def testDecodeStringEmpty(self) -> None:
        pass

    def testDecodeHexStringOddCharacters(self) -> None:
        pass

    def testDecodeHexCharArrayOutBufferUnderSizedByOffset(self) -> None:
        pass

    def testDecodeHexCharArrayOutBufferUnderSized(self) -> None:
        pass

    def testDecodeHexCharArrayOddCharacters5(self) -> None:
        pass

    def testDecodeHexCharArrayOddCharacters3(self) -> None:
        pass

    def testDecodeHexStringOddCharacters1(self) -> None:
        pass

    def testDecodeHexCharArrayOddCharacters1(self) -> None:
        pass

    def testDecodeClassCastException(self) -> None:
        pass

    def testDecodeHexStringEmpty(self) -> None:
        pass

    def testDecodeHexCharArrayEmpty(self) -> None:
        pass

    def testDecodeByteBufferWithLimitOddCharacters(self) -> None:
        pass

    def testDecodeByteBufferOddCharacters(self) -> None:
        pass

    def testDecodeByteBufferObjectEmpty(self) -> None:
        pass

    def testDecodeByteBufferAllocatedButEmpty(self) -> None:
        pass

    def testDecodeByteBufferEmpty(self) -> None:
        pass

    def testDecodeByteArrayOddCharacters(self) -> None:
        pass

    def testDecodeByteArrayObjectEmpty(self) -> None:
        pass

    def testDecodeByteArrayEmpty(self) -> None:
        pass

    def testDecodeBadCharacterPos1(self) -> None:
        pass

    def testDecodeBadCharacterPos0(self) -> None:
        pass

    def testCustomCharsetToString(self) -> None:
        pass

    def testCustomCharsetBadName(self) -> None:
        pass

    def testCustomCharset0(self) -> None:
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
