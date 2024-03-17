# Imports Begin
import unittest

# Imports End


class PrivateException(unittest.TestCase, RuntimeException):

    # Class Fields Begin
    __serialVersionUID: int = 1
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:

        super().__init__(message)

    # Class Methods End
