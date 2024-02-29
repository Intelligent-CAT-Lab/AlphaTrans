# Imports Begin
from abc import ABC

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class Closeable(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def isClosed(self) -> bool:

        try:
            self.file.close()
            return True
        except IOError:
            return False

    def close(self) -> None:

        raise NotImplementedError()

    # Class Methods End
