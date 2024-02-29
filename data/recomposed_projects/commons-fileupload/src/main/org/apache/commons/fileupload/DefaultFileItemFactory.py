# Imports Begin
from src.main.org.apache.commons.fileupload.disk.DiskFileItemFactory import *
import pathlib

from src.main.org.apache.commons.fileupload.java_handler import java_handler
# Imports End


@java_handler
class DefaultFileItemFactory(DiskFileItemFactory):

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:

        super().__init__(sizeThreshold, repository)

    @staticmethod
    def DefaultFileItemFactory1() -> DefaultFileItemFactory:

        pass  # LLM could not translate method body

    # Class Methods End
