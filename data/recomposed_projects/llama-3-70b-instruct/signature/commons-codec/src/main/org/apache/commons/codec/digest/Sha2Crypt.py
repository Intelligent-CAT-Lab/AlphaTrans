from __future__ import annotations
import re
import io


class Sha2Crypt:

    SHA512_PREFIX: str = "$6$"
    SHA256_PREFIX: str = "$5$"
    __SALT_PATTERN: re.Pattern = re.compile(
        r"^\$([56])\$(rounds=(\d+)\$)?([\.\/a-zA-Z0-9]{1,16}).*"
    )
    __SHA512_BLOCKSIZE: int = 64
    __SHA256_BLOCKSIZE: int = 32
    __ROUNDS_PREFIX: str = "rounds="
    __ROUNDS_MIN: int = 1000
    __ROUNDS_MAX: int = 999999999
    __ROUNDS_DEFAULT: int = 5000
