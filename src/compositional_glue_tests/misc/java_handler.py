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
            return x.getPythonObject()
        
        # Properties
        if hasattr(x, 'getProperty'):
            return JavaHandler.properties_to_dict(x)
        
        # Map
        if hasattr(x, 'keySet'):
            return JavaHandler.map_to_dict(x)
        
        # List
        if hasattr(x, 'toArray'):
            return JavaHandler.list_to_list(x)
        
        raise ValueError("Unknown Java object type")
    
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
