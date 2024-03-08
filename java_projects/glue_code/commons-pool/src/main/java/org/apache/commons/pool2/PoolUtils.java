package org.apache.commons.pool;

import org.graalvm.polyglot.Value;
import org.graalvm.polyglot.PolyglotException;
import org.apache.commons.pool.ContextInitializer;
import org.apache.commons.pool.ExceptionHandler;
import org.apache.commons.pool.IntegrationUtils;
import java.util.Map;
import java.util.Collection;
import java.util.Iterator;
import java.util.Collections;
import java.util.HashMap;
import java.util.NoSuchElementException;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.locks.ReentrantReadWriteLock.ReadLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock.WriteLock;
    private static final class ErodingFactor {
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "ErodingFactor");
    private Value obj;
    public ErodingFactor(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// return "ErodingFactor{"
// + "factor="
// + factor
// + ", idleHighWaterMark="
// + idleHighWaterMark
// + '}';
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void update(final long nowMillis, final int numIdle) {
// 
// final int idle = Math.max(0, numIdle);
// idleHighWaterMark = Math.max(idle, idleHighWaterMark);
// final float maxInterval = 15f;
// final float minutes = maxInterval + ((1f - maxInterval) / idleHighWaterMark) * idle;
// nextShrinkMillis = nowMillis + (long) (minutes * 60000f * factor);
// 

obj.invokeMember("update", nowMillis, numIdle);
}
        public long getNextShrink() {
// 
// return nextShrinkMillis;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNextShrink").as(long.class);
}
        public ErodingFactor(final float factor) {
// 
// this.factor = factor;
// nextShrinkMillis =
// System.currentTimeMillis() + (long) (900000 * factor); // now + 15 min * factor
// idleHighWaterMark = 1;
// 

this.obj = clz.invokeMember("__init__", factor);
}
}
public final class PoolUtils {
    static final String MSG_NULL_KEYS = "keys must not be null.";
    static final String MSG_NULL_KEY = "key must not be null.";
    private static final String MSG_NULL_POOL = "pool must not be null.";
    private static final String MSG_NULL_KEYED_POOL = "keyedPool must not be null.";
    private static final String MSG_MIN_IDLE = "minIdle must be non-negative.";
    private static final String MSG_FACTOR_NEGATIVE = "factor must be positive.";
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "PoolUtils");
    private Value obj;
    public PoolUtils(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
    public static <T> void prefill2(final ObjectPool<T> pool, final int count)
            throws Exception, IllegalArgumentException {
try {
// 
// if (pool == null) {
// throw new IllegalArgumentException(MSG_NULL_POOL);
// }
// pool.addObjects(count);
// 

clz.invokeMember("prefill2", pool, count);
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalArgumentException
    throw (Exception, IllegalArgumentException) ExceptionHandler.handle(e, "PoolUtils.prefill2");
}
}
    public static <K, V> void prefill1(
            final KeyedObjectPool<K, V> keyedPool, final K key, final int count)
            throws Exception, IllegalArgumentException {
try {
// 
// if (keyedPool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// keyedPool.addObjects1(key, count);
// 

clz.invokeMember("prefill1", keyedPool, key, count);
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalArgumentException
    throw (Exception, IllegalArgumentException) ExceptionHandler.handle(e, "PoolUtils.prefill1");
}
}
    public static <K, V> void prefill0(
            final KeyedObjectPool<K, V> keyedPool, final Collection<K> keys, final int count)
            throws Exception, IllegalArgumentException {
try {
// 
// if (keys == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYS);
// }
// keyedPool.addObjects0(keys, count);
// 

clz.invokeMember("prefill0", keyedPool, keys, count);
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalArgumentException
    throw (Exception, IllegalArgumentException) ExceptionHandler.handle(e, "PoolUtils.prefill0");
}
}
    public PoolUtils() {
// 

this.obj = clz.invokeMember("__init__");
}
    public static <T> PooledObjectFactory<T> synchronizedPooledFactory(
            final PooledObjectFactory<T> factory) {
// 
// return new SynchronizedPooledObjectFactory<>(factory);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("synchronizedPooledFactory", factory).as(PooledObjectFactory.class);
}
    public static <T> ObjectPool<T> synchronizedPool1(final ObjectPool<T> pool) {
// 
// if (pool == null) {
// throw new IllegalArgumentException(MSG_NULL_POOL);
// }
// 
// /*
// * assert !(pool instanceof GenericObjectPool) :
// * "GenericObjectPool is already thread-safe"; assert !(pool instanceof
// * SoftReferenceObjectPool) :
// * "SoftReferenceObjectPool is already thread-safe"; assert !(pool
// * instanceof StackObjectPool) :
// * "StackObjectPool is already thread-safe"; assert
// * !"org.apache.commons.pool.composite.CompositeObjectPool"
// * .equals(pool.getClass().getName()) :
// * "CompositeObjectPools are already thread-safe";
// */
// return new SynchronizedObjectPool<>(pool);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("synchronizedPool1", pool).as(ObjectPool.class);
}
    public static <K, V> KeyedObjectPool<K, V> synchronizedPool0(
            final KeyedObjectPool<K, V> keyedPool) {
// 
// /*
// * assert !(keyedPool instanceof GenericKeyedObjectPool) :
// * "GenericKeyedObjectPool is already thread-safe"; assert !(keyedPool
// * instanceof StackKeyedObjectPool) :
// * "StackKeyedObjectPool is already thread-safe"; assert
// * !"org.apache.commons.pool.composite.CompositeKeyedObjectPool"
// * .equals(keyedPool.getClass().getName()) :
// * "CompositeKeyedObjectPools are already thread-safe";
// */
// return new SynchronizedKeyedObjectPool<>(keyedPool);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("synchronizedPool0", keyedPool).as(KeyedObjectPool.class);
}
    public static <K, V> KeyedPooledObjectFactory<K, V> synchronizedKeyedPooledFactory(
            final KeyedPooledObjectFactory<K, V> keyedFactory) {
// 
// return new SynchronizedKeyedPooledObjectFactory<>(keyedFactory);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("synchronizedKeyedPooledFactory", keyedFactory).as(KeyedPooledObjectFactory.class);
}
    public static <T> ObjectPool<T> erodingPool4(final ObjectPool<T> pool, final float factor) {
// 
// if (pool == null) {
// throw new IllegalArgumentException(MSG_NULL_POOL);
// }
// if (factor <= 0f) {
// throw new IllegalArgumentException(MSG_FACTOR_NEGATIVE);
// }
// return new ErodingObjectPool<>(pool, factor);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("erodingPool4", pool, factor).as(ObjectPool.class);
}
    public static <T> ObjectPool<T> erodingPool3(final ObjectPool<T> pool) {
// 
// return erodingPool4(pool, 1f);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("erodingPool3", pool).as(ObjectPool.class);
}
    public static <K, V> KeyedObjectPool<K, V> erodingPool2(
            final KeyedObjectPool<K, V> keyedPool, final float factor, final boolean perKey) {
// 
// if (keyedPool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// if (factor <= 0f) {
// throw new IllegalArgumentException(MSG_FACTOR_NEGATIVE);
// }
// if (perKey) {
// return new ErodingPerKeyKeyedObjectPool<>(keyedPool, factor);
// }
// return ErodingKeyedObjectPool.ErodingKeyedObjectPool0(keyedPool, factor);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("erodingPool2", keyedPool, factor, perKey).as(KeyedObjectPool.class);
}
    public static <K, V> KeyedObjectPool<K, V> erodingPool1(
            final KeyedObjectPool<K, V> keyedPool, final float factor) {
// 
// return erodingPool2(keyedPool, factor, false);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("erodingPool1", keyedPool, factor).as(KeyedObjectPool.class);
}
    public static <K, V> KeyedObjectPool<K, V> erodingPool0(final KeyedObjectPool<K, V> keyedPool) {
// 
// return erodingPool1(keyedPool, 1f);
// 


// TODO: Check the type mapping below!
return clz.invokeMember("erodingPool0", keyedPool).as(KeyedObjectPool.class);
}
    public static void checkRethrow(final Throwable t) {
// 
// if (t instanceof ThreadDeath) {
// throw (ThreadDeath) t;
// }
// if (t instanceof VirtualMachineError) {
// throw (VirtualMachineError) t;
// }
// 

clz.invokeMember("checkRethrow", t);
}
    public static <T> TimerTask checkMinIdle2(
            final ObjectPool<T> pool, final int minIdle, final long periodMillis)
            throws IllegalArgumentException {
try {
// 
// if (pool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// if (minIdle < 0) {
// throw new IllegalArgumentException(MSG_MIN_IDLE);
// }
// final TimerTask task = new ObjectPoolMinIdleTimerTask<>(pool, minIdle);
// getMinIdleTimer().schedule(task, 0L, periodMillis);
// return task;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("checkMinIdle2", pool, minIdle, periodMillis).as(TimerTask.class);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "PoolUtils.checkMinIdle2");
}
}
    public static <K, V> TimerTask checkMinIdle1(
            final KeyedObjectPool<K, V> keyedPool,
            final K key,
            final int minIdle,
            final long periodMillis)
            throws IllegalArgumentException {
try {
// 
// if (keyedPool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// if (key == null) {
// throw new IllegalArgumentException(MSG_NULL_KEY);
// }
// if (minIdle < 0) {
// throw new IllegalArgumentException(MSG_MIN_IDLE);
// }
// final TimerTask task = new KeyedObjectPoolMinIdleTimerTask<>(keyedPool, key, minIdle);
// getMinIdleTimer().schedule(task, 0L, periodMillis);
// return task;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("checkMinIdle1", keyedPool, key, minIdle, periodMillis).as(TimerTask.class);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "PoolUtils.checkMinIdle1");
}
}
    public static <K, V> Map<K, TimerTask> checkMinIdle0(
            final KeyedObjectPool<K, V> keyedPool,
            final Collection<K> keys,
            final int minIdle,
            final long periodMillis)
            throws IllegalArgumentException {
try {
// 
// if (keys == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYS);
// }
// final Map<K, TimerTask> tasks = new HashMap<>(keys.size());
// final Iterator<K> iter = keys.iterator();
// while (iter.hasNext()) {
// final K key = iter.next();
// final TimerTask task = checkMinIdle1(keyedPool, key, minIdle, periodMillis);
// tasks.put(key, task);
// }
// return tasks;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("checkMinIdle0", keyedPool, keys, minIdle, periodMillis).as(Map.class);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "PoolUtils.checkMinIdle0");
}
}
    private static Timer getMinIdleTimer() {
// 
// return TimerHolder.MIN_IDLE_TIMER;
// 


// TODO: Check the type mapping below!
return clz.invokeMember("getMinIdleTimer").as(Timer.class);
}
    private static class ErodingKeyedObjectPool<K, V> implements KeyedObjectPool<K, V> {
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "ErodingKeyedObjectPool");
    private Value obj;
    public ErodingKeyedObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// return "ErodingKeyedObjectPool{"
// + "factor="
// + erodingFactor
// + ", keyedPool="
// + keyedPool
// + '}';
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void returnObject(final K key, final V obj) throws Exception {
try {
// 
// boolean discard = false;
// final long nowMillis = System.currentTimeMillis();
// final ErodingFactor factor = getErodingFactor(key);
// synchronized (keyedPool) {
// if (factor.getNextShrink() < nowMillis) {
// final int numIdle = getNumIdle1(key);
// if (numIdle > 0) {
// discard = true;
// }
// 
// factor.update(nowMillis, numIdle);
// }
// }
// try {
// if (discard) {
// keyedPool.invalidateObject0(key, obj);
// } else {
// keyedPool.returnObject(key, obj);
// }
// } catch (final Exception e) {
// }
// 

obj.invokeMember("returnObject", key, obj);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "ErodingKeyedObjectPool.returnObject");
}
}
        public void invalidateObject0(final K key, final V obj) {
// 
// try {
// keyedPool.invalidateObject0(key, obj);
// } catch (final Exception e) {
// }
// 

obj.invokeMember("invalidateObject0", key, obj);
}
        public void close() {
// 
// try {
// keyedPool.close();
// } catch (final Exception e) {
// }
// 

obj.invokeMember("close");
}
        public V borrowObject(final K key)
                throws Exception, NoSuchElementException, IllegalStateException {
try {
// 
// return keyedPool.borrowObject(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("borrowObject", key).as(V.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception, NoSuchElementException, IllegalStateException
    throw (Exception, NoSuchElementException, IllegalStateException) ExceptionHandler.handle(e, "ErodingKeyedObjectPool.borrowObject");
}
}
        public void addObject(final K key)
                throws Exception, IllegalStateException, UnsupportedOperationException {
try {
// 
// keyedPool.addObject(key);
// 

obj.invokeMember("addObject", key);
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalStateException, UnsupportedOperationException
    throw (Exception, IllegalStateException, UnsupportedOperationException) ExceptionHandler.handle(e, "ErodingKeyedObjectPool.addObject");
}
}
        public int getNumIdle1(final K key) {
// 
// return keyedPool.getNumIdle1(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle1", key).as(int.class);
}
        public int getNumIdle0() {
// 
// return keyedPool.getNumIdle0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle0").as(int.class);
}
        public int getNumActive1(final K key) {
// 
// return keyedPool.getNumActive1(key);
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive1", key).as(int.class);
}
        public int getNumActive0() {
// 
// return keyedPool.getNumActive0();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive0").as(int.class);
}
        protected KeyedObjectPool<K, V> getKeyedPool() {
// 
// return keyedPool;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getKeyedPool").as(KeyedObjectPool.class);
}
        protected ErodingFactor getErodingFactor(final K key) {
// 
// return erodingFactor;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getErodingFactor", key).as(ErodingFactor.class);
}
        public void clear1(final K key) throws Exception, UnsupportedOperationException {
try {
// 
// keyedPool.clear1(key);
// 

obj.invokeMember("clear1", key);
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "ErodingKeyedObjectPool.clear1");
}
}
        public void clear0() throws Exception, UnsupportedOperationException {
try {
// 
// keyedPool.clear0();
// 

obj.invokeMember("clear0");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "ErodingKeyedObjectPool.clear0");
}
}
        public static ErodingKeyedObjectPool ErodingKeyedObjectPool0(
                final KeyedObjectPool keyedPool, final float factor) {
// 
// return new ErodingKeyedObjectPool(keyedPool, new ErodingFactor(factor));
// 


// TODO: Check the type mapping below!
return clz.invokeMember("ErodingKeyedObjectPool0", keyedPool, factor).as(ErodingKeyedObjectPool.class);
}
        public ErodingKeyedObjectPool(
                final KeyedObjectPool<K, V> keyedPool, final ErodingFactor erodingFactor) {
// 
// if (keyedPool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// this.keyedPool = keyedPool;
// this.erodingFactor = erodingFactor;
// 

this.obj = clz.invokeMember("__init__", keyedPool, erodingFactor);
}
}
    private static class ErodingObjectPool<T> implements ObjectPool<T> {
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "ErodingObjectPool");
    private Value obj;
    public ErodingObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// return "ErodingObjectPool{" + "factor=" + factor + ", pool=" + pool + '}';
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void returnObject(final T obj) {
// 
// boolean discard = false;
// final long nowMillis = System.currentTimeMillis();
// synchronized (pool) {
// if (factor.getNextShrink() < nowMillis) { // XXX: Pool 3: move test
// final int numIdle = pool.getNumIdle();
// if (numIdle > 0) {
// discard = true;
// }
// 
// factor.update(nowMillis, numIdle);
// }
// }
// try {
// if (discard) {
// pool.invalidateObject0(obj);
// } else {
// pool.returnObject(obj);
// }
// } catch (final Exception e) {
// }
// 

obj.invokeMember("returnObject", obj);
}
        public void invalidateObject0(final T obj) {
// 
// try {
// pool.invalidateObject0(obj);
// } catch (final Exception e) {
// }
// 

obj.invokeMember("invalidateObject0", obj);
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
// try {
// pool.close();
// } catch (final Exception e) {
// }
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
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "ErodingObjectPool.clear");
}
}
        public T borrowObject() throws Exception, NoSuchElementException, IllegalStateException {
try {
// 
// return pool.borrowObject();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("borrowObject").as(T.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception, NoSuchElementException, IllegalStateException
    throw (Exception, NoSuchElementException, IllegalStateException) ExceptionHandler.handle(e, "ErodingObjectPool.borrowObject");
}
}
        public void addObject()
                throws Exception, IllegalStateException, UnsupportedOperationException {
try {
// 
// pool.addObject();
// 

obj.invokeMember("addObject");
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalStateException, UnsupportedOperationException
    throw (Exception, IllegalStateException, UnsupportedOperationException) ExceptionHandler.handle(e, "ErodingObjectPool.addObject");
}
}
        public ErodingObjectPool(final ObjectPool<T> pool, final float factor) {
// 
// this.pool = pool;
// this.factor = new ErodingFactor(factor);
// 

this.obj = clz.invokeMember("__init__", pool, factor);
}
}
    private static final class ErodingPerKeyKeyedObjectPool<K, V>
        private final Map<K, ErodingFactor> factors = Collections.synchronizedMap(new HashMap<>());
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "ErodingPerKeyKeyedObjectPool");
    private Value obj;
    public ErodingPerKeyKeyedObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// return "ErodingPerKeyKeyedObjectPool{"
