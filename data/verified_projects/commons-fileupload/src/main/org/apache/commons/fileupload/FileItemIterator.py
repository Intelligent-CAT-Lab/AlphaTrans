import pytest

# Imports Begin
from src.main.org.apache.commons.fileupload.FileUploadException import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
import typing
from typing import *
from abc import ABC

# Imports End


class FileItemIterator(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def next(self) -> FileItemStream:

        try:
            return FileItemStream(self.file_upload.next())
        except FileUploadException as e:
            raise e
        except IOError as e:
            raise e

    def hasNext(self) -> bool:

        try:
            return self.file.read(1) != b""
        except FileUploadException as e:
            raise e
        except IOError as e:
            raise e

    # Class Methods End
