from __future__ import annotations
import re
import unittest
import pytest
import io


class Base32TestData:

    BASE32_FIXTURE: str = "JBSWY3DPEBLW64TMMQ======\r\n"
    STRING_FIXTURE: str = "Hello World"
