from __future__ import annotations
import re
from abc import ABC
import io
import typing
from typing import *
from src.main.org.apache.commons.fileupload.FileItemStream import *
from src.main.org.apache.commons.fileupload.FileUploadException import *


class FileItemIterator(ABC):

    def next(self) -> FileItemStream:
        pass

    def hasNext(self) -> bool:
        return self._items.hasNext()
