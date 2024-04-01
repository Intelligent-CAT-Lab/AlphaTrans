# Imports Begin
import typing
import io

# Imports End


class FileUploadException(Exception):

    # Class Fields Begin
    __serialVersionUID: int = 8881893724388807504
    __cause: BaseException = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> BaseException:

        return self.__cause

    def printStackTrace1(self, writer: io.TextIOWrapper) -> None:

        super().printStackTrace(writer)
        if self.__cause is not None:
            writer.write("Caused by:\n")
            self.__cause.printStackTrace(writer)

    def printStackTrace0(self, stream: typing.IO[str]) -> None:

        super().printStackTrace(stream)
        if self.__cause is not None:
            stream.write("Caused by:\n")
            self.__cause.printStackTrace(stream)

    def __init__(self, msg: str, cause: BaseException) -> None:

        super().__init__(msg)
        self.__cause = cause

    @staticmethod
    def FileUploadException1(msg: str) -> "FileUploadException":

        pass  # LLM could not translate method body

    @staticmethod
    def FileUploadException0() -> "FileUploadException":

        pass  # LLM could not translate method body

    # Class Methods End
