import pytest

from urllib.parse import urljoin, urlparse
from urllib.request import urlopen
from pathlib import Path
import importlib.util

class TestGenericObjectPoolClassLoaders:

    _BASE_URL = str(Path(__file__)\
        .resolve()\
        .parent\
        .parent\
        .parent\
        .parent\
        .parent\
        .parent\
        .parent\
        .parent / 'main/resources/org/apache/commons/pool2/impl/')

    class CustomClassLoader:
        
        def __init__(self, n) -> None:
            self.__n = n
            self.__basePath = TestGenericObjectPoolClassLoaders._BASE_URL
            self.__loadedModules = {}

        
        def findResource(self, name) -> str:
            if not name.endswith(str(self.__n)):
                return None

            resourcePath = urljoin(
                self.__basePath,
                name
            )
            if Path(resourcePath).exists():
                return resourcePath
            return None
        

        def loadModule(self, moduleName, urlOrPath=None):
            if moduleName in self.__loadedModules:
                return self.__loadedModules[moduleName]

            if urlOrPath is None:
                urlOrPath = self.__basePath

            if isinstance(urlOrPath, str):
                url = urlparse(urlOrPath)
                if url.scheme == 'file':
                    modulePath = Path(url.path).resolve()
                elif url.scheme in ('http', 'https'):
                    with urlopen(urlOrPath) as response:
                        modulePath = Path(response.read()) / (moduleName + ".py")
                else:
                    modulePath = Path(url.path).resolve() / (moduleName + ".py")
            elif isinstance(urlOrPath, Path):
                modulePath = urlOrPath.resolve() / (moduleName + ".py")
            else:
                raise ValueError("Invalid URL or path")

            spec = importlib.util.spec_from_file_location(moduleName, modulePath)
            if spec is None:
                raise ImportError(f"Failed to create spec for module '{moduleName}'")
            
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            self.__loadedModules[moduleName] = module
            return module
