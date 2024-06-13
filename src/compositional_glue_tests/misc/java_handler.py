import java
import abc

class JavaHandler:
    def mapping(x):
        # if not 'foreign' type, return as it is
        if not type(x).__name__ == 'foreign':
            return x
        
        # Noneify
        if x == None:
            return None
        
        # get underlying python objects from java objects
        if hasattr(x, 'getPythonObject'):
            obj = x.getPythonObject()
            
            # recursively map all fields of the object
            if hasattr(obj, '__dict__'):
                for key in obj.__dict__:
                    if key != "javaObj": # leave javaObj as it is
                        obj.__dict__[key] = JavaHandler.mapping(obj.__dict__[key])
                    
            return obj
        
        # Properties
        if hasattr(x, 'getProperty'):
            return JavaHandler.properties_to_dict(x)
        
        # Map
        if hasattr(x, 'keySet'):
            return JavaHandler.map_to_dict(x)
        
        # List
        if hasattr(x, 'toArray'):
            return JavaHandler.list_to_list(x)
        
        # handle the 'Class' type
        # this is safe because Strings don't have the foreign type
        try:
            if str(x).startswith("java."):
                return java.type(str(x))
        except:
            pass
        
        raise ValueError("Unknown Java object type: " + repr(x))
    
    def properties_to_dict(x):
        D = dict()
        for key in x.propertyNames():
            D[key] = x.getProperty(key)
        return D

    def map_to_dict(x):
        D = dict()
        for key in x.keySet():
            D[JavaHandler.mapping(key)] = JavaHandler.mapping(x.get(key))
        return D
    
    def list_to_list(x):
        L = []
        for item in x.toArray():
            L.append(JavaHandler.mapping(item))
        return L


class Types:
    String = java.type('java.lang.String')
    Object = java.type('java.lang.Object')
    Number = java.type('java.lang.Number')
    Class = java.type('java.lang.Class')
    Date = java.type('java.util.Date')
    FileInputStream = java.type('java.io.FileInputStream')
    File = java.type('java.io.File')
    Files = java.type('java.io.File[]')
    URL = java.type('java.net.URL')


class StaticFieldRedirector(abc.ABCMeta):
    """
    This metaclass is used to redirect static field access to the corresponding Java class fields.
    """
    
    def __getattr__(cls, name):
        try:
            x = object.__getattribute__(cls, name)
            if callable(x) or name in ['javaObj', 'javaClz']:
                return x
        except AttributeError:
            pass
        return getattr(cls.javaClz, name)
