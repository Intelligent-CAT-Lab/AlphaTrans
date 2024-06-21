class ValueBean:

    def __init__(self) -> None:
        self._value = None
    

    def getValue(self) -> str:
        return self._value
    

    def setValue(self, value) -> None:
        self._value = value
