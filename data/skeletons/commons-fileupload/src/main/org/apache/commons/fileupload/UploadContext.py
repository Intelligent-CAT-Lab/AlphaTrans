from __future__ import annotations

# Imports Begin
from src.main.org.apache.commons.fileupload.RequestContext import *
import io
from abc import ABC

# Imports End


class UploadContext(ABC):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def contentLength(self) -> int:
        pass

    # Class Methods End
