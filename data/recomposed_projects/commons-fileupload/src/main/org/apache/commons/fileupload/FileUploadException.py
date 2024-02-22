# Imports Begin
# Imports End


class FileUploadException(Exception):

    # Class Fields Begin
    __version: str = "1.0"
    __cause: Exception = None
    # Class Fields End

    # Class Methods Begin
    def getCause(self) -> Exception:

        return self.__cause

    def printStackTrace1(self, writer: io.TextIOWrapper) -> None:

        super().printStackTrace(writer)
        if self.__cause is not None:
            writer.write("Caused by:\n")
            self.__cause.printStackTrace(writer)

    def printStackTrace0(self, stream: io.TextIOWrapper) -> None:

        super().printStackTrace(stream)
        if self.__cause is not None:
            stream.write("Caused by:\n")
            self.__cause.printStackTrace(stream)

    def __init__(self, msg: str, cause: Exception) -> None:

        super().__init__(msg)
        self.cause = cause

    @staticmethod
    def FileUploadException1(msg: str) -> FileUploadException:

        return FileUploadException(msg, None)

    @staticmethod
    def FileUploadException0() -> FileUploadException:

        pass  # LLM could not translate method body

    # Class Methods End
