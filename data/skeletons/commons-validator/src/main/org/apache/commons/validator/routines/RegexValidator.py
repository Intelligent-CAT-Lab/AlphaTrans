# Imports Begin
import typing

# Imports End


class RegexValidator(Serializable):

    # Class Fields Begin
    __serialVersionUID: int = None
    __patterns: typing.List[re.Pattern] = None
    # Class Fields End

    # Class Methods Begin
    def toString(self) -> str:
        pass

    def validate(self, value: str) -> str:
        pass

    def match(self, value: str) -> typing.List[str]:
        pass

    def isValid(self, value: str) -> bool:
        pass

    @staticmethod
    def RegexValidator3(regex: str) -> "RegexValidator":
        pass

    @staticmethod
    def RegexValidator2(regex: str, caseSensitive: bool) -> "RegexValidator":
        pass

    @staticmethod
    def RegexValidator1(regexs: typing.List[str]) -> "RegexValidator":
        pass

    def __init__(self, regexs: typing.List[str], caseSensitive: bool) -> None:
        pass

    # Class Methods End
