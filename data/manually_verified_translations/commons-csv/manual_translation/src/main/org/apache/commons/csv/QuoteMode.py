from __future__ import annotations
import re
import io


class QuoteMode:
    
    ALL = 1

    ALL_NON_NULL = 2

    MINIMAL = 3

    NON_NUMERIC = 4

    NONE = 5
