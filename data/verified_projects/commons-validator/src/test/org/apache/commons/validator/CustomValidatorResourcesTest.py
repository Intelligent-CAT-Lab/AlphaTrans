import pytest

import unittest
from io import StringIO
from pathlib import Path

class CustomValidatorResourcesTest(unittest.TestCase):
    
    def setUp(self) -> None:
        pass

    
    def tearDown(self) -> None:
        pass

    
    @pytest.mark.test
    def testCustomResources(self) -> None:
        inStream = None
        try:
            path = Path(__file__).resolve()\
                .parent.parent.parent.parent.parent / 'resources' \
                / 'org' / 'apache' / 'commons' / 'validator' / 'TestNumber-config.xml'
            inStream = StringIO(self.__getResourceContent(path))
        except Exception as e:
            self.fail(f"Error loading resources: {e}")
        finally:
            try:
                if inStream is not None:
                    inStream.close()
            except Exception as e:
                pass

    def __getResourceContent(self, resource_name):
        try:
            with open(resource_name, 'r') as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"Resource {resource_name} not found")
