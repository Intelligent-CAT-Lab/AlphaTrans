from __future__ import annotations
import re
import io


class DuplicateHeaderMode:

    DISALLOW: DuplicateHeaderMode = None

    ALLOW_EMPTY: DuplicateHeaderMode = None

    ALLOW_ALL: DuplicateHeaderMode = None
