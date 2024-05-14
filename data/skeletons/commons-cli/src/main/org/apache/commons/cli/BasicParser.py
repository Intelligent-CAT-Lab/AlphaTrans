# Imports Begin
from src.main.org.apache.commons.cli.Parser import *
from src.main.org.apache.commons.cli.Options import *
import typing

# Imports End


class BasicParser(Parser):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def _flatten(
        self, options: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> typing.List[str]:
        pass

    # Class Methods End
