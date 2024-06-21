from __future__ import annotations
import re
import io
import typing
from typing import *


class MessageDigestAlgorithms:

    SHA3_512: str = "SHA3-512"

    SHA3_384: str = "SHA3-384"

    SHA3_256: str = "SHA3-256"

    SHA3_224: str = "SHA3-224"

    SHA_512_256: str = "SHA-512/256"

    SHA_512_224: str = "SHA-512/224"

    SHA_512: str = "SHA-512"

    SHA_384: str = "SHA-384"

    SHA_256: str = "SHA-256"

    SHA_224: str = "SHA-224"

    SHA_1: str = "SHA-1"

    MD5: str = "MD5"

    MD2: str = "MD2"

    @staticmethod
    def values() -> typing.List[str]:

        return [
            MessageDigestAlgorithms.MD2,
            MessageDigestAlgorithms.MD5,
            MessageDigestAlgorithms.SHA_1,
            MessageDigestAlgorithms.SHA_224,
            MessageDigestAlgorithms.SHA_256,
            MessageDigestAlgorithms.SHA_384,
            MessageDigestAlgorithms.SHA_512,
            MessageDigestAlgorithms.SHA_512_224,
            MessageDigestAlgorithms.SHA_512_256,
            MessageDigestAlgorithms.SHA3_224,
            MessageDigestAlgorithms.SHA3_256,
            MessageDigestAlgorithms.SHA3_384,
            MessageDigestAlgorithms.SHA3_512,
        ]

    def __init__(self) -> None:

        pass
