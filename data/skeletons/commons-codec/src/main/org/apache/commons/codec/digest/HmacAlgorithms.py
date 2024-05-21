from __future__ import annotations

# Imports Begin
import io

# Imports End


class HmacAlgorithms:

    # Class Fields Begin
    HMAC_MD5: HmacAlgorithms = None
    HMAC_SHA_1: HmacAlgorithms = None
    HMAC_SHA_224: HmacAlgorithms = None
    HMAC_SHA_256: HmacAlgorithms = None
    HMAC_SHA_384: HmacAlgorithms = None
    HMAC_SHA_512: HmacAlgorithms = None
    __name: str = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getName(self) -> str:
        pass

    def __init__(self, algorithm: str) -> None:
        pass

    # Class Methods End
