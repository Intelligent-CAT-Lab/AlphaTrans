package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
public abstract class BasePooledObjectFactory<T> extends BaseObject
    private static Value clz = ContextInitializer.getPythonClass("/BasePooledObjectFactory.py", "BasePooledObjectFactory");
    private Value obj;
    public BasePooledObjectFactory(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public boolean validateObject(final PooledObject<T> p) {
// 
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("validateObject", p).as(boolean.class);
}
    public void passivateObject(final PooledObject<T> p) throws Exception {
try {
// 

obj.invokeMember("passivateObject", p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BasePooledObjectFactory.passivateObject");
}
}
    public PooledObject<T> makeObject() throws Exception {
try {
// 
// return wrap(create());
// 


// TODO: Check the type mapping below!
return obj.invokeMember("makeObject").as(PooledObject.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BasePooledObjectFactory.makeObject");
}
}
    public void destroyObject0(final PooledObject<T> p) throws Exception {
try {
// 

obj.invokeMember("destroyObject0", p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BasePooledObjectFactory.destroyObject0");
}
}
    public void activateObject(final PooledObject<T> p) throws Exception {
try {
// 

obj.invokeMember("activateObject", p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BasePooledObjectFactory.activateObject");
}
}
    public abstract PooledObject<T> wrap(T obj);
    public abstract T create() throws Exception;
}