// + "factor="
// + factor
// + ", keyedPool="
// + getKeyedPool()
// + '}';
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        protected ErodingFactor getErodingFactor(final K key) {
// 
// ErodingFactor eFactor = factors.get(key);
// if (eFactor == null) {
// eFactor = new ErodingFactor(this.factor);
// factors.put(key, eFactor);
// }
// return eFactor;
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getErodingFactor", key).as(ErodingFactor.class);
}
        public ErodingPerKeyKeyedObjectPool(
                final KeyedObjectPool<K, V> keyedPool, final float factor) {
// 
// super(keyedPool, null);
// this.factor = factor;
// 

this.obj = clz.invokeMember("__init__", keyedPool, factor);
}
}
    private static final class KeyedObjectPoolMinIdleTimerTask<K, V> extends TimerTask {
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "KeyedObjectPoolMinIdleTimerTask");
    private Value obj;
    public KeyedObjectPoolMinIdleTimerTask(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("KeyedObjectPoolMinIdleTimerTask");
// sb.append("{minIdle=").append(minIdle);
// sb.append(", key=").append(key);
// sb.append(", keyedPool=").append(keyedPool);
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void run() {
// 
// boolean success = false;
// try {
// if (keyedPool.getNumIdle1(key) < minIdle) {
// keyedPool.addObject(key);
// }
// success = true;
// 
// } catch (final Exception e) {
// cancel();
// 
// } finally {
// if (!success) {
// cancel();
// }
// }
// 

obj.invokeMember("run");
}
        KeyedObjectPoolMinIdleTimerTask(
                final KeyedObjectPool<K, V> keyedPool, final K key, final int minIdle)
                throws IllegalArgumentException {
try {
// 
// if (keyedPool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// this.keyedPool = keyedPool;
// this.key = key;
// this.minIdle = minIdle;
// 

this.obj = clz.invokeMember("__init__", keyedPool, key, minIdle);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "KeyedObjectPoolMinIdleTimerTask.__init__");
}
}
}
    private static final class ObjectPoolMinIdleTimerTask<T> extends TimerTask {
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "ObjectPoolMinIdleTimerTask");
    private Value obj;
    public ObjectPoolMinIdleTimerTask(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("ObjectPoolMinIdleTimerTask");
// sb.append("{minIdle=").append(minIdle);
// sb.append(", pool=").append(pool);
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void run() {
// 
// boolean success = false;
// try {
// if (pool.getNumIdle() < minIdle) {
// pool.addObject();
// }
// success = true;
// 
// } catch (final Exception e) {
// cancel();
// } finally {
// if (!success) {
// cancel();
// }
// }
// 

obj.invokeMember("run");
}
        ObjectPoolMinIdleTimerTask(final ObjectPool<T> pool, final int minIdle)
                throws IllegalArgumentException {
try {
// 
// if (pool == null) {
// throw new IllegalArgumentException(MSG_NULL_POOL);
// }
// this.pool = pool;
// this.minIdle = minIdle;
// 

this.obj = clz.invokeMember("__init__", pool, minIdle);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "ObjectPoolMinIdleTimerTask.__init__");
}
}
}
    private static final class SynchronizedKeyedObjectPool<K, V> implements KeyedObjectPool<K, V> {
        private final ReentrantReadWriteLock readWriteLock = new ReentrantReadWriteLock();
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "SynchronizedKeyedObjectPool");
    private Value obj;
    public SynchronizedKeyedObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("SynchronizedKeyedObjectPool");
