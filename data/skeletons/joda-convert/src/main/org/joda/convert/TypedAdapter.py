# Imports Begin
from src.main.org.joda.convert.TypedStringConverter import *
from src.main.org.joda.convert.StringConverter import *
import typing

# Imports End


class TypedAdapter(TypedStringConverter, TypedAdapter):

    # Class Fields Begin
    __conv: StringConverter[typing.Any] = None
    __effectiveType: typing.Type[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def getEffectiveType(self) -> typing.Type[typing.Any]:
        pass

    def convertFromString(self, cls: typing.Type[typing.Any], str: str) -> typing.Any:
        pass

    def convertToString(self, object: typing.Any) -> str:
        pass

    @staticmethod
    def adapt(
        cls: typing.Type[typing.Any], converter: StringConverter[typing.Any]
    ) -> TypedStringConverter[typing.Any]:
        pass

    def __init__(
        self, conv: StringConverter[typing.Any], effectiveType: typing.Type[typing.Any]
    ) -> None:
        pass

    # Class Methods End
