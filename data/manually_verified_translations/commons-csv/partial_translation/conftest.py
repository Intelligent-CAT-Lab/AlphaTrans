
# conftest.py
import pytest
import inspect
from abc import ABC

def pytest_collection_modifyitems(config, items):
    def is_abstract_class(item):
        # Check if the class of the item is a subclass of ABC (abstract base class)
        if inspect.isclass(item.cls):
            # Check if the class is actually abstract
            return ABC in item.cls.__bases__
        return False

    # Filter out items that belong to abstract classes
    items[:] = [item for item in items if not is_abstract_class(item)]
