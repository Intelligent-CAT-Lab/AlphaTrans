import numbers
import java # type: ignore
import abc
import inspect
import io
import pathlib
import re


class JavaHandler:
    def mapping(x, id_map=None, target_object=None):
        if id_map is None:
            id_map = dict() # map IDs of Java objects to IDs of their corresponding Python objects

        # Noneify
        if x == None:
            return None

        # if not 'foreign' type, return as it is
        if not type(x).__name__ == 'foreign':
            return x

        # check if the object has already been mapped
        id = JavaHandler.getJavaId(x)
        if id in id_map:
            return id_map[id]
        
        # if the target object is None, try to take it from the J-py map
        if target_object is None:
            target_object = JavaHandler.mapping(JavaHandler.getPyFromJ(id))

        # get underlying python objects from java objects
        if hasattr(x, 'getPythonObject'):
            obj = x.getPythonObject()
            id_map[id] = obj
            x.jToPy(id_map) # sync the java object with the python object

            return obj
        
        # Properties
        if hasattr(x, 'getProperty'):
            return JavaHandler.properties_to_dict(x, id_map, target_object)

        # Map
        if JavaHandler.isJavaMap(x):
            return JavaHandler.map_to_dict(x, id_map, target_object)

        # List
        if JavaHandler.isJavaList(x):
            return JavaHandler.list_to_list(x, id_map, target_object)

        # Set
        if JavaHandler.isJavaSet(x):
            return JavaHandler.set_to_set(x, id_map, target_object)

        # handle exception objects
        if x.getClass().getName().endswith("Exception"):
            return ExceptionHandler.instance_mapping(x)

        # handle the 'Class' type
        # builtin classes
        if JavaHandler.isJavaClass(x) and str(x).startswith("java."):
            # Handle exception classes separately
            if str(x).endswith("Exception"):
                return ExceptionHandler.mapping(x)
            
            # return other classes after mapping if possible
            return ClassMapping.get(str(x), java.type(str(x)))
        
        # package classes
        if JavaHandler.isJavaClass(x):
            cls = JavaHandler.getPythonClassFromJavaClass(x)
            if cls is not None: # check if class could be loaded
                return cls

        # handle StringBuilder
        if x.getClass().getName() == "java.lang.StringBuilder":
            obj = x.toString()
            id_map[id] = obj
            return 
        
        # handle StringBuffer
        if x.getClass().getName() == "java.lang.StringBuffer":
            obj = x.toString()
            id_map[id] = obj
            return obj

        # handle StringReader
        if x.getClass().getName() == "java.io.StringReader":
            return JavaHandler.stringreader_to_stringio(x, id_map, target_object)

        # handle StringWriter
        if x.getClass().getName() == "java.io.StringWriter":
            return JavaHandler.stringwriter_to_stringio(x, id_map, target_object)

        # Array
        if x.getClass().isArray():
            return JavaHandler.array_to_list(x, id_map, target_object)

        # File
        if x.getClass().getName() == "java.io.File":
            return JavaHandler.file_to_path(x, id_map, target_object)

        # Pattern
        if x.getClass().getName() == "java.util.regex.Pattern":
            return JavaHandler.pattern_to_pattern(x, id_map, target_object)

        # Charset
        if "sun.nio.cs." in x.getClass().getName():
            return JavaHandler.charset_to_string(x)
        
        print("[JavaHandler.mapping] Unhandled Java object type: " + repr(x))
        return x # return untranslated object

    def properties_to_dict(x, id_map, target_object=None):
        D = dict()
        if target_object:
            D = target_object
            D.clear()
        id = JavaHandler.getJavaId(x)
        id_map[id] = D
        for key in x.propertyNames():
            D[key] = x.getProperty(key)

        JavaHandler.putObjectsToMaps(x, D)
        return D

    def map_to_dict(x, id_map, target_object=None):
        D = dict()
        if target_object:
            D = target_object
            D.clear()
        id = JavaHandler.getJavaId(x)
        id_map[id] = D
        for key in x.keySet():
            D[JavaHandler.mapping(key)] = JavaHandler.mapping(x.get(key), id_map)

        JavaHandler.putObjectsToMaps(x, D)
        return D
    
    def list_to_list(x, id_map, target_object=None):
        L = []
        if target_object:
            L = target_object
            L.clear()
        id = JavaHandler.getJavaId(x)
        id_map[id] = L
        for item in x.toArray():
            L.append(JavaHandler.mapping(item, id_map))
        
        JavaHandler.putObjectsToMaps(x, L)    
        return L

    def set_to_set(x, id_map, target_object=None):
        S = set()
        if target_object:
            S = target_object
            S.clear()
        id = JavaHandler.getJavaId(x)
        id_map[id] = S
        for item in x.toArray():
            S.add(JavaHandler.mapping(item, id_map))

        JavaHandler.putObjectsToMaps(x, S)
        return S

    def array_to_list(x, id_map, target_object=None):
        L = []
        if target_object:
            L = target_object
            L.clear()
        id = JavaHandler.getJavaId(x)
        id_map[id] = L
        for i in range(x.length):
            L.append(JavaHandler.mapping(x[i], id_map))

        JavaHandler.putObjectsToMaps(x, L)
        return L

    def stringreader_to_stringio(x, id_map, target_object=None):
        S = io.StringIO()
        if target_object:
            S = target_object
            S.seek(0)
            S.truncate(0)
        id = JavaHandler.getJavaId(x)
        id_map[id] = S
        while (c := x.read()) != -1:
            S.write(chr(c))
        S.seek(0)
        return S

    def stringwriter_to_stringio(x, id_map, target_object=None):
        S = io.StringIO()
        if target_object:
            S = target_object
            S.seek(0)
            S.truncate(0)
        id = JavaHandler.getJavaId(x)
        id_map[id] = S
        S.write(x.toString())
        return S

    def file_to_path(x, id_map, target_object=None):
        P = pathlib.Path(x.getAbsolutePath())
        if target_object:
            P = target_object
        id = JavaHandler.getJavaId(x)
        id_map[id] = P
        return P

    def pattern_to_pattern(x, id_map, target_object=None):
        P = re.compile(x.pattern(), x.flags())
        if target_object:
            P = target_object
        id = JavaHandler.getJavaId(x)
        id_map[id] = P
        return P

    def charset_to_string(x):
        charsetName = x.getClass().getName().split(".")[-1]
        if charsetName == "UTF_8":
            return "UTF-8"
        if charsetName == "UTF_16":
            return "UTF-16"
        if charsetName == "UTF_16BE":
            return "UTF-16BE"
        if charsetName == "UTF_16LE":
            return "UTF-16LE"
        if charsetName == "US_ASCII":
            return "US-ASCII"
        if charsetName == "ISO_8859_1":
            return "ISO-8859-1"

        # handle other charsets with a generic rule
        return charsetName.replace("_", "-")

    def getPythonId(obj):
        return id(obj)

    IntegrationUtils = java.type('{project}.IntegrationUtils')
    ContextInitializer = java.type('{project}.ContextInitializer')

    def isPythonClass(obj):
        return inspect.isclass(obj)

    def isJavaClass(obj):
        return JavaHandler.IntegrationUtils.isJavaClass(obj)

    def isJavaList(obj):
        return JavaHandler.IntegrationUtils.isJavaList(obj)

    def isJavaSet(obj):
        return JavaHandler.IntegrationUtils.isJavaSet(obj)

    def isJavaMap(obj):
        return JavaHandler.IntegrationUtils.isJavaMap(obj)

    def getPythonClassFromJavaClass(javaClass):
        return JavaHandler.mapping(JavaHandler.ContextInitializer.getPythonClass(javaClass))

    def getJavaId(obj):
        return JavaHandler.IntegrationUtils.getIdentityHashCode(obj)

    def valueToObject(*args):
        return JavaHandler.IntegrationUtils.valueToObject(*args)

    def getPyFromJ(obj):
        return JavaHandler.IntegrationUtils.getPyFromJ(obj)

    def putObjectsToMaps(javaObj, pyObj):
        return JavaHandler.IntegrationUtils.putObjectsToMaps(javaObj, pyObj)

    def createDefaultPythonObject(cls):
        return getattr(cls, '__new__')(cls)

    def pythonSetToPythonList(s):
        return list(s)


