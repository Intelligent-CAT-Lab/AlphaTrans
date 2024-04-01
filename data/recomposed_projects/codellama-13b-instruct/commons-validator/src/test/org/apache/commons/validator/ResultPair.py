# Imports Begin
import unittest

# Imports End


class ResultPair(unittest.TestCase):

    # Class Fields Begin
    item: str = None
    valid: bool = None
    # Class Fields End

    # Class Methods Begin
    def __init__(self, item: str, valid: bool) -> None:

        self.item = item
        self.valid = valid

    # Class Methods End
