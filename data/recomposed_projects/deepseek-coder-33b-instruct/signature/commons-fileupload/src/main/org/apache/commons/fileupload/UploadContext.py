from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.fileupload.RequestContext import *


class UploadContext(ABC):

    def contentLength(self) -> int:

        # This method is abstract in the Java code, so it doesn't have a body.
        # You need to implement this method in a subclass.
        pass
