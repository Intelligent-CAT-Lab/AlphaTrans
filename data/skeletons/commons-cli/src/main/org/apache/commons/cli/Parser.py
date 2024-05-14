# Imports Begin
from src.main.org.apache.commons.cli.Util import *
from src.main.org.apache.commons.cli.UnrecognizedOptionException import *
from src.main.org.apache.commons.cli.ParseException import *
from src.main.org.apache.commons.cli.Options import *
from src.main.org.apache.commons.cli.OptionGroup import *
from src.main.org.apache.commons.cli.Option import *
from src.main.org.apache.commons.cli.MissingOptionException import *
from src.main.org.apache.commons.cli.MissingArgumentException import *
from src.main.org.apache.commons.cli.CommandLineParser import *
from src.main.org.apache.commons.cli.CommandLine import *
import typing
import configparser
from abc import ABC

# Imports End


class Parser(CommandLineParser, ABC):

    # Class Fields Begin
    _cmd: CommandLine = None
    __options: Options = None
    __requiredOptions: typing.List[typing.Any] = None
    # Class Fields End

    # Class Methods Begin
    def _setOptions(self, options: Options) -> None:
        pass

    def _processProperties(
        self,
        properties: typing.Union[
            configparser.ConfigParser, configparser.ConfigParserExtended, typing.Dict
        ],
    ) -> None:
        pass

    def _processOption(self, arg: str, iter: typing.Iterator[str]) -> None:
        pass

    def processArgs(self, opt: Option, iter: typing.Iterator[str]) -> None:
        pass

    def parse3(
        self,
        options: Options,
        arguments: typing.List[str],
        properties: typing.Union[
            configparser.ConfigParser, configparser.ConfigParserExtended, typing.Dict
        ],
        stopAtNonOption: bool,
    ) -> CommandLine:
        pass

    def parse2(
        self,
        options: Options,
        arguments: typing.List[str],
        properties: typing.Union[
            configparser.ConfigParser, configparser.ConfigParserExtended, typing.Dict
        ],
    ) -> CommandLine:
        pass

    def parse1(
        self, options: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> CommandLine:
        pass

    def parse0(self, options: Options, arguments: typing.List[str]) -> CommandLine:
        pass

    def _getRequiredOptions(self) -> typing.List[typing.Any]:
        pass

    def _getOptions(self) -> Options:
        pass

    def _checkRequiredOptions(self) -> None:
        pass

    def __updateRequiredOptions(self, opt: Option) -> None:
        pass

    def _flatten(
        self, opts: Options, arguments: typing.List[str], stopAtNonOption: bool
    ) -> typing.List[str]:
        pass

    # Class Methods End
