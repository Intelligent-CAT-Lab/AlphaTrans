from __future__ import annotations
import re
import io


class DuplicateHeaderMode:

    DISALLOW: DuplicateHeaderMode = 'DISALLOW'

    ALLOW_EMPTY: DuplicateHeaderMode = 'ALLOW_EMPTY'

    ALLOW_ALL: DuplicateHeaderMode = 'ALLOW_ALL'
