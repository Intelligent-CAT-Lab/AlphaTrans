# Imports Begin
from src.main.org.apache.commons.cli.Util import *
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.AmbiguousOptionException import *
import typing

# Imports End


class PosixParser(Parser):

    # Class Fields Begin
    __tokens: typing.List[str] = None
    __eatTheRest: bool = None
    __currentOption: Option = None
    __options: Options = None
    # Class Fields End

    # Class Methods Begin
    def _flatten(
        self, options: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> typing.List[str]:
        pass

    def _burstToken(self, token: str, stopAtNonOption: bool) -> None:
        pass

    def __processOptionToken(self, token: str, stopAtNonOption: bool) -> None:
        pass

    def __processNonOptionToken(self, value: str, stopAtNonOption: bool) -> None:
        pass

    def __init(self) -> None:
        pass

    def __gobble(self, iter: typing.Iterator[str]) -> None:
        pass

    # Class Methods End
