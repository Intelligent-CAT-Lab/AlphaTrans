from __future__ import annotations
import re
import io
from src.main.org.apache.commons.fileupload.InvalidFileNameException import *


class Streams:

    DEFAULT_BUFFER_SIZE: int = 8192

    @staticmethod
    def checkFileName(fileName: str) -> str:

        if fileName is not None and "\u0000" in fileName:
            sb = ""
            for i in range(len(fileName)):
                c = fileName[i]
                if c == "\u0000":
                    sb += "\\0"
                else:
                    sb += c
            raise InvalidFileNameException(fileName, "Invalid file name: " + sb)
        return fileName

    def __init__(self) -> None:
        pass
