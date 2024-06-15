class PrivateException(RuntimeError):

    __serialVersionUID = 1

    def __init__(self, message: str) -> None:
        super().__init__(message)
