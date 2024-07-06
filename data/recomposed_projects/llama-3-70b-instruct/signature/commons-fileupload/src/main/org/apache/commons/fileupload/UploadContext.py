from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.fileupload.RequestContext import *


class UploadContext(ABC):

    def contentLength(self) -> int:
        return self.request.getContentLength()
