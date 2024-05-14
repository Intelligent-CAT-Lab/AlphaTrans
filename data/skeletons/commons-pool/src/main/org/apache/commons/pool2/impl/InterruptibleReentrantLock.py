# Imports Begin
# Imports End


class InterruptibleReentrantLock(ReentrantLock):

    # Class Fields Begin
    __serialVersionUID: int = None
    # Class Fields End

    # Class Methods Begin
    def interruptWaiters(self, condition: threading.Condition) -> None:
        pass

    def __init__(self, fairness: bool) -> None:
        pass

    # Class Methods End


class Consumer:

    # Class Fields Begin
    # Class Fields End

    # Class Methods Begin
    def accept(self, p0: threading.Thread) -> None:
        pass

    # Class Methods End
