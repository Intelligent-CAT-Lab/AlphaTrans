from __future__ import annotations
import re
import io


class CodecPolicy:

    LENIENT: CodecPolicy = None
    STRICT: CodecPolicy = None

    @staticmethod
    def initialize_fields() -> None:
        CodecPolicy.LENIENT: CodecPolicy = None
        CodecPolicy.STRICT: CodecPolicy = None


CodecPolicy.initialize_fields()
