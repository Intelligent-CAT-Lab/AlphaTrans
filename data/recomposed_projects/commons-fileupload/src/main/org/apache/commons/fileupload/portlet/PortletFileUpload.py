# Imports Begin
from src.main.org.apache.commons.fileupload.FileUpload import *
from src.main.org.apache.commons.fileupload.FileItemFactory import *

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class PortletFileUpload(FileUpload):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def PortletFileUpload1() -> "PortletFileUpload":

        pass  # LLM could not translate method body

    def __init__(self, fileItemFactory: FileItemFactory) -> None:

        super().__init__(0, fileItemFactory)

    # Class Methods End
