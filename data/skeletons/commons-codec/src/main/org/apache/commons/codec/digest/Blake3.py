from __future__ import annotations

# Imports Begin
import typing
from typing import *
import io

# Imports End


class EngineState:

    # Class Fields Begin
    __key: typing.List[int] = None
    __flags: int = None
    __cvStack: typing.List[typing.List[int]] = None
    __stackLen: int = None
    __state: ChunkState = None
    # Class Fields End

    # Class Methods Begin
    def __popCV(self) -> typing.List[int]:
        pass

    def __pushCV(self, cv: typing.List[int]) -> None:
        pass

    def __addChunkCV(self, firstCV: typing.List[int], totalChunks: int) -> None:
        pass

    def reset(self) -> None:
        pass

    def outputHash(self, out: typing.List[int], offset: int, length: int) -> None:
        pass

    def inputData(self, in_: typing.List[int], offset: int, length: int) -> None:
        pass

    def __init__(self, key: typing.List[int], flags: int) -> None:
        pass

    # Class Methods End


class ChunkState:

    # Class Fields Begin
    __chainingValue: typing.List[int] = None
    __chunkCounter: int = None
    __flags: int = None
    __block: typing.List[int] = None
    __blockLength: int = None
    __blocksCompressed: int = None
    # Class Fields End

    # Class Methods Begin
    def output(self) -> Output:
        pass

    def update(self, input_: typing.List[int], offset: int, length: int) -> None:
        pass

    def startFlag(self) -> int:
        pass

    def length(self) -> int:
        pass

    def __init__(self, key: typing.List[int], chunkCounter: int, flags: int) -> None:
        pass

    # Class Methods End


class Output:

    # Class Fields Begin
    __inputChainingValue: typing.List[int] = None
    __blockWords: typing.List[int] = None
    __counter: int = None
    __blockLength: int = None
    __flags: int = None
    # Class Fields End

    # Class Methods Begin
    def rootOutputBytes(self, out: typing.List[int], offset: int, length: int) -> None:
        pass

    def chainingValue(self) -> typing.List[int]:
        pass

    def __init__(
        self,
        inputChainingValue: typing.List[int],
        blockWords: typing.List[int],
        counter: int,
        blockLength: int,
        flags: int,
    ) -> None:
        pass

    # Class Methods End


class Blake3:

    # Class Fields Begin
    __CHUNK_START: int = None
    __CHUNK_END: int = None
    __PARENT: int = None
    __ROOT: int = None
    __KEYED_HASH: int = None
    __DERIVE_KEY_CONTEXT: int = None
    __DERIVE_KEY_MATERIAL: int = None
    __engineState: EngineState = None
    __MSG_SCHEDULE: typing.List[typing.List[int]] = None
    __INT_BYTES: int = None
    __BLOCK_LEN: int = None
    __BLOCK_INTS: int = None
    __KEY_LEN: int = None
    __KEY_INTS: int = None
    __OUT_LEN: int = None
    __CHUNK_LEN: int = None
    __CHAINING_VALUE_INTS: int = None
    __IV: typing.List[int] = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def keyedHash(key: typing.List[int], data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def hash_(data: typing.List[int]) -> typing.List[int]:
        pass

    @staticmethod
    def initKeyDerivationFunction(kdfContext: typing.List[int]) -> Blake3:
        pass

    @staticmethod
    def initKeyedHash(key: typing.List[int]) -> Blake3:
        pass

    @staticmethod
    def initHash() -> Blake3:
        pass

    def doFinalize2(self, nrBytes: int) -> typing.List[int]:
        pass

    def doFinalize1(self, out: typing.List[int], offset: int, length: int) -> None:
        pass

    def doFinalize0(self, out: typing.List[int]) -> None:
        pass

    def update1(self, in_: typing.List[int], offset: int, length: int) -> None:
        pass

    def update0(self, in_: typing.List[int]) -> None:
        pass

    def reset(self) -> None:
        pass

    @staticmethod
    def __parentChainingValue(
        leftChildCV: typing.List[int],
        rightChildCV: typing.List[int],
        key: typing.List[int],
        flags: int,
    ) -> typing.List[int]:
        pass

    @staticmethod
    def __parentOutput(
        leftChildCV: typing.List[int],
        rightChildCV: typing.List[int],
        key: typing.List[int],
        flags: int,
    ) -> Output:
        pass

    @staticmethod
    def __compress(
        chainingValue: typing.List[int],
        blockWords: typing.List[int],
        blockLength: int,
        counter: int,
        flags: int,
    ) -> typing.List[int]:
        pass

    @staticmethod
    def __round_(
        state: typing.List[int], msg: typing.List[int], schedule: typing.List[int]
    ) -> None:
        pass

    @staticmethod
    def __g(
        state: typing.List[int], a: int, b: int, c: int, d: int, mx: int, my: int
    ) -> None:
        pass

    @staticmethod
    def __unpackInts(buf: typing.List[int], nrInts: int) -> typing.List[int]:
        pass

    @staticmethod
    def __unpackInt(buf: typing.List[int], off: int) -> int:
        pass

    @staticmethod
    def __packInt(value: int, dst: typing.List[int], off: int, len_: int) -> None:
        pass

    @staticmethod
    def __checkBufferArgs(buffer: typing.List[int], offset: int, length: int) -> None:
        pass

    def __init__(self, key: typing.List[int], flags: int) -> None:
        pass

    # Class Methods End
