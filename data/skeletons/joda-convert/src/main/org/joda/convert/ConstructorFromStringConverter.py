# Imports Begin
from src.main.org.joda.convert.TypedFromStringConverter import *
import typing

# Imports End


class ConstructorFromStringConverter(
    TypedFromStringConverter, ConstructorFromStringConverter
):

    # Class Fields Begin
    __fromString: typing.Callable[..., typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def __init__(
        self, cls: typing.Type[typing.Any], fromString: typing.Callable[..., typing.Any]
    ) -> None:
        pass

    # Class Methods End
