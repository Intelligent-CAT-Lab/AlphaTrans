# Imports Begin
from src.main.org.apache.commons.fileupload.InvalidFileNameException import *

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
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
