from __future__ import annotations
import re
import io


class Md5Crypt:

    MD5_PREFIX: str = "$1$"
    APR1_PREFIX: str = "$apr1$"
    __ROUNDS: int = 1000
    __BLOCKSIZE: int = 16
