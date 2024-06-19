import java
import abc

class JavaHandler:
    def mapping(x, id_map=None):
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

        # get underlying python objects from java objects
        if hasattr(x, 'getPythonObject'):            
            obj = x.getPythonObject()
            id_map[id] = obj            
            x.revsync() # sync the java object with the python object

            return obj
        
        # Properties
        if hasattr(x, 'getProperty'):
            return JavaHandler.properties_to_dict(x)

        # Map
        if hasattr(x, 'keySet'):
            obj = JavaHandler.map_to_dict(x, id_map)
            id_map[id] = obj
            return obj

        # List
        if hasattr(x, 'toArray'):
            obj = JavaHandler.list_to_list(x, id_map)
            id_map[id] = obj
            return obj

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

    def map_to_dict(x, id_map=None):
        D = dict()
        for key in x.keySet():
            D[JavaHandler.mapping(key)] = JavaHandler.mapping(x.get(key), id_map)
        return D
    
    def list_to_list(x, id_map=None):
        L = []
        for item in x.toArray():
            L.append(JavaHandler.mapping(item, id_map))
        return L
    
    def getJavaId(obj):
        return java.type('{project}.IntegrationUtils').getIdentityHashCode(obj)

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