// sb.append("{keyedPool=").append(keyedPool);
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void returnObject(final K key, final V obj) {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// keyedPool.returnObject(key, obj);
// } catch (final Exception e) {
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("returnObject", key, obj);
}
        public void invalidateObject0(final K key, final V obj) {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// keyedPool.invalidateObject0(key, obj);
// } catch (final Exception e) {
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("invalidateObject0", key, obj);
}
        public void close() {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// keyedPool.close();
// } catch (final Exception e) {
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("close");
}
        public V borrowObject(final K key)
                throws Exception, NoSuchElementException, IllegalStateException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// return keyedPool.borrowObject(key);
// } finally {
// writeLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("borrowObject", key).as(V.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception, NoSuchElementException, IllegalStateException
    throw (Exception, NoSuchElementException, IllegalStateException) ExceptionHandler.handle(e, "SynchronizedKeyedObjectPool.borrowObject");
}
}
        public void addObject(final K key)
                throws Exception, IllegalStateException, UnsupportedOperationException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// keyedPool.addObject(key);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("addObject", key);
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalStateException, UnsupportedOperationException
    throw (Exception, IllegalStateException, UnsupportedOperationException) ExceptionHandler.handle(e, "SynchronizedKeyedObjectPool.addObject");
}
}
        public int getNumIdle1(final K key) {
// 
// final ReadLock readLock = readWriteLock.readLock();
// readLock.lock();
// try {
// return keyedPool.getNumIdle1(key);
// } finally {
// readLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle1", key).as(int.class);
}
        public int getNumIdle0() {
// 
// final ReadLock readLock = readWriteLock.readLock();
// readLock.lock();
// try {
// return keyedPool.getNumIdle0();
// } finally {
// readLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle0").as(int.class);
}
        public int getNumActive1(final K key) {
// 
// final ReadLock readLock = readWriteLock.readLock();
// readLock.lock();
// try {
// return keyedPool.getNumActive1(key);
// } finally {
// readLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive1", key).as(int.class);
}
        public int getNumActive0() {
// 
// final ReadLock readLock = readWriteLock.readLock();
// readLock.lock();
// try {
// return keyedPool.getNumActive0();
// } finally {
// readLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive0").as(int.class);
}
        public void clear1(final K key) throws Exception, UnsupportedOperationException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// keyedPool.clear1(key);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("clear1", key);
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "SynchronizedKeyedObjectPool.clear1");
}
}
        public void clear0() throws Exception, UnsupportedOperationException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// keyedPool.clear0();
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("clear0");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "SynchronizedKeyedObjectPool.clear0");
}
}
        SynchronizedKeyedObjectPool(final KeyedObjectPool<K, V> keyedPool)
                throws IllegalArgumentException {
try {
// 
// if (keyedPool == null) {
// throw new IllegalArgumentException(MSG_NULL_KEYED_POOL);
// }
// this.keyedPool = keyedPool;
// 

this.obj = clz.invokeMember("__init__", keyedPool);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "SynchronizedKeyedObjectPool.__init__");
}
}
}
    private static final class SynchronizedKeyedPooledObjectFactory<K, V>
        private final WriteLock writeLock = new ReentrantReadWriteLock().writeLock();
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "SynchronizedKeyedPooledObjectFactory");
    private Value obj;
    public SynchronizedKeyedPooledObjectFactory(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public boolean validateObject(final K key, final PooledObject<V> p) {
// 
// writeLock.lock();
// try {
// return keyedFactory.validateObject(key, p);
// } finally {
// writeLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("validateObject", key, p).as(boolean.class);
}
        public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("SynchronizedKeyedPoolableObjectFactory");
// sb.append("{keyedFactory=").append(keyedFactory);
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void passivateObject(final K key, final PooledObject<V> p) throws Exception {
try {
// 
// writeLock.lock();
// try {
// keyedFactory.passivateObject(key, p);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("passivateObject", key, p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedKeyedPooledObjectFactory.passivateObject");
}
}
        public PooledObject<V> makeObject(final K key) throws Exception {
try {
// 
// writeLock.lock();
// try {
// return keyedFactory.makeObject(key);
// } finally {
// writeLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("makeObject", key).as(PooledObject.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedKeyedPooledObjectFactory.makeObject");
}
}
        public void destroyObject0(final K key, final PooledObject<V> p) throws Exception {
try {
// 
// writeLock.lock();
// try {
// keyedFactory.destroyObject0(key, p);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("destroyObject0", key, p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedKeyedPooledObjectFactory.destroyObject0");
}
}
        public void activateObject(final K key, final PooledObject<V> p) throws Exception {
try {
// 
// writeLock.lock();
// try {
// keyedFactory.activateObject(key, p);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("activateObject", key, p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedKeyedPooledObjectFactory.activateObject");
}
}
        SynchronizedKeyedPooledObjectFactory(final KeyedPooledObjectFactory<K, V> keyedFactory)
                throws IllegalArgumentException {
try {
// 
// if (keyedFactory == null) {
// throw new IllegalArgumentException("keyedFactory must not be null.");
// }
// this.keyedFactory = keyedFactory;
// 

this.obj = clz.invokeMember("__init__", keyedFactory);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "SynchronizedKeyedPooledObjectFactory.__init__");
}
}
}
    private static final class SynchronizedObjectPool<T> implements ObjectPool<T> {
        private final ReentrantReadWriteLock readWriteLock = new ReentrantReadWriteLock();
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "SynchronizedObjectPool");
    private Value obj;
    public SynchronizedObjectPool(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("SynchronizedObjectPool");
// sb.append("{pool=").append(pool);
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void returnObject(final T obj) {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// pool.returnObject(obj);
// } catch (final Exception e) {
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("returnObject", obj);
}
        public void invalidateObject0(final T obj) {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// pool.invalidateObject0(obj);
// } catch (final Exception e) {
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("invalidateObject0", obj);
}
        public int getNumIdle() {
// 
// final ReadLock readLock = readWriteLock.readLock();
// readLock.lock();
// try {
// return pool.getNumIdle();
// } finally {
// readLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumIdle").as(int.class);
}
        public int getNumActive() {
// 
// final ReadLock readLock = readWriteLock.readLock();
// readLock.lock();
// try {
// return pool.getNumActive();
// } finally {
// readLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("getNumActive").as(int.class);
}
        public void close() {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// pool.close();
// } catch (final Exception e) {
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("close");
}
        public void clear() throws Exception, UnsupportedOperationException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// pool.clear();
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("clear");
} catch (PolyglotException e) {
    // TODO: Handle Exception, UnsupportedOperationException
    throw (Exception, UnsupportedOperationException) ExceptionHandler.handle(e, "SynchronizedObjectPool.clear");
}
}
        public T borrowObject() throws Exception, NoSuchElementException, IllegalStateException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// return pool.borrowObject();
