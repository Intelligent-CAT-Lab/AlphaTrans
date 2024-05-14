# Imports Begin
from src.main.org.apache.commons.csv.DuplicateHeaderMode import *
import typing

# Imports End


class CSVDuplicateHeaderTest:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def duplicateHeaderData() -> typing.Iterable[typing.List]:
        pass

    @staticmethod
    def duplicateHeaderAllowsMissingColumnsNamesData() -> typing.Iterable[typing.List]:
        pass

    # Class Methods End


class Predicate:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def test(self, arg: typing.List) -> bool:
        pass

    # Class Methods End


class Function:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def apply(self, arg: typing.List) -> typing.Iterable[typing.List]:
        pass

    # Class Methods End


class Function:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def apply(self, arguments: typing.List[typing.Any]) -> typing.List:
        pass

    # Class Methods End
