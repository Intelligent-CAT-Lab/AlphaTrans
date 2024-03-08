package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
public abstract class BaseObjectPool<T> extends BaseObject implements ObjectPool<T> {
    private static Value clz = ContextInitializer.getPythonClass("/BaseObjectPool.py", "BaseObjectPool");
    private Value obj;
    public BaseObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    protected void toStringAppendFields(final StringBuilder builder) {
// 
// builder.append("closed=");
// builder.append(closed);
// 

obj.invokeMember("toStringAppendFields", builder);
}
    public int getNumIdle() {
// 
// return -1;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle").as(int.class);
}
    public int getNumActive() {
// 
// return -1;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive").as(int.class);
}
    public void close() {
// 
// closed = true;
// 

obj.invokeMember("close");
}
    public void clear() throws Exception, UnsupportedOperationException {
try {
// 
// throw new UnsupportedOperationException();
// 

obj.invokeMember("clear");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "BaseObjectPool.clear");
}
}
    public void addObject() throws Exception, UnsupportedOperationException {
try {
// 
// throw new UnsupportedOperationException();
// 

obj.invokeMember("addObject");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "BaseObjectPool.addObject");
}
}
    public final boolean isClosed() {
// 
// return closed;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("isClosed").as(boolean.class);
}
    protected final void assertOpen() throws IllegalStateException {
try {
// 
// if (isClosed()) {
// throw new IllegalStateException("Pool not open");
// }
// 

obj.invokeMember("assertOpen");
} catch (PolyglotException e) {
    // TODO: Handle IllegalStateException
    throw (IllegalStateException) ExceptionHandler.handle(e, "BaseObjectPool.assertOpen");
}
}
    public abstract void returnObject(T obj) throws Exception;
    public abstract void invalidateObject0(T obj) throws Exception;
    public abstract T borrowObject() throws Exception;
}
