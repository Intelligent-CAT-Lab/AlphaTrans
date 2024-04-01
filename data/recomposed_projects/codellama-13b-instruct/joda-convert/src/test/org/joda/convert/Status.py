# Imports Begin
from src.main.org.joda.convert.StringConvert import *
import unittest

# Imports End


class Status(unittest.TestCase):

    # Class Fields Begin
    VALID: Status = None
    INVALID: Status = None
    STRING_CONVERTIBLE: bool = StringConvert.INSTANCE.isConvertible(String)
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
