package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.io.Closeable;
import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;
public interface KeyedObjectPool<K, V> extends Closeable {
    void returnObject(K key, V obj) throws Exception;
    void invalidateObject0(K key, V obj) throws Exception;
    int getNumIdle1(K key);
    int getNumIdle0();
    int getNumActive1(K key);
    int getNumActive0();
    void close();
    void clear1(K key) throws Exception, UnsupportedOperationException;
    void clear0() throws Exception, UnsupportedOperationException;
    V borrowObject(K key) throws Exception, NoSuchElementException, IllegalStateException;
    void addObject(K key) throws Exception, IllegalStateException, UnsupportedOperationException;
    default void invalidateObject1(final K key, final V obj, final DestroyMode destroyMode)
            throws Exception {
try {
// 
// invalidateObject0(key, obj);
// 

obj.invokeMember("invalidateObject1");
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "KeyedObjectPool.invalidateObject1");
}
}
    default void addObjects1(final K key, final int count)
            throws Exception, IllegalArgumentException {
try {
// 
// if (key == null) {
// throw new IllegalArgumentException(PoolUtils.MSG_NULL_KEY);
// }
// for (int i = 0; i < count; i++) {
// addObject(key);
// }
// 

obj.invokeMember("addObjects1");
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalArgumentException
    throw (Exception, IllegalArgumentException) ExceptionHandler.handle(e, "KeyedObjectPool.addObjects1");
}
}
    default void addObjects0(final Collection<K> keys, final int count)
            throws Exception, IllegalArgumentException {
try {
// 
// if (keys == null) {
// throw new IllegalArgumentException(PoolUtils.MSG_NULL_KEYS);
// }
// final Iterator<K> iter = keys.iterator();
// while (iter.hasNext()) {
// addObjects1(iter.next(), count);
// }
// 

obj.invokeMember("addObjects0");
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalArgumentException
    throw (Exception, IllegalArgumentException) ExceptionHandler.handle(e, "KeyedObjectPool.addObjects0");
}
}
}
