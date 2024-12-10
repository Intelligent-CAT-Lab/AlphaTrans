from __future__ import annotations
import re
import io


class DuplicateHeaderMode:

    DISALLOW = 1

    ALLOW_EMPTY = 2

    ALLOW_ALL = 3
