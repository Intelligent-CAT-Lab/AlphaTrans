from __future__ import annotations
import re
import io
import typing
from typing import *
import os


class XXHash32:

    __stateUpdated: bool = False

    __pos: int = 0

    __totalLen: int = 0

    __seed: int = 0

    __buffer: typing.List[int] = [0] * BUF_SIZE
    __state: typing.List[int] = [0, 0, 0, 0]
    __oneByte: typing.List[int] = [0]
    __PRIME5: int = 374761393
    __PRIME4: int = 668265263
    __PRIME3: int = 3266489917
    __PRIME2: int = 2246822519
    __PRIME1: int = 2654435761
    __ROTATE_BITS: int = 13
    __BUF_SIZE: int = 16

    def getValue(self) -> int:

        pass  # LLM could not translate this method

    def reset(self) -> None:
        self.__initializeState()
        self.__totalLen = 0
        self.__pos = 0
        self.__stateUpdated = False

    def update1(self, b: typing.List[int], off: int, len: int) -> None:
        if len <= 0:
            return
        self.__totalLen += len

        end: int = off + len

        if self.__pos + len - self.__BUF_SIZE < 0:
            b[self.__pos : self.__pos + len] = buffer
            self.__pos += len
            return

        if self.__pos > 0:
            size: int = self.__BUF_SIZE - self.__pos
            buffer[self.__pos : self.__pos + size] = b
            self.__process(buffer, 0)
            off += size

        limit: int = end - self.__BUF_SIZE
        while off <= limit:
            self.__process(b, off)
            off += self.__BUF_SIZE

        if off < end:
            self.__pos = end - off
            buffer[0 : self.__pos] = b
        else:
            self.__pos = 0

    def update0(self, b: int) -> None:
        self.__oneByte[0] = b & 0xFF
        self.update1(self.__oneByte, 0, 1)

    @staticmethod
    def XXHash321() -> XXHash32:
        return XXHash32(0)

    def __init__(self, seed: int) -> None:
        self.__seed = seed
        self.__initializeState()

    def __process(self, b: typing.List[int], offset: int) -> None:
        s0: int = self.__state[0]
        s1: int = self.__state[1]
        s2: int = self.__state[2]
        s3: int = self.__state[3]

        s0 = (
            s0 + self.__getInt(b, offset) * self.__PRIME2
        ) << self.__ROTATE_BITS * self.__PRIME1
        s1 = (
            s1 + self.__getInt(b, offset + 4) * self.__PRIME2
        ) << self.__ROTATE_BITS * self.__PRIME1
        s2 = (
            s2 + self.__getInt(b, offset + 8) * self.__PRIME2
        ) << self.__ROTATE_BITS * self.__PRIME1
        s3 = (
            s3 + self.__getInt(b, offset + 12) * self.__PRIME2
        ) << self.__ROTATE_BITS * self.__PRIME1

        self.__state[0] = s0
        self.__state[1] = s1
        self.__state[2] = s2
        self.__state[3] = s3

        self.__stateUpdated = True

    def __initializeState(self) -> None:
        self.__state[0] = self.__seed + self.__PRIME1 + self.__PRIME2
        self.__state[1] = self.__seed + self.__PRIME2
        self.__state[2] = self.__seed
        self.__state[3] = self.__seed - self.__PRIME1

    @staticmethod
    def __getInt(buffer: typing.List[int], idx: int) -> int:

        pass  # LLM could not translate this method
