from __future__ import annotations
import re
from dataclasses import field
import io


class Base64TestData:

    ENCODED_76_CHARS_PER_LINE: str = None  # LLM could not translate this field
    ENCODED_64_CHARS_PER_LINE: str = None  # LLM could not translate this field

    CODEC_98_NPE_DECODED: str = (
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123"
    )

    CODEC_98_NPE: str = (
        "YWJjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXpBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWjAxMjM"
    )

    CODEC_101_INPUT_LENGTH_IS_MULTIPLE_OF_3: str = "124"
