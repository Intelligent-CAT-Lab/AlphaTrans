# Imports Begin
from src.main.org.apache.commons.pool2.PooledObjectFactory import *
import datetime
import typing

# Imports End


class PoolImplUtils:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def getFactoryType(
        factoryClass: typing.Type[PooledObjectFactory[typing.Any]],
    ) -> typing.Type[typing.Any]:
        pass

    @staticmethod
    def toDuration(amount: int, timeUnit: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    def nonNull(
        value: datetime.timedelta, defaultValue: datetime.timedelta
    ) -> datetime.timedelta:
        pass

    @staticmethod
    def toChronoUnit(timeUnit: datetime.timedelta) -> datetime.timedelta:
        pass

    @staticmethod
    def min(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def max(a: datetime.datetime, b: datetime.datetime) -> datetime.datetime:
        pass

    @staticmethod
    def isPositive(delay: datetime.timedelta) -> bool:
        pass

    @staticmethod
    def __getTypeParameter(
        clazz: typing.Type[typing.Any], argType: typing.Type
    ) -> typing.Any:
        pass

    @staticmethod
    def __getParameterizedType(
        type: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Generic:
        pass

    @staticmethod
    def __getGenericType(
        type: typing.Type[typing.Any], clazz: typing.Type[typing.Any]
    ) -> typing.Any:
        pass

    # Class Methods End
