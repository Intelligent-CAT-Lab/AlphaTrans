from __future__ import annotations
import time
import re
import io
import typing
from typing import *


class Flags:

    __serialVersionUID: int = 8481587558770237995

    def toString(self) -> str:

        bin_string = bin(self.__flags)[2:]  # Convert flags to binary string, removing '0b' prefix
        padded_bin = bin_string.zfill(64)  # Pad with leading zeros to make it 64 characters
        return padded_bin

    def hashCode(self) -> int:
        return int(self.__flags)

    def equals(self, obj: typing.Any) -> bool:

        if not isinstance(obj, Flags):
            return False

        if obj is self:
            return True

        f = obj

        return self.__flags == f.__flags

    def clone(self) -> typing.Any:
        try:
            return super().clone()
        except Exception as e:
            raise RuntimeError("Couldn't clone Flags object.")

    def turnOnAll(self) -> None:
        self.__flags = 0xFFFFFFFFFFFFFFFF

    def clear(self) -> None:
        self.__flags = 0

    def turnOffAll(self) -> None:
        self.__flags = 0

    def turnOff(self, flag: int) -> None:
        self.__flags &= ~flag

    def turnOn(self, flag: int) -> None:
        self.__flags |= flag

    def isOff(self, flag: int) -> bool:
        return (self.__flags & flag) == 0

    def isOn(self, flag: int) -> bool:
        return (self.__flags & flag) == flag

    def getFlags(self) -> int:
        return self.__flags

    def __init__(self, constructorId: int, flags: int) -> None:
        if constructorId == 1:
            self.__flags = flags
        else:
            self.__flags = 0
