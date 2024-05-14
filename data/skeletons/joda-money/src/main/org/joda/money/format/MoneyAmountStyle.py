# Imports Begin
from src.main.org.joda.money.format.MoneyFormatter import *
from src.main.org.joda.money.format.GroupingStyle import *
import typing

# Imports End


class MoneyAmountStyle(Serializable):

    # Class Fields Begin
    LOCALIZED_GROUPING: MoneyAmountStyle = None
    LOCALIZED_NO_GROUPING: MoneyAmountStyle = None
    __LOCALIZED_CACHE: typing.Dict[typing.Any, MoneyAmountStyle] = None
    __serialVersionUID: int = None
    __zeroCharacter: int = None
    __positiveCharacter: int = None
    __negativeCharacter: int = None
    __decimalPointCharacter: int = None
    __groupingStyle: GroupingStyle = None
    __groupingCharacter: int = None
    __groupingSize: int = None
    __extendedGroupingSize: int = None
    __forceDecimalPoint: bool = None
    __absValue: bool = None
    ASCII_DECIMAL_POINT_GROUP3_COMMA: MoneyAmountStyle = None
    ASCII_DECIMAL_POINT_GROUP3_SPACE: MoneyAmountStyle = None
    ASCII_DECIMAL_POINT_NO_GROUPING: MoneyAmountStyle = None
    ASCII_DECIMAL_COMMA_GROUP3_DOT: MoneyAmountStyle = None
    ASCII_DECIMAL_COMMA_GROUP3_SPACE: MoneyAmountStyle = None
    ASCII_DECIMAL_COMMA_NO_GROUPING: MoneyAmountStyle = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def hashCode(self) -> int:
        pass

    def equals(self, other: typing.Any) -> bool:
        pass

    def withAbsValue(self, absValue: bool) -> "MoneyAmountStyle":
        pass

    def isAbsValue(self) -> bool:
        pass

    def withForcedDecimalPoint(self, forceDecimalPoint: bool) -> "MoneyAmountStyle":
        pass

    def isForcedDecimalPoint(self) -> bool:
        pass

    def withGroupingStyle(self, groupingStyle: GroupingStyle) -> "MoneyAmountStyle":
        pass

    def getGroupingStyle(self) -> GroupingStyle:
        pass

    def withExtendedGroupingSize(self, extendedGroupingSize: int) -> "MoneyAmountStyle":
        pass

    def getExtendedGroupingSize(self) -> int:
        pass

    def withGroupingSize(self, groupingSize: int) -> "MoneyAmountStyle":
        pass

    def getGroupingSize(self) -> int:
        pass

    def withGroupingCharacter(self, groupingCharacter: str) -> "MoneyAmountStyle":
        pass

    def getGroupingCharacter(self) -> str:
        pass

    def withDecimalPointCharacter(
        self, decimalPointCharacter: str
    ) -> "MoneyAmountStyle":
        pass

    def getDecimalPointCharacter(self) -> str:
        pass

    def withNegativeSignCharacter(self, negativeCharacter: str) -> "MoneyAmountStyle":
        pass

    def getNegativeSignCharacter(self) -> str:
        pass

    def withPositiveSignCharacter(self, positiveCharacter: str) -> "MoneyAmountStyle":
        pass

    def getPositiveSignCharacter(self) -> str:
        pass

    def withZeroCharacter(self, zeroCharacter: str) -> "MoneyAmountStyle":
        pass

    def getZeroCharacter(self) -> str:
        pass

    def localize(self, locale: typing.Any) -> "MoneyAmountStyle":
        pass

    @staticmethod
    def of(locale: typing.Any) -> "MoneyAmountStyle":
        pass

    @staticmethod
    def __getLocalizedStyle(locale: typing.Any) -> "MoneyAmountStyle":
        pass

    def __init__(
        self,
        zeroCharacter: int,
        positiveCharacter: int,
        negativeCharacter: int,
        decimalPointCharacter: int,
        groupingStyle: GroupingStyle,
        groupingCharacter: int,
        groupingSize: int,
        extendedGroupingSize: int,
        forceDecimalPoint: bool,
        absValue: bool,
    ) -> None:
        pass

    # Class Methods End
