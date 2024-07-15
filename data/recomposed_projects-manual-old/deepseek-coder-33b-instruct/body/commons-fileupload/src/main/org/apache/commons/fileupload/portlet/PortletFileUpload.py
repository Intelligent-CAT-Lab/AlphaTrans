from __future__ import annotations
import re
import io
from src.main.org.apache.commons.fileupload.FileItemFactory import *
from src.main.org.apache.commons.fileupload.FileUpload import *


class PortletFileUpload(FileUpload):

    @staticmethod
    def PortletFileUpload1() -> PortletFileUpload:
        return PortletFileUpload(None)

    def __init__(self, fileItemFactory: FileItemFactory) -> None:
        super().__init__(1, fileItemFactory)
