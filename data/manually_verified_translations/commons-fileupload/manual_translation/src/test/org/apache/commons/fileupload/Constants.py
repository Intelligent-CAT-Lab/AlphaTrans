from __future__ import annotations
import re
import unittest
import pytest
import io


class Constants:

    CONTENT_TYPE: str = "multipart/form-data; boundary=---1234"

    def __init__(self) -> None:
        pass
