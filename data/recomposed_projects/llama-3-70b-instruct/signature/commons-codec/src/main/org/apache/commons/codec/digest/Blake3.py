from __future__ import annotations
import copy
import re
import io
import typing
from typing import *


class EngineState:

    __state: ChunkState = None

    __stackLen: int = 0

    __cvStack: typing.List[typing.List[int]] = [None] * 54
    __flags: int = 0

    __key: typing.List[int] = None

    def __popCV(self) -> typing.List[int]:
        return self.__cvStack[self.__stackLen - 1]

    def __pushCV(self, cv: typing.List[int]) -> None:
        self.__cvStack[self.__stackLen] = cv
        self.__stackLen += 1

    def __addChunkCV(self, firstCV: typing.List[int], totalChunks: int) -> None:
        newCV: typing.List[int] = firstCV
        chunkCounter: int = totalChunks
        while (chunkCounter & 1) == 0:
            newCV = Blake3.__parentChainingValue(
                self.__popCV(), newCV, self.__key, self.__flags
            )
            chunkCounter >>= 1
        self.__pushCV(newCV)

    def reset(self) -> None:
        self.__stackLen = 0
        self.__cvStack = [None] * 54
        self.__state = ChunkState(self.__key, 0, self.__flags)

    def outputHash(self, out: typing.List[int], offset: int, length: int) -> None:
        output = self.__state.output()
        parentNodesRemaining = self.__stackLen
        while parentNodesRemaining > 0:
            parentNodesRemaining -= 1
            parentCV = self.__cvStack[parentNodesRemaining]
            output = Blake3.__parentOutput(
                parentCV, output.chainingValue(), self.__key, self.__flags
            )
        output.rootOutputBytes(out, offset, length)

    def inputData(self, in_: typing.List[int], offset: int, length: int) -> None:
        while length > 0:
            if self.__state.length() == CHUNK_LEN:
                chunkCV = self.__state.output().chainingValue()
                totalChunks = self.__state.chunkCounter + 1
                self.__addChunkCV(chunkCV, totalChunks)
                self.__state = ChunkState(self.__key, totalChunks, self.__flags)
            want = CHUNK_LEN - self.__state.length()
            take = min(want, length)
            self.__state.update(in_, offset, take)
            offset += take
            length -= take

    def __init__(self, key: typing.List[int], flags: int) -> None:
        self.__key = key
        self.__flags = flags
        self.__state = ChunkState(key, 0, flags)


class ChunkState:

    __blocksCompressed: int = 0

    __blockLength: int = 0

    __block: typing.List[int] = None
    __flags: int = 0

    __chunkCounter: int = 0

    __chainingValue: typing.List[int] = None

    @staticmethod
    def initialize_fields() -> None:
        ChunkState.__block: typing.List[int] = [0] * ChunkState.__BLOCK_LEN

    def output(self) -> Output:
        blockWords = Blake3.__unpackInts(self.__block, Blake3.__BLOCK_INTS)
        outputFlags = self.__flags | self.startFlag() | Blake3.__CHUNK_END
        return Output(
            self.__chainingValue,
            blockWords,
            self.__chunkCounter,
            self.__blockLength,
            outputFlags,
        )

    def update(self, input: typing.List[int], offset: int, length: int) -> None:
        while length > 0:
            if self.__blockLength == Blake3.__BLOCK_LEN:
                blockWords = Blake3.__unpackInts(self.__block, Blake3.__BLOCK_INTS)
                self.__chainingValue = Blake3.__compress(
                    self.__chainingValue,
                    blockWords,
                    Blake3.__BLOCK_LEN,
                    self.__chunkCounter,
                    self.__flags | self.startFlag(),
                )
                self.__blocksCompressed += 1
                self.__blockLength = 0
                self.__block = [0] * Blake3.__BLOCK_LEN
            want = Blake3.__BLOCK_LEN - self.__blockLength
            take = min(want, length)
            input[offset : offset + take] = self.__block[
                self.__blockLength : self.__blockLength + take
            ]
            self.__blockLength += take
            offset += take
            length -= take

    def startFlag(self) -> int:
        return 0 if self.__blocksCompressed == 0 else CHUNK_START

    def length(self) -> int:
        return BLOCK_LEN * self.__blocksCompressed + self.__blockLength

    def __init__(self, key: typing.List[int], chunkCounter: int, flags: int) -> None:
        self.__chainingValue = key
        self.__chunkCounter = chunkCounter
        self.__flags = flags


