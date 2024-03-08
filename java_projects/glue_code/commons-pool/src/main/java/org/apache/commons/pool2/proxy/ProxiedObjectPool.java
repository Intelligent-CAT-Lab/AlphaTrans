package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.util.NoSuchElementException;
import org.apache.commons.pool2.ObjectPool;
import org.apache.commons.pool2.UsageTracking;
public class ProxiedObjectPool<T> implements ObjectPool<T> {
    private static Value clz = ContextInitializer.getPythonClass("/ProxiedObjectPool.py", "ProxiedObjectPool");
    private Value obj;
    public ProxiedObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// final StringBuilder builder = new StringBuilder();
// builder.append("ProxiedObjectPool [pool=");
// builder.append(pool);
// builder.append(", proxySource=");
// builder.append(proxySource);
// builder.append("]");
// return builder.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    public void returnObject(final T proxy) throws Exception {
try {
// 
// pool.returnObject(proxySource.resolveProxy(proxy));
// 

obj.invokeMember("returnObject", proxy);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "ProxiedObjectPool.returnObject");
}
}
    public void invalidateObject0(final T proxy) throws Exception {
try {
// 
// pool.invalidateObject0(proxySource.resolveProxy(proxy));
// 

obj.invokeMember("invalidateObject0", proxy);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "ProxiedObjectPool.invalidateObject0");
}
}
    public int getNumIdle() {
// 
// return pool.getNumIdle();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle").as(int.class);
}
    public int getNumActive() {
// 
// return pool.getNumActive();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive").as(int.class);
}
    public void close() {
// 
// pool.close();
// 

obj.invokeMember("close");
}
    public void clear() throws Exception, UnsupportedOperationException {
try {
// 
// pool.clear();
// 

obj.invokeMember("clear");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "ProxiedObjectPool.clear");
}
}
    public T borrowObject() throws Exception, NoSuchElementException, IllegalStateException {
try {
// 
// UsageTracking<T> usageTracking = null;
// if (pool instanceof UsageTracking) {
// usageTracking = (UsageTracking<T>) pool;
// }
// return proxySource.createProxy(pool.borrowObject(), usageTracking);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("borrowObject").as(T.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception, NoSuchElementException, IllegalStateException
    throw (Exception, NoSuchElementException, IllegalStateException) ExceptionHandler.handle(e, "ProxiedObjectPool.borrowObject");
}
}
    public void addObject() throws Exception, IllegalStateException, UnsupportedOperationException {
try {
// 
// pool.addObject();
// 

obj.invokeMember("addObject");
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalStateException, UnsupportedOperationException
    throw (Exception, IllegalStateException, UnsupportedOperationException) ExceptionHandler.handle(e, "ProxiedObjectPool.addObject");
}
}
    public ProxiedObjectPool(final ObjectPool<T> pool, final ProxySource<T> proxySource) {
// 
// this.pool = pool;
// this.proxySource = proxySource;
// 

this.obj = clz.invokeMember("__init__", pool, proxySource);
}
}
