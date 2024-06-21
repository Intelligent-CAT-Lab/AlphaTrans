
# conftest.py
import pytest
import inspect
import unittest

def pytest_collection_modifyitems(config, items):
    additional_items = []

    # Loop through all collected items to add 'unittest' marker to those marked with 'test'
    for item in items:
        if hasattr(item, 'function') and hasattr(item.function, 'pytestmark'):
            for mark in item.function.pytestmark:
                if mark.name == "test":
                    item.add_marker(pytest.mark.unittest)
                    break

    # Inspect all collected test modules to find additional methods marked with 'test'
    for item in items:
        module = inspect.getmodule(item.function)
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, unittest.TestCase):
                for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                    if hasattr(method, 'pytestmark'):
                        for mark in method.pytestmark:
                            if mark.name == "test" and method not in [i.function for i in items] and method.__name__ not in [i.name for i in additional_items]:
                                node = pytest.Function.from_parent(
                                    item.parent,
                                    name=method_name,
                                    callobj=getattr(obj(), method_name)
                                )
                                additional_items.append(node)
                                break
    
    items.extend(additional_items)
