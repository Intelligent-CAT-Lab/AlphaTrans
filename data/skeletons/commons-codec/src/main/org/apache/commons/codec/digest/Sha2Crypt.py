from __future__ import annotations

# Imports Begin
import io

# Imports End


class Sha2Crypt:

    # Class Fields Begin
    __ROUNDS_DEFAULT: int = None
    __ROUNDS_MAX: int = None
    __ROUNDS_MIN: int = None
    __ROUNDS_PREFIX: str = None
    __SHA256_BLOCKSIZE: int = None
    SHA256_PREFIX: str = None
    __SHA512_BLOCKSIZE: int = None
    SHA512_PREFIX: str = None
    __SALT_PATTERN: re.Pattern = None
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
