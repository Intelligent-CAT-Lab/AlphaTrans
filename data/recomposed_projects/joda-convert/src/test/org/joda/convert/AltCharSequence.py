# Imports Begin
import unittest

# Imports End


class AltCharSequence(unittest.TestCase, CharSequence):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def subSequence(self, start: int, end: int) -> str:

        return self[start:end]

    def charAt(self, index: int) -> str:

        return "A"

    def length(self) -> int:

        return 1

    # Class Methods End
