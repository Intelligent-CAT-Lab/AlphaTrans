from __future__ import annotations
import re
from abc import ABC
import io
from src.main.org.apache.commons.fileupload.RequestContext import *


class UploadContext(ABC):

    def contentLength(self) -> int:

        # This method is abstract in the Java code, so it doesn't have a body.
        # In Python, we can't have abstract methods in abstract classes, so we can't translate it directly.
        # However, we can raise a NotImplementedError to indicate that this method should be implemented in a subclass.
        raise NotImplementedError("Subclass must implement abstract method")
