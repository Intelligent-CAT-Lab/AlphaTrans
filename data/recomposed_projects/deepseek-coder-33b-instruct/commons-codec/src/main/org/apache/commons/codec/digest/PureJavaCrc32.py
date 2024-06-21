from __future__ import annotations
import re
from dataclasses import field
import io
import typing
from typing import *


class PureJavaCrc32:

    __T: typing.List[int] = None  # LLM could not translate this field
    __crc: int = None

    def reset(self) -> None:

        self.___reset()

    def getValue(self) -> int:

        return (~self.__crc) & 0xFFFFFFFF

    def update1(self, b: int) -> None:

        self.__crc = (self.__crc >> 8) ^ self.__T[((self.__crc ^ b) << 24) >> 24]

    def update0(self, b: typing.List[int], offset: int, len: int) -> None:

        localCrc = self.__crc

        remainder = len & 0x7
        i = offset
        for end in range(offset + len - remainder, i, 8):
            x = localCrc ^ (
                (((b[i] << 24) >> 24) + ((b[i + 1] << 24) >> 16))
                + (((b[i + 2] << 24) >> 8) + (b[i + 3] << 24))
            )

            localCrc = (
                (
                    self.__T[((x << 24) >> 24) + 0x700]
                    ^ self.__T[((x << 16) >> 24) + 0x600]
                )
                ^ (self.__T[((x << 8) >> 24) + 0x500] ^ self.__T[(x >> 24) + 0x400])
                ^ (
                    (
                        self.__T[((b[i + 4] << 24) >> 24) + 0x300]
                        ^ self.__T[((b[i + 5] << 24) >> 24) + 0x200]
                    )
                    ^ (
                        self.__T[((b[i + 6] << 24) >> 24) + 0x100]
                        ^ self.__T[((b[i + 7] << 24) >> 24)]
                    )
                )
            )
            i += 8

        match remainder:
            case 7:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case 6:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case 5:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case 4:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case 3:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case 2:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case 1:
                localCrc = (localCrc >> 8) ^ self.__T[((localCrc ^ b[i]) << 24) >> 24]
                i += 1
            case _:
                pass

        self.__crc = localCrc

    def __init__(self) -> None:

        self._reset()

    def _reset(self) -> None:
        pass

    def ___reset(self) -> None:

        self.__crc = 0xFFFFFFFF
