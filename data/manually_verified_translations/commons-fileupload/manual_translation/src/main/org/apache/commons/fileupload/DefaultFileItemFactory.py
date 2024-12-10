from __future__ import annotations
import re
import pathlib
import io
import os
from src.main.org.apache.commons.fileupload.disk.DiskFileItemFactory import *


class DefaultFileItemFactory(DiskFileItemFactory):

    def __init__(self, sizeThreshold: int, repository: pathlib.Path) -> None:
        super().__init__(sizeThreshold, repository)

    @staticmethod
    def DefaultFileItemFactory1() -> DefaultFileItemFactory:
        return DefaultFileItemFactory(0, None)
