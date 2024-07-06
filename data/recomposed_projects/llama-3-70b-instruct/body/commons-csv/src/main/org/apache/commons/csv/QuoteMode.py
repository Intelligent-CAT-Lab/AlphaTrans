from __future__ import annotations
import re
import io


class QuoteMode:

    NONE: QuoteMode = None
    NON_NUMERIC: QuoteMode = None
    MINIMAL: QuoteMode = None
    ALL_NON_NULL: QuoteMode = None
    ALL: QuoteMode = None

    @staticmethod
    def initialize_fields() -> None:
        QuoteMode.NONE: QuoteMode = None
        QuoteMode.NON_NUMERIC: QuoteMode = None
        QuoteMode.MINIMAL: QuoteMode = None
        QuoteMode.ALL_NON_NULL: QuoteMode = None
        QuoteMode.ALL: QuoteMode = None


QuoteMode.initialize_fields()
