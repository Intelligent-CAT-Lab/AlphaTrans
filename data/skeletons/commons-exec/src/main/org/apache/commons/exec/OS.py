from __future__ import annotations

# Imports Begin
import io

# Imports End


class OS:

    # Class Fields Begin
    FAMILY_9X: str = None
    FAMILY_DOS: str = None
    FAMILY_MAC: str = None
    FAMILY_NETWARE: str = None
    FAMILY_NT: str = None
    FAMILY_OS2: str = None
    FAMILY_OS400: str = None
    FAMILY_TANDEM: str = None
    FAMILY_UNIX: str = None
    FAMILY_VMS: str = None
    FAMILY_WINDOWS: str = None
    FAMILY_ZOS: str = None
    __DARWIN: str = None
    __OS_NAME: str = None
    __OS_ARCH: str = None
    __OS_VERSION: str = None
    __PATH_SEP: str = None
    # Class Fields End

    # Class Methods Begin
    @staticmethod
    def isVersion(version: str) -> bool:
        pass

    @staticmethod
    def isOs(family: str, name: str, arch: str, version: str) -> bool:
        pass

    @staticmethod
    def isName(name: str) -> bool:
        pass

    @staticmethod
    def isFamilyZOS() -> bool:
        pass

    @staticmethod
    def isFamilyWinNT() -> bool:
        pass

    @staticmethod
    def isFamilyWindows() -> bool:
        pass

    @staticmethod
    def isFamilyWin9x() -> bool:
        pass

    @staticmethod
    def isFamilyUnix() -> bool:
        pass

    @staticmethod
    def isFamilyTandem() -> bool:
        pass

    @staticmethod
    def isFamilyOS400() -> bool:
        pass

    @staticmethod
    def isFamilyOS2() -> bool:
        pass

    @staticmethod
    def isFamilyOpenVms() -> bool:
        pass

    @staticmethod
    def isFamilyNetware() -> bool:
        pass

    @staticmethod
    def isFamilyMac() -> bool:
        pass

    @staticmethod
    def isFamilyDOS() -> bool:
        pass

    @staticmethod
    def isArch(arch: str) -> bool:
        pass

    def __init__(self) -> None:
        pass

    @staticmethod
    def __isFamily(family: str) -> bool:
        pass

    # Class Methods End
