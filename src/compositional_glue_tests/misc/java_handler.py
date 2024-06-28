import java
import abc
import io


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
            x.revsync(id_map) # sync the java object with the python object

            return obj

        # Properties
        if hasattr(x, 'getProperty'):
            return JavaHandler.properties_to_dict(x)

        # Map
        if hasattr(x, 'keySet'):
            obj = JavaHandler.map_to_dict(x, id_map)
            return obj

        # List
        if hasattr(x, 'toArray'):
            obj = JavaHandler.list_to_list(x, id_map)
            return obj

        # Array
        if hasattr(x, 'length'):
            obj = JavaHandler.array_to_list(x, id_map)
            return obj

        # handle the 'Class' type
        # this is safe because Strings don't have the foreign type
        try:
            if str(x).startswith("java."):
                # Handle exception classes separately
                if str(x).endswith("Exception"):
                    return ExceptionHandler.mapping(x)
                
                # return other classes as they are
                return java.type(str(x))
        except:
            pass

        # handle StringBuilder
        if x.getClass().getName() == "java.lang.StringBuilder":
            obj = x.toString()
            id_map[id] = obj
            return obj

        # handle StringReader
        if x.getClass().getName() == "java.io.StringReader":
            obj = JavaHandler.stringreader_to_stringio(x, id_map)
            return obj

        # handle StringWriter
        if x.getClass().getName() == "java.io.StringWriter":
            obj = JavaHandler.stringwriter_to_stringio(x, id_map)
            return obj

        raise ValueError("Unknown Java object type: " + repr(x))

    def properties_to_dict(x):
        D = dict()
        for key in x.propertyNames():
            D[key] = x.getProperty(key)
        return D

    def map_to_dict(x, id_map=None):
        D = dict()
        id = JavaHandler.getJavaId(x)
        id_map[id] = D
        for key in x.keySet():
            D[JavaHandler.mapping(key)] = JavaHandler.mapping(x.get(key), id_map)
        return D
    
    def list_to_list(x, id_map=None):
        L = []
        id = JavaHandler.getJavaId(x)
        id_map[id] = L
        for item in x.toArray():
            L.append(JavaHandler.mapping(item, id_map))        
        return L
    
    def getJavaId(obj):
        return java.type('{project}.IntegrationUtils').getIdentityHashCode(obj)

    def array_to_list(x, id_map=None):
        L = []
        id = JavaHandler.getJavaId(x)
        id_map[id] = L
        for i in range(x.length):
            L.append(JavaHandler.mapping(x[i], id_map))
        return L

    def stringreader_to_stringio(x, id_map=None):
        S = io.StringIO()
        id = JavaHandler.getJavaId(x)
        id_map[id] = S
        while (c := x.read()) != -1:
            S.write(chr(c))
        S.seek(0)
        return S

    def stringwriter_to_stringio(x, id_map=None):
        S = io.StringIO()
        id = JavaHandler.getJavaId(x)
        id_map[id] = S
        S.write(x.toString())
        return S
    
    def getJavaId(obj):
        return java.type('{project}.IntegrationUtils').getIdentityHashCode(obj)

    def valueToObject(obj, class_descriptor: str):
        return java.type('{project}.IntegrationUtils').valueToObject(obj, class_descriptor)

    def getPythonId(obj):
        return id(obj)


class ExceptionHandler:
    exception_map = {exception_map}
    
    @staticmethod
    def mapping(x):
        exception_name = str(x).split(".")[-1]
        if exception_name in ExceptionHandler.exception_map:
            return eval(ExceptionHandler.exception_map[exception_name]['target'])
        
        # return the same class if the exception is not in the mapping
        return x


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

        return getattr(cls.javaClz, StaticFieldRedirector.unmangle_name(name))

    def __setattr__(cls, name, value):
        cleaned_name = StaticFieldRedirector.unmangle_name(name)        
        if hasattr(cls.javaClz, cleaned_name):
            setattr(cls.javaClz, cleaned_name, value) # TODO: type-casting

        object.__setattr__(cls, name, value)
        
    @staticmethod
    def unmangle_name(name: str):
        # undo name 'mangling'
        name =  name.split('__', 1)[-1]
        
        # remove preceding and trailing underscores
        name = name.strip('_')
        
        return name
