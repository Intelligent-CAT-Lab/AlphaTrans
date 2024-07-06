from __future__ import annotations
import re
import io


class QuoteMode:

    NONE: QuoteMode = None

    NON_NUMERIC: QuoteMode = None

    MINIMAL: QuoteMode = None

    ALL_NON_NULL: QuoteMode = None

    ALL: QuoteMode = None
