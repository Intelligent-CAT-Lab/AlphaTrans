from __future__ import annotations
import re
import io


class DuplicateHeaderMode:

    DISALLOW: DuplicateHeaderMode = None
    ALLOW_EMPTY: DuplicateHeaderMode = None
    ALLOW_ALL: DuplicateHeaderMode = None

    @staticmethod
    def initialize_fields() -> None:
        DuplicateHeaderMode.DISALLOW: DuplicateHeaderMode = None
        DuplicateHeaderMode.ALLOW_EMPTY: DuplicateHeaderMode = None
        DuplicateHeaderMode.ALLOW_ALL: DuplicateHeaderMode = None


DuplicateHeaderMode.initialize_fields()
