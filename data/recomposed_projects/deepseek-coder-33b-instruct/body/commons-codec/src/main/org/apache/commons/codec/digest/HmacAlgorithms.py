from __future__ import annotations
import re
import io


class HmacAlgorithms:

    HMAC_SHA_512: HmacAlgorithms = None

    HMAC_SHA_384: HmacAlgorithms = None

    HMAC_SHA_256: HmacAlgorithms = None

    HMAC_SHA_224: HmacAlgorithms = None

    HMAC_SHA_1: HmacAlgorithms = None

    HMAC_MD5: HmacAlgorithms = None

    __name: str = ""

    def toString(self) -> str:
        return self.__name

    def getName(self) -> str:
        return self.__name

    def __init__(self, algorithm: str) -> None:
        self.__name = algorithm