// } finally {
// writeLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("borrowObject").as(T.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception, NoSuchElementException, IllegalStateException
    throw (Exception, NoSuchElementException, IllegalStateException) ExceptionHandler.handle(e, "SynchronizedObjectPool.borrowObject");
}
}
        public void addObject()
                throws Exception, IllegalStateException, UnsupportedOperationException {
try {
// 
// final WriteLock writeLock = readWriteLock.writeLock();
// writeLock.lock();
// try {
// pool.addObject();
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("addObject");
} catch (PolyglotException e) {
    // TODO: Handle Exception, IllegalStateException, UnsupportedOperationException
    throw (Exception, IllegalStateException, UnsupportedOperationException) ExceptionHandler.handle(e, "SynchronizedObjectPool.addObject");
}
}
        SynchronizedObjectPool(final ObjectPool<T> pool) throws IllegalArgumentException {
try {
// 
// if (pool == null) {
// throw new IllegalArgumentException(MSG_NULL_POOL);
// }
// this.pool = pool;
// 

this.obj = clz.invokeMember("__init__", pool);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "SynchronizedObjectPool.__init__");
}
}
}
    private static final class SynchronizedPooledObjectFactory<T>
        private final WriteLock writeLock = new ReentrantReadWriteLock().writeLock();
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "SynchronizedPooledObjectFactory");
    private Value obj;
    public SynchronizedPooledObjectFactory(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
        public boolean validateObject(final PooledObject<T> p) {
// 
// writeLock.lock();
// try {
// return factory.validateObject(p);
// } finally {
// writeLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("validateObject", p).as(boolean.class);
}
        public String toString() {
// 
// final StringBuilder sb = new StringBuilder();
// sb.append("SynchronizedPoolableObjectFactory");
// sb.append("{factory=").append(factory);
// sb.append('}');
// return sb.toString();
// 


// TODO: Check the type mapping below!
return obj.invokeMember("toString").as(String.class);
}
        public void passivateObject(final PooledObject<T> p) throws Exception {
try {
// 
// writeLock.lock();
// try {
// factory.passivateObject(p);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("passivateObject", p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedPooledObjectFactory.passivateObject");
}
}
        public PooledObject<T> makeObject() throws Exception {
try {
// 
// writeLock.lock();
// try {
// return factory.makeObject();
// } finally {
// writeLock.unlock();
// }
// 


// TODO: Check the type mapping below!
return obj.invokeMember("makeObject").as(PooledObject.class);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedPooledObjectFactory.makeObject");
}
}
        public void destroyObject0(final PooledObject<T> p) throws Exception {
try {
// 
// writeLock.lock();
// try {
// factory.destroyObject0(p);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("destroyObject0", p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedPooledObjectFactory.destroyObject0");
}
}
        public void activateObject(final PooledObject<T> p) throws Exception {
try {
// 
// writeLock.lock();
// try {
// factory.activateObject(p);
// } finally {
// writeLock.unlock();
// }
// 

obj.invokeMember("activateObject", p);
} catch (PolyglotException e) {
    // TODO: Handle Exception
    throw (Exception) ExceptionHandler.handle(e, "SynchronizedPooledObjectFactory.activateObject");
}
}
        SynchronizedPooledObjectFactory(final PooledObjectFactory<T> factory)
                throws IllegalArgumentException {
try {
// 
// if (factory == null) {
// throw new IllegalArgumentException("factory must not be null.");
// }
// this.factory = factory;
// 

this.obj = clz.invokeMember("__init__", factory);
} catch (PolyglotException e) {
    // TODO: Handle IllegalArgumentException
    throw (IllegalArgumentException) ExceptionHandler.handle(e, "SynchronizedPooledObjectFactory.__init__");
}
}
}
    static class TimerHolder {
        static final Timer MIN_IDLE_TIMER = new Timer(true);
    private static Value clz = ContextInitializer.getPythonClass("/PoolUtils.py", "TimerHolder");
    private Value obj;
    public TimerHolder(Value obj) {
        this.obj = obj;
    }
    public Value getPythonObject() {
        return obj;
    }
}
}
