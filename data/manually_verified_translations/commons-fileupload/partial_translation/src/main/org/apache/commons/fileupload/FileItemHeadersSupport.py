from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.fileupload.FileItemHeaders import *


class FileItemHeadersSupport(ABC):

    def setHeaders(self, headers: FileItemHeaders) -> None:
        self.headers = headers

    def getHeaders(self) -> FileItemHeaders:
        pass
