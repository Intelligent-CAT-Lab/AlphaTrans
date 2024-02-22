# Imports Begin
from commons.fileupload.src.main.java.org.apache.commons.fileupload.portlet.FileUpload import (
    FileUpload,
)
from commons.fileupload.src.main.java.org.apache.commons.fileupload.portlet.FileItemFactory import (
    FileItemFactory,
)

# Imports End


class PortletFileUpload(FileUpload):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def PortletFileUpload1() -> PortletFileUpload:

        pass  # LLM could not translate method body

    def __init__(self, fileItemFactory: FileItemFactory) -> None:

        super().__init__(0, fileItemFactory)

    # Class Methods End
