from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.codec.StringEncoder import *
from src.main.org.apache.commons.codec.EncoderException import *
import os
import typing
from typing import *
import io
from abc import ABC

# Imports End


class CologneBuffer(ABC):

    # Class Fields Begin
    _data: typing.List[str] = None
    _length: int = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def isEmpty(self) -> bool:
        pass

    def length(self) -> int:
        pass

    def __init__(
        self, constructorId: int, data: typing.List[str], buffSize: int
    ) -> None:
        pass

    def _copyData(self, start: int, length: int) -> typing.List[str]:
        pass

    # Class Methods End


class CologneInputBuffer(CologneBuffer):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _copyData(self, start: int, length: int) -> typing.List[str]:
        pass

    def removeNext(self) -> str:
        pass

    def _getNextPos(self) -> int:
        pass

    def getNextChar(self) -> str:
        pass

    def __init__(self, data: typing.List[str]) -> None:
        pass

    # Class Methods End


class CologneOutputBuffer(CologneBuffer):

    # Class Fields Begin
    __lastCode: str = None
    # Class Fields End

    # Class Methods Begin
    def _copyData(self, start: int, length: int) -> typing.List[str]:
        pass

    def put(self, code: str) -> None:
        pass

    def __init__(self, buffSize: int) -> None:
        pass

    # Class Methods End


class ColognePhonetic(StringEncoder):

    # Class Fields Begin
    __AEIJOUY: typing.List[str] = None
    __CSZ: typing.List[str] = None
    __FPVW: typing.List[str] = None
    __GKQ: typing.List[str] = None
    __CKQ: typing.List[str] = None
    __AHKLOQRUX: typing.List[str] = None
    __SZ: typing.List[str] = None
    __AHKOQUX: typing.List[str] = None
    __DTX: typing.List[str] = None
    __CHAR_IGNORE: str = None
    # Class Fields End

    # Class Methods Begin
    def encode(self, text: str) -> str:
        pass

    def encode(self, object_: typing.Any) -> typing.Any:
        pass

    def isEncodeEqual(self, text1: str, text2: str) -> bool:
        pass

    def encode1(self, text: str) -> str:
        pass

    def encode0(self, object_: typing.Any) -> typing.Any:
        pass

    def colognePhonetic(self, text: str) -> str:
        pass

    def __preprocess(self, text: str) -> typing.List[str]:
        pass

    @staticmethod
    def __arrayContains(arr: typing.List[str], key: str) -> bool:
        pass

    # Class Methods End
