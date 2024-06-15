import pytest

import unittest
from io import StringIO

class CustomValidatorResourcesTest(unittest.TestCase):

    def __init__(self, methodName='runTest') -> None:
        super().__init__(methodName)

    
    def setUp(self) -> None:
        pass

    
    def tearDown(self) -> None:
        pass

    
    @pytest.mark.test
    def testCustomResources(self) -> None:
        inStream = None
        try:
            inStream = StringIO(self.__getResourceContent("TestNumber-config.xml"))
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
