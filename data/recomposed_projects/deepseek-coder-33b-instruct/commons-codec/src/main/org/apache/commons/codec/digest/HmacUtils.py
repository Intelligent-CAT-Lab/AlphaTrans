from __future__ import annotations
import re
import io


class HmacUtils:

    __STREAM_BUFFER_LENGTH: int = 1024
