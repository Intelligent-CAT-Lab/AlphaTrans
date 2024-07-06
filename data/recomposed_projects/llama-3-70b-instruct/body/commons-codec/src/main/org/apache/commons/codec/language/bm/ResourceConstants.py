from __future__ import annotations
import re
import io
from src.main.org.apache.commons.codec.CharEncoding import *


class ResourceConstants:

    EXT_CMT_START: str = "/*"
    EXT_CMT_END: str = "*/"
    ENCODING: str = CharEncoding.UTF_8
    CMT: str = "//"
