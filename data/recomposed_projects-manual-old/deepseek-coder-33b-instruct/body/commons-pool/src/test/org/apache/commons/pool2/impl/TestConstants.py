from __future__ import annotations
import time
import re
import unittest
import pytest
import io
import datetime


class TestConstants:

    ONE_MILLISECOND_DURATION: datetime.timedelta = datetime.timedelta(milliseconds=1)
    ONE_MINUTE_DURATION: datetime.timedelta = datetime.timedelta(minutes=1)
    ONE_SECOND_DURATION: datetime.timedelta = datetime.timedelta(seconds=1)
