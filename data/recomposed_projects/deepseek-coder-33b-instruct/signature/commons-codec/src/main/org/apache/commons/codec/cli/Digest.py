from __future__ import annotations
import re
import io
import typing
from typing import *
from src.main.org.apache.commons.codec.binary.Hex import *


class Digest:

    __inputs: typing.List[str] = None

    __args: typing.List[str] = None

    __algorithm: str = ""

    def toString(self) -> str:
        return f"{super().__str__()} {str(self.__args)}"

    def __println1(self, prefix: str, digest: typing.List[int], fileName: str) -> None:

        encoded_digest = Hex.encodeHexString0(digest)
        file_name_str = "  " + fileName if fileName is not None else ""
        print(prefix + encoded_digest + file_name_str)

    def __println0(self, prefix: str, digest: typing.List[int]) -> None:
        self.__println1(prefix, digest, None)

    def __init__(self, args: typing.List[str]) -> None:

        if args is None:
            raise ValueError("args cannot be None")

        args_length = len(args)
        if args_length == 0:
            raise ValueError(
                "Usage: python3.10 %s [algorithm] [FILE|DIRECTORY|string] ..."
                % self.__class__.__name__
            )

        self.__args = args
        self.__algorithm = args[0]
        if args_length <= 1:
            self.__inputs = None
        else:
            self.__inputs = args[1:]
