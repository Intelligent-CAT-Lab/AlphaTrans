# Imports Begin
from commons.fileupload.src.main.java.org.apache.commons.fileupload.util.InvalidFileNameException import (
    InvalidFileNameException,
)

# Imports End


class Streams:

    # Class Fields Begin
    DEFAULT_BUFFER_SIZE: int = 8192
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def checkFileName(fileName: str) -> str:

        if fileName and re.search(r"\x00", fileName):
            new_fileName = re.sub(r"[\x00]", r"\\0", fileName)
            raise InvalidFileNameException(
                fileName, f"Invalid file name: {new_fileName}"
            )
        return fileName

    def __init__(self) -> None:

        pass

    # Class Methods End
