# Imports Begin
import unittest

# Imports End


class CustomClassLoader(unittest.TestCase, URLClassLoader):

    # Class Fields Begin
    __n: int = None
    # Class Fields End

    # Class Methods Begin
    def findResource(self, name: str) -> typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ]:

        if not name.endswith(str(self.__n)):
            return None
        return super().findResource(name)

    def __init__(self, n: int) -> None:

        super().__init__(BASE_URL)
        self.__n = n

    # Class Methods End


class TestGenericObjectPoolClassLoaders(unittest.TestCase):

    # Class Fields Begin
    __BASE_URL: typing.Union[
        urllib.parse.ParseResult,
        urllib.parse.SplitResult,
        urllib.parse.DefragResult,
        str,
    ] = ""  # LLM could not translate field
    # Class Fields End

    # Class Methods Begin
    # Class Methods End
