from __future__ import annotations
import re
import unittest
import pytest
import io
from src.main.org.joda.convert.StringConvert import *


class Status:

    STRING_CONVERTIBLE: bool = StringConvert.INSTANCE.isConvertible(String)
    INVALID: Status = None

    VALID: Status = None
