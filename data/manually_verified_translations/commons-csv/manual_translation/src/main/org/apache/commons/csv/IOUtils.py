from __future__ import annotations
import time
import copy
import re
from io import IOBase
from io import StringIO
import io
import typing
from typing import *


class IOUtils:

    DEFAULT_BUFFER_SIZE: int = 1024 * 4
    __EOF: int = -1

    @staticmethod
    def rethrow(throwable: BaseException) -> RuntimeError:
        raise throwable

    @staticmethod
    def copyLarge1(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase],
        buffer: typing.List[str],
    ) -> int:

        count = 0
        buffer_size = len(buffer)

        while True:
            if isinstance(input_, io.BufferedReader):
                n = input_.readinto(buffer)
            elif isinstance(input_, (io.TextIOWrapper, io.TextIOBase)):
                read_data = input_.read(buffer_size)
                n = len(read_data)
                buffer[:n] = list(read_data)
            else:
                raise TypeError(f"Unsupported input type: {type(input_)}")

            if n == 0:  # EOF is reached
                break

            if isinstance(output, io.BufferedWriter):
                output.write(''.join(buffer[:n]).encode('utf-8'))
            elif isinstance(output, (io.TextIOWrapper, io.TextIOBase)):
                output.write(''.join(buffer[:n]))
            else:
                raise TypeError(f"Unsupported output type: {type(output)}")

            count += n  # Accumulate the total number of characters copied

        return count

    @staticmethod
    def copyLarge0(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[io.TextIOWrapper, io.BufferedWriter, io.TextIOBase],
    ) -> int:

        return IOUtils.copyLarge1(input_, output, ["\0"] * IOUtils.DEFAULT_BUFFER_SIZE)

    @staticmethod
    def copy1(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[typing.List, io.TextIOBase],
        buffer: typing.Union[str, typing.List[str], io.StringIO],
    ) -> int:

        count = 0
        buffer_size = len(buffer) if isinstance(buffer, (str, list)) else buffer.getbuffer().nbytes

        while True:
            if isinstance(buffer, str):
                read_data = input_.read(buffer_size)
                n = len(read_data)
                if isinstance(read_data, bytes):
                    buffer += read_data.decode('utf-8')
                else:
                    buffer += read_data
            elif isinstance(buffer, list):
                if isinstance(input_, (io.TextIOWrapper, io.TextIOBase)):
                    read_data = input_.read(buffer_size)
                    n = len(read_data)
                    buffer[:n] = list(read_data)
                elif isinstance(input_, io.BufferedReader):
                    n = input_.readinto(buffer)
                else:
                    raise TypeError(f"Unsupported input type: {type(input_)}")
            elif isinstance(buffer, io.StringIO):
                buffer_content = input_.read(buffer_size)
                buffer.seek(0)
                if isinstance(buffer_content, bytes):
                    buffer_content = buffer_content.decode('utf-8')
                buffer.write(buffer_content)
                buffer.seek(0)
                n = len(buffer_content)
            else:
                raise TypeError(f"Unsupported buffer type: {type(buffer)}")

            if n == 0:  # EOF is reached
                break

            if isinstance(buffer, str):
                flipped_buffer = buffer_content
            elif isinstance(buffer, list):
                flipped_buffer = ''.join(buffer[:n])
            elif isinstance(buffer, io.StringIO):
                flipped_buffer = buffer.getvalue()

            if isinstance(output, list):
                output.extend(flipped_buffer)
            elif isinstance(output, io.TextIOBase):
                output.write(flipped_buffer)
            elif isinstance(output, str):
                raise TypeError(
                    "Don't `str` as equivalent to `StringBuider` here since it's immutable"
                )
            else:
                raise TypeError(f"Unsupported output type: {type(output)}")

            count += n

        return count

    @staticmethod
    def copy0(
        input_: typing.Union[io.TextIOWrapper, io.BufferedReader, io.TextIOBase],
        output: typing.Union[typing.List, io.TextIOBase],
    ) -> int:

        buffer = [None] * IOUtils.DEFAULT_BUFFER_SIZE
        return IOUtils.copy1(input_, output, buffer)

    def __init__(self) -> None:
        pass
