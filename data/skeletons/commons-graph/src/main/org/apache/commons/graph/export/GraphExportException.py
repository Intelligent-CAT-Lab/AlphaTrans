# Imports Begin
import typing

# Imports End


class GraphExportException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def __init__(
        self,
        cause: BaseException,
        messagePattern: str,
        messageArguments: typing.List[typing.Any],
    ) -> None:
        pass

    # Class Methods End
