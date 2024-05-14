# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.TypeUtils import *
import typing

# Imports End


class TypeTokenStringConverter(TypedStringConverter):

    # Class Fields Begin
    TYPE_TOKEN_CLASS: typing.Type[typing.Any] = None
    TYPE_TOKEN_METHOD_OF: typing.Union[inspect.Signature, typing.Callable] = None
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString(self, object: typing.Any) -> str:
        pass

    def __init__(self) -> None:
        pass

    # Class Methods End
