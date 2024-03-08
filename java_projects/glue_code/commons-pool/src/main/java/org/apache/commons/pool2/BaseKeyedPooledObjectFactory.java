package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
public abstract class BaseKeyedPooledObjectFactory<K, V> extends BaseObject
    private static Value clz = ContextInitializer.getPythonClass("/BaseKeyedPooledObjectFactory.py", "BaseKeyedPooledObjectFactory");
    private Value obj;
    public BaseKeyedPooledObjectFactory(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public boolean validateObject(final K key, final PooledObject<V> p) {
// 
// return true;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("validateObject", key, p).as(boolean.class);
}
    public void passivateObject(final K key, final PooledObject<V> p) throws Exception {
try {
// 

obj.invokeMember("passivateObject", key, p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BaseKeyedPooledObjectFactory.passivateObject");
}
}
    public PooledObject<V> makeObject(final K key) throws Exception {
try {
// 
// return wrap(create(key));
// 


// TODO: Check the type mapping below!
return obj.invokeMember("makeObject", key).as(PooledObject.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BaseKeyedPooledObjectFactory.makeObject");
}
}
    public void destroyObject0(final K key, final PooledObject<V> p) throws Exception {
try {
// 

obj.invokeMember("destroyObject0", key, p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BaseKeyedPooledObjectFactory.destroyObject0");
}
}
    public void activateObject(final K key, final PooledObject<V> p) throws Exception {
try {
// 

obj.invokeMember("activateObject", key, p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "BaseKeyedPooledObjectFactory.activateObject");
}
}
    public abstract PooledObject<V> wrap(V value);
    public abstract V create(K key) throws Exception;
}
