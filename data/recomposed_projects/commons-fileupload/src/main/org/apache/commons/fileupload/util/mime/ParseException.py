# Imports Begin
from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class ParseException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = 5355281266579392077
    # Class Fields End

    # Class Methods Begin
    def __init__(self, message: str) -> None:

        super().__init__(message)

    # Class Methods End
