package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.util.NoSuchElementException;
import org.apache.commons.pool2.KeyedObjectPool;
import org.apache.commons.pool2.UsageTracking;
public class ProxiedKeyedObjectPool<K, V> implements KeyedObjectPool<K, V> {
    private static Value clz = ContextInitializer.getPythonClass("/ProxiedKeyedObjectPool.py", "ProxiedKeyedObjectPool");
    private Value obj;
    public ProxiedKeyedObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public String toString() {
// 
// final StringBuilder builder = new StringBuilder();
// builder.append("ProxiedKeyedObjectPool [pool=");
// builder.append(pool);
// builder.append(", proxySource=");
// builder.append(proxySource);
// builder.append("]");
// return builder.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
    public void returnObject(final K key, final V proxy) throws Exception {
try {
// 
// pool.returnObject(key, proxySource.resolveProxy(proxy));
// 

obj.invokeMember("returnObject", key, proxy);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "ProxiedKeyedObjectPool.returnObject");
}
}
    public void invalidateObject0(final K key, final V proxy) throws Exception {
try {
// 
// pool.invalidateObject0(key, proxySource.resolveProxy(proxy));
// 

obj.invokeMember("invalidateObject0", key, proxy);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "ProxiedKeyedObjectPool.invalidateObject0");
}
}
    public void close() {
// 
// pool.close();
// 

obj.invokeMember("close");
}
    public V borrowObject(final K key)
            throws Exception, NoSuchElementException, IllegalStateException {
try {
// 
// UsageTracking<V> usageTracking = null;
// if (pool instanceof UsageTracking) {
// usageTracking = (UsageTracking<V>) pool;
// }
// return proxySource.createProxy(pool.borrowObject(key), usageTracking);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("borrowObject", key).as(V.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception, NoSuchElementException, IllegalStateException
    throw (Exception, NoSuchElementException, IllegalStateException) ExceptionHandler.handle(e, "ProxiedKeyedObjectPool.borrowObject");
}
}
    public void addObject(final K key)
            throws Exception, IllegalStateException, UnsupportedOperationException {
try {
// 
// pool.addObject(key);
// 

obj.invokeMember("addObject", key);
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalStateException, UnsupportedOperationException
    throw (Exception, IllegalStateException, UnsupportedOperationException) ExceptionHandler.handle(e, "ProxiedKeyedObjectPool.addObject");
}
}
    public int getNumIdle1(final K key) {
// 
// return pool.getNumIdle1(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle1", key).as(int.class);
}
    public int getNumIdle0() {
// 
// return pool.getNumIdle0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle0").as(int.class);
}
    public int getNumActive1(final K key) {
// 
// return pool.getNumActive1(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive1", key).as(int.class);
}
    public int getNumActive0() {
// 
// return pool.getNumActive0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive0").as(int.class);
}
    public void clear1(final K key) throws Exception, UnsupportedOperationException {
try {
// 
// pool.clear1(key);
// 

obj.invokeMember("clear1", key);
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "ProxiedKeyedObjectPool.clear1");
}
}
    public void clear0() throws Exception, UnsupportedOperationException {
try {
// 
// pool.clear0();
// 

obj.invokeMember("clear0");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "ProxiedKeyedObjectPool.clear0");
}
}
    public ProxiedKeyedObjectPool(
            final KeyedObjectPool<K, V> pool, final ProxySource<V> proxySource) {
// 
// this.pool = pool;
// this.proxySource = proxySource;
// 

this.obj = clz.invokeMember("__init__", pool, proxySource);
}
}
