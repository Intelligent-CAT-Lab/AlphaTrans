# Imports Begin
# Imports End


class ParseException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = 5355281266579392077
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:

        super().__init__(message)

    # Class Methods End
