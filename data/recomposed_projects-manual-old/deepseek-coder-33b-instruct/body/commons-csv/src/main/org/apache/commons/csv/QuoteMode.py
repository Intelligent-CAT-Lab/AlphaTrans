from __future__ import annotations
import re
import io


class QuoteMode:

    NONE: QuoteMode = 'NONE'

    NON_NUMERIC: QuoteMode = 'NON_NUMERIC'

    MINIMAL: QuoteMode = 'MINIMAL'

    ALL_NON_NULL: QuoteMode = 'ALL_NON_NULL'

    ALL: QuoteMode = 'ALL'
