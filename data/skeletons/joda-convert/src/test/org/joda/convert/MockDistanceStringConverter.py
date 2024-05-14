# Imports Begin
from src.main.org.joda.convert.StringConverter import *
from src.main.org.joda.convert.DistanceMethodMethod import *
import typing

# Imports End


class MockDistanceStringConverter(Enum, StringConverter):

    # Class Fields Begin
    INSTANCE: MockDistanceStringConverter = None
    # Class Fields End

    # Class Methods Begin
    def convertFromString(
        self, cls: typing.Type[DistanceMethodMethod], str: str
    ) -> DistanceMethodMethod:
        pass

    def convertToString(self, object: DistanceMethodMethod) -> str:
        pass

    # Class Methods End