class ExceptionHandler:
    exception_map = {exception_map} # type: ignore
    
    @staticmethod
    def mapping(x):
        exception_name = str(x).split(".")[-1]
        if exception_name in ExceptionHandler.exception_map:
            return eval(ExceptionHandler.exception_map[exception_name]['target'])
        
        # return the same class if the exception is not in the mapping
        return x
    
    @staticmethod
    def instance_mapping(x):
        exception_name = x.getClass().getName().split(".")[-1]
        exception_message = str(x).split(":", 1)[-1].strip()
        if exception_name in ExceptionHandler.exception_map:
            exception_message = exception_message.replace('"', '\\"')
            return eval(f"{{ExceptionHandler.exception_map[exception_name]['target']}}(\"{{exception_message}}\")")
        
        # return the same object if the exception is not in the mapping
        return x

ClassMapping = {{
    "java.lang.String"      : str,
    "java.lang.Object"      : object,
    "java.lang.Boolean"     : bool,
    "java.lang.Number"      : numbers.Number,
    "java.lang.Class"       : type,
}}


class StaticFieldRedirector(abc.ABCMeta):
    """
    This metaclass is used to redirect static field gets and sets 
    to the corresponding Java class fields.
    """
    
    def __getattr__(cls, name):
        try:
            x = object.__getattribute__(cls, name)
            if callable(x) or name in ['javaObj', 'javaClz']:
                return x
        except AttributeError:
            pass

        return JavaHandler.mapping(getattr(cls.javaClz, StaticFieldRedirector.unmangle_name(name)))

    def __setattr__(cls, name, value):
        cleaned_name = StaticFieldRedirector.unmangle_name(name)        
        if hasattr(cls.javaClz, cleaned_name):
            translated_value = JavaHandler.valueToObject(
                value,
                JavaHandler.valueToObject(None, "Object"), # classDescriptior: None
                JavaHandler.valueToObject(dict(), "Map"), # idMap
                getattr(cls.javaClz, cleaned_name) # targetObject
            )
            setattr(cls.javaClz, cleaned_name, translated_value)

        object.__setattr__(cls, name, value)
        
    @staticmethod
    def unmangle_name(name: str):
        # undo name 'mangling'
        name =  name.split('__', 1)[-1]
        
        # remove preceding and trailing underscores
        name = name.strip('_')
        
        return name
