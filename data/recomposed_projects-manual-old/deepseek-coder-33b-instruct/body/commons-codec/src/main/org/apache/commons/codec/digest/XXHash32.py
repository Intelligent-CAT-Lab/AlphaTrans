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

    __buffer: typing.List[int] = [0] * 16
    __state: typing.List[int] = [0] * 4
    __oneByte: typing.List[int] = [0] * 1
    __PRIME5: int = 374761393
    __PRIME4: int = 668265263
    __PRIME3: int = 3266489917
    __PRIME2: int = 2246822519
    __PRIME1: int = 2654435761
    __ROTATE_BITS: int = 13
    __BUF_SIZE: int = 16

    def getValue(self) -> int:

        if self.__stateUpdated:
            hash = (self.__state[0] << 1) | (self.__state[0] >> (32 - 1))
            hash += (self.__state[1] << 7) | (self.__state[1] >> (32 - 7))
            hash += (self.__state[2] << 12) | (self.__state[2] >> (32 - 12))
            hash += (self.__state[3] << 18) | (self.__state[3] >> (32 - 18))
        else:
            hash = self.__state[2] + self.__PRIME5

        hash += self.__totalLen

        idx = 0
        limit = self.__pos - 4
        for idx in range(0, limit + 1, 4):
            hash = (
                hash + self.__getInt(self.__buffer, idx) * self.__PRIME3
            ) & 0xFFFFFFFF
            hash = (
                (hash << self.__ROTATE_BITS) | (hash >> (32 - self.__ROTATE_BITS))
            ) * self.__PRIME4

        while idx < self.__pos:
            hash = (hash + (self.__buffer[idx] & 0xFF) * self.__PRIME5) & 0xFFFFFFFF
            hash = (
                (hash << self.__ROTATE_BITS) | (hash >> (32 - self.__ROTATE_BITS))
            ) * self.__PRIME1
            idx += 1

        hash ^= hash >> 15
        hash = (hash * self.__PRIME2) & 0xFFFFFFFF
        hash ^= hash >> 13
        hash = (hash * self.__PRIME3) & 0xFFFFFFFF
        hash ^= hash >> 16
        return hash & 0xFFFFFFFF

    def reset(self) -> None:

        self.__initializeState()
        self.__totalLen = 0
        self.__pos = 0
        self.__stateUpdated = False

    def update1(self, b: typing.List[int], off: int, len: int) -> None:

        if len <= 0:
            return
        self.__totalLen += len

        end = off + len

        if self.__pos + len - self.__BUF_SIZE < 0:
            self.__buffer[self.__pos : self.__pos + len] = b[off : off + len]
            self.__pos += len
            return

        if self.__pos > 0:
            size = self.__BUF_SIZE - self.__pos
            self.__buffer[self.__pos : self.__pos + size] = b[off : off + size]
            self.__process(self.__buffer, 0)
            off += size

        limit = end - self.__BUF_SIZE
        while off <= limit:
            self.__process(b, off)
            off += self.__BUF_SIZE

        if off < end:
            self.__pos = end - off
            self.__buffer[0 : self.__pos] = b[off : off + self.__pos]
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
        self.__buffer = [0] * self.__BUF_SIZE
        self.__state = [0] * 4
        self.__oneByte = [0]
        self.__initializeState()

    def __process(self, b: typing.List[int], offset: int) -> None:

        s0 = self.__state[0]
        s1 = self.__state[1]
        s2 = self.__state[2]
        s3 = self.__state[3]

        s0 = (
            self.__rotateLeft(
                s0 + self.__getInt(b, offset) * self.__PRIME2, self.__ROTATE_BITS
            )
            * self.__PRIME1
        )
        s1 = (
            self.__rotateLeft(
                s1 + self.__getInt(b, offset + 4) * self.__PRIME2, self.__ROTATE_BITS
            )
            * self.__PRIME1
        )
        s2 = (
            self.__rotateLeft(
                s2 + self.__getInt(b, offset + 8) * self.__PRIME2, self.__ROTATE_BITS
            )
            * self.__PRIME1
        )
        s3 = (
            self.__rotateLeft(
                s3 + self.__getInt(b, offset + 12) * self.__PRIME2, self.__ROTATE_BITS
            )
            * self.__PRIME1
        )

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
        return (
            (buffer[idx] & 0xFF)
            | ((buffer[idx + 1] & 0xFF) << 8)
            | ((buffer[idx + 2] & 0xFF) << 16)
            | ((buffer[idx + 3] & 0xFF) << 24)
        )