class Output:

    __flags: int = 0

    __blockLength: int = 0

    __counter: int = 0

    __blockWords: typing.List[int] = None

    __inputChainingValue: typing.List[int] = None

    def rootOutputBytes(self, out: typing.List[int], offset: int, length: int) -> None:

        pass  # LLM could not translate this method

    def chainingValue(self) -> typing.List[int]:
        return Blake3.__compress(
            self.__inputChainingValue,
            self.__blockWords,
            self.__blockLength,
            self.__counter,
            self.__flags,
        )

    def __init__(
        self,
        inputChainingValue: typing.List[int],
        blockWords: typing.List[int],
        counter: int,
        blockLength: int,
        flags: int,
    ) -> None:
        self.__inputChainingValue = inputChainingValue
        self.__blockWords = blockWords
        self.__counter = counter
        self.__blockLength = blockLength
        self.__flags = flags


class Blake3:

    __MSG_SCHEDULE: typing.List[typing.List[int]] = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [2, 6, 3, 10, 7, 0, 4, 13, 1, 11, 12, 5, 9, 14, 15, 8],
        [3, 4, 10, 12, 13, 2, 7, 14, 6, 5, 9, 0, 11, 15, 8, 1],
        [10, 7, 12, 9, 14, 3, 13, 15, 4, 0, 11, 2, 5, 8, 1, 6],
        [12, 13, 9, 11, 15, 10, 14, 8, 7, 2, 5, 3, 0, 1, 6, 4],
        [9, 14, 11, 5, 8, 12, 15, 1, 13, 3, 0, 10, 2, 6, 4, 7],
        [11, 15, 5, 0, 1, 9, 8, 6, 14, 10, 2, 12, 3, 4, 7, 13],
    ]
    __engineState: EngineState = None

    __DERIVE_KEY_MATERIAL: int = 1 << 6
    __DERIVE_KEY_CONTEXT: int = 1 << 5
    __KEYED_HASH: int = 1 << 4
    __ROOT: int = 1 << 3
    __PARENT: int = 1 << 2
    __CHUNK_END: int = 1 << 1
    __CHUNK_START: int = 1
    __IV: typing.List[int] = [
        0x6A09E667,
        0xBB67AE85,
        0x3C6EF372,
        0xA54FF53A,
        0x510E527F,
        0x9B05688C,
        0x1F83D9AB,
        0x5BE0CD19,
    ]
    __CHAINING_VALUE_INTS: int = 8
    __CHUNK_LEN: int = 1024
    __OUT_LEN: int = 32
    __KEY_LEN: int = 32
    __BLOCK_INTS: int = 16
    __BLOCK_LEN: int = 64
    __INT_BYTES: int = 4
    __KEY_INTS: int = __KEY_LEN // __INT_BYTES

    @staticmethod
    def keyedHash(key: typing.List[int], data: typing.List[int]) -> typing.List[int]:
        blake3 = Blake3.initKeyedHash(key)
        blake3.update0(data)
        return blake3.doFinalize2(Blake3.__OUT_LEN)

    @staticmethod
    def hash(data: typing.List[int]) -> typing.List[int]:
        blake3 = Blake3.initHash()
        blake3.update0(data)
        return blake3.doFinalize2(OUT_LEN)

    @staticmethod
    def initKeyDerivationFunction(kdfContext: typing.List[int]) -> Blake3:
        Objects.requireNonNull(kdfContext)
        kdf = EngineState(IV, DERIVE_KEY_CONTEXT)
        kdf.inputData(kdfContext, 0, kdfContext.length)
        key = [0] * KEY_LEN
        kdf.outputHash(key, 0, key.length)
        return Blake3(unpackInts(key, KEY_INTS), DERIVE_KEY_MATERIAL)

    @staticmethod
    def initKeyedHash(key: typing.List[int]) -> Blake3:
        Objects.requireNonNull(key)
        if key.length != KEY_LEN:
            raise ValueError("Blake3 keys must be 32 bytes")
        return Blake3(unpackInts(key, KEY_INTS), KEYED_HASH)

    @staticmethod
    def initHash() -> Blake3:
        return Blake3(IV, 0)

    def doFinalize2(self, nrBytes: int) -> typing.List[int]:
        if nrBytes < 0:
            raise ValueError("Requested bytes must be non-negative")
        hash = [0] * nrBytes
        self.doFinalize0(hash)
        return hash

    def doFinalize1(self, out: typing.List[int], offset: int, length: int) -> None:
        self.__checkBufferArgs(out, offset, length)
        self.__engineState.outputHash(out, offset, length)

    def doFinalize0(self, out: typing.List[int]) -> None:
        Objects.requireNonNull(out)
        doFinalize1(out, 0, out.length)

    def update1(self, in_: typing.List[int], offset: int, length: int) -> None:
        self.__checkBufferArgs(in_, offset, length)
        self.__engineState.inputData(in_, offset, length)

    def update0(self, in_: typing.List[int]) -> None:
        Objects.requireNonNull(in_)
        self.update1(in_, 0, len(in_))

    def reset(self) -> None:
        self.__engineState.reset()

    @staticmethod
    def __parentChainingValue(
        leftChildCV: typing.List[int],
        rightChildCV: typing.List[int],
        key: typing.List[int],
        flags: int,
    ) -> typing.List[int]:
        return Blake3.__parentOutput(
            leftChildCV, rightChildCV, key, flags
        ).chainingValue()

    @staticmethod
    def __parentOutput(
        leftChildCV: typing.List[int],
        rightChildCV: typing.List[int],
        key: typing.List[int],
        flags: int,
    ) -> Output:
        blockWords = leftChildCV.copy()
        blockWords[8 : 8 + CHAINING_VALUE_INTS] = rightChildCV[0:CHAINING_VALUE_INTS]
        return Output(key.copy(), blockWords, 0, BLOCK_LEN, flags | PARENT)

    @staticmethod
    def __compress(
        chainingValue: typing.List[int],
        blockWords: typing.List[int],
        blockLength: int,
        counter: int,
        flags: int,
    ) -> typing.List[int]:
        state = chainingValue.copy()
        state[8:12] = Blake3.__IV[0:4]
        state[12] = counter
        state[13] = counter >> 32
        state[14] = blockLength
        state[15] = flags
        for i in range(7):
            schedule = Blake3.__MSG_SCHEDULE[i]
            Blake3.__round(state, blockWords, schedule)
        for i in range(len(state) // 2):
            state[i] ^= state[i + 8]
            state[i + 8] ^= chainingValue[i]
        return state

    @staticmethod
    def __round(
        state: typing.List[int], msg: typing.List[int], schedule: typing.List[int]
    ) -> None:
        Blake3.__g(state, 0, 4, 8, 12, msg[schedule[0]], msg[schedule[1]])
        Blake3.__g(state, 1, 5, 9, 13, msg[schedule[2]], msg[schedule[3]])
        Blake3.__g(state, 2, 6, 10, 14, msg[schedule[4]], msg[schedule[5]])
        Blake3.__g(state, 3, 7, 11, 15, msg[schedule[6]], msg[schedule[7]])

        Blake3.__g(state, 0, 5, 10, 15, msg[schedule[8]], msg[schedule[9]])
        Blake3.__g(state, 1, 6, 11, 12, msg[schedule[10]], msg[schedule[11]])
        Blake3.__g(state, 2, 7, 8, 13, msg[schedule[12]], msg[schedule[13]])
        Blake3.__g(state, 3, 4, 9, 14, msg[schedule[14]], msg[schedule[15]])

    @staticmethod
    def __g(
        state: typing.List[int], a: int, b: int, c: int, d: int, mx: int, my: int
    ) -> None:
        state[a] += state[b] + mx
        state[d] = state[d] ^ state[a]
        state[d] = state[d] >> 16
        state[c] += state[d]
        state[b] = state[b] ^ state[c]
        state[b] = state[b] >> 12
        state[a] += state[b] + my
        state[d] = state[d] ^ state[a]
        state[d] = state[d] >> 8
        state[c] += state[d]
        state[b] = state[b] ^ state[c]
        state[b] = state[b] >> 7

    @staticmethod
    def __unpackInts(buf: typing.List[int], nrInts: int) -> typing.List[int]:
        values: typing.List[int] = [0] * nrInts
        for i in range(nrInts):
            values[i] = Blake3.__unpackInt(buf, i * Blake3.__INT_BYTES)
        return values

    @staticmethod
    def __unpackInt(buf: typing.List[int], off: int) -> int:
        return (
            buf[off] & 0xFF
            | (buf[off + 1] & 0xFF) << 8
            | (buf[off + 2] & 0xFF) << 16
            | (buf[off + 3] & 0xFF) << 24
        )

    @staticmethod
    def __packInt(value: int, dst: typing.List[int], off: int, len: int) -> None:
        for i in range(len):
            dst[off + i] = (value >> i * 8) & 0xFF

    @staticmethod
    def __checkBufferArgs(buffer: typing.List[int], offset: int, length: int) -> None:
        if buffer is None:
            raise ValueError("Buffer must not be None")
        if offset < 0:
            raise IndexError("Offset must be non-negative")
        if length < 0:
            raise IndexError("Length must be non-negative")
        buffer_length = len(buffer)
        if offset > buffer_length - length:
            raise IndexError(
                f"Offset {offset} and length {length} out of bounds with buffer length {buffer_length}"
            )

    def __init__(self, key: typing.List[int], flags: int) -> None:
        self.__engineState = EngineState(key, flags)


ChunkState.initialize_fields()
